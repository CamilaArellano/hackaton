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

# Ejemplo de uso
original_name = "Amanda"
name_variants = read_name_variants('files/name_variant_hackathon.txt')
similar_names = find_similar_names(original_name, name_variants, 90, 90)
print(f"Nombres similares a {original_name}: {similar_names}")

# Ejemplo de uso
state = "NY" # Estado de Nueva York
zip_code, state, city = generate_zip_code(state)
if zip_code:
    print(f"Código postal generado para {city}, {state}: {zip_code}")
    address = generate_fake_address(zip_code)
    if address:
        address_line_1, address_line_2, city, state, zip_code, zip4 = address
        print("Dirección falsa generada:")
        print("Address-1 Line 1:", address_line_1)
        print("Address-1 Line 2:", address_line_2)
        print("Address-1 City:", city)
        print("Address-1 State:", state)
        print("Address-1 Zip:", zip_code)
        print("Address-1 Zip4:", zip4)
