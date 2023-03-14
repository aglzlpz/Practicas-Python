# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 10:13:11 2023

@author: anton
"""

pesoPP=0.112    #peso unitario PapaPig
pesoC=0.075     #peso unitario Caillou

def preguntaPepaPig():
    return int(input("¿Cuántas Pepa Pig van en el paquete? "))
    
def preguntaCaillou():
    return int(input("¿Cuántos Caillou van en el paquete? "))

def pesoPaquete(npepa,ncaillou):
    peso=npepa*pesoPP+ncaillou*pesoC
    return peso

pepas=preguntaPepaPig()
caillous=preguntaCaillou()

print(f"El peso total del paquete será {pesoPaquete(pepas,caillous)}kg")