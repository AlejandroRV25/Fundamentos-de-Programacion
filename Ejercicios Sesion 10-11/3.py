# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:56:19 2021

@author: juana
"""
num=0
contador=1
cuadrado=0
suma=0
num=int(input("Ingrese el número de datos: "))
while  contador <=num:
    cuadrado=pow(contador,2)
    suma=suma+cuadrado
    print("El cuadrado del número",contador,"es",cuadrado)
    print("La suma acumulada es:",suma)
    contador=contador+1 
print("La suma de los cuadrados es:",suma)    