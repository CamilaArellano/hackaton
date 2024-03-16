import re
import random
from fuzzywuzzy import fuzz
from uszipcode import SearchEngine
from faker import Faker

def read_name_variants(file):
    variants = []
    with open(file, 'r') as f:
        for line in f:
            words = line.split()
            variants.extend(words)
    return sorted(set(variants))

def normalize_name(name):
    return re.sub(r'[^a-zA-Z ]', '', name.lower())

def find_similar_names(name, registration, levenshtein_threshold, phonetic_threshold):
    similar_names = []
    standard_name = normalize_name(name)
    for name_registered in registration:
        phonetic_similarity = fuzz.partial_ratio(standard_name, normalize_name(name_registered))
        levenshtein_distance = fuzz.ratio(standard_name, normalize_name(name_registered))
        if phonetic_similarity >= phonetic_threshold or levenshtein_distance >= levenshtein_threshold:
            similar_names.append(name_registered)
    return similar_names

def generate_zip_code(state=None):
    search = SearchEngine()
    if state:
        zipcodes = search.by_state(state)
    else:
        # Get all zip codes
        zipcodes = search.zipcode_to_city()
    if zipcodes:
        random_zip = random.choice(zipcodes)
        return random_zip.zipcode, random_zip.state, random_zip.city
    else:
        print(f"No se encontraron códigos postales para el estado {state}.")
        return None, None, None

def generate_fake_address(zip_code):
    search = SearchEngine()
    zipcode_info = search.by_zipcode(zip_code)
    if zipcode_info:
        city = zipcode_info.major_city
        state = zipcode_info.state
        address_line_1 = f"{random.randint(1000, 9999)} {random.choice(['Main', 'Oak', 'Pine', 'Maple'])} St"
        address_line_2 = ""
        zip4 = f"{random.randint(1000, 9999)}"
        return address_line_1, address_line_2, city, state, zip_code, zip4
    else:
        print(f"No se encontró información para el código postal {zip_code}.")
        return None

# Función para generar un SSN válido
def generate_ssn(fake):
    ssn = fake.ssn().replace('-', '')
    while not is_valid_ssn(ssn):
        ssn = fake.ssn().replace('-', '')
    return ssn

# Función para verificar si un SSN es válido
def is_valid_ssn(ssn):
    # Verifica la estructura del SSN
    if not (len(ssn) == 9 and ssn.isdigit()):
        return False
    # Verifica los criterios de validez
    if (ssn[:3] == '000' or ssn[:3] == '666' or (900 <= int(ssn[:3]) <= 999) or
        ssn[3:5] == '00' or ssn[3:5] == '000' or
        ssn[5:] == '0000' or ssn[5:] == '9999' or
        ssn == ssn[0] * 9 or int(ssn) in range(123456789, 9876543221)):
        return False
    return True

def generate_phone():
    fake = Faker()
    # Generar código de área de Estados Unidos (3 dígitos)
    area_code = fake.random_int(min=200, max=999)  # Rango típico de códigos de área de Estados Unidos
    # Generar número base (7 dígitos)
    base_number = fake.random_int(min=1000000, max=9999999)

    phone_number = f"({area_code}) {base_number:03}"
    print("Número de teléfono generado:", phone_number)

    # Obtener información de ubicación
    location_info = {
        'country': 'United States',
        'state': fake.state(),
        'city': fake.city(),
        'zip_code': fake.zipcode(),  # Código postal dentro de Estados Unidos
    }
    print("Ubicación correspondiente:", location_info)
    return location_info, phone_number

# Generar ubicación y número de teléfono
location, phone = generate_phone()

# Ejemplo de uso
original_name = "Amanda"
name_variants = read_name_variants('files/name_variant_hackathon.txt')
similar_names = find_similar_names(original_name, name_variants, 90, 90)
print(f"Nombres similares a {original_name}: {similar_names}")

fake = Faker()  # Se crea una instancia de Faker
ssn = generate_ssn(fake)

while is_valid_ssn(ssn) is False:
    ssn = generate_ssn(fake)

print("Seguro social: "+ssn)

