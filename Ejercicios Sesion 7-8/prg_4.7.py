# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 17:57:50 2021

@author: juana
"""
p=int(input("Ingrese el número de personas: "))
contador_rep=0
contador_mc=0
contador_ecc=0
contador_ecs=0
contador_mis=0

while contador_rep < p:
    peso=float(input("Ingrese el peso del estudiante: "))
    
    if peso < 40:
        contador_mc=contador_mc+1
        
    elif peso >=40 and peso <50:
        contador_ecc=contador_ecc+1
        
    elif peso >= 50 and peso < 60:
        contador_ecs=contador_ecs+1
        
    elif peso >= 60: 
        contador_mis=contador_mis+1
        
    contador_rep=contador_rep+1

print("Los estudiantes con peso menor a 40kg son: ",contador_mc)
print("Los estudiantes con peso entre 40kg y 50kg son: ",contador_ecc)
print("Los estudiantes con peso entre 50kg y 60kg son: ",contador_ecs)
print("Los estudiantes con peso mayor a 60kg son: ",contador_mis)    