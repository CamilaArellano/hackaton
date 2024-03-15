from read_xlsx import fetch_data, get_row

file_path = 'files/Hackathon-Information.xlsx'
generated_data = fetch_data(file_path)
seed = get_row(generated_data, 2)

def same(seed):
    for attribute in seed:
        print(attribute)
    return

same(seed) 





