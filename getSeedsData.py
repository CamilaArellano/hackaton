#@Sylvana Salinas
import openpyxl
from tabulate import tabulate
import pandas as pd

def data(file_path):
    excel_dataFrame = openpyxl.load_workbook(file_path)
    name_dataFrame = excel_dataFrame.active

    data = []
    for row in name_dataFrame.iter_rows():
        empty_row = True  # La fila está vacía
        _row = []
        for cell in row:  # interaciones hasta el 30 en cuanto a columnas
            if cell.value is not None:  # Se checa si está vacía  # Se agrega si es que no está vacía
                empty_row = False
            _row.append(cell.value) # Se cambia la condición
        if not empty_row:  # Si la fila al final de las condiciones no está vacía, se guarda
            data.append(_row)  # Se agrega a la lista
    data.pop(0)
    
    return data

# Print the data
file_path='Hackathon-Information.xlsx'
data_generados=data(file_path)

def read_column(file_path, column_number=1):
    df = pd.read_excel(file_path)
    selected_column = df.iloc[:, column_number - 1]  # Selecciona la columna deseada (ten en cuenta que los índices de columna comienzan desde 0)
    return selected_column

def get_row(generated_data, row):
    seed = generated_data.pop(row)
    print(seed)
    return seed

print(tabulate(data_generados))
