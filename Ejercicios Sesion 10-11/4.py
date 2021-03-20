# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:20:48 2021

@author: juana
"""
import random
contador=1
num=0
suma=0
num_pos=0
num_neg=0

while contador <=10:
    num=random.randint(-100,100)
    suma=suma+num
    print(num)
    if num > 0:
        num_pos=num_pos+num
    elif num < 0:
        num_neg=num_neg+num
        
    contador=contador+1

print("La suma de todos los numeros es:",suma)
print("La suma de numeros positivos es:",num_pos)
print("La suma de numeros negativos es:",num_neg)    
        