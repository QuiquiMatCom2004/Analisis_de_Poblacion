#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analisis de Errores - Comparacion de Metodos Numericos

Compara la precision de los metodos de Euler y RK4 contra valores EXACTOS
calculados matematicamente a mano (sin errores de redondeo computacional).

Autores: Enrique A. Gonzalez Moreira, Heily Rodriguez Rodriguez, Alex L. Cuervo Grillo
Asignatura: Matematica Numerica y Ecuaciones Diferenciales Ordinarias
"""

import numpy as np
import matplotlib.pyplot as plt
import os
from ModeloTumorEuler import ModeloTumorEuler
from ModeloTumorRK4 import ModeloTumorRK4

# Directorio para guardar figuras
FIGURAS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Figuras')
os.makedirs(FIGURAS_DIR, exist_ok=True)

# ====================================================================================
# PARAMETROS FIJOS PARA TODO EL ANALISIS
# ====================================================================================
P0 = 100.0      # Poblacion inicial
beta0 = 2.0     # Tasa de crecimiento inicial
alpha = 0.5     # Tasa de decrecimiento exponencial

# Puntos de evaluacion NO equidistantes (para ver variacion del error)
t_eval = np.array([1.0, 3.5, 10.0])

# VALORES EXACTOS CALCULADOS A MANO (sin errores de redondeo computacional)
# Formula: P(t) = P0 * exp(beta0/alpha * (1 - exp(-alpha*t)))
#                = 100 * exp(4 * (1 - exp(-0.5*t)))
#
# t = 1.0:  e^(-0.5) = 0.606530659713, P(1.0) = 100 * e^(1.573877361148) = 482.532148
# t = 3.5:  e^(-1.75) = 0.173773943450, P(3.5) = 100 * e^(3.304904226200) = 2724.593201
# t = 10.0: e^(-5.0) = 0.006737946999, P(10.0) = 100 * e^(3.973048212004) = 5314.628533

P_exacto = np.array([
    482.532148288934,   # t = 1.0  (calculado a mano)
    2724.593201734644,  # t = 3.5  (calculado a mano)
    5314.628532833040   # t = 10.0 (calculado a mano)
])

# Tamaños de paso a analizar
h_values = [0.1, 0.05, 0.01]

print("=" * 80)
print("ANALISIS DE ERRORES - METODOS NUMERICOS")
print("=" * 80)
print(f"\nParametros del modelo:")
print(f"  P0 = {P0}")
print(f"  beta0 = {beta0}")
print(f"  alpha = {alpha}")
print(f"\nPuntos de evaluacion: t = {t_eval}")
print("=" * 80)

print("\nVALORES EXACTOS (calculados matematicamente a mano):")
print(f"{'t':>8} {'P(t) exacto':>20}")
print("-" * 30)
for t, P in zip(t_eval, P_exacto):
    print(f"{t:8.2f} {P:20.10f}")

# ====================================================================================
# CALCULO DE ERRORES PARA DIFERENTES TAMAÑOS DE PASO
# ====================================================================================
resultados = []

for h in h_values:
    print(f"\n{'=' * 80}")
    print(f"ANALISIS CON h = {h}")
    print("=" * 80)

    # Crear modelos numericos
    modelo_euler = ModeloTumorEuler(P0, beta0, alpha, h=h, t_max=max(t_eval))
    modelo_rk4 = ModeloTumorRK4(P0, beta0, alpha, h=h, t_max=max(t_eval))

    # Evaluar en los puntos especificos
    P_euler = modelo_euler.resolver(t_eval)
    P_rk4 = modelo_rk4.resolver(t_eval)

    # Calcular errores absolutos
    error_abs_euler = np.abs(P_exacto - P_euler)
    error_abs_rk4 = np.abs(P_exacto - P_rk4)

    # Calcular errores relativos (en porcentaje)
    error_rel_euler = (error_abs_euler / np.abs(P_exacto)) * 100
    error_rel_rk4 = (error_abs_rk4 / np.abs(P_exacto)) * 100

    # Mostrar tabla comparativa
    print(f"\n{'t':>6} {'Exacto':>15} {'Euler':>15} {'RK4':>15} {'Err.Rel Euler':>15} {'Err.Rel RK4':>15}")
    print("-" * 90)
    for i, t in enumerate(t_eval):
        print(f"{t:6.2f} {P_exacto[i]:15.6f} {P_euler[i]:15.6f} {P_rk4[i]:15.6f} "
              f"{error_rel_euler[i]:14.6f}% {error_rel_rk4[i]:14.8f}%")

    # Guardar resultados
    resultados.append({
        'h': h,
        'P_euler': P_euler,
        'P_rk4': P_rk4,
        'error_abs_euler': error_abs_euler,
        'error_abs_rk4': error_abs_rk4,
        'error_rel_euler': error_rel_euler,
        'error_rel_rk4': error_rel_rk4,
        'max_error_euler': np.max(error_rel_euler),
        'max_error_rk4': np.max(error_rel_rk4)
    })

# ====================================================================================
# RESUMEN COMPARATIVO
# ====================================================================================
print("\n" + "=" * 80)
print("RESUMEN: ERRORES MAXIMOS POR TAMAÑO DE PASO")
print("=" * 80)
print(f"{'h':>10} {'Max Err.Rel Euler':>20} {'Max Err.Rel RK4':>20} {'Razon':>10}")
print("-" * 65)
for res in resultados:
    razon = res['max_error_euler'] / res['max_error_rk4'] if res['max_error_rk4'] > 1e-10 else np.inf
    print(f"{res['h']:10.4f} {res['max_error_euler']:19.6f}% {res['max_error_rk4']:19.8f}% {razon:10.1f}x")

# ====================================================================================
# GRAFICO 1: COMPARACION DE SOLUCIONES
# ====================================================================================
fig1, axes = plt.subplots(1, 3, figsize=(16, 5))
fig1.suptitle('Comparación de Soluciones Numéricas vs Exacta\n'
              f'Parámetros: $P_0={P0}$, $\\beta_0={beta0}$, $\\alpha={alpha}$',
              fontsize=14, fontweight='bold')

for idx, (ax, h) in enumerate(zip(axes.flat, h_values)):
    # Obtener resultados para este h
    res = resultados[idx]

    # Graficar soluciones
    ax.plot(t_eval, P_exacto, 'o-', label='Exacto (manual)', linewidth=2.5, markersize=10, color='black', zorder=3)
    ax.plot(t_eval, res['P_euler'], 's--', label='Euler', linewidth=2, markersize=8, alpha=0.7, color='tab:red')
    ax.plot(t_eval, res['P_rk4'], '^--', label='RK4', linewidth=2, markersize=8, alpha=0.7, color='tab:blue')

    ax.set_xlabel('Tiempo $t$', fontsize=11, fontweight='bold')
    ax.set_ylabel('Población $P(t)$', fontsize=11, fontweight='bold')
    ax.set_title(f'$h = {h}$', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3, linestyle=':')
    ax.legend(loc='upper left', fontsize=9, framealpha=0.9)

plt.tight_layout()
output_path = os.path.join(FIGURAS_DIR, 'comparacion_metodos_numericos.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"\n✓ Gráfico guardado: {output_path}")

# ====================================================================================
# GRAFICO 2: ERRORES RELATIVOS EN FUNCION DEL TIEMPO
# ====================================================================================
fig2, axes = plt.subplots(1, 3, figsize=(16, 5))
fig2.suptitle('Errores Relativos en Función del Tiempo\n'
              f'Parámetros: $P_0={P0}$, $\\beta_0={beta0}$, $\\alpha={alpha}$',
              fontsize=14, fontweight='bold')

for idx, (ax, h) in enumerate(zip(axes.flat, h_values)):
    res = resultados[idx]

    ax.semilogy(t_eval, res['error_rel_euler'], 's-', label='Euler', linewidth=2.5, markersize=10, color='tab:red')
    ax.semilogy(t_eval, res['error_rel_rk4'], '^-', label='RK4', linewidth=2.5, markersize=10, color='tab:blue')

    ax.set_xlabel('Tiempo $t$', fontsize=11, fontweight='bold')
    ax.set_ylabel('Error Relativo (%)', fontsize=11, fontweight='bold')
    ax.set_title(f'$h = {h}$', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3, which='both', linestyle=':')
    ax.legend(loc='best', fontsize=10, framealpha=0.9)

plt.tight_layout()
output_path = os.path.join(FIGURAS_DIR, 'errores_relativos_tiempo.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"✓ Gráfico guardado: {output_path}")

# ====================================================================================
# GRAFICO 3: CONVERGENCIA (ERROR MAX VS TAMAÑO DE PASO)
# ====================================================================================
fig3, ax = plt.subplots(figsize=(10, 7))

h_arr = np.array([res['h'] for res in resultados])
max_err_euler = np.array([res['max_error_euler'] for res in resultados])
max_err_rk4 = np.array([res['max_error_rk4'] for res in resultados])

# Grafico log-log para verificar orden de convergencia
ax.loglog(h_arr, max_err_euler, 'o-', label='Euler', linewidth=2.5, markersize=12, color='tab:red')
ax.loglog(h_arr, max_err_rk4, 's-', label='RK4', linewidth=2.5, markersize=12, color='tab:blue')

# Lineas de referencia teoricas
h_ref = np.array([h_arr[0], h_arr[-1]])
# Euler: error ~ O(h) => pendiente 1 en log-log
euler_ref = max_err_euler[0] * (h_ref / h_arr[0])**1
ax.loglog(h_ref, euler_ref, 'k--', alpha=0.6, linewidth=2, label='$O(h)$ (teórico Euler)')

# RK4: error ~ O(h^4) => pendiente 4 en log-log
rk4_ref = max_err_rk4[0] * (h_ref / h_arr[0])**4
ax.loglog(h_ref, rk4_ref, 'k:', alpha=0.6, linewidth=2, label='$O(h^4)$ (teórico RK4)')

ax.set_xlabel('Tamaño de paso $h$', fontsize=13, fontweight='bold')
ax.set_ylabel('Error Relativo Máximo (%)', fontsize=13, fontweight='bold')
ax.set_title('Orden de Convergencia: Error Máximo vs Tamaño de Paso\n'
             f'Parámetros: $P_0={P0}$, $\\beta_0={beta0}$, $\\alpha={alpha}$',
             fontsize=14, fontweight='bold', pad=15)
ax.grid(True, alpha=0.3, which='both', linestyle=':')
ax.legend(loc='upper left', fontsize=11, framealpha=0.9)

plt.tight_layout()
output_path = os.path.join(FIGURAS_DIR, 'convergencia_orden.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"✓ Gráfico guardado: {output_path}")

# ====================================================================================
# CALCULO EXPERIMENTAL DEL ORDEN DE CONVERGENCIA
# ====================================================================================
print("\n" + "=" * 80)
print("ORDEN DE CONVERGENCIA EXPERIMENTAL")
print("=" * 80)
print("\nSi el error es E ~ C·h^p, entonces:")
print("  p = log(E2/E1) / log(h2/h1)")
print("\n" + "-" * 80)

for i in range(len(h_values) - 1):
    h1, h2 = h_values[i], h_values[i+1]
    E1_euler, E2_euler = resultados[i]['max_error_euler'], resultados[i+1]['max_error_euler']
    E1_rk4, E2_rk4 = resultados[i]['max_error_rk4'], resultados[i+1]['max_error_rk4']

    # Orden experimental
    p_euler = np.log(E2_euler / E1_euler) / np.log(h2 / h1)
    p_rk4 = np.log(E2_rk4 / E1_rk4) / np.log(h2 / h1)

    print(f"h: {h1} → {h2}")
    print(f"  Orden Euler: p ≈ {p_euler:.3f} (teórico: 1.0)")
    print(f"  Orden RK4:   p ≈ {p_rk4:.3f} (teórico: 4.0)")
    print("-" * 80)

# ====================================================================================
# EXPORTAR RESULTADOS PARA LATEX
# ====================================================================================
with open('resultados_analisis_errores_latex.txt', 'w', encoding='utf-8') as f:
    f.write("% TABLA DE ERRORES PARA LATEX\n")
    f.write("% Copiar esto directamente en el informe\n\n")

    for idx, h in enumerate(h_values):
        res = resultados[idx]
        f.write(f"% h = {h}\n")
        f.write("\\begin{table}[H]\n")
        f.write("\\centering\n")
        f.write("\\begin{tabular}{|c|c|c|c|c|}\n")
        f.write("\\hline\n")
        f.write("$t$ & Exacto & Euler & RK4 & Err.Rel Euler & Err.Rel RK4 \\\\\n")
        f.write("\\hline\n")
        for i, t in enumerate(t_eval):
            f.write(f"{t:.1f} & {P_exacto[i]:.4f} & {res['P_euler'][i]:.4f} & {res['P_rk4'][i]:.4f} & "
                   f"{res['error_rel_euler'][i]:.4f}\\% & {res['error_rel_rk4'][i]:.6f}\\% \\\\\n")
        f.write("\\hline\n")
        f.write("\\end{tabular}\n")
        f.write(f"\\caption{{Errores para $h = {h}$}}\n")
        f.write("\\end{table}\n\n")

print("\n✓ Resultados LaTeX guardados en: resultados_analisis_errores_latex.txt")

plt.show()
print("\n" + "=" * 80)
print("ANALISIS COMPLETADO")
print("=" * 80)
