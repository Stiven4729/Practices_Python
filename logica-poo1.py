"""
Crear varios libros donde el usuario pase los atributos y tenga opcion de buscar un libro por titulo
y llame a un metodo donde este arroje el author del libro correspondiente
"""

class libro():
    def __init__(self, titulo, genero, autor):
        self.title = titulo
        self.gene = genero
        self.author = autor

    def autho(self):
        print(f"El autor del libro es {self.author}")

libros = []
i = 0  # Inicializar el contador fuera del bucle

while True:
    respuesta = input("crear, salir, total, author: ")
    if respuesta == "crear":
        i += 1  # Incrementar el contador correctamente
        nuevo_libro = libro(input("titulo: "), input("genero: "), input("autor: "))
        libros.append(nuevo_libro)  # Almacenar el objeto libro en la lista
    elif respuesta == "salir":
        break
    elif respuesta == "total":
        print(len(libros))
    elif respuesta == "author":
        buscar = input("escribe titulo del libro: ")
        for x in libros:
            if x.title == buscar:
                x.autho()
