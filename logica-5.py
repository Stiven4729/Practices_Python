"""
Descripción: Desarrolla un programa que solicite al usuario
ingresar un número determinado de notas (pueden ser enteras o decimales) 
luego calcule y muestre el promedio de esas notas.
"""
#se declara una funcion promedio que por medio del args recibe una lista de numeros al infinito
def promedio(numeros):
    total = []
    division = []
    for i in numeros:
        total.append(float(i))
        division.append(i)
    total = sum(total)
    return(total / len(division))

def pedir_nota():
    numeros = []
    cant_notas = int(input("Digite la cantidad de notas que quieres brindar "))
    for i in range(cant_notas):
        numeros.append(input(f"digita la nota numero {i+1}: "))
        i += 1
    return(numeros)

num = pedir_nota()
promedio(num)
Total = promedio(num)
print(f"el promedio de tus notas son: {Total}")
