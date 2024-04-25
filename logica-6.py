"""
Se desea desarrollar una función llamada invertir_palabras 
que reciba como argumento una cadena de texto y devuelva otra cadena donde las palabras estén invertidas.
Además, se debe cumplir con los siguientes requisitos:

Utilizar el método split() para dividir la cadena en palabras.
Utilizar un bucle for para iterar sobre las palabras de la lista resultante del paso anterior.
Utilizar la función reversed() para invertir cada palabra.
Utilizar el método join() para unir las palabras invertidas en una cadena.
Retornar la cadena resultante con las palabras invertidas.
"""

#solucion sin correcciones
texto_final = []

def Texto_invertido(texto_inicial):
    for i in texto_inicial.split():
        texto_final.append(''.join(reversed(i)))
    return texto_final

Texto_invertido(texto_inicial = input("Digita tu texto sin signos de puntuacion para ser invertido "))

print(' '.join(texto_final))


#correcciones de gpt

#def Texto_invertido(texto_inicial):
#    texto_final = []
#    for palabra in texto_inicial.split():
#        texto_final.append(''.join(reversed(palabra)))
#    return texto_final

#texto = input("Digita tu texto sin signos de puntuacion para ser invertido: ")
#texto_invertido = Texto_invertido(texto)
#print(' '.join(texto_invertido))
