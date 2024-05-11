"""
Supongamos que estás desarrollando un sistema para una biblioteca 
que necesita gestionar diferentes tipos de materiales, como libros, revistas y periódicos.
Cada tipo de material tiene atributos y comportamientos específicos.
Necesitas crear una estructura de clases que te permita
modelar estos materiales de manera eficiente.

Cada material tiene un título, un autor (en el caso de libros) o una editorial 
(en el caso de revistas y periódicos), y un año de publicación.

-Los libros tienen un género y un número de páginas.
-Las revistas tienen un número de edición y un tema.
-Los periódicos tienen una sección principal y una fecha de publicación.

Además, necesitas implementar métodos para calcular la cantidad total de materiales
en la biblioteca, así como para imprimir los detalles de un material en particular.

Utilizando la herencia y clases en Python, 
debes crear una estructura de clases que satisfaga estas necesidades y te permita modelar 
eficazmente los diferentes tipos de materiales en la biblioteca.
"""
from POO import Poo
from Functions import functPeriodico
# Crear instancias de Periodico y agregarlas a la lista de materiales
while True:
    res = input("Que quieres hacer? periodico / revista / libro : ").lower()
    try:
        if res == "periodico":
            res = input("Que accion quieres? Crear, buscar, remover, volver: ").lower()
            while True:
                if res == "crear":
                    title, year, editorial, section = functPeriodico.crear()
                    material = Poo.Periodico(title, year, editorial, section)
                    break
                elif res == "buscar":
                    tituloBusc = input("Digita el nombre que quieres buscar: ").lower()
                    functPeriodico.buscar(tituloBusc)
                    break
                elif res == "remover":
                    tituloBusc = input("Digita nombre a borrar: ").lower()
                    for periodic, mater in zip(Poo.Periodico.periodicos, Poo.Material.materiales):
                        if periodic.title == tituloBusc and mater.title == tituloBusc:
                            Poo.Periodico.periodicos.remove(periodic)
                            Poo.Material.materiales.remove(mater)
                            print("Se ha borrado correctamente")
                    break
                elif res == "size":
                    print(Poo.Periodico.size(material))
                    break
                elif res == "volver":
                    break
                else:
                    print("Escribe bien")
                    break
        elif res == "revista":
            pass


        else:
            print("Escribe bien")

    except ValueError as Valerr:
        print(f"Tienes que escribir un numero entero: {Valerr}")

    except KeyboardInterrupt as Keyerr:
        print("\n programa interrumpido. Saliendo....")
