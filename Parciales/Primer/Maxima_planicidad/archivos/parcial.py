#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 18:04:27 2026

@author: thiago
"""

#Librerias Externas
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

#Libreria TC2
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

#  Implementacion de filtro pasabajo Chebyshev de orden 5 cascadeando dos pasabajo de orden 2 y un filtro RC

# 1er etapa filtro pasabajo de orden 2
num1 = [2,0,0]
den1 = [1,0.704,0.496]

# 2da etapa filtro pasabajo de orden 1
num2 = [1,0]
den2 = [1,0.704]


num = np.convolve(num1, num2)
den = np.convolve(den1, den2)

TF = signal.TransferFunction(num, den)

plt.close('all')

bodePlot(TF, fig_id=1)

pzmap(TF, fig_id=2)

GroupDelay(TF, fig_id=3)