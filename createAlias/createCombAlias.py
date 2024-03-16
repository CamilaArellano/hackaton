import itertools

# Función para generar combinaciones
def generar_combinaciones(nombres):
    # Generar todas las permutaciones de los nombres
    combinaciones = list(itertools.permutations(nombres, 3))
    return combinaciones

# Leer el archivo y procesar cada fila
with open('alias.txt', 'r') as archivo_entrada:
    for linea in archivo_entrada:
        # Dividir la línea en los nombres separados por espacios
        nombres = linea.strip().split()
        
        # Generar las combinaciones de los nombres
        combinaciones = generar_combinaciones(nombres)
        
        # Imprimir las combinaciones
        for combinacion in combinaciones:
            print(' '.join(combinacion))
