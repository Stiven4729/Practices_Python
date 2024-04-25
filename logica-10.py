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
palabras = []

def devolviendo_dict(texto):
    palabra_dict = {}
    for x in texto:
        palabras.append(x)  # Agrega caracter por caracter a una lista
    for palabra in palabras: # se recorre la lista creada
        if palabra in palabra_dict: # se pregunta si el caracter esta en el diccionario
            palabra_dict[palabra] += 1  # Incrementar el contador si la palabra ya está en el diccionario
        else:
            palabra_dict[palabra] = 1  # Agregar la palabra al diccionario con un contador inicial de 1
    return palabra_dict

texto = input("Escribe tu cadena de texto: ")
resultado = devolviendo_dict(texto)
print("Resultado:")
print(resultado)


#solucion GPT
"""
def devolviendo_dict(texto):
    palabra_dict = {}
    for letra in texto:
        if letra in palabra_dict:
            palabra_dict[letra] += 1
        else:
            palabra_dict[letra] = 1
    return palabra_dict

texto = input("Escribe tu cadena de texto: ")
resultado = devolviendo_dict(texto)
print("Resultado:")
print(resultado)

"""
