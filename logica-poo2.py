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

class Material():
    materiales = []  # Lista para almacenar todas las instancias de materiales

    def __init__(self, title, year, editorial, author):
        self.title = title
        self.year = year
        self.editorial = editorial
        self.author = author

    def materialView(self):
        return len(self.materiales)  # Método para obtener la cantidad de materiales

class Periodico(Material):
    periodicos = []
    def __init__(self, title, year, editorial, principalSection):
        super().__init__(title, year, editorial, None)  # Llamar al inicializador de la clase padre
        self.section = principalSection  # Atributo adicional para los periódicos
        Material.materiales.append(self)
        Periodico.periodicos.append(self)

    def periodicosView(self):
        return len(self.periodicos)

class Revista(Material):
    def __init__(self, title, year, editorial, numberEdition, tema):
        super().__init__(title, year, editorial, None)  # Llamar al inicializador de la clase padre
        self.edition = numberEdition  # Atributo adicional para las revistas
        self.tema = tema

    def revistasView(self):
        return len(self.materiales)  # Método para obtener la cantidad de revistas

class Libro(Material):
    def __init__(self, title, year, author, genero, numberpage):
        super().__init__(title, year, None, author)  # Llamar al inicializador de la clase padre
        self.genero = genero  # Atributo adicional para los libros
        self.pages = numberpage

    def librosView(self):
        return len(self.materiales)  # Método para obtener la cantidad de libros

material = []
# Crear instancias de Periodico y agregarlas a la lista de materiales
while True:
    res = input("Que quieres hacer? periodico / revista / libro : ").lower()
    try:
        if res == "periodico":
            res = input("Que accion quieres? Crear, buscar, remover, volver: ").lower()
            while True:
                if res == "crear":
                    nombre = input("Nombre del periódico: ")
                    year = int(input("year: "))
                    editorial = input("Editorial: ")
                    seccion_principal = input("Sección principal: ")
                    material = Periodico(nombre, year, editorial, seccion_principal)
                elif res == "buscar":
                    tituloBusc = input("Digita el nombre que quieres buscar: ").lower()
                    for x in Periodico.periodicos:
                        if x.title == tituloBusc:
                            print("Los Datos son los siguientes: \n")
                            print(f"El titulo es: {x.title}")
                            print(f"El año es:  {x.year}")
                            print(f"EL editorial es: {x.editorial}")
                            print(f"La seccion principal es: {x.section}")
                elif res == "remover":
                    tituloBusc = input("Digita nombre a borrar: ").lower()
                    for periodic, mater in zip(Periodico.periodicos, Material.materiales):
                        if periodic.title == tituloBusc and mater.title == tituloBusc:
                            Periodico.periodicos.remove(periodic)
                            Material.materiales.remove(mater)
                            print("Se ha borrado correctamente")
                elif res == "volver":
                    break
                else:
                    print("Escribe bien")
                    break
        else:
            print("Escribe bien")

    except ValueError as Valerr:
        print(f"Tienes que escribir un numero entero: {Valerr}")

    except KeyboardInterrupt as Keyerr:
        print("\n programa interrumpido. Saliendo....")
        break

    except Exception as err:
        print(f"Cometiste este error: {err.__class__}")
