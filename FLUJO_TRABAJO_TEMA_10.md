# FLUJO DE TRABAJO - TEMA 10: Poblaciones Acotadas y la Ecuación Logística

## INFORMACIÓN GENERAL DEL PROYECTO

### Equipo Asignado: Equipo 10
- Enrique A. González Moreira
- Heily Rodríguez Rodríguez
- Alex L. Cuervo Grillo

### Referencias Bibliográficas
- **Edwards & Penney, 4ta edición**: "Ecuaciones Diferenciales y Problemas con Valores en la Frontera"
  - Capítulo 1: Ecuaciones diferenciales de primer orden
  - Capítulo 2: Modelos matemáticos y métodos numéricos (págs. 81-82 - ejemplo resuelto)
  - Capítulo 5: Sistemas lineales de ecuaciones diferenciales
  - Capítulo 6: Sistemas no lineales y fenómenos
- **Burden et al., 10ma edición**: "Análisis Numérico"
  - Capítulo 1: Preliminares matemáticos y análisis de error
  - Capítulo 5: Problemas de valor inicial para ecuaciones diferenciales ordinarias
  - Capítulo 6: Métodos directos para resolver sistemas lineales
  - Capítulo 7: Técnicas iterativas en álgebra de matrices

### Entregables
1. **Informe técnico**: Máximo 10 páginas (plantilla JCE MatCom)
2. **Código interactivo**: IPython Notebooks o dashboards en Python
3. **Presentación**: 10 minutos + 5 minutos de preguntas

---

## ESTRUCTURA DEL TEMA 10

El Tema 10 tiene **3 PARTES**:

### PARTE A: Modelo logístico con tasa variable e isoclinas
### PARTE B: Bifurcación
### PARTE C: Plano de fase y estabilidad

---

# FLUJO DE TRABAJO DETALLADO

## FASE 1: ESTUDIO TEÓRICO Y MODELACIÓN

### Tarea 1.1: Estudiar la teoría de ecuaciones logísticas

**Referencias específicas:**
- **Edwards**: Capítulo 2 "Modelos matemáticos y métodos numéricos"
  - Sección 2.1: "Modelos de población" (págs. 75-84)
  - Sección 2.2: "Ecuaciones de equilibrio y estabilidad" (págs. 85-92)
  - **Págs. 81-82**: Ejemplo resuelto sobre poblaciones acotadas
- **Burden**: No aplicable directamente (enfoque numérico)

**Subtareas:**
1. Leer **Edwards & Penney, 4ta edición, págs. 81-82**
   - Ubicación: `Edwards_Capitulos/02_capitulo.pdf` (buscar páginas 81-82)
   - **NOTA**: El PDF del capítulo 2 está disponible pero es de 1.3 MB
   - Enfocarse en el ejemplo resuelto sobre poblaciones acotadas

2. Entender el modelo logístico básico: `dP/dt = kP(M - P)`
   - Donde `k` es tasa de crecimiento
   - `M` es capacidad de carga (población límite)
   - `P(t)` es la población en tiempo t

3. Estudiar la variante con tasa exponencial decreciente
   - **Documentación requerida**: Edwards & Penney, Cap. 2, Secc. 2.1
   - Si no está disponible, buscar en libros alternativos de EDO

**Salida esperada**:
- Resumen de 1-2 páginas sobre ecuaciones logísticas
- Ecuaciones clave identificadas
- Conceptos de capacidad de carga y crecimiento saturado

---

### Tarea 1.2: Analizar el Problema del Tumor (Parte A)

**Referencias específicas:**
- **Edwards**: Capítulo 1 "Ecuaciones diferenciales de primer orden"
  - Sección 1.4: "Ecuaciones separables y aplicaciones" (págs. 32-47)
  - Sección 1.5: "Ecuaciones lineales de primer orden" (págs. 48-60)
- **Edwards**: Capítulo 2 "Modelos matemáticos y métodos numéricos"
  - Sección 2.1: "Modelos de población" (págs. 75-84)
  - Sección 2.3: "Campos de pendientes y curvas solución" (págs. 93-101)
- **Burden**: No aplicable (métodos numéricos se verán en Fase 2)

**Subtareas:**

1. **Plantear el modelo matemático**
   - EDO dada: `dP/dt = β₀e^(-αt)P, P(0) = P₀`
   - Identificar parámetros:
     * `β₀`: tasa de natalidad inicial de células
     * `α`: constante de decrecimiento exponencial
     * `P₀`: población inicial de células tumorales
   - **Referencia**: Edwards Cap. 2, Secc. 2.1

2. **Resolver analíticamente la EDO**
   - Método: Variables separables
   - Integrar: `∫(dP/P) = ∫β₀e^(-αt)dt`
   - Obtener solución: `P(t) = P₀ exp(β₀/α (1 - e^(-αt)))`
   - **Referencia**: Edwards Cap. 1, Secc. 1.4 (ecuaciones separables)

3. **Analizar el comportamiento límite**
   - Calcular: `lim(t→∞) P(t) = P₀ exp(β₀/α)`
   - Interpretar: La población se aproxima a un límite finito
   - **Referencia**: Edwards Cap. 2, Secc. 2.2 (estabilidad)

4. **Campo de isoclinas**
   - Ecuación: `dP/dt = β₀e^(-αt)P = C` (constante)
   - Resolver: `P = Ce^(αt)/β₀`
   - Graficar familia de curvas en plano (t, P)
   - Interpretar: Mostrar cómo las soluciones tienden al límite
   - **Referencia**: Edwards Cap. 2, Secc. 2.3 (campos de pendientes)

**Salida esperada**:
- Solución analítica completa y verificada
- Cálculo del límite poblacional
- Gráfico del campo de isoclinas con interpretación

---

### Tarea 1.3: Análisis de Bifurcación (Parte B)

**Referencias específicas:**
- **Edwards**: Capítulo 6 "Sistemas no lineales y fenómenos"
  - Sección 6.1: "Estabilidad y el plano de fase" (págs. 447-461)
  - Sección 6.2: "Sistemas lineales y estabilidad" (págs. 462-475)
  - Sección 6.5: "Caos en sistemas dinámicos" (págs. 515-530) - bifurcaciones
- **Edwards**: Capítulo 2 "Modelos matemáticos y métodos numéricos"
  - Sección 2.2: "Ecuaciones de equilibrio y estabilidad" (págs. 85-92)
- **Burden**: No aplicable directamente
- **Complemento**: Libros de sistemas dinámicos (ej. Strogatz) para teoría completa de bifurcaciones

**Subtareas:**

1. **Plantear el modelo reducido de bifurcación**
   - EDO: `dz/dt = μz - z³`
   - Parámetro `μ`: parámetro de control ambiental
   - **Referencia**: Edwards Cap. 6, Secc. 6.1

2. **Encontrar puntos de equilibrio**
   - Resolver: `μz - z³ = 0`
   - Factorizar: `z(μ - z²) = 0`
   - Soluciones: `z* = 0, z* = ±√μ` (si μ > 0)
   - **Referencia**: Edwards Cap. 2, Secc. 2.2 (equilibrios)

3. **Análisis de estabilidad**
   - Derivada: `dz'/dz = μ - 3z²`
   - En z = 0: `f'(0) = μ`
     * μ < 0: estable
     * μ > 0: inestable
   - En z = ±√μ: `f'(±√μ) = μ - 3μ = -2μ < 0` (estable si μ > 0)
   - **Referencia**: Edwards Cap. 6, Secc. 6.1 (análisis de estabilidad)

4. **Construir diagrama de bifurcación**
   - Eje horizontal: μ
   - Eje vertical: z*
   - Graficar ramas: z = 0, z = ±√μ
   - Marcar estabilidad con líneas sólidas/discontinuas
   - **Tipo de bifurcación**: Bifurcación de horquilla (pitchfork)
   - **Referencia**: Edwards Cap. 6, Secc. 6.5 (bifurcaciones)

5. **Interpretación biológica**
   - μ < 0: Solo equilibrio trivial (extinción)
   - μ > 0: Aparecen dos estados estables no triviales
   - μ = 0: Punto crítico de bifurcación
   - Contexto: Umbral ambiental para supervivencia poblacional
   - **Referencia**: Edwards Cap. 2, Secc. 2.1-2.2 (modelos poblacionales)

**Salida esperada**:
- Tabla con puntos de equilibrio y estabilidad
- Diagrama de bifurcación completo
- Interpretación física del parámetro μ

---

### Tarea 1.4: Plano de Fase y Estabilidad (Parte C)

**Referencias específicas:**
- **Edwards**: Capítulo 5 "Sistemas lineales de ecuaciones diferenciales"
  - Sección 5.1: "Matrices y sistemas lineales" (págs. 333-346)
  - Sección 5.2: "El método del eigenvalor para sistemas lineales" (págs. 347-361)
  - Sección 5.3: "Un álbum de segunda solución de sistemas lineales" (págs. 362-378)
- **Edwards**: Capítulo 6 "Sistemas no lineales y fenómenos"
  - Sección 6.1: "Estabilidad y el plano de fase" (págs. 447-461)
  - Sección 6.2: "Sistemas lineales y estabilidad" (págs. 462-475)
- **Burden**: Capítulo 6 "Métodos directos para resolver sistemas lineales"
  - Sección 6.6: "Técnicas especiales para matrices especiales" (para eigenvalores)
- **Burden**: Capítulo 7 "Técnicas iterativas en álgebra de matrices"
  - Sección 7.2: "El método de potencia" (págs. 451-462) - cálculo de eigenvalores
- **Burden**: Capítulo 9 "Aproximación de eigenvalores"

**Subtareas:**

1. **Analizar el sistema lineal dado**
   - Sistema:
     ```
     dx/dt = x - y
     dy/dt = 2x - 3y
     ```
   - **Referencia**: Edwards Cap. 5, Secc. 5.1

2. **Encontrar puntos críticos**
   - Resolver: `x - y = 0` y `2x - 3y = 0`
   - Única solución: `(x*, y*) = (0, 0)`
   - **Referencia**: Edwards Cap. 6, Secc. 6.1

3. **Clasificar el punto crítico**
   - Matriz jacobiana:
     ```
     J = [1  -1]
         [2  -3]
     ```
   - Calcular eigenvalores:
     * Ecuación característica: `det(J - λI) = 0`
     * `(1-λ)(-3-λ) + 2 = 0`
     * `λ² + 2λ - 1 = 0`
     * `λ₁,₂ = -1 ± √2`
     * Ambos negativos → **Nodo estable**
   - **Referencia**: Edwards Cap. 5, Secc. 5.2 (eigenvalores); Burden Cap. 7, Secc. 7.2

4. **Construir plano de fase**
   - Calcular eigenvectores asociados
   - Trazar direcciones principales
   - Graficar trayectorias típicas
   - Mostrar convergencia al origen
   - **Referencia**: Edwards Cap. 6, Secc. 6.1-6.2 (plano de fase)

5. **Interpretación biológica**
   - x(t): Subpoblación activa de células
   - y(t): Subpoblación inactiva de células
   - Comportamiento: Ambas subpoblaciones → 0 (equilibrio)
   - Significado: Sistema estable, células tienden a estado basal
   - **Referencia**: Edwards Cap. 6, Secc. 6.2 (clasificación y estabilidad)

**Salida esperada**:
- Cálculos completos de eigenvalores/eigenvectores
- Diagrama del plano de fase con trayectorias
- Interpretación del comportamiento dinámico

---

## FASE 2: ANÁLISIS NUMÉRICO

### Tarea 2.1: Determinar si el problema está bien planteado

**Referencias específicas:**
- **Burden**: Capítulo 5 "Problemas de valor inicial para ecuaciones diferenciales ordinarias"
  - Sección 5.1: "Teoría elemental de problemas de valores iniciales" (págs. 267-274)
  - Incluye Teorema de Picard-Lindelöf para existencia y unicidad
- **Edwards**: Capítulo 1 "Ecuaciones diferenciales de primer orden"
  - Sección 1.3: "Campos de pendientes y curvas solución" (págs. 17-31)
  - Teorema de existencia y unicidad mencionado
- **Edwards**: Capítulo 6 "Sistemas no lineales y fenómenos"
  - Sección 6.1: "Estabilidad y el plano de fase" (págs. 447-461) - estabilidad

**Subtareas:**

1. **Verificar existencia y unicidad (Teorema de Picard-Lindelöf)**
   - Para la EDO: `dP/dt = β₀e^(-αt)P, P(0) = P₀`
   - Verificar: `f(t,P) = β₀e^(-αt)P` es continua
   - Verificar: `∂f/∂P = β₀e^(-αt)` es continua y acotada
   - Conclusión: Existe solución única en cualquier intervalo [0, T]
   - **Referencia**: Burden Cap. 5, Secc. 5.1

2. **Análisis de estabilidad de la solución**
   - Estudiar sensibilidad a condiciones iniciales
   - Analizar efecto de perturbaciones en β₀ y α
   - **Referencia**: Edwards Cap. 6, Secc. 6.1; Burden Cap. 5, Secc. 5.1

**Salida esperada**:
- Demostración formal de existencia y unicidad
- Análisis de estabilidad teórico

---

### Tarea 2.2: Evaluar la condición del problema

**Referencias específicas:**
- **Burden**: Capítulo 1 "Preliminares matemáticos y análisis de error"
  - Sección 1.2: "Errores de redondeo y aritmética computacional" (págs. 17-30)
  - Sección 1.3: "Algoritmos y convergencia" (págs. 31-42)
  - Incluye análisis de condición y estabilidad
- **Burden**: Capítulo 5 "Problemas de valor inicial para ecuaciones diferenciales ordinarias"
  - Sección 5.1: "Teoría elemental de problemas de valores iniciales" (págs. 267-274)
  - Análisis de sensibilidad a condiciones iniciales

**Subtareas:**

1. **Análisis de sensibilidad a condiciones iniciales**
   - Perturbar P₀ → P₀ + ε
   - Calcular: `|P(t; P₀+ε) - P(t; P₀)|`
   - Determinar factor de amplificación
   - **Referencia**: Burden Cap. 5, Secc. 5.1; Cap. 1, Secc. 1.3

2. **Análisis de sensibilidad a parámetros**
   - Perturbar β₀ y α
   - Estudiar efecto en solución
   - **Referencia**: Burden Cap. 1, Secc. 1.2-1.3

3. **Número de condición**
   - Definir y calcular número de condición del problema
   - Clasificar: bien condicionado vs mal condicionado
   - **Referencia**: Burden Cap. 1, Secc. 1.2

**Salida esperada**:
- Cálculos de sensibilidad
- Número de condición
- Clasificación del problema

---

### Tarea 2.3: Implementar métodos numéricos (mínimo 2)

**Referencias específicas:**
- **Burden**: Capítulo 5 "Problemas de valor inicial para ecuaciones diferenciales ordinarias"
  - Sección 5.2: "Método de Euler" (págs. 275-284)
  - Sección 5.3: "Métodos de Taylor de orden superior" (págs. 285-292)
  - Sección 5.4: "Métodos de Runge-Kutta" (págs. 293-306)
  - Sección 5.5: "Control de errores y método de Runge-Kutta-Fehlberg" (págs. 307-316)
  - Sección 5.6: "Métodos multipaso" (págs. 317-332) - Adams-Bashforth
- **Edwards**: Capítulo 2 "Modelos matemáticos y métodos numéricos"
  - Sección 2.4: "Aproximación numérica: Método de Euler" (págs. 102-115)
  - Sección 2.5: "Un método mejorado de Euler" (págs. 116-125)
  - Sección 2.6: "El método de Runge-Kutta" (págs. 126-135)

**Subtareas:**

1. **Método 1: Euler Explícito**
   - Fórmula: `P_{n+1} = P_n + h·f(t_n, P_n)`
   - Implementar en Python
   - Parámetros: paso h, intervalo [0, T]
   - **Referencia**: Burden Cap. 5, Secc. 5.2; Edwards Cap. 2, Secc. 2.4

2. **Método 2: Runge-Kutta de orden 4 (RK4)**
   - Fórmula estándar RK4
   - Implementar en Python
   - Usar mismo h que Euler para comparación
   - **Referencia**: Burden Cap. 5, Secc. 5.4; Edwards Cap. 2, Secc. 2.6

3. **(Opcional) Método 3: Método de Adams-Bashforth**
   - Para análisis más completo
   - **Referencia**: Burden Cap. 5, Secc. 5.6

**Salida esperada**:
- Código Python funcional para cada método
- Funciones reutilizables y documentadas

---

### Tarea 2.4: Análisis de errores

**Referencias específicas:**
- **Burden**: Capítulo 1 "Preliminares matemáticos y análisis de error"
  - Sección 1.2: "Errores de redondeo y aritmética computacional" (págs. 17-30)
  - Sección 1.3: "Algoritmos y convergencia" (págs. 31-42)
- **Burden**: Capítulo 5 "Problemas de valor inicial para ecuaciones diferenciales ordinarias"
  - Sección 5.2: "Método de Euler" (págs. 275-284) - análisis de error local y global
  - Sección 5.4: "Métodos de Runge-Kutta" (págs. 293-306) - análisis de error
  - Sección 5.5: "Control de errores y método de Runge-Kutta-Fehlberg" (págs. 307-316)

**Subtareas:**

1. **Error relativo**
   - Fórmula: `E_rel = |P_exacto - P_numérico| / |P_exacto|`
   - Calcular para cada método en puntos seleccionados
   - Comparar métodos
   - **Referencia**: Burden Cap. 1, Secc. 1.2; Cap. 5, Secc. 5.2

2. **Análisis hacia adelante (forward error)**
   - Perturbar datos iniciales: P₀ → P₀ + δ
   - Medir propagación del error
   - Analizar para diferentes h
   - **Referencia**: Burden Cap. 1, Secc. 1.3; Cap. 5, Secc. 5.2

3. **Análisis hacia atrás (backward error)**
   - Determinar qué problema resuelve exactamente el método numérico
   - Evaluar estabilidad del algoritmo
   - **Referencia**: Burden Cap. 1, Secc. 1.3

**Salida esperada**:
- Tabla de errores relativos
- Gráficos de propagación de error
- Análisis de estabilidad numérica

---

### Tarea 2.5: Orden de convergencia

**Referencias específicas:**
- **Burden**: Capítulo 1 "Preliminares matemáticos y análisis de error"
  - Sección 1.3: "Algoritmos y convergencia" (págs. 31-42)
  - Definiciones de orden y tasa de convergencia
- **Burden**: Capítulo 5 "Problemas de valor inicial para ecuaciones diferenciales ordinarias"
  - Sección 5.2: "Método de Euler" (págs. 275-284) - orden 1
  - Sección 5.3: "Métodos de Taylor de orden superior" (págs. 285-292)
  - Sección 5.4: "Métodos de Runge-Kutta" (págs. 293-306) - orden 4
  - Análisis de error de truncamiento local y global

**Subtareas:**

1. **Determinar orden teórico**
   - Euler: orden 1
   - RK4: orden 4
   - Verificar con análisis de Taylor
   - **Referencia**: Burden Cap. 5, Secc. 5.2 (Euler), 5.4 (RK4)

2. **Verificación experimental**
   - Método: Refinamiento de paso
   - Reducir h a la mitad repetidamente
   - Calcular: `log₂(E(h)/E(h/2))`
   - Debe tender al orden teórico
   - **Referencia**: Burden Cap. 1, Secc. 1.3; Cap. 5

3. **Gráfico log-log**
   - Eje x: log(h)
   - Eje y: log(Error)
   - Pendiente = orden de convergencia
   - **Referencia**: Burden Cap. 1, Secc. 1.3

**Salida esperada**:
- Tabla de convergencia
- Gráfico log-log
- Verificación del orden teórico

---

### Tarea 2.6: Complejidad computacional

**Referencias específicas:**
- **Burden**: Capítulo 1 "Preliminares matemáticos y análisis de error"
  - Sección 1.3: "Algoritmos y convergencia" (págs. 31-42)
  - Análisis de complejidad computacional de algoritmos
- **Burden**: Capítulo 5 "Problemas de valor inicial para ecuaciones diferenciales ordinarias"
  - Sección 5.2: "Método de Euler" (págs. 275-284) - complejidad
  - Sección 5.4: "Métodos de Runge-Kutta" (págs. 293-306) - complejidad
  - Sección 5.6: "Métodos multipaso" (págs. 317-332) - comparación de eficiencia

**Subtareas:**

1. **Análisis teórico**
   - Contar operaciones por paso:
     * Euler: 1 evaluación de f → O(1)
     * RK4: 4 evaluaciones de f → O(1)
   - Para n pasos:
     * Euler: O(n)
     * RK4: O(4n) = O(n)
   - **Referencia**: Burden Cap. 1, Secc. 1.3; Cap. 5, Secc. 5.2 y 5.4

2. **Medición experimental**
   - Usar `time` o `timeit` en Python
   - Medir tiempo de ejecución
   - Comparar para diferentes n
   - **Referencia**: Burden Cap. 1, Secc. 1.3

3. **Relación precisión vs costo**
   - RK4 más preciso pero ~4× más costoso por paso
   - Pero puede usar h más grande para misma precisión
   - Análisis de eficiencia global
   - **Referencia**: Burden Cap. 5, Secc. 5.4 y 5.6

**Salida esperada**:
- Tabla de complejidad teórica
- Mediciones de tiempo
- Análisis de eficiencia

---

### Tarea 2.7: Validación con benchmarks

**Referencias específicas:**
- **Edwards**: Capítulo 2 "Modelos matemáticos y métodos numéricos"
  - Sección 2.1: "Modelos de población" (págs. 75-84) - ecuación logística
  - **Págs. 81-82**: Ejemplo resuelto (benchmark principal)
  - Sección 2.4-2.6: Ejemplos numéricos de validación
- **Burden**: Capítulo 5 "Problemas de valor inicial para ecuaciones diferenciales ordinarias"
  - Sección 5.2-5.6: Ejemplos y problemas de prueba en cada sección
  - Problemas estándar para validación de métodos

**Subtareas:**

1. **Crear casos de prueba con solución conocida**
   - Caso 1: EDO del Tema 10 (solución analítica conocida)
   - Caso 2: EDO logística estándar: `dP/dt = kP(M-P)`
   - Caso 3: Otros problemas de prueba
   - **Referencia**: Edwards Cap. 2, Secc. 2.1, págs. 81-82

2. **Comparar con solución exacta**
   - Calcular errores en puntos de prueba
   - Verificar precisión de cada método
   - **Referencia**: Burden Cap. 5 (ejemplos en cada sección)

3. **Validación con solvers profesionales**
   - Comparar con `scipy.integrate.odeint`
   - Verificar consistencia
   - **Referencia**: Burden Cap. 5, Secc. 5.4-5.6

**Salida esperada**:
- Conjunto de benchmarks
- Tabla comparativa de precisión
- Validación de implementación

---

## FASE 3: VISUALIZACIÓN Y ANÁLISIS CUALITATIVO

### Tarea 3.1: Campo de isoclinas (Parte A)

**Referencias específicas:**
- **Edwards**: Capítulo 1 "Ecuaciones diferenciales de primer orden"
  - Sección 1.3: "Campos de pendientes y curvas solución" (págs. 17-31)
- **Edwards**: Capítulo 2 "Modelos matemáticos y métodos numéricos"
  - Sección 2.3: "Campos de pendientes y curvas solución" (págs. 93-101)
  - Ejemplos de visualización de isoclinas
- **Burden**: No aplicable (enfoque numérico, no gráfico)

**Subtareas:**

1. **Implementar graficador de isoclinas**
   - Plano (t, P)
   - Ecuación: `dP/dt = β₀e^(-αt)P = C`
   - Resolver para P: `P = Ce^(αt)/β₀`
   - Graficar familia de curvas para diferentes C
   - **Referencia**: Edwards Cap. 2, Secc. 2.3

2. **Superponer soluciones numéricas**
   - Agregar trayectorias calculadas
   - Mostrar convergencia al límite
   - **Referencia**: Edwards Cap. 2, Secc. 2.3

3. **Interpretación cualitativa**
   - Describir patrón de flujo
   - Explicar tendencia hacia población límite
   - Relacionar con biología tumoral
   - **Referencia**: Edwards Cap. 2, Secc. 2.1-2.2

**Herramientas**:
- `matplotlib` para gráficos
- `numpy` para cálculos

**Salida esperada**:
- Gráfico de campo de isoclinas
- Trayectorias superpuestas
- Interpretación escrita

---

### Tarea 3.2: Diagrama de bifurcación (Parte B)

**Referencias específicas:**
- **Edwards**: Capítulo 6 "Sistemas no lineales y fenómenos"
  - Sección 6.5: "Caos en sistemas dinámicos" (págs. 515-530)
  - Incluye diagramas de bifurcación y su interpretación
- **Edwards**: Capítulo 2 "Modelos matemáticos y métodos numéricos"
  - Sección 2.2: "Ecuaciones de equilibrio y estabilidad" (págs. 85-92)
- **Burden**: No aplicable directamente
- **Complemento**: Strogatz "Nonlinear Dynamics and Chaos" para teoría completa

**Subtareas:**

1. **Implementar graficador de bifurcación**
   - Eje x: μ (rango: [-2, 2])
   - Eje y: z* (puntos de equilibrio)
   - Rama 1: z* = 0 (toda μ)
   - Rama 2: z* = √μ (μ > 0)
   - Rama 3: z* = -√μ (μ > 0)
   - **Referencia**: Edwards Cap. 6, Secc. 6.5

2. **Marcar estabilidad**
   - Línea sólida: estable
   - Línea discontinua: inestable
   - Color: cambiar en punto de bifurcación
   - **Referencia**: Edwards Cap. 6, Secc. 6.5

3. **Anotaciones**
   - Marcar μ = 0 (punto crítico)
   - Etiquetar regiones
   - Indicar tipo de bifurcación
   - **Referencia**: Edwards Cap. 6, Secc. 6.5

**Herramientas**:
- `matplotlib` con estilos personalizados

**Salida esperada**:
- Diagrama de bifurcación completo
- Interpretación del fenómeno
- Conexión con modelo poblacional

---

### Tarea 3.3: Plano de fase (Parte C)

**Referencias específicas:**
- **Edwards**: Capítulo 6 "Sistemas no lineales y fenómenos"
  - Sección 6.1: "Estabilidad y el plano de fase" (págs. 447-461)
  - Sección 6.2: "Sistemas lineales y estabilidad" (págs. 462-475)
  - Incluye ejemplos de planos de fase y trayectorias
- **Edwards**: Capítulo 5 "Sistemas lineales de ecuaciones diferenciales"
  - Sección 5.2: "El método del eigenvalor para sistemas lineales" (págs. 347-361)
  - Sección 5.3: "Un álbum de segunda solución de sistemas lineales" (págs. 362-378)
  - Retratos fase para diferentes tipos de puntos críticos
- **Burden**: No aplicable directamente para visualización

**Subtareas:**

1. **Implementar graficador de plano de fase**
   - Plano (x, y)
   - Campo vectorial: (x-y, 2x-3y)
   - Usar `quiver` de matplotlib
   - **Referencia**: Edwards Cap. 6, Secc. 6.1-6.2

2. **Calcular y graficar trayectorias**
   - Resolver sistema numéricamente
   - Diferentes condiciones iniciales
   - Mostrar convergencia al origen
   - **Referencia**: Edwards Cap. 6, Secc. 6.2; Cap. 5, Secc. 5.3

3. **Agregar elementos**
   - Punto crítico (0,0)
   - Eigenvectores (direcciones principales)
   - Nullclinas: x-y=0 y 2x-3y=0
   - **Referencia**: Edwards Cap. 6, Secc. 6.1-6.2

4. **Interpretación**
   - Explicar dinámica de subpoblaciones
   - Describir estabilidad
   - Significado biológico
   - **Referencia**: Edwards Cap. 6, Secc. 6.2

**Herramientas**:
- `matplotlib` para plano de fase
- `scipy.integrate` para trayectorias

**Salida esperada**:
- Diagrama de plano de fase completo
- Múltiples trayectorias
- Análisis cualitativo escrito

---

## FASE 4: DOCUMENTACIÓN Y CÓDIGO

### Tarea 4.1: Crear Jupyter Notebooks interactivos
**Subtareas:**

1. **Notebook 1: Parte A - Modelo del Tumor**
   - Sección 1: Teoría y modelo matemático
   - Sección 2: Solución analítica
   - Sección 3: Soluciones numéricas (comparación)
   - Sección 4: Campo de isoclinas
   - Widgets interactivos para β₀, α, P₀

2. **Notebook 2: Parte B - Bifurcación**
   - Sección 1: Teoría de bifurcaciones
   - Sección 2: Análisis de equilibrios
   - Sección 3: Diagrama de bifurcación interactivo
   - Widget para explorar diferentes μ

3. **Notebook 3: Parte C - Plano de Fase**
   - Sección 1: Sistema lineal y eigenvalores
   - Sección 2: Plano de fase interactivo
   - Sección 3: Trayectorias desde diferentes CI
   - Widgets para condiciones iniciales

4. **Notebook 4: Análisis Numérico Completo**
   - Comparación de métodos
   - Análisis de errores
   - Convergencia
   - Benchmarks

**Herramientas**:
- Jupyter Notebook
- `ipywidgets` para interactividad
- `matplotlib`, `numpy`, `scipy`

**Salida esperada**:
- 4 notebooks completamente funcionales
- Documentación inline clara
- Interactividad para exploración

---

### Tarea 4.2: Dashboard opcional (extra)
**Subtareas:**

1. **Crear dashboard con Plotly Dash o Streamlit**
   - Página 1: Modelo del tumor
   - Página 2: Bifurcación
   - Página 3: Plano de fase
   - Página 4: Comparación de métodos

2. **Características**
   - Sliders para parámetros
   - Gráficos interactivos
   - Actualización en tiempo real

**Herramientas**:
- `plotly` y `dash` o `streamlit`

**Salida esperada** (opcional):
- Dashboard web interactivo
- Facilita presentación

---

### Tarea 4.3: Preparar tablas comparativas
**Subtareas:**

1. **Tabla 1: Comparación de métodos numéricos**
   - Columnas: Método, Error máximo, Orden, Tiempo CPU, Evaluaciones de f
   - Filas: Euler, RK4, (Adams-Bashforth)

2. **Tabla 2: Análisis de convergencia**
   - Columnas: h, Error (Euler), Razón, Error (RK4), Razón
   - Múltiples valores de h

3. **Tabla 3: Puntos de equilibrio y estabilidad**
   - Para Parte B: μ, z*, Eigenvalor, Estabilidad
   - Para Parte C: Punto crítico, Eigenvalores, Tipo, Estabilidad

**Formato**:
- LaTeX para informe
- Markdown para notebooks

**Salida esperada**:
- Tablas formateadas y listas para incluir
- Datos completos y verificados

---

## FASE 5: INFORME TÉCNICO

### Tarea 5.1: Estructura del informe (plantilla JCE MatCom)
**Subtareas:**

1. **Configurar plantilla**
   - Usar `jcematcom.sty`
   - Título: "Análisis de Poblaciones Acotadas mediante la Ecuación Logística"
   - Autores y equipo
   - Resumen (100-200 palabras)
   - Abstract en inglés
   - Palabras clave

2. **Estructura de secciones (máx. 10 páginas)**
   - 1. Introducción (0.5 pág)
   - 2. Modelación matemática (1.5 pág)
   - 3. Análisis teórico (1 pág)
   - 4. Visualización (1.5 pág)
   - 5. Análisis numérico (3 pág)
   - 6. Resultados y discusión (1.5 pág)
   - 7. Conclusiones (0.5 pág)
   - Referencias

**Documentación necesaria**:
- Plantilla en `jcematcom/jcematcom.tex`
- Archivo de estilo `jcematcom.sty`

**Salida esperada**:
- Archivo .tex configurado
- Estructura completa

---

### Tarea 5.2: Redactar contenido
**Subtareas:**

1. **Sección 1: Introducción**
   - Contexto: Crecimiento poblacional y limitaciones
   - Aplicación: Modelos de tumores
   - Objetivos del trabajo
   - Estructura del documento

2. **Sección 2: Modelación matemática**
   - Parte A: Modelo del tumor
     * Deducción de la EDO
     * Parámetros biológicos
     * Condiciones iniciales
   - Parte B: Modelo de bifurcación
     * Reducción del sistema
     * Parámetro de control
   - Parte C: Sistema de subpoblaciones
     * Acoplamiento lineal
     * Matriz del sistema

3. **Sección 3: Análisis teórico**
   - Existencia y unicidad (Teorema de Picard-Lindelöf)
   - Estabilidad de soluciones
   - Análisis de equilibrios
   - Eigenvalores y clasificación

4. **Sección 4: Visualización**
   - Campo de isoclinas (con figura)
   - Diagrama de bifurcación (con figura)
   - Plano de fase (con figura)
   - Interpretación cualitativa

5. **Sección 5: Análisis numérico**
   - Condición del problema
   - Métodos implementados
   - Análisis de errores
   - Orden de convergencia
   - Complejidad computacional
   - Validación con benchmarks
   - Tablas comparativas

6. **Sección 6: Resultados y discusión**
   - Comparación de métodos
   - Ventajas y desventajas
   - Aplicabilidad
   - Limitaciones

7. **Sección 7: Conclusiones**
   - Síntesis de resultados
   - Cumplimiento de objetivos
   - Trabajo futuro

8. **Referencias**
   - Edwards & Penney, 4ta ed.
   - Burden et al., Análisis numérico
   - Otros libros de EDO y análisis numérico

**Salida esperada**:
- Informe completo en LaTeX
- Máximo 10 páginas
- Todas las figuras y tablas incluidas

---

### Tarea 5.3: Figuras y gráficos
**Subtareas:**

1. **Generar figuras de alta calidad**
   - Guardar gráficos en formato PDF o PNG (300 dpi)
   - Títulos y etiquetas claros
   - Leyendas completas

2. **Figuras requeridas**:
   - Fig. 1: Campo de isoclinas con soluciones
   - Fig. 2: Solución P(t) vs tiempo
   - Fig. 3: Diagrama de bifurcación
   - Fig. 4: Plano de fase con trayectorias
   - Fig. 5: Comparación de métodos (errores vs h)
   - Fig. 6: Convergencia (log-log)
   - Fig. 7-10: Otras según necesidad

3. **Insertar en LaTeX**
   - Usar entorno `figure`
   - Referencias correctas `\ref{fig:xxx}`
   - Captions descriptivos

**Salida esperada**:
- Conjunto completo de figuras
- Correctamente referenciadas en texto

---

### Tarea 5.4: Compilar y revisar
**Subtareas:**

1. **Compilar PDF**
   - Usar `pdflatex` o `xelatex`
   - Resolver errores de compilación
   - Verificar formato

2. **Revisión de contenido**
   - Ortografía y gramática
   - Coherencia matemática
   - Secuencia lógica
   - Referencias cruzadas

3. **Verificar límite de páginas**
   - Máximo 10 páginas
   - Ajustar si es necesario

4. **Revisión por pares (dentro del equipo)**
   - Cada miembro revisa secciones de otros
   - Retroalimentación constructiva

**Salida esperada**:
- PDF final del informe
- Listo para entrega

---

## FASE 6: PRESENTACIÓN

### Tarea 6.1: Preparar diapositivas
**Subtareas:**

1. **Estructura (10 minutos = ~10-12 diapositivas)**
   - Diap. 1: Título y equipo
   - Diap. 2: Introducción y motivación
   - Diap. 3: Parte A - Modelo del tumor
   - Diap. 4: Parte A - Solución y isoclinas
   - Diap. 5: Parte B - Bifurcación (teoría)
   - Diap. 6: Parte B - Diagrama de bifurcación
   - Diap. 7: Parte C - Plano de fase
   - Diap. 8: Métodos numéricos
   - Diap. 9: Resultados comparativos
   - Diap. 10: Conclusiones
   - Diap. 11: Demostración interactiva (opcional)
   - Diap. 12: Preguntas

2. **Elementos visuales**
   - Usar figuras generadas
   - Animaciones si es posible
   - Código mínimo (solo fragmentos clave)

**Herramientas**:
- LaTeX Beamer o PowerPoint
- Jupyter Notebook para demo en vivo

**Salida esperada**:
- Presentación completa
- Timing practicado

---

### Tarea 6.2: Preparar demostración interactiva
**Subtareas:**

1. **Seleccionar notebook para demo**
   - Preferir Notebook con widgets
   - Mostrar interactividad

2. **Practicar demo**
   - Tiempo: 2-3 minutos
   - Ensayar transiciones
   - Plan B si falla tecnología

**Salida esperada**:
- Demo lista y probada
- Backup en video (opcional)

---

### Tarea 6.3: Ensayo de presentación
**Subtareas:**

1. **Distribuir roles**
   - Miembro 1: Introducción + Parte A (3 min)
   - Miembro 2: Parte B + Parte C (3 min)
   - Miembro 3: Análisis numérico + Conclusiones (3 min)
   - Todos: Demo (1 min)

2. **Ensayar con cronómetro**
   - Ajustar timing
   - Practicar transiciones

3. **Preparar respuestas a preguntas**
   - Posibles preguntas:
     * ¿Por qué RK4 es mejor que Euler?
     * ¿Qué es una bifurcación de horquilla?
     * ¿Cómo se relaciona con tumores reales?
     * ¿Qué limitaciones tiene el modelo?
   - Preparar respuestas claras

**Salida esperada**:
- Presentación fluida
- Equipo coordinado
- Respuestas preparadas

---

## REQUERIMIENTOS Y RECURSOS

### Requerimientos de Software
- **Python 3.8+**
- **Librerías**:
  - `numpy` (cálculos numéricos)
  - `scipy` (integración de EDO, eigenvalores)
  - `matplotlib` (gráficos)
  - `jupyter` (notebooks)
  - `ipywidgets` (interactividad)
  - `plotly` (gráficos interactivos, opcional)
  - `sympy` (cálculos simbólicos, opcional)
- **LaTeX** (con pdflatex o xelatex)
- **Editor**: VS Code, Overleaf, o similar

### Requerimientos de Documentación

#### DISPONIBLE en las carpetas:
1. **Orientación del proyecto**: `Orientación.pdf` ✓
2. **Plantilla JCE MatCom**: `jcematcom/` ✓
3. **Burden (Análisis numérico)**:
   - Capítulo 1: `Burden_Capitulos/01_capitulo.pdf` ✓ (~1.1 MB)
   - Capítulo 2: `Burden_Capitulos/02_capitulo.pdf` ✓ (~1.1 MB)
4. **Edwards & Penney**:
   - Capítulo 1: `Edwards_Capitulos/01_capitulo.pdf` ✓ (~2.7 MB)
   - Capítulo 2: `Edwards_Capitulos/02_capitulo.pdf` ✓ (~1.3 MB)

#### NECESARIO BUSCAR (si no está en los PDFs):
1. **Edwards & Penney, 4ta edición, págs. 81-82**:
   - Tema: Poblaciones acotadas y ecuación logística
   - Ejemplo resuelto sobre modelo de tumor
   - **ACCIÓN**: Verificar si está en `Edwards_Capitulos/02_capitulo.pdf`
   - **ALTERNATIVA**: Buscar en libro completo o fuentes online

2. **Burden - Capítulos 1 y 2 (temas específicos)**:
   - Cap 1: Existencia y unicidad, análisis de errores
   - Cap 2: Métodos de Euler, RK4, Adams-Bashforth
   - **ACCIÓN**: Leer PDFs disponibles y extraer información relevante

3. **Teoría de bifurcaciones**:
   - No mencionada en materiales básicos
   - **ACCIÓN**: Buscar en:
     * Libros de sistemas dinámicos (Strogatz, "Nonlinear Dynamics and Chaos")
     * Recursos online (Wikipedia, tutoriales)
     * Papers académicos

4. **Análisis de eigenvalues/eigenvectors**:
   - Debería estar en Burden o en libro de Álgebra Lineal
   - **ALTERNATIVA**: Material de cursos previos de Álgebra Lineal

### Recursos Adicionales Recomendados
1. **Libros complementarios**:
   - Zill, "Ecuaciones Diferenciales con aplicaciones de modelado"
   - Strogatz, "Nonlinear Dynamics and Chaos"
   - Chapra & Canale, "Métodos Numéricos para Ingenieros"

2. **Recursos online**:
   - Khan Academy (EDO básicas)
   - MIT OCW (Differential Equations)
   - 3Blue1Brown (visualización de eigenvalores)

3. **Software de verificación**:
   - Wolfram Alpha (soluciones analíticas)
   - MATLAB/Octave (comparación de métodos)
   - Desmos (visualización 2D)

---

## CRONOGRAMA SUGERIDO

### Semana 6 (Revisión de avances - YA PASÓ)
- ✓ Formación del equipo
- ✓ Asignación del tema

### Semanas 7-8: Estudio teórico
- Tarea 1.1: Estudiar teoría logística
- Tarea 1.2: Analizar Parte A
- Tarea 1.3: Analizar Parte B
- Tarea 1.4: Analizar Parte C

### Semanas 9-10: Análisis numérico
- Tarea 2.1-2.2: Análisis del problema
- Tarea 2.3: Implementar métodos
- Tarea 2.4-2.6: Análisis de errores y convergencia
- Tarea 2.7: Validación

### Semanas 11-12: Visualización y código
- Tarea 3.1-3.3: Gráficos (isoclinas, bifurcación, plano de fase)
- Tarea 4.1: Notebooks interactivos
- Tarea 4.2: Dashboard (opcional)
- Tarea 4.3: Tablas

### Semana 13: Documentación
- Tarea 5.1: Estructura del informe
- Tarea 5.2: Redacción
- Tarea 5.3: Figuras
- Tarea 5.4: Compilación y revisión

### Semana 14-16: Presentación y entrega
- Tarea 6.1: Diapositivas
- Tarea 6.2: Demo interactiva
- Tarea 6.3: Ensayo
- **Entrega final y presentación**

---

## CRITERIOS DE EVALUACIÓN (según Orientación)

### Informe técnico (peso estimado: 50%)
- ✓ Introducción y modelado claro
- ✓ Análisis teórico completo (existencia, unicidad, estabilidad)
- ✓ Análisis numérico detallado (errores, convergencia, complejidad)
- ✓ Tablas comparativas bien elaboradas
- ✓ Gráficos de calidad (isoclinas, bifurcación, plano de fase)
- ✓ Máximo 10 páginas respetado
- ✓ Formato JCE MatCom correcto

### Código interactivo (peso estimado: 30%)
- ✓ Notebooks funcionales
- ✓ Interactividad (widgets)
- ✓ Simulaciones para diferentes parámetros
- ✓ Comparativas visuales de métodos
- ✓ Exploración de bifurcaciones y estabilidad
- ✓ Código bien documentado

### Presentación (peso estimado: 20%)
- ✓ Claridad expositiva (10 min)
- ✓ Respuestas a preguntas (5 min)
- ✓ Demostración interactiva
- ✓ Dominio del tema
- ✓ Trabajo en equipo

---

## CHECKLIST FINAL

### Antes de la entrega:
- [ ] Informe PDF compilado y revisado
- [ ] Máximo 10 páginas verificado
- [ ] Todas las figuras incluidas y referenciadas
- [ ] Tablas completas
- [ ] Referencias bibliográficas
- [ ] Código fuente organizado
- [ ] Notebooks funcionales probados
- [ ] README con instrucciones de ejecución
- [ ] Presentación lista
- [ ] Demo probada
- [ ] Ensayo realizado
- [ ] Respuestas a posibles preguntas preparadas

### Estructura de archivos a entregar:
```
Tema_10_Ecuacion_Logistica/
├── Informe/
│   ├── informe.tex
│   ├── informe.pdf
│   ├── jcematcom.sty
│   └── figuras/
│       ├── isoclinas.pdf
│       ├── bifurcacion.pdf
│       ├── plano_fase.pdf
│       └── ...
├── Codigo/
│   ├── README.md
│   ├── requirements.txt
│   ├── Parte_A_Tumor.ipynb
│   ├── Parte_B_Bifurcacion.ipynb
│   ├── Parte_C_Plano_Fase.ipynb
│   ├── Analisis_Numerico.ipynb
│   └── utils/
│       ├── metodos_numericos.py
│       ├── visualizacion.py
│       └── analisis.py
├── Presentacion/
│   ├── presentacion.pdf
│   └── demo_video.mp4 (opcional)
└── Referencias/
    └── bibliografia.bib
```

---

## NOTAS IMPORTANTES

1. **Sobre los PDFs de referencia**:
   - Verificar contenido específico de Edwards págs. 81-82
   - Extraer información relevante de Burden caps 1-2
   - Buscar material complementario si es necesario

2. **Sobre bifurcaciones**:
   - Teoría probablemente NO está en libros básicos
   - Recurrir a fuentes especializadas
   - Aplicar teoría estándar de bifurcaciones de horquilla

3. **Sobre eigenvalores**:
   - Debería estar en Burden o Álgebra Lineal
   - Usar scipy.linalg si es necesario

4. **Sobre límite de tokens**:
   - NO leer PDFs completos (muy grandes)
   - Buscar secciones específicas
   - Usar índices de capítulos
   - Complementar con conocimiento general de EDO

5. **División de trabajo sugerida**:
   - **Miembro 1**: Parte A (tumor) + Métodos numéricos
   - **Miembro 2**: Parte B (bifurcación) + Análisis de errores
   - **Miembro 3**: Parte C (plano de fase) + Visualización
   - **Todos**: Integración, informe, presentación

---

## CONTACTOS Y RECURSOS

### Equipo 10:
- Enrique A. González Moreira
- Heily Rodríguez Rodríguez
- Alex L. Cuervo Grillo

### Profesores (según necesidad):
- Consultar durante orientación docente (Semana 4)
- Aprovechar revisión de avances (Semana 6)

### Recursos computacionales:
- Laboratorios de MatCom
- Computadoras personales
- Google Colab (para notebooks en la nube)

---

## REFLEXIÓN FINAL

Este flujo de trabajo proporciona una **hoja de ruta completa** para resolver el Tema 10. La clave del éxito está en:

1. **Organización**: Seguir el cronograma y dividir el trabajo
2. **Documentación**: Registrar TODO (cálculos, código, decisiones)
3. **Iteración**: Revisar y mejorar continuamente
4. **Comunicación**: Trabajo en equipo efectivo
5. **Rigor**: Verificar cada resultado, tanto teórico como numérico

**¡Éxito con el proyecto!**
