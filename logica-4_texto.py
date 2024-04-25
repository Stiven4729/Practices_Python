"""
Descripción: Escribe un programa que solicite al usuario ingresar un texto y luego
analice el texto para contar cuántas veces aparece cada palabra en él. 
El programa debe mostrar un resumen que incluya cada palabra única en el texto
junto con el número de veces que aparece.
"""

palabras = {}
texto = input("Escribe tu texto sin comas ni puntos: ")

for palabra in texto.split():
    if palabra in palabras:
        palabras[palabra] += 1
    else:
        palabras[palabra] = 1

print("Conteo de palabras:")
for palabra, cantidad in palabras.items():
    print(f"{palabra}: {cantidad}")