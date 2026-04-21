#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 13:41:23 2026

@author: thiago
"""

#Librerias Externas
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np

#Libreria TC2
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

w0 = 1
qq = np.sqrt(2)/2
k = 2

TF = TransferFunction([1,-(k*w0)], [1,w0])

plt.close('all')

bodePlot(TF, fig_id=1, filter_description= 'Q={:3.3f}'.format(qq))

pzmap(TF, fig_id=2, filter_description= 'Q={:3.3f}'.format(qq))

GroupDelay(TF, fig_id=3, filter_description= 'Q={:3.3f}'.format(qq))

