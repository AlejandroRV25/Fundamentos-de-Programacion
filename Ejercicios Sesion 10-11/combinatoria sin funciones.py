# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 10:48:14 2021

@author: juana
"""
#Entradas
factM=1
factN=1
factMN=1
M=int(input("Ingrese el primer valor: "))
N=int(input("Ingrese el segundo valor: "))

#Calcular fatorial M
for f1 in range(1,M+1,1):
    factM=factM*f1
    
contador=1 
while(contador<N):
    contador=contador+1
    factN=factN*contador
    
factMN=M-N
for j in range(1,M-N,1):
    factMN=factMN*j

combinatoria= factM/(factN*factMN)

print("Factorial de M:",factM)    
print("Factorial de N:",factN)
print("Factorial de M-N:",factMN)
print("La combinatoria es:",combinatoria)