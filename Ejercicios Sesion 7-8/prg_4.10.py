# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:34:55 2021

@author: juana
"""
est=int(input("Ingrese la cantidad de estudiantes: "))

contador_rep=0
contador_a=0
contador_b=0
contador_c=0
contador_d=0
contador_f=0

while contador_rep < est:
    
    p=int(input("Ingrese el puntaje: "))
    
    if p < 69:
        contador_f=contador_f+1
    elif p < 70 and p >= 69:
        contador_d=contador_d+1
    elif p < 80 and p >= 70:
        contador_c=contador_c+1
    elif p < 90 and p >= 80:
        contador_b=contador_b+1
    elif p >= 90 and p <=100:
        contador_a=contador_a+1
        
    contador_rep=contador_rep+1

print("Los estudiantes con nota de A son: ",contador_a)

print("Los estudiantes con nota de B son: ",contador_b)

print("Los estudiantes con nota de C son: ",contador_c)

print("Los estudiantes con nota de D son: ",contador_d)

print("Los estudiantes con nota de F son: ",contador_f)
    