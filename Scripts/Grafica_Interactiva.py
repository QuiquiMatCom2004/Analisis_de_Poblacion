#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualizacion Interactiva con Widgets
Parte A - Modelo de Crecimiento de Tumor

Este modulo contiene la visualizacion interactiva con sliders para manipular
los parametros del modelo en tiempo real.

Autores: Enrique A. Gonzalez Moreira, Heily Rodriguez Rodriguez, Alex L. Cuervo Grillo
Asignatura: Matematica Numerica y Ecuaciones Diferenciales Ordinarias
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, CheckButtons
from Ecuacion_De_Poblacion import ModeloTumorAnalitico
from ModeloTumorEuler import ModeloTumorEuler
from ModeloTumorRK4 import ModeloTumorRK4


def graficar_interactivo(P0_init=1.0, beta0_init=2.0, alpha_init=0.5, t_max=15):
    """
    Crea una grafica interactiva con sliders para manipular parametros en tiempo real.

    Incluye tres subgraficos:
    - Poblacion P(t) vs tiempo
    - Tasa de crecimiento r(t) vs tiempo
    - Diagrama de fase (P vs dP/dt)

    Parametros:
    -----------
    P0_init : float, opcional
        Poblacion inicial (default: 1.0)
    beta0_init : float, opcional
        Tasa de crecimiento inicial (default: 2.0)
    alpha_init : float, opcional
        Tasa de decrecimiento exponencial (default: 0.5)
    t_max : float, opcional
        Tiempo maximo de simulacion (default: 15)

    Retorna:
    --------
    None
    """
    # Crear figura con subplots
    fig = plt.figure(figsize=(14, 10))
    gs = fig.add_gridspec(3, 2, height_ratios=[2, 2, 1], hspace=0.35, wspace=0.3)

    ax_poblacion = fig.add_subplot(gs[0, :])
    ax_tasa = fig.add_subplot(gs[1, 0])
    ax_fase = fig.add_subplot(gs[1, 1])

    # Crear tiempo
    t = np.linspace(0, t_max, 500)

    # Modelo inicial (usando polimorfismo)
    modelo = ModeloTumorAnalitico(P0_init, beta0_init, alpha_init)

    # Calculos iniciales
    P = modelo.resolver(t)  # ¡Polimorfismo!
    P_lim = modelo.limite_asintotico()
    r = modelo.tasa_crecimiento(t)
    dPdt = r * P

    # Grafica de poblacion con gradiente de color
    line_pop, = ax_poblacion.plot(t, P, linewidth=3, color='#2E86DE', label='P(t)')
    scatter_pop = ax_poblacion.scatter([], [], c=[], cmap='plasma', s=50, alpha=0.6, vmin=0, vmax=t_max)
    line_lim = ax_poblacion.axhline(y=P_lim, color='#EE5A6F', linestyle='--', linewidth=2,
                                     label=f'P_inf = {P_lim:.3f}', alpha=0.8)
    fill_area = ax_poblacion.fill_between(t, 0, P, alpha=0.2, color='#2E86DE')

    ax_poblacion.set_xlabel('Tiempo t', fontsize=12, fontweight='bold')
    ax_poblacion.set_ylabel('Poblacion P(t)', fontsize=12, fontweight='bold')
    ax_poblacion.set_title('Modelo de Tumor con Tasa Variable', fontsize=14, fontweight='bold', pad=20)
    ax_poblacion.grid(True, alpha=0.3, linestyle='--')
    ax_poblacion.legend(loc='upper left', fontsize=10)
    ax_poblacion.set_ylim([0, P_lim * 1.5])

    # Grafica de tasa de crecimiento con gradiente
    line_tasa, = ax_tasa.plot(t, r, linewidth=3, color='#10AC84')
    fill_tasa = ax_tasa.fill_between(t, 0, r, alpha=0.3, color='#10AC84')
    ax_tasa.set_xlabel('Tiempo t', fontsize=11, fontweight='bold')
    ax_tasa.set_ylabel('Tasa r(t)', fontsize=11, fontweight='bold')
    ax_tasa.set_title('Tasa de Crecimiento Variable', fontsize=12, fontweight='bold')
    ax_tasa.grid(True, alpha=0.3, linestyle='--')

    # Diagrama de fase (P vs dP/dt)
    line_fase, = ax_fase.plot(P, dPdt, linewidth=3, color='#A55EEA')
    scatter_fase = ax_fase.scatter([], [], c=[], cmap='viridis', s=50, alpha=0.7, vmin=0, vmax=t_max)
    ax_fase.set_xlabel('Poblacion P', fontsize=11, fontweight='bold')
    ax_fase.set_ylabel('dP/dt', fontsize=11, fontweight='bold')
    ax_fase.set_title('Diagrama de Fase', fontsize=12, fontweight='bold')
    ax_fase.grid(True, alpha=0.3, linestyle='--')

    # Crear sliders
    ax_P0 = fig.add_subplot(gs[2, 0])
    ax_beta0 = fig.add_subplot(gs[2, 1])

    slider_P0 = Slider(ax_P0, 'P_0', 0.1, 5.0, valinit=P0_init, color='#2E86DE')
    slider_beta0 = Slider(ax_beta0, 'beta_0', 0.1, 5.0, valinit=beta0_init, color='#EE5A6F')

    # Crear slider adicional para alpha
    fig.text(0.05, 0.02, 'alpha', fontsize=10, fontweight='bold')
    ax_alpha = plt.axes([0.15, 0.02, 0.35, 0.02])
    slider_alpha = Slider(ax_alpha, '', 0.1, 3.0, valinit=alpha_init, color='#10AC84')

    # Texto informativo dinamico
    info_text = fig.text(0.55, 0.02, '', fontsize=9, family='monospace',
                         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

    def update(val):
        """Actualiza las graficas cuando cambian los sliders"""
        # Obtener valores de sliders
        P0 = slider_P0.val
        beta0 = slider_beta0.val
        alpha = slider_alpha.val

        # Crear nuevo modelo (usando polimorfismo)
        modelo = ModeloTumorAnalitico(P0, beta0, alpha)

        # Recalcular
        P = modelo.resolver(t)  # ¡Polimorfismo!
        P_lim = modelo.limite_asintotico()
        r = modelo.tasa_crecimiento(t)
        dPdt = r * P

        # Actualizar lineas
        line_pop.set_ydata(P)
        line_lim.set_ydata([P_lim, P_lim])
        line_lim.set_label(f'P_inf = {P_lim:.3f}')

        # Actualizar area de relleno
        for coll in ax_poblacion.collections[:]:
            coll.remove()
        ax_poblacion.fill_between(t, 0, P, alpha=0.2, color='#2E86DE')

        # Puntos con gradiente de color
        indices = np.arange(0, len(t), 10)
        scatter_pop.set_offsets(np.c_[t[indices], P[indices]])
        scatter_pop.set_array(t[indices])

        # Actualizar limites
        ax_poblacion.set_ylim([0, max(P) * 1.2])
        ax_poblacion.legend(loc='upper left', fontsize=10)

        # Actualizar tasa
        line_tasa.set_ydata(r)
        for coll in ax_tasa.collections[:]:
            coll.remove()
        ax_tasa.fill_between(t, 0, r, alpha=0.3, color='#10AC84')
        ax_tasa.set_ylim([0, max(r) * 1.2])

        # Actualizar fase
        line_fase.set_data(P, dPdt)
        scatter_fase.set_offsets(np.c_[P[indices], dPdt[indices]])
        scatter_fase.set_array(t[indices])
        ax_fase.set_xlim([0, max(P) * 1.1])
        ax_fase.set_ylim([0, max(dPdt) * 1.1])

        # Actualizar texto informativo
        info_text.set_text(
            f'P_0={P0:.2f} | beta_0={beta0:.2f} | alpha={alpha:.2f} | '
            f'P_inf={P_lim:.3f} | P_max={max(P):.3f}'
        )

        fig.canvas.draw_idle()

    # Conectar sliders
    slider_P0.on_changed(update)
    slider_beta0.on_changed(update)
    slider_alpha.on_changed(update)

    # Actualizar inicial
    update(None)

    plt.suptitle('Visualizacion Interactiva del Modelo de Tumor',
                 fontsize=16, fontweight='bold', y=0.98)
    plt.show()


def graficar_comparacion_metodos_interactiva(P0_init=100, beta0_init=2.0, alpha_init=0.5, h_init=0.1, t_max=10):
    """
    Visualizacion interactiva comparando diferentes metodos (¡POLIMORFISMO!).

    Permite ajustar parametros y ver en tiempo real como se comparan:
    - Solucion Analitica
    - Metodo de Euler
    - Metodo de Runge-Kutta 4

    Parametros:
    -----------
    P0_init : float, opcional
        Poblacion inicial (default: 100)
    beta0_init : float, opcional
        Tasa de crecimiento inicial (default: 2.0)
    alpha_init : float, opcional
        Tasa de decrecimiento exponencial (default: 0.5)
    h_init : float, opcional
        Tamaño de paso para metodos numericos (default: 0.1)
    t_max : float, opcional
        Tiempo maximo de simulacion (default: 10)
    """
    # Crear figura
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
    plt.subplots_adjust(left=0.1, bottom=0.25)

    t = np.linspace(0, t_max, 500)

    # Crear modelos iniciales (¡POLIMORFISMO!)
    modelo_analitico = ModeloTumorAnalitico(P0_init, beta0_init, alpha_init)
    modelo_euler = ModeloTumorEuler(P0_init, beta0_init, alpha_init, h=h_init, t_max=t_max)
    modelo_rk4 = ModeloTumorRK4(P0_init, beta0_init, alpha_init, h=h_init, t_max=t_max)

    # Calcular soluciones usando polimorfismo
    P_analitico = modelo_analitico.resolver(t)
    P_euler = modelo_euler.resolver(t)
    P_rk4 = modelo_rk4.resolver(t)

    # Graficar en ax1: Comparacion de soluciones
    line_analitico, = ax1.plot(t, P_analitico, 'b-', linewidth=3, label='Analítico', alpha=0.9)
    line_euler, = ax1.plot(t, P_euler, 'r--', linewidth=2, label='Euler', alpha=0.7)
    line_rk4, = ax1.plot(t, P_rk4, 'g-.', linewidth=2, label='RK4', alpha=0.7)

    ax1.set_xlabel('Tiempo t', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Poblacion P(t)', fontsize=12, fontweight='bold')
    ax1.set_title('Comparacion de Metodos Numericos', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='best', fontsize=11)

    # Graficar en ax2: Errores relativos
    error_euler = np.abs(P_analitico - P_euler) / np.abs(P_analitico) * 100
    error_rk4 = np.abs(P_analitico - P_rk4) / np.abs(P_analitico) * 100

    line_error_euler, = ax2.semilogy(t, error_euler, 'r-', linewidth=2, label='Error Euler (%)')
    line_error_rk4, = ax2.semilogy(t, error_rk4, 'g-', linewidth=2, label='Error RK4 (%)')

    ax2.set_xlabel('Tiempo t', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Error Relativo (%)', fontsize=12, fontweight='bold')
    ax2.set_title('Errores Relativos (escala logarítmica)', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3, which='both')
    ax2.legend(loc='best', fontsize=11)

    # Crear sliders
    ax_P0 = plt.axes([0.15, 0.15, 0.35, 0.03])
    ax_beta0 = plt.axes([0.15, 0.10, 0.35, 0.03])
    ax_alpha = plt.axes([0.15, 0.05, 0.35, 0.03])
    ax_h = plt.axes([0.60, 0.15, 0.35, 0.03])

    slider_P0 = Slider(ax_P0, 'P_0', 10, 200, valinit=P0_init, color='#2E86DE')
    slider_beta0 = Slider(ax_beta0, 'beta_0', 0.1, 5.0, valinit=beta0_init, color='#EE5A6F')
    slider_alpha = Slider(ax_alpha, 'alpha', 0.1, 3.0, valinit=alpha_init, color='#10AC84')
    slider_h = Slider(ax_h, 'h (paso)', 0.01, 0.5, valinit=h_init, color='#FFA502')

    # Texto informativo
    info_text = fig.text(0.60, 0.08, '', fontsize=9, family='monospace',
                         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    def update(val):
        """Actualizar graficas cuando cambian sliders"""
        P0 = slider_P0.val
        beta0 = slider_beta0.val
        alpha = slider_alpha.val
        h = slider_h.val

        # Recrear modelos (¡POLIMORFISMO!)
        modelo_analitico = ModeloTumorAnalitico(P0, beta0, alpha)
        modelo_euler = ModeloTumorEuler(P0, beta0, alpha, h=h, t_max=t_max)
        modelo_rk4 = ModeloTumorRK4(P0, beta0, alpha, h=h, t_max=t_max)

        # Recalcular soluciones usando polimorfismo
        P_analitico = modelo_analitico.resolver(t)
        P_euler = modelo_euler.resolver(t)
        P_rk4 = modelo_rk4.resolver(t)

        # Actualizar lineas de soluciones
        line_analitico.set_ydata(P_analitico)
        line_euler.set_ydata(P_euler)
        line_rk4.set_ydata(P_rk4)

        # Recalcular errores
        error_euler = np.abs(P_analitico - P_euler) / np.abs(P_analitico) * 100
        error_rk4 = np.abs(P_analitico - P_rk4) / np.abs(P_analitico) * 100

        # Actualizar lineas de errores
        line_error_euler.set_ydata(error_euler)
        line_error_rk4.set_ydata(error_rk4)

        # Ajustar limites
        ax1.set_ylim([0, max(P_analitico) * 1.1])
        ax2.set_ylim([max(1e-8, min(error_rk4.min(), error_euler.min()) / 10),
                      max(error_euler.max(), error_rk4.max()) * 2])

        # Actualizar info
        P_inf = modelo_analitico.limite_asintotico()
        error_max_euler = error_euler.max()
        error_max_rk4 = error_rk4.max()

        info_text.set_text(
            f'P_inf={P_inf:.2f} | h={h:.3f}\n'
            f'Max Error Euler: {error_max_euler:.4f}%\n'
            f'Max Error RK4: {error_max_rk4:.6f}%'
        )

        fig.canvas.draw_idle()

    # Conectar sliders
    slider_P0.on_changed(update)
    slider_beta0.on_changed(update)
    slider_alpha.on_changed(update)
    slider_h.on_changed(update)

    # Inicializar
    update(None)

    plt.suptitle('Comparacion Interactiva de Metodos Numericos (Polimorfismo)',
                 fontsize=16, fontweight='bold', y=0.98)
    plt.show()


if __name__ == "__main__":
    print("=" * 70)
    print("VISUALIZACION INTERACTIVA - MODELO DE TUMOR")
    print("=" * 70)
    print("\nElige modo de visualizacion:")
    print("1. Visualizacion clasica (solo solucion analitica)")
    print("2. Comparacion de metodos numericos (polimorfismo + errores)")

    opcion = input("\nOpcion (1/2): ").strip()

    if opcion == '1':
        print("\n--- Modo Clasico ---")
        print("Usa los sliders para cambiar los parametros en tiempo real!")
        print("\nControles:")
        print("  - P_0: Poblacion inicial (0.1 - 5.0)")
        print("  - beta_0: Tasa de crecimiento inicial (0.1 - 5.0)")
        print("  - alpha: Coeficiente de decaimiento (0.1 - 3.0)")
        print()

        graficar_interactivo()

    elif opcion == '2':
        print("\n--- Modo Comparacion (Polimorfismo) ---")
        print("¡Compara en tiempo real Analitico vs Euler vs RK4!")
        print("\nControles:")
        print("  - P_0: Poblacion inicial (10 - 200)")
        print("  - beta_0: Tasa de crecimiento inicial (0.1 - 5.0)")
        print("  - alpha: Coeficiente de decaimiento (0.1 - 3.0)")
        print("  - h: Tamaño de paso para metodos numericos (0.01 - 0.5)")
        print("\n¡Observa como cambian los errores con diferentes valores de h!")
        print()

        graficar_comparacion_metodos_interactiva()

    else:
        print("Opcion invalida. Usa '1' o '2'.")
