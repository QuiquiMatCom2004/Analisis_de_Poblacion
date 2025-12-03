#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualización del Plano de Fase - Parte C
==========================================

Análisis del sistema lineal de subpoblaciones:
    dx/dt = x - y
    dy/dt = 2x - 3y

Sistema matricial: dX/dt = AX, donde A = [[1, -1], [2, -3]]

Autores: E. González, H. Rodríguez, A. Cuervo
Proyecto: Análisis de Poblaciones Acotadas mediante la Ecuación Logística
"""

import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.integrate import odeint
from scipy.linalg import eig
import matplotlib.patches as mpatches

# Directorio para guardar figuras
FIGURAS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Figuras')
os.makedirs(FIGURAS_DIR, exist_ok=True)


class PlanoFaseSistemaLineal:
    """
    Clase para visualizar el plano de fase del sistema lineal de subpoblaciones.

    Attributes:
        A (np.ndarray): Matriz del sistema 2x2
        eigenvalues (np.ndarray): Valores propios de A
        eigenvectors (np.ndarray): Vectores propios de A
    """

    def __init__(self):
        """Inicializa el sistema con la matriz A definida en el problema."""
        self.A = np.array([[1, -1],
                           [2, -3]])

        # Calcular valores y vectores propios
        self.eigenvalues, self.eigenvectors = eig(self.A)

        print("="*60)
        print("SISTEMA DE SUBPOBLACIONES - PARTE C")
        print("="*60)
        print("\nMatriz del sistema A:")
        print(self.A)
        print(f"\nValores propios:")
        print(f"  λ₁ = {self.eigenvalues[0]:.6f} = -1 + √2 ≈ {-1 + np.sqrt(2):.6f}")
        print(f"  λ₂ = {self.eigenvalues[1]:.6f} = -1 - √2 ≈ {-1 - np.sqrt(2):.6f}")
        print(f"\nVectores propios:")
        print(f"  v₁ = {self.eigenvectors[:, 0]}")
        print(f"  v₂ = {self.eigenvectors[:, 1]}")

        # Clasificar punto crítico
        self._clasificar_punto_critico()

    def _clasificar_punto_critico(self):
        """Clasifica el punto crítico en (0,0) según los valores propios."""
        lambda1, lambda2 = self.eigenvalues

        print("\n" + "-"*60)
        print("CLASIFICACIÓN DEL PUNTO CRÍTICO (0,0)")
        print("-"*60)

        if lambda1.real > 0 and lambda2.real < 0:
            print("Tipo: PUNTO SILLA (Saddle Point)")
            print("Estabilidad: INESTABLE")
            print(f"  - Dirección estable (λ₂ < 0): hacia el origen")
            print(f"  - Dirección inestable (λ₁ > 0): alejándose del origen")
        elif lambda1.real < 0 and lambda2.real < 0:
            if lambda1.imag == 0 and lambda2.imag == 0:
                print("Tipo: NODO ESTABLE")
            else:
                print("Tipo: ESPIRAL ESTABLE")
        elif lambda1.real > 0 and lambda2.real > 0:
            if lambda1.imag == 0 and lambda2.imag == 0:
                print("Tipo: NODO INESTABLE")
            else:
                print("Tipo: ESPIRAL INESTABLE")
        else:
            print("Tipo: CENTRO (eigenvalores imaginarios puros)")

        print("-"*60)

    def sistema(self, X, t):
        """
        Define el sistema de ecuaciones diferenciales.

        Parameters:
            X (array): Vector de estado [x, y]
            t (float): Tiempo (no usado en sistemas autónomos)

        Returns:
            array: Derivadas [dx/dt, dy/dt]
        """
        x, y = X
        dxdt = x - y
        dydt = 2*x - 3*y
        return [dxdt, dydt]

    def calcular_trayectoria(self, X0, t_span=10, num_points=1000):
        """
        Calcula una trayectoria desde una condición inicial.

        Parameters:
            X0 (list): Condición inicial [x0, y0]
            t_span (float): Tiempo total de integración
            num_points (int): Número de puntos de evaluación

        Returns:
            tuple: (t, trayectoria) donde trayectoria es array Nx2
        """
        t = np.linspace(0, t_span, num_points)
        trayectoria = odeint(self.sistema, X0, t)
        return t, trayectoria

    def visualizar_plano_fase(self, xlim=(-3, 3), ylim=(-3, 3),
                              num_arrows=20, figsize=(12, 10)):
        """
        Genera la visualización completa del plano de fase.

        Parameters:
            xlim (tuple): Límites en x (xmin, xmax)
            ylim (tuple): Límites en y (ymin, ymax)
            num_arrows (int): Número de flechas en cada dirección del campo vectorial
            figsize (tuple): Tamaño de la figura
        """
        fig, ax = plt.subplots(figsize=figsize)

        # 1. CAMPO VECTORIAL
        x = np.linspace(xlim[0], xlim[1], num_arrows)
        y = np.linspace(ylim[0], ylim[1], num_arrows)
        X_grid, Y_grid = np.meshgrid(x, y)

        # Calcular las componentes del campo vectorial
        U = X_grid - Y_grid
        V = 2*X_grid - 3*Y_grid

        # Normalizar para mejor visualización
        M = np.sqrt(U**2 + V**2)
        M[M == 0] = 1  # Evitar división por cero
        U_norm = U / M
        V_norm = V / M

        # Dibujar campo vectorial
        ax.quiver(X_grid, Y_grid, U_norm, V_norm, M,
                 cmap='viridis', alpha=0.6, scale=25, width=0.003,
                 pivot='mid', headwidth=4, headlength=5)

        # 2. VECTORES PROPIOS (DIRECCIONES CARACTERÍSTICAS)
        lambda1, lambda2 = self.eigenvalues
        v1, v2 = self.eigenvectors[:, 0], self.eigenvectors[:, 1]

        # Normalizar vectores propios para visualización
        scale_factor = 2.5

        # Vector propio 1 (inestable, λ₁ > 0)
        ax.arrow(0, 0, scale_factor*v1[0].real, scale_factor*v1[1].real,
                head_width=0.15, head_length=0.2, fc='red', ec='red',
                linewidth=2.5, label=f'v₁ (λ₁={lambda1.real:.3f} > 0, inestable)',
                zorder=5)
        ax.arrow(0, 0, -scale_factor*v1[0].real, -scale_factor*v1[1].real,
                head_width=0.15, head_length=0.2, fc='red', ec='red',
                linewidth=2.5, zorder=5)

        # Vector propio 2 (estable, λ₂ < 0)
        ax.arrow(0, 0, scale_factor*v2[0].real, scale_factor*v2[1].real,
                head_width=0.15, head_length=0.2, fc='blue', ec='blue',
                linewidth=2.5, label=f'v₂ (λ₂={lambda2.real:.3f} < 0, estable)',
                zorder=5)
        ax.arrow(0, 0, -scale_factor*v2[0].real, -scale_factor*v2[1].real,
                head_width=0.15, head_length=0.2, fc='blue', ec='blue',
                linewidth=2.5, zorder=5)

        # 3. LÍNEAS PROPIAS (RECTAS POR EL ORIGEN EN DIRECCIÓN DE VECTORES PROPIOS)
        t_line = np.linspace(-5, 5, 100)

        # Línea propia 1 (dirección inestable)
        pendiente1 = v1[1].real / v1[0].real if v1[0].real != 0 else np.inf
        if pendiente1 != np.inf:
            y_line1 = pendiente1 * t_line
            ax.plot(t_line, y_line1, 'r--', linewidth=1.5, alpha=0.5,
                   label=f'Línea propia 1 (m={pendiente1:.3f})')

        # Línea propia 2 (dirección estable)
        pendiente2 = v2[1].real / v2[0].real if v2[0].real != 0 else np.inf
        if pendiente2 != np.inf:
            y_line2 = pendiente2 * t_line
            ax.plot(t_line, y_line2, 'b--', linewidth=1.5, alpha=0.5,
                   label=f'Línea propia 2 (m={pendiente2:.3f})')

        # 4. NULLCLINAS (curvas donde dx/dt=0 y dy/dt=0)
        # dx/dt = 0 => x - y = 0 => y = x
        ax.plot(t_line, t_line, 'g--', linewidth=2, alpha=0.7,
               label='Nullclina dx/dt=0 (y=x)')

        # dy/dt = 0 => 2x - 3y = 0 => y = (2/3)x
        ax.plot(t_line, (2/3)*t_line, 'm--', linewidth=2, alpha=0.7,
               label='Nullclina dy/dt=0 (y=2x/3)')

        # 5. TRAYECTORIAS DESDE DIFERENTES CONDICIONES INICIALES
        # Conjunto diverso de condiciones iniciales
        condiciones_iniciales = [
            # Cerca de la dirección estable (v2)
            [0.1, 0.1 * pendiente2],
            [-0.1, -0.1 * pendiente2],

            # Cerca de la dirección inestable (v1)
            [0.1, 0.1 * pendiente1],
            [-0.1, -0.1 * pendiente1],

            # Otros puntos
            [2, 1],
            [-2, -1],
            [1, -1],
            [-1, 2],
            [2.5, 0],
            [0, 2.5],
            [-2.5, 0],
            [0, -2.5],
        ]

        for i, X0 in enumerate(condiciones_iniciales):
            # Integrar hacia adelante (tiempo positivo)
            t_forward = np.linspace(0, 5, 500)
            traj_forward = odeint(self.sistema, X0, t_forward)

            # Integrar hacia atrás (tiempo negativo)
            t_backward = np.linspace(0, -5, 500)
            traj_backward = odeint(self.sistema, X0, t_backward)

            # Dibujar trayectorias
            if i == 0:
                ax.plot(traj_forward[:, 0], traj_forward[:, 1], 'orange',
                       linewidth=1.5, alpha=0.8, label='Trayectorias')
            else:
                ax.plot(traj_forward[:, 0], traj_forward[:, 1], 'orange',
                       linewidth=1.5, alpha=0.8)

            ax.plot(traj_backward[:, 0], traj_backward[:, 1], 'orange',
                   linewidth=1.5, alpha=0.8)

            # Marcar condición inicial
            ax.plot(X0[0], X0[1], 'ko', markersize=4, zorder=4)

        # 6. PUNTO CRÍTICO
        ax.plot(0, 0, 'ro', markersize=12, markeredgewidth=2,
               markerfacecolor='white', label='Punto crítico (0,0) - SILLA',
               zorder=6)

        # Configuración de la gráfica
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        ax.set_xlabel('x (Subpoblación 1)', fontsize=12, fontweight='bold')
        ax.set_ylabel('y (Subpoblación 2)', fontsize=12, fontweight='bold')
        ax.set_title('Plano de Fase: Sistema de Subpoblaciones\n' +
                    r'$\frac{dx}{dt} = x - y, \quad \frac{dy}{dt} = 2x - 3y$',
                    fontsize=14, fontweight='bold', pad=15)
        ax.grid(True, alpha=0.3, linestyle='--')
        ax.axhline(y=0, color='k', linewidth=0.8)
        ax.axvline(x=0, color='k', linewidth=0.8)
        ax.legend(loc='upper left', fontsize=9, framealpha=0.9)
        ax.set_aspect('equal', adjustable='box')

        plt.tight_layout()

        # Guardar figura
        output_path = os.path.join(FIGURAS_DIR, 'plano_fase.png')
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"\n✓ Figura guardada en: {output_path}")

        plt.close()

    def analizar_comportamiento_asintotico(self):
        """
        Analiza el comportamiento asintótico de trayectorias cerca de direcciones propias.
        """
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))

        # Dirección estable (v2, λ₂ < 0)
        v2 = self.eigenvectors[:, 1].real
        lambda2 = self.eigenvalues[1].real

        X0_estable = 2 * v2  # Condición inicial en dirección estable
        t = np.linspace(0, 10, 1000)
        traj_estable = odeint(self.sistema, X0_estable, t)

        axes[0].plot(t, traj_estable[:, 0], 'b-', linewidth=2, label='x(t)')
        axes[0].plot(t, traj_estable[:, 1], 'r-', linewidth=2, label='y(t)')
        axes[0].set_xlabel('Tiempo t', fontsize=12)
        axes[0].set_ylabel('Población', fontsize=12)
        axes[0].set_title(f'Dirección Estable (λ₂={lambda2:.3f} < 0)\nConverge al origen',
                         fontsize=12, fontweight='bold')
        axes[0].grid(True, alpha=0.3)
        axes[0].legend()

        # Dirección inestable (v1, λ₁ > 0)
        v1 = self.eigenvectors[:, 0].real
        lambda1 = self.eigenvalues[0].real

        X0_inestable = 0.1 * v1  # Condición inicial pequeña en dirección inestable
        t = np.linspace(0, 5, 1000)
        traj_inestable = odeint(self.sistema, X0_inestable, t)

        axes[1].plot(t, traj_inestable[:, 0], 'b-', linewidth=2, label='x(t)')
        axes[1].plot(t, traj_inestable[:, 1], 'r-', linewidth=2, label='y(t)')
        axes[1].set_xlabel('Tiempo t', fontsize=12)
        axes[1].set_ylabel('Población', fontsize=12)
        axes[1].set_title(f'Dirección Inestable (λ₁={lambda1:.3f} > 0)\nDiverge del origen',
                         fontsize=12, fontweight='bold')
        axes[1].grid(True, alpha=0.3)
        axes[1].legend()

        plt.tight_layout()

        # Guardar figura
        output_path = os.path.join(FIGURAS_DIR, 'comportamiento_asintotico.png')
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"✓ Figura guardada en: {output_path}")

        plt.close()


def main():
    """Función principal para ejecutar el análisis del plano de fase."""

    # Crear objeto del sistema
    sistema = PlanoFaseSistemaLineal()

    print("\n" + "="*60)
    print("GENERANDO VISUALIZACIONES...")
    print("="*60)

    # Generar plano de fase completo
    print("\n[1/2] Generando plano de fase...")
    sistema.visualizar_plano_fase(xlim=(-3, 3), ylim=(-3, 3), num_arrows=20)

    # Analizar comportamiento asintótico
    print("\n[2/2] Analizando comportamiento asintótico...")
    sistema.analizar_comportamiento_asintotico()

    print("\n" + "="*60)
    print("✓ ANÁLISIS COMPLETADO")
    print("="*60)
    print("\nInterpretación del Plano de Fase:")
    print("-"*60)
    print("• El origen (0,0) es un PUNTO SILLA (inestable)")
    print("• Dirección ROJA: vector propio v₁ (λ₁ > 0, inestable)")
    print("  → Las trayectorias se ALEJAN del origen en esta dirección")
    print("• Dirección AZUL: vector propio v₂ (λ₂ < 0, estable)")
    print("  → Las trayectorias se ACERCAN al origen en esta dirección")
    print("• Las trayectorias NARANJA muestran el comportamiento típico:")
    print("  → Se aproximan por la dirección estable (azul)")
    print("  → Se alejan siguiendo la dirección inestable (roja)")
    print("="*60)


if __name__ == "__main__":
    main()
