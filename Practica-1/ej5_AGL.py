# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 09:26:39 2023

@author: anton
"""

def preguntaHora():
    h=float(input("¿Cuántas horas ha trabajado? "))
    return h

def preguntaCoste():
    c=float(input("¿Cuál es el coste por cada hora? "))
    return c

tiempo=preguntaHora()
coste=preguntaCoste()

print("Le corresponde una paga de",tiempo*coste)