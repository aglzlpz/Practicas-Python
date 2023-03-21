# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 09:37:30 2023

@author: anton
"""

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
5
# vector de tiempos
t = np.linspace(0,2,1000)*1e-3 # 2 ms máximo
# Parametros de las señales
f=1.0e3 # Frecuencia de 1 kHz
duty=0.5 # Ciclo de trabajo
width=0.5 # Ancho ascendente
# senal cuadrada
y = signal.square(2*np.pi*f*t,duty)
# suma de tonos
y1 = (4/np.pi)*np.sin(2*np.pi*f*t) # armonico 1
y3 = y1 + (4/(3*np.pi))*np.sin(2*np.pi*3*f*t) # + armonico 3
y5 = y3 + (4/(5*np.pi))*np.sin(2*np.pi*5*f*t) # + armonico 5
# grafica
plt.plot(t*1000,y,label='Onda cuadrada')
plt.plot(t*1000,y1,label='Armónico 1')
plt.plot(t*1000,y3,label='Armónico 1 y 3')
plt.plot(t*1000,y5,label='Armónico 1, 3 y 5')
plt.xlabel('Tiempo (ms)')
plt.ylabel('Amplitud')
plt.axis([0,2,-1.5,1.5])
plt.legend()


#SEÑAL CUADRADA N ARMÓNICOS
plt.figure()
# vector de tiempos
t = np.linspace(0,2,1000)*1e-3 # 2 ms máximo
# Parametros de la señal cuadrada
f=1.0e3 # Frecuencia de 1 kHz
duty=0.5 # Ciclo de trabajo
# senal cuadrada
y = signal.square(2*np.pi*f*t,duty)
N=50 # Numero de armonicos sumados a representar
# la variable con la suma de armonicos se inicializa a cero
y0 = np.zeros(len(t))
# Bucle con acumulador
for n in np.arange(1,N):
    y0 += 4/(np.pi)*np.sin((2*n-1)*2*np.pi*f*t)/(2*n-1)
# grafica
plt.plot(t*1000,y,label='Onda cuadrada')
plt.plot(t*1000,y0,label='Suma de armonicos')
plt.xlabel('Tiempo (ms)')
plt.ylabel('Amplitud')

#SEÑAL TRIANGULAR N ARMÓNICOS
plt.figure()
# vector de tiempos
t = np.linspace(0,2,1000)*1e-3 # 2 ms máximo
# Parametros de la señal cuadrada
f=1.0e3 # Frecuencia de 1 kHz
width=0.5 
# senal cuadrada
y = signal.sawtooth(2*np.pi*f*t,width)
N=4 # Numero de armonicos sumados a representar
# la variable con la suma de armonicos se inicializa a cero
y0 = np.zeros(len(t))
# Bucle con acumulador
for n in np.arange(1,N):
    y0 += (-8/(np.pi)**2)*np.cos((2*n-1)*2*np.pi*f*t)/(2*n-1)**2
# grafica
plt.plot(t*1000,y,label='Onda cuadrada')
plt.plot(t*1000,y0,label='Suma de armonicos')
plt.xlabel('Tiempo (ms)')
plt.ylabel('Amplitud')