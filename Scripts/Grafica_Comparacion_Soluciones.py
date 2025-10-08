#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualizacion de Comparacion de Soluciones
Parte A - Modelo de Crecimiento de Tumor

Este modulo contiene funciones para comparar:
1. Multiples soluciones con diferentes condiciones iniciales
2. Diferentes metodos numericos (Analitico, Euler, RK4) usando polimorfismo

Autores: Enrique A. Gonzalez Moreira, Heily Rodriguez Rodriguez, Alex L. Cuervo Grillo
Asignatura: Matematica Numerica y Ecuaciones Diferenciales Ordinarias
"""

import numpy as np
import matplotlib.pyplot as plt
from Ecuacion_De_Poblacion import ModeloTumorAnalitico
from ModeloTumorEuler import ModeloTumorEuler
from ModeloTumorRK4 import ModeloTumorRK4


def graficar_comparacion_soluciones(P0_values, beta0, alpha, t_max=10, figsize=(12, 8), guardar=None):
    """
    Grafica multiples soluciones con diferentes condiciones iniciales.

    Parametros:
    -----------
    P0_values : list
        Lista de poblaciones iniciales a comparar
    beta0 : float
        Tasa de crecimiento inicial (beta_0)
    alpha : float
        Tasa de decrecimiento exponencial (alpha)
    t_max : float, opcional
        Tiempo maximo de simulacion (default: 10)
    figsize : tuple, opcional
        Tamano de la figura (ancho, alto) en pulgadas (default: (12, 8))
    guardar : str, opcional
        Ruta del archivo para guardar el grafico (default: None, no guarda)

    Retorna:
    --------
    tuple : (fig, ax)
        Objetos Figure y Axes de matplotlib
    """
    fig, ax = plt.subplots(figsize=figsize)

    t = np.linspace(0, t_max, 500)

    # Generar un color para cada condicion inicial
    colors = plt.cm.tab10(np.linspace(0, 1, len(P0_values)))

    for i, P0 in enumerate(P0_values):
        # Crear modelo analitico para cada P0
        modelo = ModeloTumorAnalitico(P0, beta0, alpha)

        # Calcular solucion usando polimorfismo (resolver)
        P = modelo.resolver(t)
        P_inf = modelo.limite_asintotico()

        # Graficar solucion
        ax.plot(t, P, linewidth=2.5, color=colors[i],
                label=f'P_0={P0}, P_inf={P_inf:.2f}')

        # Marcar condicion inicial
        ax.plot(0, P0, 'o', markersize=8, color=colors[i])

        # Linea asintotica
        ax.axhline(y=P_inf, linestyle='--', alpha=0.5, color=colors[i])

    ax.set_xlabel('Tiempo t', fontsize=14)
    ax.set_ylabel('Poblacion P(t)', fontsize=14)
    ax.set_title(f'Soluciones con Diferentes Condiciones Iniciales\n' +
                 f'dP/dt = beta_0 * exp(-alpha*t) * P  (beta_0={beta0}, alpha={alpha})',
                 fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=11)
    ax.set_xlim(0, t_max)

    plt.tight_layout()

    # Guardar si se especifica
    if guardar:
        plt.savefig(guardar, dpi=300, bbox_inches='tight')
        print(f"Grafico guardado: {guardar}")

    return fig, ax


def graficar_comparacion_metodos(modelos, t_max=10, figsize=(12, 8), guardar=None):
    """
    Compara diferentes metodos numericos usando polimorfismo.

    Esta funcion aprovecha el polimorfismo: todos los modelos heredan de
    ModeloTumorBase y tienen el metodo resolver(t), por lo que podemos
    tratarlos de manera uniforme.

    Parametros:
    -----------
    modelos : list de ModeloTumorBase
        Lista de instancias de modelos (Analitico, Euler, RK4, etc.)
        Todos deben tener los mismos parametros (P0, beta0, alpha)
    t_max : float, opcional
        Tiempo maximo de simulacion (default: 10)
    figsize : tuple, opcional
        Tamano de la figura (ancho, alto) en pulgadas (default: (12, 8))
    guardar : str, opcional
        Ruta del archivo para guardar el grafico (default: None, no guarda)

    Retorna:
    --------
    tuple : (fig, ax)
        Objetos Figure y Axes de matplotlib
    """
    fig, ax = plt.subplots(figsize=figsize)

    t = np.linspace(0, t_max, 500)

    # Estilos para cada tipo de metodo
    estilos = [
        {'linewidth': 3, 'linestyle': '-', 'alpha': 0.8},   # Analitico
        {'linewidth': 2, 'linestyle': '--', 'alpha': 0.7},  # Euler
        {'linewidth': 2, 'linestyle': '-.', 'alpha': 0.7},  # RK4
    ]

    for i, modelo in enumerate(modelos):
        # ¡POLIMORFISMO! Llamamos resolver() sin importar el tipo concreto
        P = modelo.resolver(t)

        # Obtener estilo (ciclar si hay mas modelos que estilos)
        estilo = estilos[i % len(estilos)]

        # Graficar
        ax.plot(t, P, label=modelo.nombre, **estilo)

    # Graficar limite asintotico (es el mismo para todos si tienen mismo P0, beta0, alpha)
    P_inf = modelos[0].limite_asintotico()
    ax.axhline(y=P_inf, linestyle=':', alpha=0.5, color='gray',
               label=f'Límite: P_inf={P_inf:.2f}')

    ax.set_xlabel('Tiempo t', fontsize=14)
    ax.set_ylabel('Poblacion P(t)', fontsize=14)
    ax.set_title(f'Comparacion de Metodos Numericos\n' +
                 f'P0={modelos[0].P0}, beta_0={modelos[0].beta0}, alpha={modelos[0].alpha}',
                 fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=11, loc='lower right')
    ax.set_xlim(0, t_max)

    plt.tight_layout()

    # Guardar si se especifica
    if guardar:
        plt.savefig(guardar, dpi=300, bbox_inches='tight')
        print(f"Grafico guardado: {guardar}")

    return fig, ax


if __name__ == '__main__':
    print("="*70)
    print("COMPARACION DE SOLUCIONES - MODELO DE TUMOR")
    print("="*70)

    # Parametros comunes
    beta0 = 2.0
    alpha = 0.5

    # =========================================================================
    # 1. Comparacion con diferentes condiciones iniciales (solo analitico)
    # =========================================================================
    print("\n1. Comparacion de Soluciones con Diferentes Condiciones Iniciales")
    print("-"*70)

    P0_values = [50, 100, 150, 200]
    print(f"Parametros: beta_0={beta0}, alpha={alpha}")
    print(f"Condiciones iniciales: {P0_values}\n")

    print("Generando grafico de condiciones iniciales...")
    fig1, ax1 = graficar_comparacion_soluciones(
        P0_values,
        beta0,
        alpha,
        t_max=10,
        guardar='comparacion_soluciones.png'
    )

    # =========================================================================
    # 2. Comparacion de metodos numericos (¡POLIMORFISMO!)
    # =========================================================================
    print("\n2. Comparacion de Metodos Numericos (Polimorfismo)")
    print("-"*70)

    P0 = 100
    h_euler = 0.1
    h_rk4 = 0.1

    print(f"Parametros: P0={P0}, beta_0={beta0}, alpha={alpha}")
    print(f"Tamaño de paso: h_Euler={h_euler}, h_RK4={h_rk4}\n")

    # Crear lista de modelos (¡todos heredan de ModeloTumorBase!)
    modelos = [
        ModeloTumorAnalitico(P0, beta0, alpha),
        ModeloTumorEuler(P0, beta0, alpha, h=h_euler, t_max=10.0),
        ModeloTumorRK4(P0, beta0, alpha, h=h_rk4, t_max=10.0)
    ]

    print("Modelos a comparar:")
    for modelo in modelos:
        print(f"  - {modelo.nombre}")

    print("\nGenerando grafico de comparacion de metodos...")
    fig2, ax2 = graficar_comparacion_metodos(
        modelos,
        t_max=10,
        guardar='comparacion_metodos_numericos.png'
    )

    # =========================================================================
    # 3. Mostrar ambos graficos
    # =========================================================================
    print("\n" + "="*70)
    print("Mostrando graficos...")
    print("="*70)
    plt.show()
