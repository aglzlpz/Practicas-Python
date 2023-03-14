# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 09:31:28 2023

@author: anton
"""

#USANDO UN BUCLE
a=int(input("Dime un número natural: "))
suma=0
for a in range(1,a+1):
    suma=suma+a
print("La suma de todos los números naturales de 1 a",a, "es",suma)

#USANDO LA FÓRMULA DE GAUSS
def gauss(n):
    g=n*((n+1)/2)
    return g

print("Usando la fórmula de Gauss, el resultado es",gauss(a))