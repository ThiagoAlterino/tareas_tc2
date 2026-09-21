#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:09:17 2026

@author: thiago
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Coeficientes del sistema H7(z)[cite: 1]
b = [1, 0, 0, 0, 0, 0, 0, 0, 1]             # Numerador
a = [1, 0, 0, 0, 0, 0, 0, 0, 0]     # Denominador

# Polos y ceros
zeros = np.roots(b)
poles = np.roots(a)

# Respuesta en frecuencia
w, h = signal.freqz(b, a, worN=1000)
frecuencia_normalizada = w / np.pi  # De 0 a pi (normalizado)

# ==========================================
# 1. DIAGRAMA DE POLOS Y CEROS
# ==========================================
plt.figure(figsize=(6, 6))

# Círculo unitario
unit_circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--')
plt.gca().add_patch(unit_circle)

# Marcadores de ceros y polos
plt.plot(np.real(zeros), np.imag(zeros), 'go', label='Ceros', markersize=8)
plt.plot(np.real(poles), np.imag(poles), 'rx', label='Polos', markersize=8)

plt.title("Diagrama de Polos y Ceros (Plano Z)")
plt.xlabel("Parte Real (Re)")
plt.ylabel("Parte Imaginaria (Im)")
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.tight_layout()
plt.show()

# ==========================================
# 2. RESPUESTA EN MÓDULO (MAGNITUD)
# ==========================================
plt.figure(figsize=(7, 4))
plt.plot(frecuencia_normalizada, np.abs(h), color='b', linewidth=1.5)
plt.title("Respuesta en Módulo |H(w)|")
plt.xlabel("Frecuencia Normalizada (x π rad/muestra)")
plt.ylabel("Magnitud")
plt.grid(True)
plt.tight_layout()
plt.show()

# ==========================================
# 3. RESPUESTA EN FASE
# ==========================================
plt.figure(figsize=(7, 4))
fase = np.unwrap(np.angle(h))  # Desenrolla la fase para evitar saltos bruscos
plt.plot(frecuencia_normalizada, fase, color='r', linewidth=1.5)
plt.title("Respuesta en Fase")
plt.xlabel("Frecuencia Normalizada (x π rad/muestra)")
plt.ylabel("Fase (Radianes)")
plt.grid(True)
plt.tight_layout()
plt.show()