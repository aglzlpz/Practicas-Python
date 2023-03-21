# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 09:25:27 2023

@author: anton
"""

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
# Creando vector de tiempos para que se muestren varios ciclos
t = np.linspace(0,3,1000)*1e-3 # 3 ms máximo
# Parametros de las señales
f=1.0e3 # Frecuencia de 1 kHz
duty=0 # Ciclo de trabajo
width=0 # Ancho ascendente
# Generacion de las señales usando el modulo signal
y1=signal.square(2*np.pi*f*t,duty)
y2=signal.sawtooth(2*np.pi*f*t,width)
# Representacion grafica
plt.subplot(211)
plt.plot(t*1000,y1)
plt.ylabel('Amplitud')
plt.subplot(212)
plt.plot(t*1000,y2)
plt.xlabel('Tiempo (ms)')
plt.ylabel('Amplitud')
