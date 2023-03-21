# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 10:11:53 2023

@author: anton
"""
import matplotlib.pyplot as plt
import numpy as np
T0 = 3.0 # segundos
sr = 5000 # frecuencia de muestreo
t = np.arange(0, T0, 1/sr) # vector de tiempo
x_c4 = np.sin(2*np.pi*261.6*t) # tono C4
x_a4 = np.sin(2*np.pi*440*t) # tono A4
x_c5 = np.sin(2*np.pi*523.2*t) # tono C5
x_a5 = np.sin(2*np.pi*880*t) # tono A5
chord = x_c4 + x_a4 + x_c5 + x_a5 # acorde

plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')


