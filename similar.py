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

def generate_similar_record(seed):
    # Copiar la semilla para modificarla
    similar_record = seed.copy()
    
    # Definir los atributos que podrían cambiar
    attributes_to_change = ["Dirección", "Teléfono", "Alias"]
    
    # Modificar algunos atributos aleatorios
    for attribute in attributes_to_change:
        # Aquí podrías implementar la lógica para generar valores similares
        # Por ejemplo, podrías cambiar la dirección por una dirección cercana o el teléfono por un número similar
        # En este caso, simplemente lo dejaremos vacío
        similar_record[attribute] = ""
    
    return similar_record

def same(seed):
    # Generar un registro similar para cada atributo de la semilla
    for attribute in seed:
        similar_record = generate_similar_record(seed)
        print(similar_record)


def same(seed):
    for attribute in seed:
        print(attribute)


# Llamar a las funciones
same(seed)
structure(header)






