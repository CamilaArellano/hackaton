import random
import csv
from uszipcode import SearchEngine
import pandas as pd

class Location:
    def __init__(self, zip_code, state, city, area_code, address_line_1, address_line_2, zip4, phone):
        self.zip = zip_code
        self.state = state
        self.city = city
        self.code = area_code
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.zip4 = zip4
        self.phone = phone

def generate_random_state_city():
    # Cargar el archivo CSV que contiene los códigos de área y la información de las ciudades y estados
    area_codes_df = pd.read_csv('area_codes.csv')  # Reemplaza 'area_codes.csv' con el nombre real de tu archivo CSV

    # Seleccionar aleatoriamente una entrada del DataFrame
    random_entry = area_codes_df.sample()

    # Obtener el estado y la ciudad aleatorios
    primary_state = random_entry.iloc[0]['primary_state']
    primary_city = random_entry.iloc[0]['primary_city']
    primary_code = random_entry.iloc[0]['area_code']

    return primary_state, primary_city, primary_code

def generate_fake_address():
    address_line_1 = f"{random.randint(1000, 9999)} {random.choice(['Main', 'Oak', 'Pine', 'Maple'])} St"
    address_line_2 = ""
    zip4 = f"{random.randint(1000, 9999)}"
    return address_line_1, address_line_2, zip4

def generate_random_number():
    while True:
        # Generar un número de 7 dígitos aleatorio
        random_number = random.randint(1000000, 9999999)

        # Verificar que el número no sea consecutivo
        digits = [int(digit) for digit in str(random_number)]
        is_consecutive = any(abs(digits[i] - digits[i+1]) == 1 for i in range(len(digits) - 1))

        if not is_consecutive:
            return random_number

def generate_zip_code():
    search = SearchEngine()
    zipcodes_not_found = True

    while zipcodes_not_found != False:
        # Generate random state and city
        random_state, random_city, random_code = generate_random_state_city()

        try:
            zipcodes = search.by_city_and_state(random_city, random_state)

            if zipcodes:
                random_zip = random.choice(zipcodes)
                zipcodes_not_found = False
            
        except Exception as e:
            print(f"Error al buscar códigos postales para {random_city}, {random_state}: {e}")
            # Generate a new state and city to try finding a valid zip code
            continue
        
        random_zip_city = random_city
        random_zip_state = random_state
        ad1, ad2, zip4 = generate_fake_address()
        number = generate_random_number()
        return random_zip.zipcode, random_zip_state, random_zip_city, random_code, ad1, ad2, zip4, number




<<<<<<< HEAD
=======

>>>>>>> parent of 8a850cd (Optimizacion Repositorio)
# Ejemplo de uso
zip_code, state, city, area_code, zip_ad1, zip_ad2, zip_zip4, number = generate_zip_code()
location_instance = Location(zip_code, state, city, area_code, zip_ad1, zip_ad2, zip_zip4, number)

print("Código Postal:", location_instance.zip)
print("Estado:", location_instance.state)
print("Ciudad:", location_instance.city)
print("Código de Área:", location_instance.code)
print("Dirección 1:", location_instance.address_line_1)
print("Dirección 2:", location_instance.address_line_2)
print("zip 4:", location_instance.zip4)
print("Número de teléfono:", location_instance.phone)
<<<<<<< HEAD


=======
>>>>>>> parent of 8a850cd (Optimizacion Repositorio)
