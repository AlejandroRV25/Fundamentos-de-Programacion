# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:44:43 2021

@author: juana
"""

cuadrado=0
suma=0
num=1

cantidadNum=int(input("Ingrese la cantidad de numeros: "))

for num in range(cantidadNum+1):
    cuadrado=num*num
    suma=suma+cuadrado
    print("El cuadrado del número",num,"es",cuadrado)
    print("La suma de los cuadrados es:",suma)