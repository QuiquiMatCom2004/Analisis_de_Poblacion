#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modelo de Tumor - Metodo de Euler

Implementacion del metodo de Euler (orden 1) para resolver numericamente
la EDO del modelo de tumor: dP/dt = beta_0 * e^(-alpha*t) * P

El metodo de Euler es el metodo numerico mas simple:
P_{n+1} = P_n + h * f(t_n, P_n)

Autores: Enrique A. Gonzalez Moreira, Heily Rodriguez Rodriguez, Alex L. Cuervo Grillo
Asignatura: Matematica Numerica y Ecuaciones Diferenciales Ordinarias
"""

import numpy as np
from ModeloTumorBase import ModeloTumorBase


class ModeloTumorEuler(ModeloTumorBase):
    """
    Resolucion numerica del modelo de tumor usando el metodo de Euler.

    Metodo de Euler (orden 1):
    --------------------------
    P_{n+1} = P_n + h * f(t_n, P_n)

    donde f(t, P) = beta_0 * e^(-alpha*t) * P

    Error local de truncamiento: O(h^2)
    Error global: O(h)

    Atributos adicionales:
    ---------------------
    h : float
        Tamano de paso (step size)
    t_max : float
        Tiempo maximo de integracion
    """

    def __init__(self, P0, beta0, alpha, h=0.01, t_max=10.0):
        """
        Inicializa el modelo con el metodo de Euler.

        Parametros:
        -----------
        P0 : float
            Poblacion inicial
        beta0 : float
            Tasa de crecimiento inicial (beta_0)
        alpha : float
            Tasa de decrecimiento exponencial (alpha)
        h : float, opcional
            Tamano de paso (default: 0.01)
        t_max : float, opcional
            Tiempo maximo de integracion (default: 10.0)
        """
        super().__init__(P0, beta0, alpha, nombre=f"Euler (h={h})")
        self.h = h
        self.t_max = t_max

        # Precalcular la solucion numerica
        self.t_vals, self.P_vals = self._integrar()

    def _integrar(self):
        """
        Integra la EDO usando el metodo de Euler desde t=0 hasta t=t_max.

        Retorna:
        --------
        tuple : (t_vals, P_vals)
            t_vals : array de tiempos
            P_vals : array de poblaciones
        """
        # Crear malla temporal
        t_vals = np.arange(0, self.t_max + self.h, self.h)
        P_vals = np.zeros_like(t_vals)

        # Condicion inicial
        P_vals[0] = self.P0

        # Iterar metodo de Euler
        for i in range(len(t_vals) - 1):
            t_n = t_vals[i]
            P_n = P_vals[i]

            # Paso de Euler: P_{n+1} = P_n + h * f(t_n, P_n)
            P_vals[i + 1] = P_n + self.h * self.f(t_n, P_n)

        return t_vals, P_vals

    def resolver(self, t):
        """
        Retorna la aproximacion numerica de P(t) usando Euler.

        Interpola linealmente entre los valores precalculados.

        Parametros:
        -----------
        t : float or array_like
            Tiempo(s) donde evaluar la solucion

        Retorna:
        --------
        float or array_like : P(t) aproximado
        """
        # Si t es escalar, convertir a array
        t_escalar = np.isscalar(t)
        t = np.atleast_1d(t)

        # Interpolar valores
        P = np.interp(t, self.t_vals, self.P_vals)

        # Retornar escalar si la entrada era escalar
        return P[0] if t_escalar else P

    def obtener_trayectoria(self):
        """
        Retorna la trayectoria completa calculada por Euler.

        Retorna:
        --------
        tuple : (t_vals, P_vals)
            t_vals : array de tiempos
            P_vals : array de poblaciones
        """
        return self.t_vals, self.P_vals

    def __repr__(self):
        """Representacion en string del modelo."""
        return (f"{self.nombre}\n"
                f"  P0={self.P0}, beta0={self.beta0}, alpha={self.alpha}\n"
                f"  h={self.h}, t_max={self.t_max}\n"
                f"  Puntos calculados: {len(self.t_vals)}\n"
                f"  Limite asintotico teorico: {self.limite_asintotico():.4f}")


if __name__ == '__main__':
    # Ejemplo de uso del metodo de Euler
    print("=== Metodo de Euler para Modelo de Tumor ===\n")

    # Crear instancia con diferentes tamaños de paso
    h_values = [0.1, 0.05, 0.01]

    for h in h_values:
        modelo = ModeloTumorEuler(P0=100, beta0=2.0, alpha=0.5, h=h, t_max=10.0)
        print(modelo)

        # Evaluar en puntos especificos
        t_test = np.array([0, 5, 10])
        P_test = modelo.resolver(t_test)

        print(f"\nSolucion numerica (Euler, h={h}):")
        for t, P in zip(t_test, P_test):
            print(f"  t = {t:5.1f} -> P(t) ≈ {P:8.2f}")
        print("\n" + "="*50 + "\n")

    # Comparar con solucion analitica
    from Ecuacion_De_Poblacion import ModeloTumorAnalitico

    modelo_euler = ModeloTumorEuler(P0=100, beta0=2.0, alpha=0.5, h=0.01)
    modelo_analitico = ModeloTumorAnalitico(P0=100, beta0=2.0, alpha=0.5)

    t_comp = np.array([1, 2, 5, 10])
    P_euler = modelo_euler.resolver(t_comp)
    P_exacto = modelo_analitico.resolver(t_comp)

    print("Comparacion Euler vs Analitico:")
    print(f"{'t':>6} {'Euler':>12} {'Exacto':>12} {'Error Rel':>12}")
    print("-" * 48)
    for t, Pe, Pex in zip(t_comp, P_euler, P_exacto):
        error_rel = abs(Pex - Pe) / abs(Pex) * 100
        print(f"{t:6.1f} {Pe:12.4f} {Pex:12.4f} {error_rel:11.4f}%")
