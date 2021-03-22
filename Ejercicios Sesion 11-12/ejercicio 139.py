# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:07:41 2021

@author: juana
"""

def tabla(numero, terminos=10):
    for x in range(terminos):
        va=x*numero
        print(va,",",sep="",end="")
    print()
    

# bloque principal

print("Tabla del 8")
tabla(8)
print("Tabla del 8 con 7 terminos")
tabla(8,7)
print("Tabla del 8 con 20 terminos")
tabla(terminos=20,numero=8)