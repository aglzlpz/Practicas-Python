# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 09:44:06 2023

@author: anton
"""

def pidePeso():
    p=float(input("¿Cuánto pesas? (en kg)"))
    return p

def pideAltura():
    h=float(input("¿Cuánto mides? (en metros)"))
    return h

def imc(peso,altura):
    r=peso/(altura**2)      #Fórmula de imc
    imc=round(r,2)          #Redondeo con dos decimales
    print("Tu IMC es de",imc)

p=pidePeso()
a=pideAltura()
imc(p,a)