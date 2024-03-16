from read_xlsx import fetch_data, get_row

file_path = 'files/Hackathon-Information.xlsx'
generated_data = fetch_data(file_path)
seed = get_row(generated_data, 2)
header = get_row(generated_data, 0)

def structure(header):
    # Iterar sobre los elementos del encabezado y asignar nombres dinámicos a las variables
    for index, attribute in enumerate(header):
        # Construir dinámicamente el nombre de la variable
        attribute_name = f"attribute_name_{index + 1}"
        # Asignar el valor del atributo a la variable con el nombre construido
        globals()[attribute_name] = attribute
        # Imprimir el nombre y el valor de la variable
        print(f"{attribute_name}: {attribute}")

def same(seed):
    for attribute in seed:
        print(attribute)
        

# Llamar a las funciones
same(seed)
structure(header)






