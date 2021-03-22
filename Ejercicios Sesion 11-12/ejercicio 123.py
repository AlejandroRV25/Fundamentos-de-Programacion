# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:07:41 2021

@author: juana
"""

def retornar_perimetro(lado):
    perimetro=lado*4
    return perimetro


# bloque principal

lado=int(input("Lado del cuadrado:"))
print("El perimetro es:",retornar_perimetro(lado))
