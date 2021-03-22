# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:07:41 2021

@author: juana
"""

def mascaracteres(palabras):
    pos=0
    for x in range(len(palabras)):
        if len(palabras[x])>len(palabras[pos]):
            pos=x
    return palabras[pos]


# bloque principal

palabras=["lunes", "martes", "miercoles", "jueves", "viernes", "sabado"]
print("Palabra con mas caracteres:",mascaracteres(palabras))