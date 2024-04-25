"""
Dado un texto, se te pide queesc ribas una función en Python
que identifique y cuente el número de palabras palíndromas en el texto.
Una palabra palíndroma es aquella que se lee igual de izquierda a derecha que de derecha a izquierda
como "reconocer" o "radar".
"""

#creamos una funcion donde convierte en una lista el texto dado y lo agregamos en una lista aparte
#luego invertimos el texto dado y lo acomodamos en una lista con el .split
# y lo almacenamos en otra lista distinta
#por ultimo retornamos las dos listas (Texto_Derecho y Texto_Alcontrario)

def Alterar_texto(texto):
    Texto_Derecho = []
    Texto_Alcontrario = []
    Texto_Derecho = texto.split()
    for palabra in texto.split():
        Texto_Alcontrario.append(''.join(reversed(palabra)))
    return Texto_Derecho, Texto_Alcontrario

#creamos una funcion donde recibe como parametros las dos listas retornadas
# por la funcion Alterar_texto, luego recorremos las dos listas para comparar si la lista 1
# es igual a lista2 (hola = aloh) para buscar la igualdad y asi hallar las palabras palindromas

def Contar_Palindromas(texto1, texto2):
    contenido = 0
    for i, x in zip(texto1, texto2):
        if i == x:
            contenido += 1
    return contenido

Derecho, Contrario = Alterar_texto(input("Digite tu texto para saber cuantas palabras palindromas hay en el: "))
resultado = Contar_Palindromas(Derecho, Contrario)
print(f"hay {resultado} palabras palindroma en el texto")
