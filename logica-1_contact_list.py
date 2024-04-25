"""
Desarrolla un programa para gestionar una lista de contactos. 
El programa debe permitir al usuario
agregar nuevos contactos con información
como nombre, apellido, número de teléfono y correo electrónico. 
Además, el usuario debe poder buscar contactos por nombre y eliminar contactos de la lista.
"""
#Nota el programa se desarrolla sin bucles ni con funciones para fomentar la logica
contacts = [
    {
        'name' : "Stiven",
        'lastName' : "Lopez",
        'num' : 3022200976,
        'adress' : "gallegostiven4729@gmail.com"
    },
    {
        'name' : "Esteban",
        'lastName' : "Lopez",
        'num' : 3113047469,
        'adress' : "esteban@gmail.com"
    },
    {
        'name' : "Oscar",
        'lastName' : "Gallego",
        'num' : 112233445,
        'adress' : "Oscar@gmail.com"
    }
]

respuesta = input("quieres agregar un contacto? escribe si o no ").lower()#el .lower para convertir todo a minusculas
if respuesta == "si":
    name = input("Ëscribe el nombre ")
    lastname = input("Ëscribe el apellido ")
    num = input("Ëscribe el numero ")
    adress = input("Ëscribe el correo ")
    print(name)
    contacts += [
        {
            'name' : name,
            'lastName' : lastname, 
            'num' : num,
            'adress' : adress
        }
    ]
    print(contacts)
elif respuesta == "no":
    respuesta = input("Quieres buscar un contacto? escribe si o no ").lower()
    if respuesta == "si":
        nombre = input("Escribe el nombre de la persona que quieres buscar ")
        if nombre in contacts[0].values():#el .values() es para coger los valores del diccionario para ser comparados por el nombre (nombre ==? nom)
            print(contacts[0])
            respuesta = input("quieres eliminar el contacto buscado? si o no ").lower()
            if respuesta == "si":
                del contacts[0]
                print(contacts)
        elif nombre in contacts[1].values():
            print(contacts[1])
            respuesta = input("quieres eliminar el contacto buscado? si o no ").lower()
            if respuesta == "si":
                del contacts[1]
                print(contacts)
        elif nombre in contacts[2].values():
            print(contacts[2])
            respuesta = input("quieres eliminar el contacto buscado? si o no ").lower()
            if respuesta == "si":
                del contacts[2]
                print(contacts)
        else:
            print("El contacto no esta")
else:
    print("Las unicas respuestas validas son si/no vuelvelo a intentar")
