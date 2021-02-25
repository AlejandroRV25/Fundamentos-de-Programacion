# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:27:05 2021

@author: juana
"""
na=int(input("Ingrese el numero de datos: "))
contador_rep=0
contador_rec=0
contador_obt=0
contador_agu=0
contador_pla=0

while contador_rep < na:
    a=float(input("Ingrese el valor del angulo: "))
    
    if a < 90:
        print("Este angulo es agudo")
        contador_agu=contador_agu+1
        
    elif a == 90:
        print("Este angulo es recto")
        contador_rec=contador_rec+1
    
    elif a > 90 and a < 180:
        print("Este angulo es obtuso")
        contador_obt=contador_obt+1
     
    elif a == 180:
        print("ESte angulo es plano")
        contador_pla=contador_pla+1
        
    contador_rep=contador_rep+1

print("La cantidad de angulos agudos es: ",contador_agu)

print("La cantidad de angulos rectos es: ",contador_rec)

print("La cantidad de angulos obtusos es: ",contador_obt)

print("La cantidad de angulos planos es : ",contador_pla)    