import Levenshtein # Se instala
import re
import random  # Se agrega la importación de random
from fuzzywuzzy import fuzz # Se instala
from uszipcode import SearchEngine # Se instala
from faker import Faker # Se instala


def read_name_variant(file, data=[]):
    with open(file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Divide cada línea en palabras
            words = line.split()
            word_1 = words[0]
            word_2 = words[1]
            data.append(word_1)
            data.append(word_2)
    data.sort()
    data_repetitions = list(set(data))
    return data_repetitions

def normalize_name(name):
    # Convertir a minúsculas y eliminar caracteres no alfabéticos
    standard_name = name.lower()
    standard_name = re.sub(r'[^a-zA-Z ]', '', standard_name)
    return standard_name

def find_names(name, registration, levenshtein_threshold, phonetic_threshold):
    similar_names = []
    standard_name = normalize_name(name)
    for name_registered in registration:
        # Similaridad fonética
        phonetic_similarity = fuzz.partial_ratio(standard_name, normalize_name(name_registered))
        # Distancia de Levenshtein
        levenshtein_distance = Levenshtein.distance(standard_name, normalize_name(name_registered))
        # Compara si superan el umbral
        if phonetic_similarity >= phonetic_threshold or levenshtein_distance <= levenshtein_threshold:
            similar_names.append(name_registered)
    return similar_names

# Ejemplo de uso
# original_name = "Amanda"
# name_registration = read_name_variant('files/name_variant_hackathon.txt', data=[])
# similar_names = find_names(original_name, name_registration, 1, 90)
# print(f"Nombres similares a {original_name}: {similar_names}")

def generate_zip_code(state):
    search = SearchEngine()
    zipcodes = search.by_state(state)
    if zipcodes:
        # Selecciona un código postal aleatorio del estado
        random_zip = random.choice(zipcodes)
        return random_zip.zipcode
    else:
        print(f"No se encontraron códigos postales para el estado {state}.")
        return None

# Ejemplo de uso
# state = "NY" # Estado de Nueva York
# random_zip_code = generate_zip_code(state)
# if random_zip_code:
#     print(f"Código postal generado para {state}: {random_zip_code}")


#* Sylvana

# def generate_phone():
#     fake = Faker()
#     # Generar código de área de Estados Unidos (3 dígitos)
#     area_code = fake.random_int(min=200, max=999)  # Rango típico de códigos de área de Estados Unidos
#     # Generar número base (7 dígitos)
#     base_number = fake.random_int(min=1000000, max=9999999)

#     phone_number = f"({area_code}) {base_number:03}"
#     print("Número de teléfono generado:", phone_number)

#     # Obtener información de ubicación
#     location_info = {
#         'country': 'United States',
#         'state': fake.state(),
#         'city': fake.city(),
#         'zip_code': fake.zipcode(),  # Código postal dentro de Estados Unidos
#     }
#     print("Ubicación correspondiente:", location_info)
#     return location_info, phone_number

# # Generar ubicación y número de teléfono
# location, phone = generate_phone()