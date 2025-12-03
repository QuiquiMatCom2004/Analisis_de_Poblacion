#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualizacion del Diagrama de Bifurcacion - Versión Completa
Parte B - Modelo de Bifurcacion Poblacional

Este modulo contiene funciones para visualizar el diagrama de bifurcacion
del modelo reducido dz/dt = μz - z³.

Autores: Enrique A. Gonzalez Moreira, Heily Rodriguez Rodriguez, Alex L. Cuervo Grillo
Asignatura: Matematica Numerica y Ecuaciones Diferenciales Ordinarias
"""

import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib import cm
from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib.patches as patches
from matplotlib.lines import Line2D
from ModeloBifurcacion import ModeloBifurcacion

# Directorio para guardar figuras
FIGURAS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Figuras')
os.makedirs(FIGURAS_DIR, exist_ok=True)

# =============================================================================
# FUNCIONES ORIGINALES DEL CÓDIGO
# =============================================================================

def graficar_diagrama_bifurcacion(modelo, mu_range=(-2, 2), z_range=(-2, 2), num_puntos=1000, figsize=(12, 8), guardar=None):
    """
    Genera el diagrama de bifurcacion completo
    
    Parametros:
    -----------
    modelo : ModeloBifurcacion
        Instancia del modelo
    mu_range : tuple, opcional
        Rango de μ (min, max) (default: (-2, 2))
    z_range : tuple, opcional
        Rango de z (min, max) (default: (-2, 2))
    num_puntos : int, opcional
        Numero de puntos para calcular (default: 1000)
    figsize : tuple, opcional
        Tamano de la figura (default: (12, 8))
    guardar : str, opcional
        Ruta para guardar el grafico (default: None)
        
    Retorna:
    --------
    tuple : (fig, ax)
        Objetos Figure y Axes
    """
    # Crear figura
    fig, ax = plt.subplots(figsize=figsize)

    # CALCULAR PUNTOS DE EQUILIBRIO
    mu = np.linspace(mu_range[0], mu_range[1], num_puntos)
    estables, inestables = modelo.puntos_equilibrio(mu)
    
    # GRAFICAR RAMAS ESTABLES
    # Rama z = 0 para μ < 0 (estable)
    mask_mu_neg = mu < 0
    ax.plot(mu[mask_mu_neg], np.zeros_like(mu[mask_mu_neg]), 
            'b-', linewidth=3, alpha=0.8, label='Estable')
    
    # Ramas z = ±√μ para μ > 0 (estables)
    mask_mu_pos = mu > 0
    ax.plot(mu[mask_mu_pos], np.sqrt(mu[mask_mu_pos]), 
            'b-', linewidth=3, alpha=0.8)
    ax.plot(mu[mask_mu_pos], -np.sqrt(mu[mask_mu_pos]), 
            'b-', linewidth=3, alpha=0.8)
    
    # GRAFICAR RAMAS INESTABLES 
    # Rama z = 0 para μ > 0 (inestable)
    ax.plot(mu[mask_mu_pos], np.zeros_like(mu[mask_mu_pos]), 
            'r--', linewidth=3, alpha=0.8, label='Inestable')
    
    # MARCAR PUNTO DE BIFURCACION 
    # Linea vertical en μ = 0
    ax.axvline(x=0, color='k', linestyle=':', alpha=0.7, linewidth=2)
    
    # Punto de bifurcacion
    ax.plot(0, 0, 'ko', markersize=10, markerfacecolor='red', 
            markeredgewidth=2, label='Punto de Bifurcación')
    
    # Anotacion del punto de bifurcacion
    ax.annotate('Bifurcación de Horquilla\nμ = 0', 
                xy=(0, 0), xytext=(0.5, -1.5),
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
                fontsize=12, color='red', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))
    
    # ZONAS COLOREDAS PARA INTERPRETACION 
    # Zona de extincion (μ < 0)
    ax.axvspan(mu_range[0], 0, alpha=0.1, color='red', label='μ < 0: Extinción')
    
    # Zona de supervivencia (μ > 0)  
    ax.axvspan(0, mu_range[1], alpha=0.1, color='green', label='μ > 0: Supervivencia')
    
    # CONFIGURACION DEL GRAFICO 
    ax.set_xlabel('Parámetro de Control μ', fontsize=14, fontweight='bold')
    ax.set_ylabel('Puntos de Equilibrio z*', fontsize=14, fontweight='bold')
    ax.set_title('Diagrama de Bifurcación: dz/dt = μz - z³\n' +
                'Transición: Extinción ↔ Supervivencia Poblacional', 
                fontsize=16, fontweight='bold')
    
    ax.grid(True, alpha=0.3)
    ax.set_xlim(mu_range)
    ax.set_ylim(z_range)
    
    # ========== LEYENDA PERSONALIZADA ==========
    legend_elements = [
        Line2D([0], [0], color='blue', lw=3, label='Ramas Estables'),
        Line2D([0], [0], color='red', lw=3, linestyle='--', label='Ramas Inestables'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='red', 
               markersize=8, label='Punto de Bifurcación'),
        patches.Patch(color='red', alpha=0.1, label='μ < 0: Extinción'),
        patches.Patch(color='green', alpha=0.1, label='μ > 0: Supervivencia')
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=10)
    
    # TEXTO EXPLICATIVO
    texto_explicacion = (
        "INTERPRETACIÓN POBLACIONAL:\n"
        "• μ < 0: Condiciones desfavorables\n"
        "  → Extinción (z=0 estable)\n"
        "• μ = 0: Umbral crítico\n"
        "  → Bifurcación de horquilla\n"
        "• μ > 0: Condiciones favorables\n"
        "  → Supervivencia (z=±√μ estables)"
    )
    
    ax.text(0.02, 0.98, texto_explicacion, transform=ax.transAxes,
            fontsize=11, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
    
    # INFORMACION MATEMATICA
    texto_matematico = (
        "ANÁLISIS MATEMÁTICO:\n"
        "• Puntos equilibrio: z* = 0, ±√μ\n"
        "• Estabilidad: f'(z) = μ - 3z²\n"
        "• Tipo: Bifurcación horquilla supercrítica\n"
        "• Simetría: Sistema es impar (z → -z)"
    )
    
    ax.text(0.02, 0.15, texto_matematico, transform=ax.transAxes,
            fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))
    
    plt.tight_layout()
    
    # Guardar si se especifica
    if guardar:
        # Si guardar es solo un nombre de archivo, usar carpeta Figuras
        if not os.path.dirname(guardar):
            guardar = os.path.join(FIGURAS_DIR, guardar)
        plt.savefig(guardar, dpi=300, bbox_inches='tight')
        print(f"Diagrama de bifurcación guardado: {guardar}")
    
    return fig, ax

def graficar_bifurcacion_interactiva(mu_range=(-2, 2), z_range=(-2, 2)):
    """
    Genera visualizacion interactiva del diagrama de bifurcacion
    
    Parametros:
    -----------
    mu_range : tuple, opcional
        Rango de μ (default: (-2, 2))
    z_range : tuple, opcional
        Rango de z (default: (-2, 2))
    """
    # Crear figura con espacio para controles
    fig, ax = plt.subplots(figsize=(14, 9))
    plt.subplots_adjust(left=0.1, bottom=0.3)
    
    # Modelo
    modelo = ModeloBifurcacion()
    
    # ========== DIAGRAMA BASE ==========
    mu_diagrama = np.linspace(mu_range[0], mu_range[1], 1000)
    
    # Calcular y graficar ramas estables
    mask_mu_neg = mu_diagrama < 0
    mask_mu_pos = mu_diagrama > 0
    
    # Ramas estables
    linea_estable1, = ax.plot(mu_diagrama[mask_mu_neg], 
                             np.zeros_like(mu_diagrama[mask_mu_neg]), 
                             'b-', linewidth=3, alpha=0.8)
    linea_estable2, = ax.plot(mu_diagrama[mask_mu_pos], 
                             np.sqrt(mu_diagrama[mask_mu_pos]), 
                             'b-', linewidth=3, alpha=0.8)
    linea_estable3, = ax.plot(mu_diagrama[mask_mu_pos], 
                             -np.sqrt(mu_diagrama[mask_mu_pos]), 
                             'b-', linewidth=3, alpha=0.8)
    
    # Rama inestable
    linea_inestable, = ax.plot(mu_diagrama[mask_mu_pos], 
                              np.zeros_like(mu_diagrama[mask_mu_pos]), 
                              'r--', linewidth=3, alpha=0.8)
    
    # Punto de bifurcacion
    linea_bifurcacion = ax.axvline(x=0, color='k', linestyle=':', alpha=0.7)
    punto_bifurcacion, = ax.plot(0, 0, 'ko', markersize=10, 
                                markerfacecolor='red', markeredgewidth=2)
    
    # ELEMENTOS INTERACTIVOS
    # Linea vertical para μ actual
    mu_actual = 1.0
    line_mu_actual = ax.axvline(x=mu_actual, color='purple', 
                               linestyle='-', alpha=0.8, linewidth=2)
    
    # Puntos de equilibrio para μ actual
    analisis = modelo.analizar_bifurcacion(mu_actual)
    
    puntos_estables = []
    for z_eq in analisis['estables']:
        punto, = ax.plot(mu_actual, z_eq, 'bo', markersize=8,
                        markerfacecolor='blue', markeredgewidth=2)
        puntos_estables.append(punto)

    puntos_inestables = []
    for z_eq in analisis['inestables']:
        punto, = ax.plot(mu_actual, z_eq, 'ro', markersize=8,
                        markerfacecolor='none', markeredgewidth=2)
        puntos_inestables.append(punto)
    
    # CONFIGURACION INICIAL
    ax.set_xlabel('Parámetro de Control μ', fontsize=14, fontweight='bold')
    ax.set_ylabel('Puntos de Equilibrio z*', fontsize=14, fontweight='bold')
    ax.set_title('Diagrama de Bifurcación Interactivo\n' +
                'dz/dt = μz - z³', fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(mu_range)
    ax.set_ylim(z_range)

    # CONTROLES INTERACTIVOS
    # Slider para μ
    ax_mu = plt.axes([0.15, 0.15, 0.7, 0.03])
    slider_mu = Slider(ax_mu, 'Parámetro μ', mu_range[0], mu_range[1], 
                      valinit=mu_actual, color='#2E86DE')
    
    # Area de informacion
    info_text = fig.text(0.5, 0.05, '', fontsize=11, ha='center', 
                        family='monospace',
                        bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
    
    def update(val):
        """Actualiza el diagrama cuando cambia el slider"""
        mu_val = slider_mu.val
        
        # Actualizar linea de μ actual
        line_mu_actual.set_xdata([mu_val, mu_val])

         # Actualizar analisis
        analisis = modelo.analizar_bifurcacion(mu_val)
        
        # Limpiar puntos anteriores
        for punto in puntos_estables + puntos_inestables:
            punto.set_data([], [])
        
        # Actualizar puntos estables
        for i, z_eq in enumerate(analisis['estables']):
            if i < len(puntos_estables):
                puntos_estables[i].set_data([mu_val], [z_eq])
        
        # Actualizar puntos inestables
        for i, z_eq in enumerate(analisis['inestables']):
            if i < len(puntos_inestables):
                puntos_inestables[i].set_data([mu_val], [z_eq])

         # Actualizar informacion
        info_str = (f"μ = {mu_val:.2f}\n"
                   f"Regimen: {analisis['regimen']}\n"
                   f"Equilibrios estables: {[f'{z:.3f}' for z in analisis['estables']]}\n"
                   f"Equilibrios inestables: {[f'{z:.3f}' for z in analisis['inestables']]}\n"
                   f"Interpretación: {analisis['interpretacion']}")
        
        info_text.set_text(info_str)
        fig.canvas.draw_idle()
    
    # Conectar slider
    slider_mu.on_changed(update)
    
    # Informacion inicial
    update(None)

    plt.show()

# =============================================================================
# NUEVAS FUNCIONALIDADES AÑADIDAS
# =============================================================================

def graficar_diagrama_estatico_multiple_funciones():
    """
    Diagrama estático que muestra múltiples funciones z = ±√μ para diferentes valores de μ
    """
    modelo = ModeloBifurcacion()
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # ========== DIAGRAMA DE BIFURCACIÓN BASE ==========
    mu_fondo = np.linspace(-2, 2, 1000)
    
    # Rama estable z = 0 para μ < 0
    mask_mu_neg = mu_fondo < 0
    ax.plot(mu_fondo[mask_mu_neg], np.zeros_like(mu_fondo[mask_mu_neg]), 
            'b-', linewidth=3, alpha=0.8, label='Ramas Estables')
    
    # Ramas estables z = ±√μ para μ > 0
    mask_mu_pos = mu_fondo > 0
    ax.plot(mu_fondo[mask_mu_pos], np.sqrt(mu_fondo[mask_mu_pos]), 
            'b-', linewidth=3, alpha=0.8)
    ax.plot(mu_fondo[mask_mu_pos], -np.sqrt(mu_fondo[mask_mu_pos]), 
            'b-', linewidth=3, alpha=0.8)
    
    # Rama inestable z = 0 para μ > 0
    ax.plot(mu_fondo[mask_mu_pos], np.zeros_like(mu_fondo[mask_mu_pos]), 
            'r--', linewidth=3, alpha=0.8, label='Rama Inestable')
    
    # ========== MULTIPLES FUNCIONES z = ±√μ ==========
    mu_valores = [0.25, 0.5, 1.0, 1.5, 2.0]
    colores = ['red', 'green', 'blue', 'purple', 'orange']
    
    for i, (mu_val, color) in enumerate(zip(mu_valores, colores)):
        # Puntos en las funciones z = ±√μ
        z_pos = np.sqrt(mu_val)
        z_neg = -np.sqrt(mu_val)
        
        # Líneas verticales para cada μ
        ax.axvline(x=mu_val, color=color, linestyle=':', alpha=0.5)
        
        # Puntos en las funciones
        ax.plot(mu_val, z_pos, 'o', color=color, markersize=8, 
               label=f'μ={mu_val}, z=√μ={z_pos:.2f}')
        ax.plot(mu_val, z_neg, 's', color=color, markersize=8,
               label=f'μ={mu_val}, z=-√μ={z_neg:.2f}')
        
        # Etiquetas de los valores
        ax.text(mu_val + 0.05, z_pos + 0.1, f'√{mu_val}={z_pos:.2f}', 
               fontsize=9, color=color)
        ax.text(mu_val + 0.05, z_neg - 0.1, f'-√{mu_val}={z_neg:.2f}', 
               fontsize=9, color=color)
    
    # ========== ELEMENTOS ADICIONALES ==========
    # Punto de bifurcación
    ax.axvline(x=0, color='k', linestyle=':', alpha=0.7, linewidth=2)
    ax.plot(0, 0, 'ko', markersize=10, markerfacecolor='red', 
            markeredgewidth=2, label='Punto de Bifurcación')
    
    # Zonas coloreadas
    ax.axvspan(-2, 0, alpha=0.1, color='red', label='μ < 0: Extinción')
    ax.axvspan(0, 2, alpha=0.1, color='green', label='μ > 0: Supervivencia')
    
    # Configuración
    ax.set_xlabel('Parámetro de Control μ', fontsize=14, fontweight='bold')
    ax.set_ylabel('Puntos de Equilibrio z*', fontsize=14, fontweight='bold')
    ax.set_title('Diagrama de Bifurcación con Múltiples Funciones z = ±√μ\n' +
                'dz/dt = μz - z³', fontsize=16, fontweight='bold')
    
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    plt.tight_layout()
    plt.show()

def graficar_diagrama_interactivo_funciones():
    """
    Diagrama interactivo donde se puede variar μ y ver las funciones z = ±√μ actualizarse
    """
    modelo = ModeloBifurcacion()
    
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.subplots_adjust(bottom=0.25)
    
    # ========== CONFIGURACIÓN INICIAL ==========
    mu_actual = 1.0
    mu_range = (-2, 2)
    z_range = (-2, 2)
    
    # ========== DIAGRAMA DE FONDO ==========
    mu_fondo = np.linspace(mu_range[0], mu_range[1], 1000)
    
    # Rama estable z = 0 para μ < 0
    mask_mu_neg = mu_fondo < 0
    ax.plot(mu_fondo[mask_mu_neg], np.zeros_like(mu_fondo[mask_mu_neg]), 
            'gray', linewidth=2, alpha=0.5)
    
    # Ramas estables z = ±√μ para μ > 0
    mask_mu_pos = mu_fondo > 0
    ax.plot(mu_fondo[mask_mu_pos], np.sqrt(mu_fondo[mask_mu_pos]), 
            'gray', linewidth=2, alpha=0.5)
    ax.plot(mu_fondo[mask_mu_pos], -np.sqrt(mu_fondo[mask_mu_pos]), 
            'gray', linewidth=2, alpha=0.5)
    
    # Rama inestable z = 0 para μ > 0
    ax.plot(mu_fondo[mask_mu_pos], np.zeros_like(mu_fondo[mask_mu_pos]), 
            'gray', linestyle='--', linewidth=2, alpha=0.5)
    
    # ========== FUNCIONES INTERACTIVAS z = ±√μ ==========
    # Líneas para las funciones que se actualizarán
    line_func_pos, = ax.plot([], [], 'b-', linewidth=3, label='z = √μ')
    line_func_neg, = ax.plot([], [], 'r-', linewidth=3, label='z = -√μ')
    
    # Puntos actuales en las funciones
    punto_pos, = ax.plot([], [], 'bo', markersize=10, markerfacecolor='blue')
    punto_neg, = ax.plot([], [], 'ro', markersize=10, markerfacecolor='red')
    
    # Línea vertical para μ actual
    line_mu_actual = ax.axvline(x=mu_actual, color='purple', linewidth=2, 
                               alpha=0.8, label='μ Actual')
    
    # ========== CONFIGURACIÓN DEL GRÁFICO ==========
    ax.axvline(x=0, color='k', linestyle=':', alpha=0.7)
    ax.axhline(y=0, color='k', linestyle=':', alpha=0.7)
    
    ax.set_xlabel('Parámetro de Control μ', fontsize=14, fontweight='bold')
    ax.set_ylabel('Puntos de Equilibrio z*', fontsize=14, fontweight='bold')
    ax.set_title('Diagrama de Bifurcación Interactivo\n' +
                'Variar μ para ver las funciones z = ±√μ', 
                fontsize=16, fontweight='bold')
    
    ax.grid(True, alpha=0.3)
    ax.set_xlim(mu_range)
    ax.set_ylim(z_range)
    ax.legend(loc='upper right')
    
    # ========== CONTROLES INTERACTIVOS ==========
    # Slider para μ
    ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
    slider_mu = Slider(ax_slider, 'Parámetro μ', mu_range[0], mu_range[1], 
                      valinit=mu_actual, valstep=0.01)
    
    # Área de información
    info_text = fig.text(0.5, 0.02, '', fontsize=12, ha='center', 
                        bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
    
    def update(val):
        """Actualiza las funciones cuando cambia μ"""
        mu_actual = slider_mu.val
        
        # Actualizar línea vertical de μ actual
        line_mu_actual.set_xdata([mu_actual, mu_actual])
        
        # Actualizar funciones z = ±√μ
        if mu_actual >= 0:
            # Mostrar funciones completas
            mu_func = np.linspace(0, max(2, mu_actual), 1000)
            z_pos_func = np.sqrt(mu_func)
            z_neg_func = -np.sqrt(mu_func)
            
            line_func_pos.set_data(mu_func, z_pos_func)
            line_func_neg.set_data(mu_func, z_neg_func)
            
            # Actualizar puntos actuales
            punto_pos.set_data([mu_actual], [np.sqrt(mu_actual)])
            punto_neg.set_data([mu_actual], [-np.sqrt(mu_actual)])
            
            func_info = f"z = √μ = {np.sqrt(mu_actual):.3f}\nz = -√μ = {-np.sqrt(mu_actual):.3f}"
        else:
            # Ocultar funciones para μ < 0
            line_func_pos.set_data([], [])
            line_func_neg.set_data([], [])
            punto_pos.set_data([], [])
            punto_neg.set_data([], [])
            func_info = "Funciones no definidas para μ < 0"
        
        # Análisis del sistema
        analisis = modelo.analizar_bifurcacion(mu_actual)
        
        # Actualizar información
        info_str = (f"μ = {mu_actual:.2f} | {analisis['regimen']}\n"
                   f"{func_info}\n"
                   f"Puntos estables: {[f'{z:.3f}' for z in analisis['estables']]}\n"
                   f"Puntos inestables: {[f'{z:.3f}' for z in analisis['inestables']]}")
        
        info_text.set_text(info_str)
        fig.canvas.draw_idle()
    
    # Conectar el slider
    slider_mu.on_changed(update)
    
    # Botón de reset
    ax_reset = plt.axes([0.85, 0.15, 0.1, 0.04])
    boton_reset = Button(ax_reset, 'Reset', color='lightcoral')
    
    def reset(event):
        slider_mu.set_val(1.0)
    
    boton_reset.on_clicked(reset)
    
    # Actualización inicial
    update(None)
    
    plt.show()

def demostrar_tipos_bifurcacion():
    """
    Demuestra diferentes tipos de bifurcacion para comparacion
    """
    print("\n" + "="*70)
    print("TIPOS DE BIFURCACIÓN - COMPARACIÓN")
    print("="*70)
    
    print("\n1. BIFURCACIÓN DE HORQUILLA SUPERCRÍTICA (nuestro caso):")
    print("   - Ecuación: dz/dt = μz - z³")
    print("   - Características:")
    print("     * Transición suave entre regímenes")
    print("     * Nuevos equilibrios son estables")
    print("     * Típica en sistemas físicos y biológicos")
    print("   - Interpretación poblacional:")
    print("     * μ < 0: Extinción inevitable")
    print("     * μ = 0: Umbral crítico")
    print("     * μ > 0: Supervivencia estable")
    
    print("\n2. BIFURCACIÓN DE HORQUILLA SUBCRÍTICA:")
    print("   - Ecuación: dz/dt = μz + z³") 
    print("   - Características:")
    print("     * Transición abrupta (catastrófica)")
    print("     * Nuevos equilibrios son inestables")
    print("     * Menos común en sistemas naturales")
    print("   - Interpretación poblacional:")
    print("     * Cambios bruscos en la población")
    print("     * Posibles colapsos abruptos")
    
    print("\n3. BIFURCACIÓN DE SILLA-NODO:")
    print("   - Ecuación: dz/dt = μ - z²")
    print("   - Características:")
    print("     * Colisión y aniquilación de equilibrios")
    print("     * Umbral absoluto")
    print("     * Común en sistemas de umbral")
    print("   - Interpretación poblacional:")
    print("     * Umbrales absolutos de supervivencia")
    print("     * Efectos de punto de no retorno")
    
    print("\n" + "="*70)
    print("NUESTRO CASO: BIFURCACIÓN DE HORQUILLA SUPERCRÍTICA")
    print("  - Representa transición gradual extinción-supervivencia")
    print("  - Parámetro μ representa condiciones ambientales netas")
    print("  - Equilibrios estables no nulos → Poblaciones sostenibles")
    print("  - Punto μ=0 → Umbral crítico de supervivencia")
    print("="*70)

# =============================================================================
# PROGRAMA PRINCIPAL COMPLETO
# =============================================================================
if __name__ == '__main__':
    print("="*70)
    print("DIAGRAMA DE BIFURCACIÓN - PARTE B - VERSIÓN COMPLETA")
    print("Modelo: dz/dt = μz - z³")
    print("="*70)
    
    print("\nElige modo de visualización:")
    print("1. Diagrama estático completo (original)")
    print("2. Visualización interactiva (original)")
    print("3. Diagrama estático con múltiples funciones z = ±√μ")
    print("4. Visualización interactiva de funciones z = ±√μ")
    print("5. Análisis comparativo de bifurcaciones")
    
    opcion = input("\nOpción (1/2/3/4/5): ").strip()
    
    modelo = ModeloBifurcacion()
    
    if opcion == '1':
        print("\n--- Diagrama Estático Completo ---")
        print("Generando diagrama de bifurcación...")
        print(f"Tipo de bifurcación: {modelo.tipo_bifurcacion}")
        
        fig, ax = graficar_diagrama_bifurcacion(
            modelo,
            mu_range=(-2, 2),
            z_range=(-2, 2),
            num_puntos=1000,
            guardar='diagrama_bifurcacion.png'
        )
        
        print("\nMostrando diagrama...")
        plt.show()
        
    elif opcion == '2':
        print("\n--- Visualización Interactiva ---")
        print("Instrucciones:")
        print("  - Usa el slider para explorar diferentes valores de μ")
        print("  - Observa cómo cambian los puntos de equilibrio")
        print("  - La línea púrpura indica el valor actual de μ")
        print("  - Los puntos azules son equilibrios estables")
        print("  - Los puntos rojos vacíos son equilibrios inestables")
        print("\nAbriendo visualización interactiva...")
        
        graficar_bifurcacion_interactiva(mu_range=(-2, 2), z_range=(-2, 2))
        
    elif opcion == '3':
        print("\n--- Diagrama Estático con Múltiples Funciones ---")
        print("Mostrando funciones z = ±√μ para μ = 0.25, 0.5, 1.0, 1.5, 2.0")
        graficar_diagrama_estatico_multiple_funciones()
        
    elif opcion == '4':
        print("\n--- Visualización Interactiva de Funciones ---")
        print("Instrucciones:")
        print("  - Usa el slider para variar μ de -2 a 2")
        print("  - Observa cómo las funciones z = √μ (azul) y z = -√μ (rojo) se actualizan")
        print("  - La línea púrpura muestra el valor actual de μ")
        print("  - Los puntos azul y rojo muestran los valores actuales de las funciones")
        print("\nAbriendo visualización interactiva de funciones...")
        graficar_diagrama_interactivo_funciones()
        
    elif opcion == '5':
        print("\n--- Análisis Comparativo ---")
        demostrar_tipos_bifurcacion()
        
    else:
        print("Opción inválida. Usa '1', '2', '3', '4' o '5'.")