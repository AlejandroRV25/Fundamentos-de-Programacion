# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 17:29:34 2021

@author: juana
"""

from math import sqrt
x=int(input("Ingrese el valor: "))
if x>0:
    print("La raiz cuadrada de este número es: ",sqrt(x))
elif x<0:
    print("Es un número imaginario")