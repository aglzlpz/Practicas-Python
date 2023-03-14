# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 09:15:22 2023

@author: antonio
"""

def suma(a,b):
    s=a+b
    return s

def division(a,b):
    d=a/b
    return d

def producto(a,b):
    p=a*b
    return p

def exponente(a,b):
    e=a**b
    return e

def pedirN():                       #En enunciado = 3
    n=int(input("Número n: "))
    return n

def pedirM():                       #En enunciado = 2
    m=int(input("Número m: "))
    return m

def pedirO():                       #En enunciado = 5
    o=int(input("Número o: "))
    return o

#Se guardan los números introducidos por el usuario en variables
n=pedirN()
m=pedirM()
o=pedirO() 

#Se opera con las variables
s=suma(n,m)
p=producto(m,o)
fraccion=division(s,p)
res=exponente(fraccion,2)
print("El resultado es",res)