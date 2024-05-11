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
from Functions import functPeriodico
# Crear instancias de Periodico y agregarlas a la lista de materiales
try:
    while True:
        res = input("Que quieres hacer? periodico / revista / libro : ").lower()
        if res == "periodico":
            res = input("Que accion quieres? Crear, buscar, remover, volver: ").lower()
            try:
                while True:
                    if res == "crear":
                        try:
                            functPeriodico.crear()
                        except UnboundLocalError as err:
                            print(f"No se pudo crear: {err}")
                        break
                    elif res == "buscar":
                        tituloBusc = input("Digita el nombre que quieres buscar: ").lower()
                        functPeriodico.buscar(tituloBusc)
                        break
                    elif res == "remover":
                        tituloBusc = input("Digita nombre a borrar: ").lower()
                        functPeriodico.remover(tituloBusc)
                        break
                    elif res == "size":
                        print(functPeriodico.size())
                        break
                    elif res == "volver":
                        break
                    else:
                        print("Escribe bien")
                        break
            except KeyboardInterrupt:
                print("Saliendo........")
        elif res == "revista":
            pass
        else:
            print("Escribe bien")
except KeyboardInterrupt as keyerr:
    print("Saliendo.....")
