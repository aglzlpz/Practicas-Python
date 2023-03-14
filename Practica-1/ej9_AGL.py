# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 09:58:00 2023

@author: anton
"""
def inversionInic():
    inv=float(input("¿Cuál es la inversión inicial? "))
    return inv

def tipoInteres():
    tin=float(input("¿Cuál es el tipo de interés anual de la inversión? (porcentual)"))
    return tin

def numyears():
    years=int(input("¿Cuántos años va a tener el plan de inversión? "))
    return years

def capitalGenerado(inv,tin,year):
    cg=inv*(1+tin/100)**year        #Fórmula interés compuesto
    return cg

inv=inversionInic()
tin=tipoInteres()
years=numyears()

print("Ha generado un capital igual a",\
      capitalGenerado(inv,tin,years))