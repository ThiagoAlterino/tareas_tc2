#Librerias Externas
from scipy import signal
import matplotlib.pyplot as plt

#Libreria TC2
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

b,a = signal.butter(6,1,btype='low',analog=True,output='ba')

TF = signal.TransferFunction(b, a)

plt.close('all')

bodePlot(TF, fig_id=1, filter_description= 'Q')

pzmap(TF, fig_id=2, filter_description= 'Q')

GroupDelay(TF, fig_id=3, filter_description= 'Q')
