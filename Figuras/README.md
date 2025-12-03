# Figuras Generadas - Análisis de Poblaciones Acotadas

Esta carpeta contiene todas las figuras generadas por los scripts del proyecto de análisis de poblaciones acotadas mediante la ecuación logística.

**Autores:** Enrique A. González Moreira, Heily Rodríguez Rodríguez, Alex L. Cuervo Grillo
**Asignaturas:** Matemática Numérica y Ecuaciones Diferenciales Ordinarias
**Fecha:** 2025-12-02

---

## Organización de Figuras por Parte del Proyecto

### Parte A: Modelo de Crecimiento Tumoral

**Modelo:** `dP/dt = β₀e^(-αt)P, P(0) = P₀`

| Archivo | Dimensiones | Script Generador | Descripción |
|---------|------------|------------------|-------------|
| `campo_isoclinas.png` | 513 KB | `Grafica_Campo_Isoclinas.py` | Campo de isoclinas con solución analítica, campo de direcciones y límite asintótico |
| `campo_isoclinas_comparacion.png` | 694 KB | `Grafica_Campo_Isoclinas.py` | Comparación de soluciones analítica, Euler y RK4 sobre campo de isoclinas |
| `comparacion_soluciones.png` | 333 KB | `Grafica_Comparacion_Soluciones.py` | Familia de soluciones con diferentes condiciones iniciales (P₀ = 50, 100, 150, 200) |

**Características visualizadas:**
- Curvas de isoclinas (familia de soluciones implícitas)
- Solución analítica para P₀ = 100
- Campo de direcciones (vectores tangentes)
- Límite asintótico P∞ = P₀ exp(β₀/α)

---

### Parte A: Análisis Numérico

**Métodos implementados:** Euler explícito (orden 1) y Runge-Kutta 4 (orden 4)

| Archivo | Dimensiones | Script Generador | Descripción |
|---------|------------|------------------|-------------|
| `comparacion_metodos_numericos.png` | 308 KB | `Analisis_Errores.py` | Comparación visual de soluciones exactas vs aproximaciones numéricas para h = 0.1, 0.05, 0.01 |
| `errores_relativos_tiempo.png` | 273 KB | `Analisis_Errores.py` | Evolución temporal del error relativo (escala semilog) para ambos métodos |
| `convergencia_orden.png` | 317 KB | `Analisis_Errores.py` | Gráfico log-log verificando órdenes de convergencia teóricos (Euler: O(h), RK4: O(h⁴)) |

**Métricas analizadas:**
- Error absoluto y relativo
- Orden de convergencia experimental vs teórico
- Error hacia atrás (backward error)
- Complejidad computacional

**Puntos de evaluación:** t = 1.0, 3.5, 10.0
**Tamaños de paso:** h = 0.1, 0.05, 0.01
**Valores exactos:** Calculados matemáticamente a mano (sin errores de redondeo)

---

### Parte B: Modelo de Bifurcación

**Modelo:** `dz/dt = μz - z³`

| Archivo | Dimensiones | Script Generador | Descripción |
|---------|------------|------------------|-------------|
| `diagrama_bifurcacion.png` | 443 KB | `Diagrama_de_Bifurcacion.py` | Diagrama de bifurcación mostrando bifurcación de horquilla (pitchfork) en μ = 0 |

**Elementos visualizados:**
- Puntos de equilibrio estables (líneas continuas)
- Puntos de equilibrio inestables (líneas discontinuas)
- Punto de bifurcación en μ = 0
- Regiones de estabilidad sombreadas

**Puntos de equilibrio:**
- μ < 0: z* = 0 (estable)
- μ = 0: Bifurcación
- μ > 0: z* = 0 (inestable), z* = ±√μ (estables)

---

### Parte C: Sistema de Subpoblaciones

**Sistema:** `dx/dt = x - y, dy/dt = 2x - 3y`

| Archivo | Dimensiones | Script Generador | Descripción |
|---------|------------|------------------|-------------|
| `plano_fase.png` | 1.1 MB | `Plano_Fase.py` | Plano de fase completo con campo vectorial, trayectorias, vectores propios y nullclinas |
| `comportamiento_asintotico.png` | 216 KB | `Plano_Fase.py` | Análisis temporal en direcciones estable (λ₂ < 0) e inestable (λ₁ > 0) |

**Elementos del plano de fase:**
- Campo vectorial (quiver) coloreado por magnitud
- Vectores propios: v₁ (rojo, λ₁ ≈ 0.414, inestable), v₂ (azul, λ₂ ≈ -2.414, estable)
- Líneas propias (rectas por el origen)
- Nullclinas: dx/dt = 0 (verde), dy/dt = 0 (magenta)
- 12 trayectorias desde condiciones iniciales variadas
- Punto crítico (0,0) - clasificado como PUNTO SILLA

**Análisis de estabilidad:**
- Valores propios: λ₁ = -1 + √2, λ₂ = -1 - √2
- Clasificación: Punto silla (inestable)
- Dirección estable: trayectorias convergen al origen
- Dirección inestable: trayectorias divergen del origen

---

## Especificaciones Técnicas

### Configuración de Generación

- **Resolución:** 300 DPI (alta calidad para publicación)
- **Formato:** PNG con compresión
- **Backend:** matplotlib (versión ≥ 3.7.0)
- **Formato de guardado:** `bbox_inches='tight'` (elimina márgenes innecesarios)

### Paletas de Colores Utilizadas

- **Campo vectorial:** Colormap 'viridis' (perceptualmente uniforme)
- **Isoclinas:** Colormap 'tab10' o 'viridis'
- **Estabilidad:** Verde (estable), Rojo (inestable)
- **Métodos numéricos:** Azul (exacto), Naranja (Euler), Verde (RK4)

---

## Regeneración de Figuras

Para regenerar todas las figuras, ejecutar en orden:

```bash
# Desde el directorio raíz del proyecto

# Parte A - Modelo de Tumor
cd Scripts
python Grafica_Campo_Isoclinas.py
python Grafica_Comparacion_Soluciones.py

# Parte A - Análisis Numérico
python Analisis_Errores.py

# Parte B - Bifurcación
python Diagrama_de_Bifurcacion.py

# Parte C - Plano de Fase
python Plano_Fase.py
```

Todas las figuras se generarán automáticamente en la carpeta `Figuras/`.

---

## Uso en el Informe LaTeX

Para incluir las figuras en el informe, usar:

```latex
\begin{figure}[H]
    \centering
    \includegraphics[width=0.45\textwidth]{Figuras/campo_isoclinas.png}
    \caption{Campo de isoclinas y solución analítica para el modelo del tumor.}
    \label{fig:isoclinas}
\end{figure}
```

**Nota:** Ajustar el parámetro `width` según el layout de dos columnas del template JCE MatCom.

---

## Notas de Versión

**Versión 1.0** (2025-12-02):
- Organización inicial de todas las figuras
- Carpeta centralizada para gestión de imágenes
- Actualización de todos los scripts para guardar en `Figuras/`
- README con documentación completa

---

## Estructura de Archivos

```
Figuras/
├── README.md                           # Este archivo
├── campo_isoclinas.png                 # Parte A
├── campo_isoclinas_comparacion.png     # Parte A
├── comparacion_soluciones.png          # Parte A
├── comparacion_metodos_numericos.png   # Análisis Numérico
├── errores_relativos_tiempo.png        # Análisis Numérico
├── convergencia_orden.png              # Análisis Numérico
├── diagrama_bifurcacion.png            # Parte B
├── plano_fase.png                      # Parte C
└── comportamiento_asintotico.png       # Parte C
```

Total: 9 figuras, 4.2 MB

---

**Última actualización:** 2025-12-02
**Mantenedores:** E. González, H. Rodríguez, A. Cuervo
