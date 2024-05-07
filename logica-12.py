"""
Desarrolla un programa en Python para administrar una biblioteca.
El programa debe permitir al usuario realizar las siguientes operaciones:

  . Agregar un nuevo libro al catálogo de la biblioteca, incluyendo
    información como título, autor, género y año de publicación.
  . Prestar un libro a un usuario, registrando quién tomó prestado el libro y la fecha de préstamo.
  . Devolver un libro prestado, actualizando su estado en el sistema.
  . Ver la lista de todos los libros disponibles en la biblioteca,
    así como los libros prestados y a quién.
  . Salir del programa.
  
El programa debe proporcionar un menú interactivo para que el usuario seleccione
la operación que desea realizar. Además, debe mantener un registro de todos
los libros en la biblioteca y su estado de disponibilidad.
"""

prestados = [   #se crea un diccionario con un ejemplo de un libro prestado
]

books = [{  #se crea un diccionario donde seran guardados los libros
  'title' : 'tiven', 
  'author' : 'tiven', 
  'type' : 'accion', 
  'year' : 2004, 
  'estado' : 'EN CASA',  
}]

def create(title, author, ype, year, estado = 'EN CASA'): #funcion recibe serie de parametros
    book = { #crea un libro de valores los parametros recibidos
      'title' : title, 
      'author' : author, 
      'type' : ype, 
      'year' : year, 
      'estado' : estado, 
    }
    books.append(book) #metemos el libro nuevo en la lista de libros
    print("------------------------------")
    print("Create perfect")
    print("------------------------------")

def Prestar(title, name, date, estado="OCUPADO"):#funcion recibe serie de parametros
    book_found = False #definimos una variable boolean para usarlo como validador
    for book in books:#recorremos la lista de books
        if book['title'] == title and book['estado'] != estado:#buscamos coincidencia en el title
            prest = {#creamos un libro prestado con los parametros
                'title': title,
                'guest': name,
                'date': date
            }
            prestados.append(prest)#agregamos el nuevo libro prestado a la lista de libros prestados
            print("------------------------------")
            print("The book is property")
            print("------------------------------")
            book['estado'] = estado#cambiamos el estado del libro
            book_found = True #despues realizado todo lo necesario el validador lo ponemos verdadero
            break #rompemos el ciclo
    if not book_found: #entrara aqui si el validador es falso indicando que el nombre no coincide
        print("Book not found or already borrowed")

def Devolver(title, estado="EN CASA"):
    book_found = False
    for book in prestados:
        if book['title'] == title:
            prestados.remove(book)  # Eliminar el libro de la lista de prestados
            for x in books:
                if x['title'] == title:
                    x['estado'] = estado  # Cambiar el estado del libro en la lista de libros
                    break  # Salir del bucle después de actualizar el estado del libro en books
            print("------------------------------")
            print("devuelto")
            print("------------------------------")
            book_found = True
            break

    if not book_found:
        print("Book not found")

def Disponibles():
    for book in books:
        if book['estado'] == "OCUPADO":
            continue
        print(book)

while True: #pequeña interfaz por consola usando while
    res = input("Create, books, Get, prestados, devolver, disponibles, salir ").lower()
    if res == "create":
        print(create(input('book name: '), input('author book: '), input('type: '), input("date: ")))
    elif res == "books":
        print(f"Estos son los libros: {books}")
    elif res == "get":
        print(Prestar(input("Book name: "), input("Guess name: "), input("Date today: ")))
    elif res == "prestados":
        print(f"estos son los libros prestados {prestados}")
    elif res == "devolver":
        print(Devolver(input("book name: ")))
    elif res == "disponibles":
        print(Disponibles())
    elif res == "salir":
        break
    else:
        print("escribe bien")
