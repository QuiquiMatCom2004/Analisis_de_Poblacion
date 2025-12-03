# Documentación de API - Scripts de Análisis de Población

Este documento describe todos los métodos disponibles en los scripts del proyecto, organizados por módulo.

**Última actualización:** 2025-10-07
**Versión:** 2.0 - Arquitectura Modular
**Asignaturas:** Matemática Numérica y Ecuaciones Diferenciales Ordinarias

---

## Arquitectura del Proyecto

El proyecto está organizado en módulos separados siguiendo el principio de separación de responsabilidades:

- **`Ecuacion_De_Poblacion.py`**: Modelo matemático (cálculos puros, sin visualización)
- **`Grafica_Campo_Isoclinas.py`**: Visualización del campo de isoclinas
- **`Grafica_Comparacion_Soluciones.py`**: Visualización comparativa de soluciones
- **`Grafica_Interactiva.py`**: Visualización interactiva con sliders
- **`Isoclina_Edo.py`**: Script principal que integra todos los módulos

---

## Módulo: `Ecuacion_De_Poblacion.py`

**Descripción general:** Contiene la clase `ModeloTumor` que encapsula todos los cálculos matemáticos del modelo de crecimiento de tumor. Este módulo es independiente de matplotlib y solo maneja la lógica matemática.

### Clase: `ModeloTumor`

**Ecuación diferencial:** dP/dt = β₀e^(-αt)P
**Solución analítica:** P(t) = P₀ exp(β₀/α (1 - e^(-αt)))
**Límite asintótico:** lim(t→∞) P(t) = P₀ exp(β₀/α)

#### Constructor

| Método | Parámetros | Descripción / Retorno |
|--------|------------|----------------------|
| `__init__(P0, beta0, alpha)` | `P0` (float): Población inicial<br>`beta0` (float): Tasa de crecimiento inicial (β₀)<br>`alpha` (float): Tasa de decrecimiento exponencial (α) | **Descripción:** Inicializa el modelo con los parámetros dados.<br>**Retorna:** Instancia de `ModeloTumor` |

#### Métodos de Cálculo

| Método | Parámetros | Descripción / Retorno |
|--------|------------|----------------------|
| `ecuacion_diferencial(t, P)` | `t` (float/array): Tiempo<br>`P` (float/array): Población | **Descripción:** Calcula dP/dt según el modelo.<br>**Retorna:** `float/array` - dP/dt = β₀e^(-αt)P |
| `solucion_analitica(t)` | `t` (float/array): Tiempo(s) | **Descripción:** Calcula la solución analítica exacta.<br>**Retorna:** `float/array` - P(t) |
| `isoclina(t, C)` | `t` (array): Valores de tiempo<br>`C` (float): Constante de isoclina | **Descripción:** Calcula curva isoclina P = C·e^(αt).<br>**Retorna:** `array` - P(t) para la isoclina |
| `limite_asintotico()` | Ninguno | **Descripción:** Calcula P∞ = P₀ exp(β₀/α).<br>**Retorna:** `float` - Límite asintótico |
| `factor_crecimiento()` | Ninguno | **Descripción:** Calcula exp(β₀/α).<br>**Retorna:** `float` - Factor de crecimiento |
| `tasa_crecimiento(t)` | `t` (float/array): Tiempo(s) | **Descripción:** Calcula r(t) = β₀e^(-αt).<br>**Retorna:** `float/array` - Tasa de crecimiento |
| `campo_direcciones(t_grid, P_grid)` | `t_grid` (array 2D): Grilla de tiempo<br>`P_grid` (array 2D): Grilla de población | **Descripción:** Calcula vectores normalizados del campo de direcciones.<br>**Retorna:** `tuple(dT_norm, dP_norm)` |
| `generar_isoclinas(t, num_isoclinas, rango_factor)` | `t` (array): Valores de tiempo<br>`num_isoclinas` (int, opcional): Cantidad (default: 8)<br>`rango_factor` (tuple, opcional): Rango (default: (0.2, 1.5)) | **Descripción:** Genera múltiples isoclinas para visualización.<br>**Retorna:** `list` - Lista de tuplas `(C, P_isoclina)` |
| `__repr__()` | Ninguno | **Descripción:** Representación en string del modelo.<br>**Retorna:** `str` - Información del modelo |

#### Función Auxiliar

| Función | Parámetros | Descripción / Retorno |
|---------|------------|----------------------|
| `crear_modelo(P0, beta0, alpha)` | `P0` (float): Población inicial<br>`beta0` (float): Tasa de crecimiento<br>`alpha` (float): Tasa de decrecimiento | **Descripción:** Helper para crear instancia del modelo.<br>**Retorna:** `ModeloTumor` |

#### Ejemplo de Uso

```python
from Ecuacion_De_Poblacion import ModeloTumor
import numpy as np

# Crear modelo
modelo = ModeloTumor(P0=100, beta0=2.0, alpha=0.5)
print(modelo)  # Muestra info del modelo

# Evaluar solución en puntos específicos
t_vals = np.array([0, 5, 10, 15, 20])
P_vals = modelo.solucion_analitica(t_vals)

# Calcular derivada
dP_dt = modelo.ecuacion_diferencial(t=5.0, P=150.0)

# Generar isoclinas
t = np.linspace(0, 10, 100)
isoclinas = modelo.generar_isoclinas(t, num_isoclinas=5)
```

---

## Módulo: `Grafica_Campo_Isoclinas.py`

**Descripción general:** Visualización del campo de isoclinas, solución analítica y campo de direcciones.

### Funciones de Visualización

| Función | Parámetros | Descripción / Retorno |
|---------|------------|----------------------|
| `graficar_campo_isoclinas(modelo, t_max, num_isoclinas, figsize, guardar)` | `modelo` (ModeloTumor): Instancia del modelo<br>`t_max` (float, opcional): Tiempo máximo (default: 10)<br>`num_isoclinas` (int, opcional): Cantidad (default: 8)<br>`figsize` (tuple, opcional): Tamaño figura (default: (12, 8))<br>`guardar` (str, opcional): Ruta archivo (default: None) | **Descripción:** Genera gráfico completo con isoclinas, solución analítica, campo de direcciones y límite asintótico.<br>**Retorna:** `tuple(fig, ax)` |

#### Ejemplo de Uso

```python
from Ecuacion_De_Poblacion import ModeloTumor
from Grafica_Campo_Isoclinas import graficar_campo_isoclinas

modelo = ModeloTumor(P0=100, beta0=2.0, alpha=0.5)
fig, ax = graficar_campo_isoclinas(
    modelo,
    t_max=15,
    num_isoclinas=10,
    guardar='campo_isoclinas.png'
)
```

---

## Módulo: `Grafica_Comparacion_Soluciones.py`

**Descripción general:** Visualización comparativa de múltiples soluciones con diferentes condiciones iniciales.

### Funciones de Visualización

| Función | Parámetros | Descripción / Retorno |
|---------|------------|----------------------|
| `graficar_comparacion_soluciones(P0_values, beta0, alpha, t_max, figsize, guardar)` | `P0_values` (list): Lista de poblaciones iniciales<br>`beta0` (float): Tasa de crecimiento<br>`alpha` (float): Tasa de decrecimiento<br>`t_max` (float, opcional): Tiempo máximo (default: 10)<br>`figsize` (tuple, opcional): Tamaño figura (default: (12, 8))<br>`guardar` (str, opcional): Ruta archivo (default: None) | **Descripción:** Grafica múltiples soluciones con diferentes P₀, mostrando convergencia a límites asintóticos.<br>**Retorna:** `tuple(fig, ax)` |

#### Ejemplo de Uso

```python
from Grafica_Comparacion_Soluciones import graficar_comparacion_soluciones

fig, ax = graficar_comparacion_soluciones(
    P0_values=[50, 100, 150, 200],
    beta0=2.0,
    alpha=0.5,
    t_max=12,
    guardar='comparacion.png'
)
```

---

## Módulo: `Grafica_Interactiva.py`

**Descripción general:** Visualización interactiva con sliders para manipular parámetros en tiempo real. Incluye tres subgráficos sincronizados: población vs tiempo, tasa de crecimiento, y diagrama de fase.

### Funciones de Visualización

| Función | Parámetros | Descripción / Retorno |
|---------|------------|----------------------|
| `graficar_interactivo(P0_init, beta0_init, alpha_init, t_max)` | `P0_init` (float, opcional): P₀ inicial (default: 1.0)<br>`beta0_init` (float, opcional): β₀ inicial (default: 2.0)<br>`alpha_init` (float, opcional): α inicial (default: 0.5)<br>`t_max` (float, opcional): Tiempo máximo (default: 15) | **Descripción:** Crea visualización interactiva con sliders para P₀ (0.1-5.0), β₀ (0.1-5.0), α (0.1-3.0). Incluye texto informativo dinámico.<br>**Retorna:** `None` (muestra gráfico interactivo) |

#### Ejemplo de Uso

```python
from Grafica_Interactiva import graficar_interactivo

# Lanzar visualización interactiva
graficar_interactivo(P0_init=1.0, beta0_init=2.0, alpha_init=0.5)
```

---

## Dependencias Externas

### NumPy

| Método Usado | Parámetros | Descripción / Retorno |
|--------------|------------|----------------------|
| `np.linspace(start, stop, num)` | `start` (float): Valor inicial<br>`stop` (float): Valor final<br>`num` (int): Número de puntos | **Descripción:** Genera array de valores uniformemente espaciados.<br>**Retorna:** `ndarray` |
| `np.exp(x)` | `x` (array_like): Valor(es) de entrada | **Descripción:** Calcula exponencial e^x.<br>**Retorna:** `array_like` |
| `np.sqrt(x)` | `x` (array_like): Valor(es) de entrada | **Descripción:** Calcula raíz cuadrada.<br>**Retorna:** `array_like` |
| `np.ones_like(a)` | `a` (array_like): Array de referencia | **Descripción:** Crea array de unos con misma forma que `a`.<br>**Retorna:** `ndarray` |
| `np.meshgrid(x, y)` | `x` (array_like): Coordenadas x<br>`y` (array_like): Coordenadas y | **Descripción:** Genera grilla 2D de coordenadas.<br>**Retorna:** `tuple(X, Y)` - Arrays 2D |
| `np.arange(start, stop, step)` | `start` (int): Inicio<br>`stop` (int): Fin<br>`step` (int): Paso | **Descripción:** Genera secuencia de enteros.<br>**Retorna:** `ndarray` |
| `np.c_[a, b]` | `a, b` (array): Arrays a concatenar | **Descripción:** Concatena arrays por columnas.<br>**Retorna:** `ndarray` |
| `np.array(list)` | `list` (list): Lista de valores | **Descripción:** Convierte lista a array NumPy.<br>**Retorna:** `ndarray` |

### Matplotlib

| Método Usado | Parámetros | Descripción / Retorno |
|--------------|------------|----------------------|
| `plt.figure(figsize)` | `figsize` (tuple): Tamaño (ancho, alto) en pulgadas | **Descripción:** Crea nueva figura.<br>**Retorna:** `Figure` |
| `plt.subplots(figsize)` | `figsize` (tuple): Tamaño (ancho, alto) en pulgadas | **Descripción:** Crea figura y ejes.<br>**Retorna:** `tuple(fig, ax)` |
| `fig.add_gridspec(nrows, ncols, height_ratios, hspace, wspace)` | `nrows, ncols` (int): Filas/columnas<br>`height_ratios` (list): Proporciones altura<br>`hspace, wspace` (float): Espaciado | **Descripción:** Crea especificación de grilla para subplots.<br>**Retorna:** `GridSpec` |
| `fig.add_subplot(gridspec)` | `gridspec`: Posición en grilla | **Descripción:** Añade subplot a la figura.<br>**Retorna:** `Axes` |
| `ax.plot(x, y, ...)` | `x, y` (array): Coordenadas<br>`kwargs`: Opciones (color, linewidth, label, etc.) | **Descripción:** Grafica línea 2D.<br>**Retorna:** `list` - Objetos Line2D |
| `ax.scatter(x, y, c, cmap, s, alpha, vmin, vmax)` | `x, y` (array): Coordenadas<br>`c` (array): Colores<br>`cmap` (str): Mapa de colores<br>`s` (int): Tamaño<br>`alpha` (float): Transparencia<br>`vmin, vmax` (float): Rango colores | **Descripción:** Grafica puntos dispersos con colores.<br>**Retorna:** `PathCollection` |
| `ax.quiver(X, Y, U, V, ...)` | `X, Y` (array 2D): Posiciones<br>`U, V` (array 2D): Componentes vectores<br>`kwargs`: Opciones (alpha, width, etc.) | **Descripción:** Grafica campo vectorial.<br>**Retorna:** `Quiver` |
| `ax.axhline(y, ...)` | `y` (float): Posición vertical<br>`kwargs`: Opciones (color, linestyle, linewidth, label) | **Descripción:** Dibuja línea horizontal.<br>**Retorna:** `Line2D` |
| `ax.fill_between(x, y1, y2, alpha, color)` | `x` (array): Coordenadas x<br>`y1, y2` (array): Límites verticales<br>`alpha` (float): Transparencia<br>`color` (str): Color | **Descripción:** Rellena área entre dos curvas.<br>**Retorna:** `PolyCollection` |
| `ax.set_xlabel(label, fontsize, fontweight)` | `label` (str): Texto<br>`fontsize` (int): Tamaño<br>`fontweight` (str): Peso | **Descripción:** Etiqueta eje X.<br>**Retorna:** `Text` |
| `ax.set_ylabel(label, fontsize, fontweight)` | `label` (str): Texto<br>`fontsize` (int): Tamaño<br>`fontweight` (str): Peso | **Descripción:** Etiqueta eje Y.<br>**Retorna:** `Text` |
| `ax.set_title(label, fontsize, fontweight, pad)` | `label` (str): Título<br>`fontsize` (int): Tamaño<br>`fontweight` (str): Peso<br>`pad` (float): Espaciado | **Descripción:** Título del gráfico.<br>**Retorna:** `Text` |
| `ax.grid(bool, alpha, linestyle)` | `bool`: Activar/desactivar<br>`alpha` (float): Transparencia<br>`linestyle` (str): Estilo línea | **Descripción:** Muestra grilla.<br>**Retorna:** `None` |
| `ax.legend(loc, fontsize)` | `loc` (str): Ubicación<br>`fontsize` (int): Tamaño fuente | **Descripción:** Muestra leyenda.<br>**Retorna:** `Legend` |
| `ax.set_xlim(left, right)` | `left, right` (float): Límites | **Descripción:** Límites eje X.<br>**Retorna:** `tuple` |
| `ax.set_ylim(bottom, top)` | `bottom, top` (float): Límites | **Descripción:** Límites eje Y.<br>**Retorna:** `tuple` |
| `plt.tight_layout()` | Ninguno | **Descripción:** Ajusta espaciado automáticamente.<br>**Retorna:** `None` |
| `plt.savefig(filename, dpi, bbox_inches)` | `filename` (str): Nombre archivo<br>`dpi` (int): Resolución<br>`bbox_inches` (str): Ajuste bordes | **Descripción:** Guarda gráfico.<br>**Retorna:** `None` |
| `plt.show()` | Ninguno | **Descripción:** Muestra gráficos.<br>**Retorna:** `None` |
| `plt.axes([left, bottom, width, height])` | `left, bottom, width, height` (float): Posición y tamaño | **Descripción:** Crea nuevos ejes en posición específica.<br>**Retorna:** `Axes` |
| `plt.suptitle(title, fontsize, fontweight, y)` | `title` (str): Título<br>`fontsize` (int): Tamaño<br>`fontweight` (str): Peso<br>`y` (float): Posición vertical | **Descripción:** Título general de la figura.<br>**Retorna:** `Text` |
| `cm.viridis(x)` | `x` (array): Valores normalizados 0-1 | **Descripción:** Colores del mapa viridis.<br>**Retorna:** `array` - Colores RGBA |
| `cm.tab10(x)` | `x` (array): Valores normalizados 0-1 | **Descripción:** Colores del mapa tab10.<br>**Retorna:** `array` - Colores RGBA |
| `fig.text(x, y, text, fontsize, family, bbox)` | `x, y` (float): Posición<br>`text` (str): Texto<br>`fontsize` (int): Tamaño<br>`family` (str): Familia fuente<br>`bbox` (dict): Cuadro de fondo | **Descripción:** Añade texto a la figura.<br>**Retorna:** `Text` |
| `fig.canvas.draw_idle()` | Ninguno | **Descripción:** Redibuja la figura (para gráficos interactivos).<br>**Retorna:** `None` |

### Matplotlib.widgets

| Método Usado | Parámetros | Descripción / Retorno |
|--------------|------------|----------------------|
| `Slider(ax, label, valmin, valmax, valinit, color)` | `ax` (Axes): Ejes para el slider<br>`label` (str): Etiqueta<br>`valmin, valmax` (float): Rango<br>`valinit` (float): Valor inicial<br>`color` (str): Color | **Descripción:** Crea slider interactivo.<br>**Retorna:** `Slider` |
| `slider.on_changed(func)` | `func` (callable): Función callback | **Descripción:** Conecta función a cambios del slider.<br>**Retorna:** `int` - ID de conexión |
| `slider.val` | Propiedad (lectura) | **Descripción:** Obtiene valor actual del slider.<br>**Retorna:** `float` |

---

## Notas de Implementación

### Convenciones de Nombres

- **Variables de parámetros:** `beta0`, `alpha` (sin símbolos especiales)
- **Variables de población:** `P`, `P0`, `P_inf`
- **Variables de tiempo:** `t`, `t_max`
- **Objetos matplotlib:** `fig`, `ax`
- **Clases:** PascalCase (`ModeloTumor`)
- **Funciones:** snake_case (`graficar_campo_isoclinas`)

### Arquitectura Modular

La separación de responsabilidades permite:
- **Reutilización:** El modelo matemático puede usarse en cualquier contexto
- **Testing:** Probar cálculos sin dependencias gráficas
- **Mantenibilidad:** Modificar visualizaciones sin tocar la lógica matemática
- **Extensibilidad:** Agregar nuevos tipos de gráficos fácilmente

### Gestión de Gráficos

Todos los métodos de graficación devuelven `(fig, ax)` para personalización posterior:

```python
fig, ax = graficar_campo_isoclinas(modelo)
ax.set_xlim(0, 20)  # Personalizar después
ax.text(5, 100, 'Anotación')  # Agregar texto
plt.savefig('custom.png')
```

### Manejo de Arrays

Las funciones del modelo aceptan escalares y arrays:

```python
# Escalar
dP_dt = modelo.ecuacion_diferencial(t=5.0, P=100)

# Array
t_vals = np.array([1, 2, 3, 4, 5])
P_vals = modelo.solucion_analitica(t_vals)
```

---

## Estructura de Archivos Generados

```
Scripts/
├── Ecuacion_De_Poblacion.py          # Modelo matemático (clase)
├── Grafica_Campo_Isoclinas.py        # Visualización isoclinas
├── Grafica_Comparacion_Soluciones.py # Visualización comparativa
├── Grafica_Interactiva.py            # Visualización interactiva
├── DOCUMENTACION_API.md              # Esta documentación
└── requirements.txt                  # Dependencias Python
```

**Directorio de figuras:**
- **Todas las figuras se guardan en:** `../Figuras/`
- Ruta configurada mediante: `FIGURAS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Figuras')`
- La carpeta se crea automáticamente si no existe: `os.makedirs(FIGURAS_DIR, exist_ok=True)`

**Archivos generados por ejecución:**
- `Figuras/campo_isoclinas.png` (513 KB, 300 DPI)
- `Figuras/campo_isoclinas_comparacion.png` (694 KB, 300 DPI)
- `Figuras/comparacion_soluciones.png` (333 KB, 300 DPI)
- `Figuras/comparacion_metodos_numericos.png` (308 KB, 300 DPI) - generado por `Analisis_Errores.py`
- `Figuras/errores_relativos_tiempo.png` (273 KB, 300 DPI) - generado por `Analisis_Errores.py`
- `Figuras/convergencia_orden.png` (317 KB, 300 DPI) - generado por `Analisis_Errores.py`
- `Figuras/diagrama_bifurcacion.png` (443 KB, 300 DPI) - generado por `Diagrama_de_Bifurcacion.py`
- `Figuras/plano_fase.png` (1.1 MB, 300 DPI) - generado por `Plano_Fase.py`
- `Figuras/comportamiento_asintotico.png` (216 KB, 300 DPI) - generado por `Plano_Fase.py`

---

## Módulo: `Analisis_Errores.py`

**Descripción general:** Script de análisis comparativo de errores entre los métodos de Euler y RK4 contra soluciones exactas calculadas matemáticamente a mano (sin errores de redondeo computacional).

### Parámetros Fijos del Análisis

| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| `P0` | 100.0 | Población inicial |
| `beta0` | 2.0 | Tasa de crecimiento inicial |
| `alpha` | 0.5 | Tasa de decrecimiento exponencial |
| `t_eval` | [1.0, 3.5, 10.0] | Puntos de evaluación no equidistantes |
| `h_values` | [0.1, 0.05, 0.01] | Tamaños de paso analizados |

### Valores Exactos de Referencia

Calculados matemáticamente usando la fórmula analítica (sin errores computacionales):

| Tiempo | Valor Exacto |
|--------|--------------|
| t = 1.0 | P(1.0) = 482.532148288934 |
| t = 3.5 | P(3.5) = 2724.593201734644 |
| t = 10.0 | P(10.0) = 5314.628532833040 |

### Salidas del Script

#### Gráficos Generados

| Archivo | Descripción |
|---------|-------------|
| `comparacion_metodos_numericos.png` | 3 subplots comparando soluciones exactas vs Euler vs RK4 para h=[0.1, 0.05, 0.01] |
| `errores_relativos_tiempo.png` | 3 subplots (escala semilog) mostrando evolución del error relativo en función del tiempo |
| `convergencia_orden.png` | Gráfico log-log del error máximo vs tamaño de paso con líneas de referencia teóricas O(h) y O(h⁴) |

#### Archivos de Texto

| Archivo | Descripción |
|---------|-------------|
| `resultados_analisis_errores_latex.txt` | Tablas LaTeX listas para copiar al informe con todos los resultados numéricos |

### Métricas Calculadas

| Métrica | Fórmula | Descripción |
|---------|---------|-------------|
| Error Absoluto | `\|P_exacto - P_numerico\|` | Diferencia absoluta entre solución exacta y numérica |
| Error Relativo (%) | `(\|P_exacto - P_numerico\| / \|P_exacto\|) × 100` | Error como porcentaje del valor exacto |
| Orden de Convergencia | `p ≈ log(E2/E1) / log(h2/h1)` | Orden experimental verificado contra teórico (Euler: 1, RK4: 4) |

### Resultados Clave del Análisis

**Errores Máximos por Tamaño de Paso:**

| h | Max Err.Rel Euler | Max Err.Rel RK4 | Razón (Euler/RK4) |
|---|-------------------|-----------------|-------------------|
| 0.1 | 9.82% | 0.00094% | ~10,471x |
| 0.05 | 5.22% | 0.000063% | ~83,467x |
| 0.01 | 1.10% | 0.0000001% | ~10,439,338x |

**Orden de Convergencia Experimental:**

| Transición | Orden Euler | Orden RK4 | Teórico |
|------------|-------------|-----------|---------|
| h: 0.1 → 0.05 | p ≈ 0.913 | p ≈ 3.907 | Euler: 1, RK4: 4 |
| h: 0.05 → 0.01 | p ≈ 0.968 | p ≈ 3.968 | Euler: 1, RK4: 4 |

### Ejemplo de Uso

```python
# Ejecutar análisis completo
python Analisis_Errores.py

# El script genera automáticamente:
# - 3 gráficos PNG (300 DPI)
# - 1 archivo de texto con tablas LaTeX
# - Salida en consola con todos los resultados numéricos
```

---

## Archivo Generado

**Autores:** Enrique A. González Moreira, Heily Rodríguez Rodríguez, Alex L. Cuervo Grillo
**Fecha:** 2025-12-02 (Actualizado)
**Versión:** 2.3 - Organización centralizada de figuras y actualización de rutas
**Asignaturas:** Matemática Numérica y Ecuaciones Diferenciales Ordinarias

---

## Cambios en Versión 2.3 (2025-12-02)

- ✅ **Organización de figuras:** Todas las imágenes ahora se guardan en carpeta centralizada `Figuras/`
- ✅ **Actualización de rutas:** Todos los scripts actualizados para usar `FIGURAS_DIR`
- ✅ **Portabilidad mejorada:** Rutas relativas usando `os.path.join()`
- ✅ **Documentación de figuras:** Nuevo `Figuras/README.md` con descripción completa
- ✅ **Creación automática:** Carpeta Figuras se crea automáticamente si no existe

---

## Módulo: `Plano_Fase.py`

**Descripción general:** Visualización completa del plano de fase para el sistema lineal de subpoblaciones de la Parte C. Incluye análisis de estabilidad, campo vectorial, trayectorias, vectores propios, nullclinas y comportamiento asintótico.

### Sistema Matemático Analizado

**Sistema de EDOs:**
```
dx/dt = x - y
dy/dt = 2x - 3y
```

**Forma matricial:** dX/dt = AX, donde A = [[1, -1], [2, -3]]

**Valores propios:**
- λ₁ = -1 + √2 ≈ 0.414 (positivo, dirección inestable)
- λ₂ = -1 - √2 ≈ -2.414 (negativo, dirección estable)

**Vectores propios:**
- v₁ = [1, 2-√2] (dirección inestable)
- v₂ = [1, 2+√2] (dirección estable)

**Clasificación:** Punto crítico (0,0) es un **PUNTO SILLA** (inestable)

### Clase: `PlanoFaseSistemaLineal`

#### Constructor

| Método | Parámetros | Descripción / Retorno |
|--------|------------|----------------------|
| `__init__()` | Ninguno | **Descripción:** Inicializa el sistema con la matriz A, calcula valores y vectores propios, y clasifica el punto crítico.<br>**Retorna:** Instancia de `PlanoFaseSistemaLineal` |

#### Métodos Principales

| Método | Parámetros | Descripción / Retorno |
|--------|------------|----------------------|
| `sistema(X, t)` | `X` (array): Vector [x, y]<br>`t` (float): Tiempo | **Descripción:** Define el sistema de EDOs dx/dt = x-y, dy/dt = 2x-3y.<br>**Retorna:** `list` - [dx/dt, dy/dt] |
| `calcular_trayectoria(X0, t_span, num_points)` | `X0` (list): Condición inicial [x0, y0]<br>`t_span` (float, opcional): Tiempo total (default: 10)<br>`num_points` (int, opcional): Puntos de evaluación (default: 1000) | **Descripción:** Calcula trayectoria desde condición inicial usando `scipy.integrate.odeint`.<br>**Retorna:** `tuple(t, trayectoria)` - array Nx2 |
| `visualizar_plano_fase(xlim, ylim, num_arrows, figsize)` | `xlim` (tuple, opcional): Límites eje x (default: (-3,3))<br>`ylim` (tuple, opcional): Límites eje y (default: (-3,3))<br>`num_arrows` (int, opcional): Densidad campo vectorial (default: 20)<br>`figsize` (tuple, opcional): Tamaño figura (default: (12,10)) | **Descripción:** Genera visualización completa: campo vectorial, vectores propios, líneas propias, nullclinas, trayectorias y punto crítico.<br>**Retorna:** `None` (guarda 'plano_fase.png') |
| `analizar_comportamiento_asintotico()` | Ninguno | **Descripción:** Analiza y grafica comportamiento temporal en direcciones estable e inestable.<br>**Retorna:** `None` (guarda 'comportamiento_asintotico.png') |

#### Métodos Privados

| Método | Parámetros | Descripción / Retorno |
|--------|------------|----------------------|
| `_clasificar_punto_critico()` | Ninguno | **Descripción:** Clasifica el punto crítico (0,0) según signos de valores propios.<br>**Retorna:** `None` (imprime clasificación) |

#### Función Principal

| Función | Parámetros | Descripción / Retorno |
|---------|------------|----------------------|
| `main()` | Ninguno | **Descripción:** Ejecuta análisis completo: crea sistema, genera plano de fase y analiza comportamiento asintótico.<br>**Retorna:** `None` |

### Elementos Visualizados

#### Plano de Fase Completo (`plano_fase.png`)

1. **Campo Vectorial (quiver):**
   - Flechas normalizadas coloreadas según magnitud (colormap 'viridis')
   - Muestra dirección del flujo del sistema en cada punto

2. **Vectores Propios:**
   - **ROJO:** v₁ (λ₁ > 0, dirección inestable) - trayectorias se alejan
   - **AZUL:** v₂ (λ₂ < 0, dirección estable) - trayectorias se acercan

3. **Líneas Propias:**
   - Rectas por el origen en direcciones de vectores propios
   - Línea discontinua roja: pendiente m₁ = 2 - √2
   - Línea discontinua azul: pendiente m₂ = 2 + √2

4. **Nullclinas:**
   - **VERDE:** dx/dt = 0 ⟹ y = x
   - **MAGENTA:** dy/dt = 0 ⟹ y = (2/3)x
   - Intersección en (0,0) confirma punto crítico

5. **Trayectorias (NARANJA):**
   - 12 trayectorias desde condiciones iniciales variadas
   - Integración bidireccional (t positivo y negativo)
   - Patrón típico de punto silla: aproximación por dirección estable, alejamiento por inestable

6. **Punto Crítico:**
   - Círculo rojo con centro blanco en (0,0)
   - Etiquetado como "SILLA"

#### Comportamiento Asintótico (`comportamiento_asintotico.png`)

Dos subplots mostrando evolución temporal:

1. **Dirección Estable (λ₂ < 0):**
   - x(t) y y(t) convergen exponencialmente a cero
   - Condición inicial: X0 = 2v₂

2. **Dirección Inestable (λ₁ > 0):**
   - x(t) y y(t) divergen exponencialmente desde origen
   - Condición inicial: X0 = 0.1v₁

### Ejemplo de Uso

```python
#!/usr/bin/env python3
from Plano_Fase import PlanoFaseSistemaLineal, main

# Opción 1: Usar función main (análisis completo)
main()

# Opción 2: Uso manual del objeto
sistema = PlanoFaseSistemaLineal()

# Ver información del sistema
print(f"Valores propios: {sistema.eigenvalues}")
print(f"Vectores propios: {sistema.eigenvectors}")

# Calcular trayectoria específica
X0 = [1.5, 0.5]
t, trayectoria = sistema.calcular_trayectoria(X0, t_span=8, num_points=500)

# Generar visualización personalizada
sistema.visualizar_plano_fase(xlim=(-4, 4), ylim=(-4, 4), num_arrows=25)

# Analizar comportamiento asintótico
sistema.analizar_comportamiento_asintotico()
```

### Salida del Script

**Archivos generados:**
- `plano_fase.png` (300 DPI) - Plano de fase completo
- `comportamiento_asintotico.png` (300 DPI) - Análisis temporal

**Salida en consola:**
```
============================================================
SISTEMA DE SUBPOBLACIONES - PARTE C
============================================================

Matriz del sistema A:
[[ 1 -1]
 [ 2 -3]]

Valores propios:
  λ₁ = 0.414214 = -1 + √2 ≈ 0.414214
  λ₂ = -2.414214 = -1 - √2 ≈ -2.414214

Vectores propios:
  v₁ = [0.76536686 0.64359425]
  v₂ = [-0.38268343  0.92387953]

------------------------------------------------------------
CLASIFICACIÓN DEL PUNTO CRÍTICO (0,0)
------------------------------------------------------------
Tipo: PUNTO SILLA (Saddle Point)
Estabilidad: INESTABLE
  - Dirección estable (λ₂ < 0): hacia el origen
  - Dirección inestable (λ₁ > 0): alejándose del origen
------------------------------------------------------------

============================================================
GENERANDO VISUALIZACIONES...
============================================================

[1/2] Generando plano de fase...
✓ Figura guardada en: .../plano_fase.png

[2/2] Analizando comportamiento asintótico...
✓ Figura guardada en: .../comportamiento_asintotico.png

============================================================
✓ ANÁLISIS COMPLETADO
============================================================

Interpretación del Plano de Fase:
------------------------------------------------------------
• El origen (0,0) es un PUNTO SILLA (inestable)
• Dirección ROJA: vector propio v₁ (λ₁ > 0, inestable)
  → Las trayectorias se ALEJAN del origen en esta dirección
• Dirección AZUL: vector propio v₂ (λ₂ < 0, estable)
  → Las trayectorias se ACERCAN al origen en esta dirección
• Las trayectorias NARANJA muestran el comportamiento típico:
  → Se aproximan por la dirección estable (azul)
  → Se alejan siguiendo la dirección inestable (roja)
============================================================
```

### Interpretación Biológica

En el contexto de subpoblaciones (ej. células tumorales activas vs latentes):

- **Punto silla:** Sistema inherentemente inestable
- **Dirección estable (v₂):** Combinación de poblaciones que tiende a extinción
- **Dirección inestable (v₁):** Combinación que crece sin límite
- **Implicación práctica:** Pequeñas perturbaciones pueden llevar a extinción o crecimiento ilimitado

### Dependencias Adicionales

| Biblioteca | Método Usado | Descripción |
|------------|--------------|-------------|
| `scipy.linalg` | `eig(A)` | Calcula valores y vectores propios de matriz A |
| `scipy.integrate` | `odeint(func, X0, t)` | Integra sistema de EDOs numéricamente |
| `matplotlib.patches` | `mpatches` | Importado pero no usado actualmente |

---

## Archivo Generado


