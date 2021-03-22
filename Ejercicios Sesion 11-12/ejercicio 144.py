# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:07:41 2021

@author: juana
"""

def cantidad_mayores18(edad1,*edades):
    cant=0
    if edad1>=18:
        cant=cant+1
    for x in range(len(edades)):
        if edades[x]>=18:
            cant=cant+1
    return cant


# bloque principal

print("La cantidad de personas mayores a 18 son:", cantidad_mayores18(23,30,8,19,24))