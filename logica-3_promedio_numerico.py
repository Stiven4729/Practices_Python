"""
Desarrolla un programa que solicite al usuario
ingresar una lista de números enteros separados por espacios.
Luego, el programa debe calcular el promedio de los números en la lista y mostrarlo al usuario.
"""

numbers_list = input("digine una serie de numeros separadas por un espacio para allar el promedio de la lista ")
numbers_list = list(map(int, numbers_list.split(" ")))

total = sum(numbers_list) / len(numbers_list)

print(f"el promedio es {total}")
 