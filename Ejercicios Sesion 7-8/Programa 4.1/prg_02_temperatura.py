# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 16:27:29 2021

@author: juana
"""

temp= float(input("Ingrese la temperatura: "))
if temp > 100:
    print("Por encima del punto de ebullición del agua")
elif temp < 100:
    print("Por debajo del punto de ebullición del agua")
else:
    print("Punto exacto de ebullición del agua")
   