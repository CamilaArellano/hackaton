import re
import random
import spacy
from fuzzywuzzy import fuzz
from uszipcode import SearchEngine
from faker import Faker
from read_xlsx import read_row

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
def find_similar_last_names(target_name, last_names, similarity_threshold):
    target_name = normalize_name(target_name)
    similar_names = []
    target_doc = nlp(target_name)
    for name in last_names:
        name = normalize_name(name)
        name_doc = nlp(name)
        similarity = target_doc.similarity(name_doc)
        if similarity >= similarity_threshold:
            similar_names.append(name)
    return similar_names

def generate_last_name(similar_names):
    if not similar_names:
        return None  # Return None if the list is empty
    last_name = random.choice(similar_names)
    return last_name

# Generar un nombre
original_name = "Susan"
name_variants = read_name_variants(file_name)
similar_names = find_similar_names(original_name, name_variants, 1, 90)
name = generate_name(similar_names)
print("Nombre generado:", name)

# Generar un apellido
original_last_name = "Brill"
last_names = read_row(file_last_name,1)
similar_last_names = find_similar_last_names(original_last_name,last_names, 0.7 )
last_name = generate_last_name(similar_last_names)
print("Apellido generado:", last_name)

# Generar un SSN válido
ssn = generate_ssn()
print("SSN generado:", ssn)

# Generar una fecha de nacimiento
dob = generate_DOB()
print("Fecha de nacimiento generada:", dob)
