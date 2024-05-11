class Material():
    materiales = []  # Lista para almacenar todas las instancias de materiales

    def __init__(self, title, year, editorial, author):
        self.title = title
        self.year = year
        self.editorial = editorial
        self.author = author

    def size(self):
        return len(self.materiales)  # Método para obtener la cantidad de materiales

class Periodico(Material):
    periodicos = []
    def __init__(self, title, year, editorial, principalSection):
        super().__init__(title, year, editorial, None)  # Llamar al inicializador de la clase padre
        self.section = principalSection  # Atributo adicional para los periódicos
        Material.materiales.append(self)
        Periodico.periodicos.append(self)
    def size(self):
        return len(Periodico.materiales)

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
