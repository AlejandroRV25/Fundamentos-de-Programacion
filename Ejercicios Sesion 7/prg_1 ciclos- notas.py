# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:43:24 2021

@author: juan a
"""

print("SISTEMA DE NOTAS DE UN CURSO DE PROOGRAMACIÓN")

#Entradas

n_est= int(input("Digite el número de estudiantes del grupo: "))
#Declarar la variable que controla ciclo
contador_repeticiones = 0
est_aprobados=0
est_reprobados=0
suma_nd_est=0
suma_est_aprobados=0
suma_est_reprobados=0
promedio_nd_est=0
promedio_est_aprobados=0
promedio_est_reprobados=0
#Iniciar el ciclo
while contador_repeticiones < n_est:
    #Lectura de las notas de cada estudiante
    N1estudiantes= float(input("Por favor ingrese la primera nota: "))
    N2estudiantes= float(input("Por favor ingrese la segunda nota: "))
    N3estudiantes= float(input("Por favor ingrese la tercer nota: "))
     #Incrementar la variable que controla el ciclo
    n_d= (N1estudiantes + N2estudiantes + N3estudiantes)/3
    
    suma_nd_est=suma_nd_est+n_d
    print("1.  La nota definitva es: ",n_d)
    
    if (n_d>= 3.0):
        est_aprobados= est_aprobados+1
        #Sumar las notas de los estudiantes que aprobaron
        suma_est_aprobados=suma_est_aprobados+n_d
    else:
        est_reprobados= est_reprobados+1
        #Sumar las notas de los estudiantes que reprobaron
        suma_est_reprobados=suma_est_reprobados+n_d
        
    
    contador_repeticiones= contador_repeticiones+1
    
    #Fin ciclo
promedio_nd_est=suma_nd_est/n_est    
promedio_est_aprobados=suma_est_aprobados/est_aprobados
promedio_est_reprobados=suma_est_reprobados/est_reprobados
print("OTROS CALCULOS")
print("2.  Cantidad de estudiantes que aprobaron: ", est_aprobados)
print("3.  Cantidad de estudiantes que reprobaron: ",est_reprobados)
print("4.  Promedio de las definitivas: ",promedio_nd_est)
print("5.  Promedio estudiantes aprobados: ",promedio_est_aprobados)
print("6.  Promedio estudiantes reprobados: ",promedio_est_reprobados)