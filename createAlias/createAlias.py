#@Angel Pinacho - Generar alias aletorias mediante 3 campos

#Imports
import generarAlias


#Biblioteca de python para trabajar con archivos Excel
import openpyxl
from tabulate import tabulate

#Carga del archivo 'data.xlsx'
excel_dataFrame = openpyxl.load_workbook('data.xlsx')

#Seleccion de la hoja activa
name_dataFrame = excel_dataFrame.active

#Declaracion de la lista que almacenara cada fila de la hoja activa
data=[]
for row in name_dataFrame.iter_rows():
    empty_row = True  
    _row = []
    for cell in row[2:5]: 
        if cell.value is not None:  
            empty_row = False
        _row.append(cell.value) 
    if not empty_row:  
        data.append(_row) 
data.pop(0)

cont = 0
for item in data:
    cont = 0
    alias = generarAlias.generar_alias(item)
    with open ('alias.txt','a') as archivo:
        for i in alias:
            archivo.write(i + " ")
            cont = cont + 1
            if cont == 3:
                archivo.write("\n")





