#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
import numpy as np

class ModeloBifurcacion(ABC):
    """
    Clase para el modelo de bifurcacion dz/dt = μz - z³
    """
    
    def __init__(self, nombre="Modelo Bifurcacion"):
        self.nombre = nombre
        self.tipo_bifurcacion = "Horquilla Supercrítica"
    
    def puntos_equilibrio(self, mu):
        """
        Calcula los puntos de equilibrio y su estabilidad
        
        Parametros:
        -----------
        mu : array_like
            Valores del parametro μ
            
        Retorna:
        --------
        tuple : (estables, inestables)
            Listas con puntos estables e inestables
        """
        mu = np.asarray(mu)
        
        # Puntos de equilibrio: z(μ - z²) = 0
        z0 = np.zeros_like(mu)  # z* = 0
        
        # z* = ±√μ (solo para μ >= 0)
        mask_positivo = mu >= 0
        z_positivo = np.where(mask_positivo, np.sqrt(mu), np.nan)
        z_negativo = np.where(mask_positivo, -np.sqrt(mu), np.nan)
        
        # Determinar estabilidad
        mask_mu_neg = mu < 0
        mask_mu_pos = mu > 0
        
        # Puntos estables
        estables = [
            np.where(mask_mu_neg, z0, np.nan),  # z=0 para μ<0 (estable)
            z_positivo,  # z=√μ para μ>0 (estable)
            z_negativo   # z=-√μ para μ>0 (estable)
        ]
        
        # Puntos inestables
        inestables = [
            np.where(mask_mu_pos, z0, np.nan)  # z=0 para μ>0 (inestable)
            ]
        
        return estables, inestables
    
    def campo_direcciones(self, mu, z):
        """
        Calcula el campo de direcciones para visualizacion
        
        Parametros:
        -----------
        mu : array_like
            Valores del parametro μ
        z : array_like  
            Valores de la variable z
            
        Retorna:
        --------
        tuple : (dmu_norm, dz_norm)
            Componentes normalizadas del campo de direcciones
        """
        MU, Z = np.meshgrid(mu, z)
        
        # dz/dt = μz - z³
        dZ = MU * Z - Z**3
        dMU = np.zeros_like(dZ)  # μ es parametro, no evoluciona
        
        # Normalizar para visualizacion
        magnitud = np.sqrt(dMU**2 + dZ**2)
        magnitud[magnitud == 0] = 1  # Evitar division por cero
        
        return dMU/magnitud, dZ/magnitud
    
    def resolver(self, mu, z0, t_max=10, dt=0.01):
        """
        Resuelve numericamente la EDO para parametros dados
        Implementa polimorfismo con modelos de la Parte A
        
        Parametros:
        -----------
        mu : float
            Parametro de bifurcacion
        z0 : float
            Condicion inicial
        t_max : float
        Tiempo maximo de integracion
        dt : float
            Paso de tiempo
            
        Retorna:
        --------
        tuple : (t, z)
            Arrays de tiempo y solucion
        """
        t = np.arange(0, t_max, dt)
        z = np.zeros_like(t)
        z[0] = z0
        
        # Metodo de Euler
        for i in range(1, len(t)):
            dz_dt = mu * z[i-1] - z[i-1]**3
            z[i] = z[i-1] + dt * dz_dt
        return t, z
    
    def analizar_bifurcacion(self, mu_val):
        """
        Analiza el comportamiento del sistema para un μ dado
        
        Parametros:
        -----------
        mu_val : float
            Valor del parametro μ
            
        Retorna:
        --------
         dict : Informacion del analisis
        """
        estables, inestables = self.puntos_equilibrio([mu_val])
        
        resultado = {
            'mu': mu_val,
            'estables': [],
            'inestables': [],
            'interpretacion': '',
            'regimen': ''
        }
        
        # Procesar puntos estables
        for z_eq in estables:
            z_val = z_eq[0]
            if not np.isnan(z_val):
                resultado['estables'].append(z_val)

        # Procesar puntos inestables
        for z_eq in inestables:
            z_val = z_eq[0]
            if not np.isnan(z_val):
                resultado['inestables'].append(z_val)
        
        # Determinar regimen e interpretacion
        if mu_val < 0:
            resultado['regimen'] = 'EXTINCIÓN'
            resultado['interpretacion'] = 'Condiciones adversas: población converge a cero'
        elif mu_val == 0:
            resultado['regimen'] = 'BIFURCACIÓN'
            resultado['interpretacion'] = 'Umbral crítico: transición entre regímenes'
        else:
            resultado['regimen'] = 'SUPERVIVENCIA'
            resultado['interpretacion'] = 'Condiciones favorables: población estabiliza en valor positivo'
            
        return resultado