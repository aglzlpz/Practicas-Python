# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 09:54:56 2023

@author: anton
"""
import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy as np
T0 = 3.0 # segundos
f0 = 261.6 # frecuencia del tono
sr = 5000 # frecuencia de muestreo
t = np.arange(0, T0, 1/sr) # vector de tiempo
x = np.sin(2*np.pi*f0*t) # señal sinusoidal
plt.figure(figsize=(15,7))
plt.subplot(211)
plt.plot(t,x)
plt.ylabel('Amplitud')
plt.subplot(212)
plt.plot(t[:200],x[:200])
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')


plt.figure()
T0 = 3.0 # segundos
sr = 5000 # frecuencia de muestreo
t = np.arange(0, T0, 1/sr) # vector de tiempo
x_c4 = np.sin(2*np.pi*261.6*t) # tono C4
x_a4 = np.sin(2*np.pi*440*t) # tono A4
x_c5 = np.sin(2*np.pi*523.2*t) # tono C5
x_a5 = np.sin(2*np.pi*880*t) # tono A5
chord = x_c4 + x_a4 + x_c5 + x_a5 # acorde
plt.figure(figsize=(15,5))
plt.plot(t[:200],chord[:200])
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
ipd.Audio(chord, rate=sr)