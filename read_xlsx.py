import openpyxl
import pandas as pd

def fetch_data(file_path):
    excel_workbook = openpyxl.load_workbook(file_path)
    active_sheet = excel_workbook.active

    data = []
    for row in active_sheet.iter_rows():
        empty_row = True  # Assume the row is empty
        _row = []
        for cell in row[:30]:  # Iterate through columns up to 30
            if cell.value is not None:  # Check if the cell is not empty
                empty_row = False
            _row.append(cell.value)  # Add the cell value to the row
        if not empty_row:  # If the row is not empty after checking
            data.append(_row)  # Add it to the list
    data.pop(0)  # Remove the first row (assuming it's a header)
    data.pop()   # Remove the last row (assuming it's empty)
    return data

def read_column(file_path, column_number=1):
    df = pd.read_excel(file_path)
    selected_column = df.iloc[:, column_number - 1]  # Selecciona la columna deseada (ten en cuenta que los índices de columna comienzan desde 0)
    return selected_column

# Print the data
file_path = 'Hackathon-Information.xlsx'
generated_data = fetch_data(file_path)

def get_row(generated_data, row):
    seed = generated_data.pop(row)
    print(seed)
    return seed
