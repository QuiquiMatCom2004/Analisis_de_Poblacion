#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clase Base Abstracta para Modelos de Tumor

Define la interfaz comun para todos los metodos de resolucion del modelo de tumor.
Permite usar polimorfismo para comparar facilmente diferentes metodos (analitico, Euler, RK4, etc.)

Ecuacion Diferencial: dP/dt = beta_0 * e^(-alpha*t) * P

Autores: Enrique A. Gonzalez Moreira, Heily Rodriguez Rodriguez, Alex L. Cuervo Grillo
Asignatura: Matematica Numerica y Ecuaciones Diferenciales Ordinarias
"""

from abc import ABC, abstractmethod
import numpy as np


class ModeloTumorBase(ABC):
    """
    Clase abstracta base para modelos de tumor.

    Define la interfaz comun que deben implementar todos los metodos de resolucion
    (analitico, Euler, RK4, etc.), permitiendo usar polimorfismo para:
    - Comparar soluciones
    - Graficar multiples metodos juntos
    - Calcular errores entre metodos

    La EDO es la misma para todos: dP/dt = beta_0 * e^(-alpha*t) * P
    Lo que varia es el metodo de resolucion (analitico vs numericos).

    Atributos:
    ----------
    P0 : float
        Poblacion inicial
    beta0 : float
        Tasa de crecimiento inicial (beta_0)
    alpha : float
        Tasa de decrecimiento exponencial (alpha)
    nombre : str
        Nombre descriptivo del metodo
    """

    def __init__(self, P0, beta0, alpha, nombre="Modelo Base"):
        """
        Inicializa el modelo base con parametros comunes.

        Parametros:
        -----------
        P0 : float
            Poblacion inicial
        beta0 : float
            Tasa de crecimiento inicial (beta_0)
        alpha : float
            Tasa de decrecimiento exponencial (alpha)
        nombre : str, opcional
            Nombre descriptivo del metodo
        """
        self.P0 = P0
        self.beta0 = beta0
        self.alpha = alpha
        self.nombre = nombre

    def f(self, t, P):
        """
        Ecuacion diferencial del modelo: dP/dt = f(t, P)

        f(t, P) = beta_0 * e^(-alpha*t) * P

        Esta es la EDO que todos los metodos resuelven.
        Es CONCRETA porque es la misma para todos los metodos.

        Parametros:
        -----------
        t : float or array_like
            Tiempo
        P : float or array_like
            Poblacion

        Retorna:
        --------
        float or array_like : dP/dt
        """
        return self.beta0 * np.exp(-self.alpha * t) * P

    @abstractmethod
    def resolver(self, t):
        """
        Resuelve la EDO y retorna P(t).

        Este metodo DEBE ser implementado por cada subclase:
        - ModeloTumorAnalitico: usa la formula cerrada
        - ModeloTumorEuler: itera con el metodo de Euler
        - ModeloTumorRK4: itera con Runge-Kutta de orden 4

        Parametros:
        -----------
        t : float or array_like
            Tiempo(s) donde evaluar la solucion

        Retorna:
        --------
        float or array_like : P(t)
        """
        pass

    def limite_asintotico(self):
        """
        Calcula el limite asintotico de la poblacion cuando t tiende a infinito.

        lim(t->inf) P(t) = P_0 * exp(beta_0/alpha)

        Este resultado teorico es independiente del metodo de resolucion.

        Retorna:
        --------
        float : Poblacion limite P_inf
        """
        return self.P0 * np.exp(self.beta0 / self.alpha)

    def factor_crecimiento(self):
        """
        Calcula el factor de crecimiento total del modelo.

        Factor = exp(beta_0/alpha)

        Retorna:
        --------
        float : Factor de crecimiento
        """
        return np.exp(self.beta0 / self.alpha)

    def tasa_crecimiento(self, t):
        """
        Calcula la tasa de crecimiento variable r(t) = beta_0 * e^(-alpha*t).

        Parametros:
        -----------
        t : float or array_like
            Tiempo(s)

        Retorna:
        --------
        float or array_like : Tasa de crecimiento r(t)
        """
        return self.beta0 * np.exp(-self.alpha * t)

    def generar_isoclinas(self, t, num_isoclinas=8):
        """
        Genera curvas isoclinas para el campo de direcciones.

        Las isoclinas son curvas de la familia:
        P(t) = C * exp(-beta_0/alpha * e^(-alpha*t))

        donde C es una constante que varia para diferentes isoclinas.

        Parametros:
        -----------
        t : array_like
            Array de tiempos donde evaluar las isoclinas
        num_isoclinas : int, opcional
            Numero de isoclinas a generar (default: 8)

        Retorna:
        --------
        list of tuples : Lista de tuplas (C, P_iso) donde:
            - C es la constante de la isoclina
            - P_iso es el array de valores P(t) para esa isoclina
        """
        P_inf = self.limite_asintotico()
        C_values = np.linspace(0.2 * self.P0, 2.5 * P_inf, num_isoclinas)

        isoclinas = []
        for C in C_values:
            P_iso = C * np.exp(-self.beta0 / self.alpha * np.exp(-self.alpha * t))
            isoclinas.append((C, P_iso))

        return isoclinas

    def campo_direcciones(self, T, P):
        """
        Calcula el campo de direcciones normalizado para visualizacion.

        El campo de direcciones muestra las pendientes dP/dt en cada punto (t, P).
        Los vectores se normalizan para mejor visualizacion.

        Parametros:
        -----------
        T : array_like
            Grilla de tiempos (meshgrid)
        P : array_like
            Grilla de poblaciones (meshgrid)

        Retorna:
        --------
        tuple : (dT_norm, dP_norm)
            - dT_norm: Componentes normalizadas en direccion t
            - dP_norm: Componentes normalizadas en direccion P
        """
        # En el plano (t, P), el vector de direccion es (1, dP/dt)
        dT = np.ones_like(T)
        dP = self.f(T, P)

        # Normalizar para visualizacion
        magnitud = np.sqrt(dT**2 + dP**2)
        dT_norm = dT / magnitud
        dP_norm = dP / magnitud

        return dT_norm, dP_norm

    def __repr__(self):
        """Representacion en string del modelo."""
        return (f"{self.nombre}\n"
                f"  P0={self.P0}, beta0={self.beta0}, alpha={self.alpha}\n"
                f"  Limite asintotico: {self.limite_asintotico():.4f}\n"
                f"  Factor de crecimiento: {self.factor_crecimiento():.4f}")


if __name__ == '__main__':
    # Esta clase es abstracta, no se puede instanciar directamente
    print("ModeloTumorBase es una clase abstracta.")
    print("Debe ser heredada por clases concretas (ModeloTumorAnalitico, ModeloTumorEuler, etc.)")

    # Intentar instanciar (esto dara error)
    try:
        modelo = ModeloTumorBase(P0=100, beta0=2.0, alpha=0.5)
        print("Instancia creada (no deberia pasar)")
    except TypeError as e:
        print(f"\nError esperado al intentar instanciar clase abstracta:")
        print(f"  {e}")
