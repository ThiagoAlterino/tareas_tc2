#Librerias Externas
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

#Libreria TC2
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

#  Implementacion de filtro pasabajo Chebyshev de orden 5 cascadeando dos pasabajo de orden 2 y un filtro RC

# 1er etapa filtro pasabajo de orden 2
num1 = [0.495]
den1 = [1,0.625,0.495]

# 2da etapa filtro pasabajo de orden 2
num2 = [1.054]
den2 = [1,0.239,1.054]

# 3er etapa filtro pasabajo de orden 2
num3 = [0.386]
den3 = [1,0.386]

num = np.convolve(num1, np.convolve(num2, num3))
den = np.convolve(den1, np.convolve(den2, den3))

TF = signal.TransferFunction(num, den)

plt.close('all')

bodePlot(TF, fig_id=1)

pzmap(TF, fig_id=2)

GroupDelay(TF, fig_id=3)
