#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualizacion del Campo de Isoclinas
Parte A - Modelo de Crecimiento de Tumor

Este modulo contiene funciones para visualizar el campo de isoclinas,
la solucion analitica y el campo de direcciones del modelo de tumor.

Autores: Enrique A. Gonzalez Moreira, Heily Rodriguez Rodriguez, Alex L. Cuervo Grillo
Asignatura: Matematica Numerica y Ecuaciones Diferenciales Ordinarias
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.widgets import Slider
from Ecuacion_De_Poblacion import ModeloTumorAnalitico
from ModeloTumorBase import ModeloTumorBase


def graficar_campo_isoclinas(modelo, modelos_adicionales=None, t_max=10, num_isoclinas=8, figsize=(12, 8), guardar=None):
    """
    Genera el grafico del campo de isoclinas con soluciones (usando polimorfismo).

    Parametros:
    -----------
    modelo : ModeloTumorBase
        Instancia del modelo principal (usualmente analitico)
        Usado para calcular isoclinas y campo de direcciones
    modelos_adicionales : list de ModeloTumorBase, opcional
        Lista de modelos adicionales a comparar (Euler, RK4, etc.)
        Todos se grafican usando polimorfismo (default: None)
    t_max : float, opcional
        Tiempo maximo de simulacion (default: 10)
    num_isoclinas : int, opcional
        Numero de isoclinas a graficar (default: 8)
    figsize : tuple, opcional
        Tamano de la figura (ancho, alto) en pulgadas (default: (12, 8))
    guardar : str, opcional
        Ruta del archivo para guardar el grafico (default: None, no guarda)

    Retorna:
    --------
    tuple : (fig, ax)
        Objetos Figure y Axes de matplotlib
    """
    # Crear figura
    fig, ax = plt.subplots(figsize=figsize)

    # Rango de tiempo
    t = np.linspace(0, t_max, 500)

    # Calcular limite asintotico
    P_inf = modelo.limite_asintotico()

    # Generar y graficar isoclinas
    isoclinas = modelo.generar_isoclinas(t, num_isoclinas)
    colors = cm.viridis(np.linspace(0, 1, num_isoclinas))

    for i, (C, P_iso) in enumerate(isoclinas):
        ax.plot(t, P_iso, color=colors[i], alpha=0.4, linewidth=1.5,
                label=f'C = {C:.1f}' if i % 2 == 0 else '')

    # Graficar solucion principal (usando polimorfismo)
    P_principal = modelo.resolver(t)
    ax.plot(t, P_principal, 'r-', linewidth=3, label=f'{modelo.nombre}, P_0={modelo.P0}')

    # Graficar modelos adicionales si existen (¡POLIMORFISMO!)
    if modelos_adicionales:
        estilos = [
            {'linestyle': '--', 'linewidth': 2.5, 'color': 'blue'},
            {'linestyle': '-.', 'linewidth': 2.5, 'color': 'green'},
            {'linestyle': ':', 'linewidth': 2.5, 'color': 'orange'},
        ]
        for i, mod in enumerate(modelos_adicionales):
            P_adicional = mod.resolver(t)  # ¡Polimorfismo!
            estilo = estilos[i % len(estilos)]
            ax.plot(t, P_adicional, label=mod.nombre, **estilo)

    # Marcar condicion inicial
    ax.plot(0, modelo.P0, 'ro', markersize=10, label=f'Condicion inicial: P(0)={modelo.P0}')

    # Linea asintotica
    ax.axhline(y=P_inf, color='k', linestyle='--', linewidth=2,
               label=f'Limite: P_inf = {P_inf:.2f}')

    # Campo de direcciones
    t_campo = np.linspace(0, t_max, 15)
    P_campo = np.linspace(0, P_inf * 1.6, 15)
    T, P_grid = np.meshgrid(t_campo, P_campo)

    dT_norm, dP_norm = modelo.campo_direcciones(T, P_grid)

    # Graficar campo de direcciones
    ax.quiver(T, P_grid, dT_norm, dP_norm, alpha=0.5, width=0.003)

    # Configuracion del grafico
    ax.set_xlabel('Tiempo t', fontsize=14)
    ax.set_ylabel('Poblacion P(t)', fontsize=14)
    ax.set_title(f'Campo de Isoclinas - Modelo de Tumor\n' +
                 f'dP/dt = beta_0 * exp(-alpha*t) * P  (beta_0={modelo.beta0}, alpha={modelo.alpha})',
                 fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='best', fontsize=10)
    ax.set_xlim(0, t_max)
    ax.set_ylim(0, P_inf * 1.7)

    plt.tight_layout()

    # Guardar si se especifica
    if guardar:
        plt.savefig(guardar, dpi=300, bbox_inches='tight')
        print(f"Grafico guardado: {guardar}")

    return fig, ax


def graficar_campo_isoclinas_interactivo(P0_init=100, beta0_init=2.0, alpha_init=0.5, t_max=10, num_isoclinas=8):
    """
    Genera grafico interactivo del campo de isoclinas con sliders para beta0 y alpha.

    Parametros:
    -----------
    P0_init : float, opcional
        Poblacion inicial (default: 100)
    beta0_init : float, opcional
        Tasa de crecimiento inicial (default: 2.0)
    alpha_init : float, opcional
        Tasa de decrecimiento exponencial (default: 0.5)
    t_max : float, opcional
        Tiempo maximo de simulacion (default: 10)
    num_isoclinas : int, opcional
        Numero de isoclinas a graficar (default: 8)

    Retorna:
    --------
    None
    """
    # Crear figura con espacio para sliders
    fig, ax = plt.subplots(figsize=(14, 10))
    plt.subplots_adjust(left=0.1, bottom=0.25)

    # Rango de tiempo
    t = np.linspace(0, t_max, 500)

    # Modelo inicial
    modelo = ModeloTumorAnalitico(P0_init, beta0_init, alpha_init)
    P_inf = modelo.limite_asintotico()

    # Elementos graficos iniciales
    isoclinas = modelo.generar_isoclinas(t, num_isoclinas)
    colors = cm.viridis(np.linspace(0, 1, num_isoclinas))

    # Almacenar lineas de isoclinas para actualizar
    lineas_isoclinas = []
    for i, (C, P_iso) in enumerate(isoclinas):
        line, = ax.plot(t, P_iso, color=colors[i], alpha=0.4, linewidth=1.5,
                        label=f'C = {C:.1f}' if i % 2 == 0 else '')
        lineas_isoclinas.append(line)

    # Solucion analitica
    #P_analitica = modelo.solucion_analitica(t)
    #line_solucion, = ax.plot(t, P_analitica, 'r-', linewidth=3,
    #                          label=f'Solucion: P(t), P_0={modelo.P0}')

    # Condicion inicial
    punto_inicial, = ax.plot(0, modelo.P0, 'ro', markersize=10,
                             label=f'Condicion inicial: P(0)={modelo.P0}')

    # Linea asintotica
    line_limite = ax.axhline(y=P_inf, color='k', linestyle='--', linewidth=2,
                             label=f'Limite: P_inf = {P_inf:.2f}')

    # Campo de direcciones
    t_campo = np.linspace(0, t_max, 15)
    P_campo = np.linspace(0, P_inf * 1.6, 15)
    T, P_grid = np.meshgrid(t_campo, P_campo)
    dT_norm, dP_norm = modelo.campo_direcciones(T, P_grid)
    quiver = ax.quiver(T, P_grid, dT_norm, dP_norm, alpha=0.5, width=0.003)

    # Configuracion inicial del grafico
    ax.set_xlabel('Tiempo t', fontsize=14)
    ax.set_ylabel('Poblacion P(t)', fontsize=14)
    ax.set_title(f'Campo de Isoclinas - Modelo de Tumor (Interactivo)\n' +
                 f'dP/dt = beta_0 * exp(-alpha*t) * P  (beta_0={modelo.beta0:.2f}, alpha={modelo.alpha:.2f})',
                 fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='best', fontsize=10)
    ax.set_xlim(0, t_max)
    ax.set_ylim(0, P_inf * 1.7)

    # Crear sliders
    ax_beta0 = plt.axes([0.15, 0.15, 0.7, 0.03])
    ax_alpha = plt.axes([0.15, 0.10, 0.7, 0.03])
    ax_P0 = plt.axes([0.15, 0.05, 0.7, 0.03])

    slider_beta0 = Slider(ax_beta0, 'beta_0', 0.1, 5.0, valinit=beta0_init, color='#EE5A6F')
    slider_alpha = Slider(ax_alpha, 'alpha', 0.1, 3.0, valinit=alpha_init, color='#10AC84')
    slider_P0 = Slider(ax_P0, 'P_0', 10, 200, valinit=P0_init, color='#2E86DE')

    # Texto informativo
    info_text = fig.text(0.5, 0.22, '', fontsize=10, ha='center', family='monospace',
                         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    def update(val):
        """Actualiza el grafico cuando cambian los sliders"""
        # Obtener valores actuales
        P0 = slider_P0.val
        beta0 = slider_beta0.val
        alpha = slider_alpha.val

        # Crear nuevo modelo
        modelo = ModeloTumorAnalitico(P0, beta0, alpha)
        P_inf = modelo.limite_asintotico()

        # Actualizar isoclinas
        isoclinas = modelo.generar_isoclinas(t, num_isoclinas)
        for i, (line, (C, P_iso)) in enumerate(zip(lineas_isoclinas, isoclinas)):
            line.set_ydata(P_iso)

        # Actualizar solucion analitica
        #P_analitica = modelo.solucion_analitica(t)
        #line_solucion.set_ydata(P_analitica)
        #line_solucion.set_label(f'Solucion: P(t), P_0={P0:.0f}')

        # Actualizar condicion inicial
        punto_inicial.set_data([0], [P0])
        punto_inicial.set_label(f'Condicion inicial: P(0)={P0:.0f}')

        # Actualizar linea limite
        line_limite.set_ydata([P_inf, P_inf])
        line_limite.set_label(f'Limite: P_inf = {P_inf:.2f}')

        # Actualizar campo de direcciones
        P_campo_new = np.linspace(0, P_inf * 1.6, 15)
        T_new, P_grid_new = np.meshgrid(t_campo, P_campo_new)
        dT_norm_new, dP_norm_new = modelo.campo_direcciones(T_new, P_grid_new)

        quiver.set_offsets(np.c_[T_new.ravel(), P_grid_new.ravel()])
        quiver.set_UVC(dT_norm_new, dP_norm_new)

        # Actualizar limites y titulo
        ax.set_ylim(0, P_inf * 1.7)
        ax.set_title(f'Campo de Isoclinas - Modelo de Tumor (Interactivo)\n' +
                     f'dP/dt = beta_0 * exp(-alpha*t) * P  (beta_0={beta0:.2f}, alpha={alpha:.2f})',
                     fontsize=16, fontweight='bold')

        # Actualizar leyenda
        ax.legend(loc='best', fontsize=10)

        # Actualizar texto informativo
        factor = modelo.factor_crecimiento()
        info_text.set_text(
            f'P_0={P0:.1f} | beta_0={beta0:.2f} | alpha={alpha:.2f} | '
            f'P_inf={P_inf:.2f} | Factor={factor:.2f}'
        )

        fig.canvas.draw_idle()

    # Conectar sliders
    slider_beta0.on_changed(update)
    slider_alpha.on_changed(update)
    slider_P0.on_changed(update)

    # Actualizar inicial
    update(None)

    plt.show()


if __name__ == '__main__':
    from ModeloTumorEuler import ModeloTumorEuler
    from ModeloTumorRK4 import ModeloTumorRK4

    print("="*70)
    print("VISUALIZACION DEL CAMPO DE ISOCLINAS - MODELO DE TUMOR")
    print("="*70)
    print("\nElige modo de visualizacion:")
    print("1. Grafico estatico - Solo solucion analitica")
    print("2. Grafico estatico - Comparacion con metodos numericos (polimorfismo)")
    print("3. Grafico interactivo - Explorar parametros")

    opcion = input("\nOpcion (1/2/3): ").strip()

    if opcion == '1':
        # Modo estatico simple
        print("\n--- Modo Estatico (Solo Analitico) ---")
        modelo = ModeloTumorAnalitico(P0=100, beta0=2.0, alpha=0.5)
        print(f"Modelo: {modelo}\n")

        print("Generando campo de isoclinas...")
        fig, ax = graficar_campo_isoclinas(
            modelo,
            t_max=10,
            num_isoclinas=8,
            guardar='campo_isoclinas.png'
        )

        print("\nMostrando grafico...")
        plt.show()

    elif opcion == '2':
        # Modo estatico con comparacion (¡POLIMORFISMO!)
        print("\n--- Modo Estatico (Comparacion de Metodos) ---")
        print("Comparando: Analitico vs Euler vs RK4\n")

        # Parametros
        P0, beta0, alpha = 100, 2.0, 0.5
        h = 0.1

        # Crear modelos usando polimorfismo
        modelo_principal = ModeloTumorAnalitico(P0, beta0, alpha)
        modelos_adicionales = [
            ModeloTumorEuler(P0, beta0, alpha, h=h, t_max=10.0),
            ModeloTumorRK4(P0, beta0, alpha, h=h, t_max=10.0)
        ]

        print("Modelos:")
        print(f"  - {modelo_principal.nombre}")
        for mod in modelos_adicionales:
            print(f"  - {mod.nombre}")

        print("\nGenerando campo de isoclinas con comparacion...")
        fig, ax = graficar_campo_isoclinas(
            modelo_principal,
            modelos_adicionales=modelos_adicionales,
            t_max=10,
            num_isoclinas=8,
            guardar='campo_isoclinas_comparacion.png'
        )

        print("\nMostrando grafico...")
        plt.show()

    elif opcion == '3':
        # Modo interactivo
        print("\n--- Modo Interactivo ---")
        print("Usa los sliders para explorar como cambian las isoclinas")
        print("con diferentes valores de beta_0 y alpha.\n")
        print("Controles:")
        print("  - beta_0: Tasa de crecimiento inicial (0.1 - 5.0)")
        print("  - alpha: Tasa de decrecimiento exponencial (0.1 - 3.0)")
        print("  - P_0: Poblacion inicial (10 - 200)")
        print("\nAbriendo visualizacion interactiva...")

        graficar_campo_isoclinas_interactivo(
            P0_init=100,
            beta0_init=2.0,
            alpha_init=0.5,
            t_max=10,
            num_isoclinas=8
        )

    else:
        print("Opcion invalida. Usa '1', '2' o '3'.")
