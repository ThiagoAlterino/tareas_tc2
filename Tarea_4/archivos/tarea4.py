#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 17:58:47 2026

@author: thiago
"""

#Librerias Externas
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

#Libreria TC2
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

#  Implementacion de filtro pasa banda Chebyshev de orden 6

# 1er etapa filtro pasabajo de orden 2
num1 = [1,0]
den1 = [1,0.125,1]

# 2da etapa filtro pasabajo de orden 2
num2 = [1,0]
den2 = [1,0.069,1.226]

# 3er etapa filtro pasabajo de orden 1
num3 = [0.00572,0]
den3 = [1,0.056,0.815]

num = np.convolve(num1, np.convolve(num2, num3))
den = np.convolve(den1, np.convolve(den2, den3))

TF = signal.TransferFunction(num, den)

plt.close('all')

bodePlot(TF, fig_id=1)

pzmap(TF, fig_id=2)

GroupDelay(TF, fig_id=3)