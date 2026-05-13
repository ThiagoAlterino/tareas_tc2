#Librerias Externas
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np

#Libreria TC2
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

f0=10000
w0 = 2*np.pi*f0
qq = 20
C = 0.00000001
R1 = 1/(w0*C)
R = qq*R1

TF = TransferFunction([0,2/(R*C),0], [1,1/(R*C),1/(R1*C)**2])

plt.close('all')

bodePlot(TF, fig_id=1, filter_description= 'Q={}'.format(qq))

pzmap(TF, fig_id=2, filter_description= 'Q={}'.format(qq))

GroupDelay(TF, fig_id=3, filter_description= 'Q={}'.format(qq))