# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 10:31:17 2021

@author: juana
"""
#1. Declara la matriz
matrizNumeros= [[12,32,56,48],[8,48,18,58],[2,4,6,8]]

#2. Imprimir la matriz
print (matrizNumeros)

#3. Imprimir una posición fija
print("Posición Específica:",matrizNumeros[0][2])

#4. Solicitar la posición al usuario
fil=int(input("Fila: "))
col=int(input("Columna: "))
print("Posición leída por teclado:",matrizNumeros[fil-1][col-1])


#5. Imprimir una fila determinada
print("Fila 0:",matrizNumeros[0])
print("Fila 1:",matrizNumeros[1])
print("Fila 2:",matrizNumeros[2])

#6. Imprimir una columna
for f in range (3):
    print(matrizNumeros[f][1])
    
#7. Imprimir la columna que el usuario quiera
col=int(input("Columna: "))
for f in range(3):
    print(matrizNumeros[f][col-1])    
    
#8. Sumar todos los elementos de la matriz
sumaElem=0
for f in range(3):
    for c in range(4):
        sumaElem=sumaElem+matrizNumeros[f][c]
print("La suma de los elementos es:",sumaElem)  

#9. Sumar una sola fila
sumaElem=0
for f in range(3):
    for c in range(4):
        sumaElem=sumaElem+matrizNumeros[f][c]
    print("La suma de los elementos de la fila es:",sumaElem)  
    sumaElem=0  