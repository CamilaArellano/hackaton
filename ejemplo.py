from faker import Faker
import random

fake = Faker()

# Función para generar un SSN válido
def generate_ssn():
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

# Genera registros de identificación personal
def generate_personal_info(seed_record, num_records, similar_ratio, family_ratio):
    seed_info = seed_record.split('|')
    seed_fn, seed_ln, seed_dob, seed_zip = seed_info[2], seed_info[4], seed_info[9], seed_info[14]

    # Genera registros similares
    similar_records = []
    for _ in range(int(num_records * similar_ratio)):
        similar_fn = fake.first_name()
        similar_ln = fake.last_name()
        similar_dob = fake.date_of_birth(minimum_age=18, maximum_age=100).strftime('%Y-%m-%d')
        similar_ssn = generate_ssn()
        similar_address = fake.street_address() + '|' + fake.city() + '|' + fake.state_abbr() + '|' + fake.zipcode() + '|' + fake.phone_number()[:3]
        similarity_score = random.uniform(0.8, 1.0)
        case_type = 'SAME' if random.random() < 0.8 else 'TYPO'
        similar_record = f"{seed_info[0]}||{similar_fn}||{similar_ln}||{seed_info[4]}||{similar_dob}||{similar_ssn}||{similar_address}||||||||{seed_info[23]}|{case_type}|{similarity_score}"
        similar_records.append(similar_record)

    # Genera registros familiares
    family_records = []
    for _ in range(int(num_records * family_ratio)):
        family_fn = fake.first_name()
        family_ln = fake.last_name()
        family_dob = fake.date_of_birth(minimum_age=18, maximum_age=100).strftime('%Y-%m-%d')
        family_ssn = generate_ssn()
        family_address = fake.street_address() + '|' + fake.city() + '|' + fake.state_abbr() + '|' + fake.zipcode() + '|' + fake.phone_number()[:3]
        similarity_score = random.uniform(0.3, 0.89)
        case_type = random.choice(['TWINS', 'PARENT-CHILD', 'SIBLINGS'])
        family_record = f"{seed_info[0]}||{family_fn}||{family_ln}||{seed_info[4]}||{family_dob}||{family_ssn}||{family_address}||||||||{seed_info[23]}|{case_type}|{similarity_score}"
        family_records.append(family_record)

    return similar_records + family_records

# Ejemplo de uso
seed_record = "123ABC||Timothy||Paul||OBrien||II||Tim,,OBrien||T,P,Obrien||1983-11-11||229874532||4251 Seminole Dr||Tallahassee||FL||32312||3475||563 Lightning Ave||Tallahassee||FL||32306||3469||850||4635593||850||6445756||M||1.0||SEED"

num_records = 5
similar_ratio = 0.4
family_ratio = 0.2

generated_records = generate_personal_info(seed_record, num_records, similar_ratio, family_ratio)

# Imprime los registros generados
for record in generated_records:
    print(record)
