"""
Escribe un programa en Python para gestionar un inventario simple.
El programa debe permitir al usuario realizar las siguientes operaciones:

    Agregar un nuevo elemento al inventario.
    Eliminar un elemento existente del inventario.
    Mostrar todos los elementos del inventario.
    Actualizar la cantidad de un elemento en el inventario.
    Buscar un elemento en el inventario por su nombre.
    
El inventario debe almacenarse como un diccionario donde las claves son los nombres
de los elementos y los valores son las cantidades disponibles de cada elemento.

El programa debe mostrar un menú de opciones al usuario y permitirle seleccionar una operación.
Una vez completada la operación seleccionada,
el menú debe mostrarse nuevamente para permitir
al usuario realizar más operaciones o salir del programa.
"""

Invent = { #se declara un diccionario con nombre Invent donde tiene dos parametros
    'teclado' : 2, #ProductName
    'deskop' : 4   #Cant
}

def create(ProductName, Cant): #funcion que recibe dos parametros una cadena de texto y un entero
    Invent[ProductName.lower()] = Cant # llamamos al diccionario y agregamos el primer parametro
    print("------------------------------") #usamos el .lower() para convertir en minuscula
    print("Create perfect")                 # y le brindamos el valor el cual es el parametro entero
    print("------------------------------")

def delete(ProductName): #funcion que recibe un parametro la cual es una cadena de texto
    if ProductName in Invent: #parametro recibido se busca si esta en el diccionario (Invent)
        Invent.pop(ProductName) #cuando lo busque lo elimina con el .pop()
        print("------------------------------")
        print("Delete perfect")
        print("------------------------------")
    else:   #si no se encuentra suelta mensaje
        print("incorrect search")
def Update(ProductName, newCant): #funcion que recibe dos parametros una cadena de texto y entera
    if ProductName in Invent: #si cadena de texto se encuentra en Invent
        Invent[ProductName] = newCant #se actualiza el valor con el newCant
        print("------------------------------")
        print("Update perfect")
        print("------------------------------")
    else:
        print("incorrect search")

def Read(ProductName): #funcion que recibe un parametro la cual es una cadena de texto
    if ProductName in Invent: #parametro recibido se busca si esta en el diccionario (Invent)
        print("--------------------------")
        print(f"have {Invent.get(ProductName)} UND") #arroja cantidad de und que tiene este producto
        print("--------------------------")
    else:
        print("incorrect search")

while True: #se crea un menu con el ciclo while
    res = input("Options: CREATE, UPDATE, READ, DELETE, INVENT, EXIT: ").lower()#se pide respuesta
    if res == "create":
        product_name = input("Enter the product name: ")
        quantity = int(input("Enter the quantity: "))
        create(product_name, quantity) #se llama la funcion pasando los paramatros dados
    elif res == "update":
        product_name = input("Enter the product name to update: ")
        new_quantity = int(input("Enter the new quantity: "))
        Update(product_name, new_quantity) #se llama la funcion pasando los paramatros dados
    elif res == "read":
        product_name = input("Enter the product name to read: ")
        Read(product_name) #se llama la funcion pasando los paramatros dados
    elif res == "delete":
        product_name = input("Enter the product name to delete: ")
        delete(product_name) #se llama la funcion pasando los paramatros dados
    elif res == "invent":
        print(f"This is the inventory list: {Invent}") #se llama todo el diccionario
    elif res == "exit": #si es exit la respuesta se rompe el ciclo con el break
        break
    else:
        print("Incorrect option") #si se marca una opcion incorrecta sale mensaje
