import openpyxl

def data(file_path):
    excel_dataFrame = openpyxl.load_workbook(file_path)
    name_dataFrame = excel_dataFrame.active

    data = []
    for row in name_dataFrame.iter_rows():
        empty_row = True  # La fila está vacía
        _row = []
        for cell in row[:30]:  # interaciones hasta el 30 en cuanto a columnas
            if cell.value is not None:  # Se checa si está vacía  # Se agrega si es que no está vacía
                empty_row = False
            _row.append(cell.value) # Se cambia la condición
        if not empty_row:  # Si la fila al final de las condiciones no está vacía, se guarda
            data.append(_row)  # Se agrega a la lista
    data.pop(0)
    data.pop()
    return data

# Print the data
file_path='C:\\Users\\NOM\\Downloads\\Hackathon-Information.xlsx'
data_generados=data(file_path)
for row in data_generados:
    print(row)
