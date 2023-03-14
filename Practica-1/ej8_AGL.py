# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 09:49:37 2023

@author: anton
"""

n=int(input("Introduce el dividendo: "))
m=int(input("Introduce el divisor: "))

def cociente(n,m):
    cociente=n//m
    return cociente

def resto(n,m):
    resto=n%m
    return resto

c=cociente(n,m)
r=resto(n,m)

print(f"{n} entre {m} da como cociente: {c} y como resto: {r}")
