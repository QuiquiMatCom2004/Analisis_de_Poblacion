# Changelog - Análisis de Poblaciones Acotadas

Todos los cambios notables en este proyecto serán documentados en este archivo.

**Formato:** Basado en [Keep a Changelog](https://keepachangelog.com/es/)
**Versionado:** Versionado semántico implícito

---

## [2025-12-02] - Organización y Centralización

### Añadido
- ✅ **Carpeta `Figuras/`**: Nueva carpeta centralizada para todas las imágenes generadas
- ✅ **`Figuras/README.md`**: Documentación completa de todas las figuras (9 archivos, 4.2 MB)
- ✅ **`RESUMEN_PROYECTO.md`**: Documento de revisión completa del proyecto
- ✅ **`CHANGELOG.md`**: Este archivo de control de cambios
- ✅ **Script `Plano_Fase.py`**: Análisis completo del plano de fase (Parte C)
  - Clase `PlanoFaseSistemaLineal`
  - Visualización de campo vectorial, vectores propios, nullclinas y trayectorias
  - Análisis de comportamiento asintótico
  - Clasificación automática de punto crítico
- ✅ **Figuras de Parte C**:
  - `plano_fase.png` (1.1 MB)
  - `comportamiento_asintotico.png` (216 KB)

### Cambiado
- 🔄 **Rutas de guardado**: Todos los scripts actualizados para guardar en `Figuras/`
  - `Analisis_Errores.py`
  - `Grafica_Campo_Isoclinas.py`
  - `Grafica_Comparacion_Soluciones.py`
  - `Diagrama_de_Bifurcacion.py`
  - `Plano_Fase.py`
- 🔄 **Portabilidad**: Uso de rutas relativas con `os.path.join()` en todos los scripts
- 🔄 **Documentación API**: Actualizada a versión 2.3
  - Nueva sección de cambios en v2.3
  - Actualización de rutas de figuras
  - Documentación completa del módulo `Plano_Fase.py`
- 🔄 **Organización de imágenes**: 9 figuras movidas a carpeta `Figuras/`

### Mejorado
- ⚡ **Consistencia**: Verificación completa de nomenclatura y parámetros
- 📚 **Documentación**: Tres nuevos documentos de proyecto
- 🎨 **Visualización**: Figuras organizadas y documentadas

---

## [2025-11-08] - Análisis de Errores Completo

### Añadido
- ✅ **Script `Analisis_Errores.py`**: Análisis comparativo de métodos numéricos
  - Comparación Euler vs RK4 vs solución exacta
  - Cálculo de errores relativos y absolutos
  - Error hacia atrás (backward error)
  - Verificación de orden de convergencia
  - Análisis de complejidad computacional
- ✅ **Figuras de análisis numérico**:
  - `comparacion_metodos_numericos.png` (308 KB)
  - `errores_relativos_tiempo.png` (273 KB)
  - `convergencia_orden.png` (317 KB)
- ✅ **Valores exactos de referencia**: Calculados matemáticamente a mano para t = 1.0, 3.5, 10.0
- ✅ **Secciones del informe**:
  - §5 Análisis Numérico completo
  - §6.3 Análisis de Errores con tablas LaTeX
  - §6.4 Complejidad Computacional

### Mejorado
- 📊 **Visualización de errores**: Gráficos semilog y log-log
- 🔬 **Validación numérica**: Comparación con scipy.integrate.odeint
- 📈 **Orden de convergencia**: Verificación experimental (Euler: p≈1, RK4: p≈4)

---

## [2025-11-07] - Diagrama de Bifurcación

### Añadido
- ✅ **Script `Diagrama_de_Bifurcacion.py`**: Visualización completa del diagrama de bifurcación
  - Función `graficar_bifurcacion()`
  - Función `graficar_bifurcacion_interactiva()` con sliders
  - Análisis de estabilidad de puntos de equilibrio
- ✅ **`ModeloBifurcacion.py`**: Clase para el modelo reducido dz/dt = μz - z³
- ✅ **Figura `diagrama_bifurcacion.png`** (443 KB)
- ✅ **Secciones del informe**:
  - §2.2 Modelo de Bifurcación
  - §3.2 Análisis de Equilibrios y Estabilidad
  - §4.2 Diagrama de Bifurcación
  - Tabla de clasificación de puntos de equilibrio

### Mejorado
- 🎨 **Visualización interactiva**: Sliders para explorar dinámicamente
- 📐 **Análisis matemático**: Bifurcación de horquilla documentada

---

## [2025-10-07] - Arquitectura Modular y Visualizaciones Parte A

### Añadido
- ✅ **Arquitectura modular**: Separación de responsabilidades
  - `Ecuacion_De_Poblacion.py`: Modelo analítico puro (sin matplotlib)
  - `ModeloTumorBase.py`: Clase base abstracta
  - `ModeloTumorEuler.py`: Implementación método de Euler
  - `ModeloTumorRK4.py`: Implementación método RK4
- ✅ **Scripts de visualización**:
  - `Grafica_Campo_Isoclinas.py`
  - `Grafica_Comparacion_Soluciones.py`
  - `Grafica_Interactiva.py` (con sliders)
- ✅ **Figuras de Parte A**:
  - `campo_isoclinas.png` (513 KB)
  - `campo_isoclinas_comparacion.png` (694 KB)
  - `comparacion_soluciones.png` (333 KB)
- ✅ **Documentación API v2.0**: Primera versión completa (~360 líneas)

### Mejorado
- 🏗️ **Polimorfismo**: Interfaz común `ModeloTumorBase` para todos los métodos
- 🔄 **Reutilización**: Modelo matemático independiente de visualización
- 📚 **Mantenibilidad**: Código más limpio y organizado

---

## [2025-10-05] - Informe LaTeX Inicial

### Añadido
- ✅ **Archivo LaTeX**: `Informe_Sobre_Analisis_de_Poblacion.tex`
  - Template JCE MatCom configurado
  - Estructura de secciones definida
  - Resumen en español e inglés
  - Palabras clave y topics
- ✅ **Secciones escritas**:
  - §1 Introducción
  - §2.1 Modelo del Tumor (deducción analítica)
  - §3.1 Existencia y Unicidad (Teorema de Picard-Lindelöf)
- ✅ **Referencias bibliográficas**: Edwards & Penney, Burden et al.

---

## [Inicial] - Estructura del Proyecto

### Añadido
- ✅ **Documentos de planificación**:
  - `README.md`: Descripción general
  - `FLUJO_TRABAJO_TEMA_10.md`: Plan detallado de 6 fases
  - `CLAUDE.md`: Guía para Claude Code
- ✅ **Carpeta `Documentation/`**:
  - Edwards & Penney (PDF ~35 MB)
  - Burden et al. (PDF ~7.6 MB)
  - Orientación del proyecto (PDF)
  - `Readme.md` explicativo
- ✅ **Carpeta `Scripts/`**:
  - Estructura inicial
  - `requirements.txt` con dependencias
  - `Isoclina_Edo.py` (script integrador principal)
- ✅ **Template LaTeX**: `jcematcom.sty`

### Configurado
- 🐍 **Entorno Python**: Dependencias instaladas
  - numpy >= 1.24.0
  - matplotlib >= 3.7.0
  - scipy >= 1.10.0
  - jupyter >= 1.0.0
  - ipywidgets >= 8.0.0
  - sympy >= 1.12

---

## Resumen de Versiones

| Versión | Fecha | Descripción | Archivos | Estado |
|---------|-------|-------------|----------|--------|
| **v2.3** | 2025-12-02 | Organización y Parte C | +4 docs, 9 figuras | ✅ Actual |
| **v2.2** | 2025-11-08 | Análisis de errores | +4 archivos | ✅ Completo |
| **v2.1** | 2025-11-07 | Bifurcación | +3 archivos | ✅ Completo |
| **v2.0** | 2025-10-07 | Arquitectura modular | +7 archivos | ✅ Completo |
| **v1.1** | 2025-10-05 | Informe LaTeX inicial | +1 archivo | ✅ Completo |
| **v1.0** | Inicial | Estructura base | +10 archivos | ✅ Completo |

---

## Estadísticas del Proyecto

### Archivos por Tipo

| Tipo | Cantidad | Tamaño aprox. |
|------|----------|---------------|
| **Python (.py)** | 11 | ~2,500 líneas |
| **Markdown (.md)** | 6 | ~3,500 líneas |
| **LaTeX (.tex)** | 1 | ~850 líneas |
| **Imágenes (.png)** | 9 | 4.2 MB |
| **PDFs (biblio)** | 3 | 43 MB |

### Progreso del Proyecto

- ✅ **Código:** 100% completado (11/11 scripts)
- ✅ **Visualizaciones:** 100% completadas (9/9 figuras)
- ✅ **Documentación:** 100% completa (6/6 documentos)
- ⚠️ **Informe:** 90% completado (~7.5/10 páginas)
- ⏸️ **Notebooks:** 0% (opcional)
- ⏸️ **Presentación:** 0% (pendiente)

**Estado general:** 95% COMPLETO

---

## Próximas Versiones (Planificado)

### [Próximo] - Finalización del Informe

#### Por hacer
- [ ] Completar §6 Resultados y Discusión
- [ ] Completar §7 Conclusiones
- [ ] Incluir figura `plano_fase.png` en §4.3
- [ ] Compilar PDF final
- [ ] Revisión ortográfica y gramatical

### [Futuro] - Notebooks Interactivos (Opcional)

#### Por hacer
- [ ] `Parte_A_Tumor.ipynb`
- [ ] `Parte_B_Bifurcacion.ipynb`
- [ ] `Parte_C_Plano_Fase.ipynb`
- [ ] `Analisis_Numerico.ipynb`

### [Futuro] - Presentación

#### Por hacer
- [ ] Diseño de slides (10 min)
- [ ] Selección de figuras clave
- [ ] Ensayo de presentación
- [ ] Material de apoyo Q&A (5 min)

---

## Notas de Mantenimiento

### Contribuidores
- Enrique A. González Moreira
- Heily Rodríguez Rodríguez
- Alex L. Cuervo Grillo

### Asistentes
- Claude Code (Anthropic) - Desarrollo y documentación

### Repositorio
- **Ubicación:** `/home/kiki/Proyectos/Analisis_de_Poblacion`
- **Git:** Inicializado (branch: main)
- **Último commit:** e4cd116 - "feat: Add analysis of subpopulation dynamics and stability in the report"

---

**Última actualización:** 2025-12-02
**Mantenido por:** E. González, H. Rodríguez, A. Cuervo
