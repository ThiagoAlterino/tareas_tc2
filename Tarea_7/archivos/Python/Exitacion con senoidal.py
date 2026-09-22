#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:47:31 2026

@author: thiago
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# -------------------------------------------------------------
# 1. Configuración de parámetros de muestreo y frecuencia
# -------------------------------------------------------------
fs = 1000               # Frecuencia de muestreo (1000 muestras/segundo)
Ts = 1 / fs             # Período de muestreo en segundos
t = np.arange(0, 0.5, Ts) # Vector de tiempo (0.5 segundos)

f0 = 5                  # Frecuencia del seno de entrada (5 Hz)
w0 = 2 * np.pi * f0     # Frecuencia angular rad/s

# -------------------------------------------------------------
# 2. Definición de señales y sistema
# -------------------------------------------------------------
# Entrada: Seno discreto x[n]
x = np.sin(w0 * t)

# Derivada analítica exacta: d/dt [sin(w0*t)] = w0 * cos(w0*t)
dx_exacta = w0 * np.cos(w0 * t)

# Definición del sistema H(Z)
b = [0.5,0,-0.5]        # Numerador
a = [1]                 # Denominador

# -------------------------------------------------------------
# 3. Filtrado y aproximación a la derivada continua
# -------------------------------------------------------------
# Respuesta del sistema discreto
y = signal.lfilter(b, a, x)

# Salida escalada por el período de muestreo (para unidades de dx/dt)
y_derivada_aprox = y / Ts 

# -------------------------------------------------------------
# 4. Visualización y Comparación
# -------------------------------------------------------------
plt.figure(figsize=(10, 5))

# Señal de entrada
plt.plot(t, x, color='gray', linestyle='--', label='Entrada x[n] = sin(w t)')

# Derivada analítica exacta (referencia)
plt.plot(t, dx_exacta, color='red', linewidth=2, label="Derivada analítica x'(t) = w·cos(w t)")

# Salida del filtro ajustada
plt.plot(t, y_derivada_aprox, color='blue', linewidth=1.5, label='Salida del filtro y[n] / Ts')

plt.title('Evaluación del Sistema Discreto vs. Derivada Analítica')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()