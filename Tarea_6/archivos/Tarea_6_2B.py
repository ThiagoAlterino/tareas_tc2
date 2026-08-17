#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 10:42:42 2026

@author: thiago
"""

#Librerias Externas
from scipy import signal
import matplotlib.pyplot as plt

#Libreria TC2
from pytc2.sistemas_lineales import pzmap, bodePlot

num = [1,0,0]
den = [1,0,1]

TF = signal.TransferFunction(num, den)

plt.close('all')

bodePlot(TF, fig_id=1)

pzmap(TF, fig_id=2)