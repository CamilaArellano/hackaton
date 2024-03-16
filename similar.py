from getSeedsData import data, get_row
from generator_methods2 import read_name_variants, find_similar_names, generate_name, generate_fake_address, generate_random_state_city, generate_zip_code
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


file_path = 'Hackathon-Information.xlsx'
generated_data = data(file_path)
seed = get_row(generated_data, 2)
header = get_row(generated_data, 0)

probability_same= per_arcs*percentageSimilar*percentageSame
print(probability_same)


# for subcases_same in probability_same:
#     subcase_same(seed)

def subcase_same_columns(header):
    columns = []
    for index, attribute in enumerate(header):
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

def modify_same_address1(seed, columns):
    address = generate_fake_address()
    location = generate_random_state_city()
    zip_code = generate_zip_code()
    for column_index in columns:
        if header[column_index] == 'Address-1 Line 1':
            seed[column_index] = address[0]
        if header[column_index] == 'Address-1 Line 2':
            seed[column_index] = address[1]
        if header[column_index] == 'Address-1 City':
            seed[column_index] = location[1]
        if header[column_index] == 'Address-1 State':
            seed[column_index] = location[0]
        if header[column_index] == 'Address-1 Zip':
            seed[column_index] = zip_code[0]
        if header[column_index] == 'Address-1 Zip4':
            seed[column_index] = address[2]
    print(seed)

# This method only modifies the Address-1 fields.

def modify_same_address2(seed, columns):
    address = generate_fake_address()
    location = generate_random_state_city()
    zip_code = generate_zip_code()
    for column_index in columns:
        if header[column_index] == 'Address-2 Line 1':
            seed[column_index] = address[0]
        if header[column_index] == 'Address-2 Line 2':
            seed[column_index] = address[1]
        if header[column_index] == 'Address-2 City':
            seed[column_index] = location[1]
        if header[column_index] == 'Address-2 State':
            seed[column_index] = location[0]
        if header[column_index] == 'Address-2 Zip':
            seed[column_index] = zip_code[0]
        if header[column_index] == 'Address-2 Zip4':
            seed[column_index] = address[2]
    print(seed)

# This method only modifies the fields related to method 2.

            


columnas = subcase_same_columns(header)
print("Columnas: ", subcase_same_columns(header))
modify_same_address1(seed, columnas )
modify_same_address2(seed, columnas )






