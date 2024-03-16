from getSeedsData import data, get_row
from generator_methods import read_name_variants, find_similar_names, generate_name
import getJsonData as js

ruta='files/config_file.json'

similar = js.listSimilar
per_arcs = js.PerArc

similar_txt = similar[0]
same_txt = similar[2]
typo_txt = similar[4]

percentageSimilar = similar[1]
percentageSame = similar[3]
percentageTypo = similar[5]


file_path = 'files/Hackathon-Information.xlsx'
generated_data = data(file_path)
seed = get_row(generated_data, 2)
header = get_row(generated_data, 0)

probability_same= per_arcs*percentageSimilar*percentageSame
print(probability_same)


# for subcases_same in probability_same:
#     subcase_same(seed)

def subcase_same(header):
    columns = []
    for index, attribute in enumerate(header):
        if attribute == 'FirstName':
            columns.append(index)
        if attribute == 'Alias-1':
            columns.append(index)
        if attribute == 'Alias-2':
            columns.append(index)
        if attribute == 'Alias-3':
            columns.append(index)
        if attribute == 'Address-1 Line 1':
            columns.append(index)
        if attribute == 'Address-1 Line 2':
            columns.append(index)
        if attribute == 'Address-1 City':
            columns.append(index)
        if attribute == 'Address-1 State':
            columns.append(index)
        if attribute == 'Address-1 Zip':
            columns.append(index)
        if attribute == 'Address-1 Zip4':
            columns.append(index)
        if attribute == 'Address-2 Line 1':
            columns.append(index)
        if attribute == 'Address-2 Line 2':
            columns.append(index)
        if attribute == 'Address-2 City':
            columns.append(index)
        if attribute == 'Address-2 State':
            columns.append(index)
        if attribute == 'Address-2 Zip':
            columns.append(index)
        if attribute == 'Address-2 Zip4':
            columns.append(index)
        if attribute == 'Phone-1 Area Code':
            columns.append(index)
        if attribute == 'Phone-1 Base Number':
            columns.append(index)
        if attribute == 'Phone-2 Area Code':
            columns.append(index)
        if attribute == 'Phone-2 Base Number':
            columns.append(index)
    return columns

def modify_same(seed, columns):
    for column_index in columns:
        if header[column_index] == 'FirstName':
            # Modificar el valor de 'FirstName'
            name_variants = read_name_variants('files/name_variant_hackathon.txt')
            similar_names = find_similar_names(seed[column_index], name_variants, 90, 90)
            if seed[column_index] in similar_names:
                similar_names.remove(seed[column_index])
            name = generate_name(similar_names)
            print("Nombres similares: ", similar_names)
            print("Nombre generado: ", name)

def modify_typo(seed, columns:)
    for column_index in columns:
        if header[column_index] == 'FirstName':
            # Modificar el valor de 'FirstName'
            name_variants = read_name_variants('files/name_variant_hackathon.txt')
            similar_names = find_similar_names(seed[column_index], name_variants, 90, 90)
            if seed[column_index] in similar_names:
                similar_names.remove(seed[column_index])
            name = generate_name(similar_names)


columnas = subcase_same(header)
print("Columnas: ", subcase_same(header))
modify_same(seed, columnas )






