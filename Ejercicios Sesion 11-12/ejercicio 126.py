# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:07:41 2021

@author: juana
"""

def multiplicar(lista,va):
    for x in range(len(lista)):
        multi=lista[x]*va
        print(multi)


# bloque principal

lista=[2, 9, 5, 12, 0]
print("Lista original:",lista)
print("Lista multiplicando cada elemento por 3")
multiplicar(lista,3)