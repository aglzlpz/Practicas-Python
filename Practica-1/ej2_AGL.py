# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 09:09:07 2023

@author: antonio
"""
n1 = float(input("Primer sumando: "))
n2 = float(input("Segundo sumando: "))

def suma(a,b):
    sum=a+b
    return sum

print(f"El resultado de la operación {n1}+{n2} es {suma(n1,n2)}")