# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:07:41 2021

@author: juana
"""

def sumar(v1,v2,v3=0,v4=0,v5=0):
    s=v1+v2+v3+v4+v5
    return s


# bloque principal

print("La suma de 7 + 8")
print(sumar(7,8))
print("La suma de 1 + 4 + 6")
print(sumar(1,4,6))
print("La suma de 1 + 2 + 3 + 4 + 5")
x=sumar(1,2,3,4,5)
print(x)