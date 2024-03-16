import re
import random
import spacy
from fuzzywuzzy import fuzz
from uszipcode import SearchEngine
from faker import Faker
from read_xlsx import read_column

# Fake
fake = Faker()

# Load SpaCy's English model
nlp = spacy.load("en_core_web_md")

# Files
file_name = 'files/name_variant_hackathon.txt'
file_last_name = 'files/Names_2010Census_Top1000.xlsx'

# Generación de Nombres
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

def generate_name(similar_names):
    if not similar_names:
        return None  # Return None if the list is empty
    name = random.choice(similar_names)
    return name

# Generación de SSN
def generate_ssn():
    ssn = fake.ssn().replace('-', '')
    while not is_valid_ssn(ssn):
        ssn = fake.ssn().replace('-', '')
    return ssn

def is_valid_ssn(ssn):
    if not (len(ssn) == 9 and ssn.isdigit()):
        return False
    if (ssn[:3] == '000' or ssn[:3] == '666' or (900 <= int(ssn[:3]) <= 999) or
        ssn[3:5] == '00' or ssn[3:5] == '000' or
        ssn[5:] == '0000' or ssn[5:] == '9999' or
        ssn == ssn[0] * 9 or int(ssn) in range(123456789, 9876543221)):
        return False
    return True

# Generación de fecha de nacimiento
def generate_DOB():
    DOB = fake.date_of_birth(minimum_age=18, maximum_age=100).strftime('%Y-%m-%d')
    return DOB

# Generación de Apellido
def generate_last_name(similar_names, original_last_name, similarity_threshold):
    while not similar_names:
        random_last_name = generate_random_last_name()  # Generate a new random name each time
        similar_names = find_similar_names(random_last_name, last_names, similarity_threshold, similarity_threshold)
    last_name = random.choice(similar_names)
    return last_name

def generate_random_last_name():
    return fake.last_name()

def mutate_last_name(original_last_name):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    mutated_last_name = list(original_last_name.lower())
    
    # Probabilidad inicial de mutación
    mutation_probability = 0.2
    
    # Iterar sobre cada letra en el apellido original
    for i in range(len(mutated_last_name)):
        # Si la letra actual es una vocal, hay una probabilidad de mutación
        if mutated_last_name[i] in vowels:
            if random.random() < mutation_probability:
                # Agregar una consonante aleatoria después de la vocal
                mutated_last_name.insert(i + 1, random.choice(consonants))
                # Aumentar la probabilidad de mutación para la próxima iteración
                mutation_probability += 0.1
        # Si la letra actual es una consonante, hay una probabilidad de mutación
        elif mutated_last_name[i] in consonants:
            if random.random() < mutation_probability:
                # Agregar una vocal aleatoria después de la consonante
                mutated_last_name.insert(i + 1, random.choice(vowels))
                # Aumentar la probabilidad de mutación para la próxima iteración
                mutation_probability += 0.1
    
    # Convertir la lista de letras mutadas de nuevo a una cadena y capitalizar la primera letra
    mutated_last_name = "".join(mutated_last_name).capitalize()
    
    return mutated_last_name

# Generar un nombre
original_name = "Susan"
name_variants = read_name_variants('files/name_variant_hackathon.txt')
similar_names = find_similar_names(original_name, name_variants, 90, 90)
if original_name in similar_names:
    similar_names.remove(original_name)
name = generate_name(similar_names)
print("Nombres similares: ", similar_names)
print("Nombre generado: ", name)

# Generar un apellido
original_last_name = "Adams"
last_names = read_column(file_last_name, 1)
similar_last_names = find_similar_names(original_last_name, last_names, 70, 80)

# Excluir el apellido original de la lista similar_last_names
if original_last_name in similar_last_names:
    similar_last_names.remove(original_last_name)

# Agregar el apellido mutado a la lista
mutated_last_name = mutate_last_name(original_last_name)
similar_last_names.append(mutated_last_name)

print(similar_last_names)

# Generar un apellido
last_name = generate_last_name(similar_last_names, original_last_name, 0.6)
print("Apellido original:", original_last_name)
print("Apellido generado:", last_name)

# Generar un SSN válido
ssn = generate_ssn()
print("SSN generado:", ssn)

# Generar una fecha de nacimiento
dob = generate_DOB()
print("Fecha de nacimiento generada:", dob)
