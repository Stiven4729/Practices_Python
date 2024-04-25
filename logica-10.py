"""
Escribe una función en Python que reciba una cadena de texto y devuelva un diccionario
donde las claves sean las letras encontradas en el texto y los valores sean
la cantidad de veces que cada letra aparece en la cadena.

Por ejemplo: 

Para la cadena "python", el diccionario resultante sería: 
{'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}.
Para la cadena "hello world", el diccionario resultante sería: 
{'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}.



"""


def devolviendo_dict(texto):
    for x in texto:
        print(x)
devolviendo_dict(input("Escribe tu cadena de texto: "))
