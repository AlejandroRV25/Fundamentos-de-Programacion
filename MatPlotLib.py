# -*- coding: utf-8 -*-
"""
Created on Thu May 13 10:30:27 2021

@author: juana
"""

import matplotlib
import matplotlib.pyplot as plt


#Generar Datos
#Interactuar con Las Listas

nombreProductos=['Arroz','Azucar','Vino','Leche']
ventaProductos=[100,50,30,20]

#Funciones que resuleven las preguntas

def totalVentas():
    sumTotVen=0
    for pos in range (4):
        sumTotVen=sumTotVen+ventaProductos[pos]   
    return(sumTotVen)
def promVenTot():
    promVen=0.0
    promVen=totalVentas()/len(ventaProductos)
    return(promVen)

#Llamar a la función
print("El total de Ventas es de:",totalVentas())    
print("El promedio de Ventas es de:", promVenTot())


#Generar el Grafico
fig, ax = plt.subplots()
ax.set_title('Ventas de la Empresa')
ax.set_ylabel('Valor')

#Crear el Grafico
plt.bar(nombreProductos,ventaProductos)
plt.show()