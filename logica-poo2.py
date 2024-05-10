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
        Material.materiales.append(self)  # Agregar la instancia actual a la lista de materiales

    def materialView(self):
        return len(self.materiales)  # Método para obtener la cantidad de materiales

class Periodico(Material):
    def __init__(self, title, year, editorial, principalSection):
        super().__init__(title, year, editorial, None)  # Llamar al inicializador de la clase padre
        self.section = principalSection  # Atributo adicional para los periódicos

    def periodicosView(self):
        return len(self.materiales)  # Método para obtener la cantidad de periódicos

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

# Crear instancias de Periodico y agregarlas a la lista de materiales
periodico1 = Material("nombr", 2344, "editorial", "seccion_principa")

while True:
    res = input("Que quieres hacer? periodico / revista / libro : ").lower()
    if res == "periodico":
        res = input("Que accion quieres? Crear, buscar, remover: ").lower()
        if res == "crear":
            nombre = input("Nombre del periódico: ")
            año = input("Año: ")
            editorial = input("Editorial: ")
            seccion_principal = input("Sección principal: ")

            periodico1 = Periodico(nombre, año, editorial, seccion_principal)
            print(periodico1.periodicosView())  # Imprimir la cantidad de periódicos
