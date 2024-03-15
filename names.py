import Levenshtein
import re
from fuzzywuzzy import fuzz

def read_name_variant(file, data=[]):
    with open(file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Divide each line in words (' ')
            words = line.split()
            word_1 = words[0]
            word_2 = words[1]
            data.append(word_1)
            data.append(word_2)
    data.sort()
    data_repetitions = list(set(data))
    return data_repetitions

def normalize_name(name):
    # Convert to lowercase
    standard_name = name.lower()
    standard_name = re.sub(r'[^a-zA-Z ]', '', standard_name)
    return standard_name

def find_names(name, registration, levenshtein_threshold, phonetic_threshold):
    similar_names = []
    standard_name = normalize_name(name)
    for name_registered in registration:
        # Phonetic similarity
        phonetic_similarity = fuzz.partial_ratio(standard_name, normalize_name(name_registered))
        # Levenshtein distance
        levenshtein_distance = Levenshtein.distance(standard_name, normalize_name(name_registered))
        # Compare if they are over the threshold
        if phonetic_similarity >= phonetic_threshold or levenshtein_distance <= levenshtein_threshold:
            similar_names.append(name_registered)
    return similar_names

original_name = "Amanda"
name_registration = read_name_variant('C:/Users/eirac/Workspace/hackaton/files/name_variant_hackathon.txt', data=[])
similar_names = find_names(original_name, name_registration, 1, 90)

print(f"Nombres similares a {original_name}: {similar_names}")
