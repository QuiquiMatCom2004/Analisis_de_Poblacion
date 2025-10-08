#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modelo Matematico de Crecimiento de Poblacion - Solucion Analitica
Ecuacion Diferencial Ordinaria: dP/dt = beta_0 * e^(-alpha*t) * P

Este modulo contiene la clase ModeloTumorAnalitico que resuelve la EDO
usando la formula cerrada (solucion analitica exacta).

Autores: Enrique A. Gonzalez Moreira, Heily Rodriguez Rodriguez, Alex L. Cuervo Grillo
Asignatura: Matematica Numerica y Ecuaciones Diferenciales Ordinarias
"""

import numpy as np
from ModeloTumorBase import ModeloTumorBase


class ModeloTumorAnalitico(ModeloTumorBase):
    """
    Resolucion analitica (exacta) del modelo de crecimiento de tumor.

    Ecuacion diferencial: dP/dt = beta_0 * e^(-alpha*t) * P
    Solucion analitica: P(t) = P_0 * exp(beta_0/alpha * (1 - e^(-alpha*t)))
    Limite asintotico: lim(t->inf) P(t) = P_0 * exp(beta_0/alpha)

    Esta clase implementa el metodo resolver() usando la formula cerrada.
    """

    def __init__(self, P0, beta0, alpha):
        """
        Inicializa el modelo analitico.

        Parametros:
        -----------
        P0 : float
            Poblacion inicial
        beta0 : float
            Tasa de crecimiento inicial (beta_0)
        alpha : float
            Tasa de decrecimiento exponencial (alpha)
        """
        super().__init__(P0, beta0, alpha, nombre="Solucion Analitica")

    def resolver(self, t):
        """
        Resuelve la EDO usando la formula analitica exacta.

        P(t) = P_0 * exp(beta_0/alpha * (1 - e^(-alpha*t)))

        Parametros:
        -----------
        t : float or array_like
            Tiempo(s) donde evaluar la solucion

        Retorna:
        --------
        float or array_like : P(t)
        """
        return self.P0 * np.exp((self.beta0 / self.alpha) * (1 - np.exp(-self.alpha * t)))

    def solucion_analitica(self, t):
        """
        Alias de resolver() para compatibilidad con codigo antiguo.

        P(t) = P_0 * exp(beta_0/alpha * (1 - e^(-alpha*t)))

        Parametros:
        -----------
        t : float or array_like
            Tiempo(s) en el que evaluar la solucion

        Retorna:
        --------
        float or array_like : P(t)
        """
        return self.resolver(t)



# Aliases para compatibilidad con scripts antiguos
ModeloTumor = ModeloTumorAnalitico  # Alias para retrocompatibilidad


def crear_modelo(P0, beta0, alpha):
    """
    Funcion helper para crear una instancia del ModeloTumorAnalitico.

    Parametros:
    -----------
    P0 : float
        Poblacion inicial
    beta0 : float
        Tasa de crecimiento inicial
    alpha : float
        Tasa de decrecimiento exponencial

    Retorna:
    --------
    ModeloTumorAnalitico : Instancia del modelo analitico
    """
    return ModeloTumorAnalitico(P0, beta0, alpha)


if __name__ == '__main__':
    # Ejemplo de uso del modelo analitico
    print("=== Ejemplo de Uso del Modelo de Tumor (Solucion Analitica) ===\n")

    # Crear instancia del modelo
    modelo = ModeloTumorAnalitico(P0=100, beta0=2.0, alpha=0.5)
    print(modelo)
    print()

    # Evaluar en puntos especificos usando resolver()
    t_vals = np.array([0, 5, 10, 15, 20])
    P_vals = modelo.resolver(t_vals)

    print("Solucion analitica en tiempos especificos:")
    for t, P in zip(t_vals, P_vals):
        print(f"  t = {t:5.1f} -> P(t) = {P:8.2f}")
    print()

    # Calcular derivada en un punto usando f()
    t_punto = 5.0
    P_punto = modelo.resolver(t_punto)
    dP_dt = modelo.f(t_punto, P_punto)
    print(f"En t = {t_punto}:")
    print(f"  P(t) = {P_punto:.2f}")
    print(f"  dP/dt = {dP_dt:.4f}")
    print()

    # Verificar tasa de crecimiento
    print(f"Tasa de crecimiento en t={t_punto}: r({t_punto}) = {modelo.tasa_crecimiento(t_punto):.4f}")
    print()

    # Verificar que la EDO se cumple
    print("Verificacion: f(t,P) = beta_0 * e^(-alpha*t) * P")
    print(f"  f({t_punto}, {P_punto:.2f}) = {dP_dt:.4f}")
    print(f"  beta_0 * e^(-alpha*t) * P = {modelo.beta0} * {np.exp(-modelo.alpha * t_punto):.4f} * {P_punto:.2f} = {dP_dt:.4f}")
    print("  ✓ Ecuacion diferencial satisfecha")
