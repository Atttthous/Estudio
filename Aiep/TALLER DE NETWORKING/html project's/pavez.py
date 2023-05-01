import itertools
import random

# Pedimos al usuario que ingrese una lista de palabras separadas por comas
palabras = input("Ingrese las palabras a combinar separadas por comas: ").split(',')

# Generamos contraseñas con diferentes longitudes
longitudes = [ 8,  9, 10, 11, 12, 13, 14, 15, 16,]
contraseñas = []
for longitud in longitudes:
    for i in range(700):
        # Elegimos palabras al azar de la lista de palabras
        combinacion = random.sample(palabras, k=min(longitud, len(palabras)))
        # Generamos una contraseña con la combinación de palabras
        contraseña = ''.join(combinacion)[:longitud]
        contraseñas.append(contraseña)

# Guardamos las contraseñas en un archivo de texto
with open('contraseñas.txt', 'w') as f:
    for contraseña in contraseñas:
        f.write(contraseña + '\n')