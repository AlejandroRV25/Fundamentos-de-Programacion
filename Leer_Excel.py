#Lectura de Archivos tipo Excel
#Importar librerias
import pandas as pd

#Leer archivo Excel

archivoExcel= pd.read_excel('ventas_Productos.xlsx') 
# Imprimir los datos

print(archivoExcel)