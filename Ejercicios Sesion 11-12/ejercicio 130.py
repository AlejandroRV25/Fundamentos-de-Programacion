# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:07:41 2021

@author: juana
"""

def producto(lista):
    prod=1
    for x in range(len(lista)):
        prod=prod*lista[x]
    return prod


# bloque principal

lista=[2, 4, 6, 8, 10]
print("Lista:", lista)
print("Multiplicacion de todos sus elementos:",producto(lista))