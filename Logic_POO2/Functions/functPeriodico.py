from POO import Poo
def crear():
    try:
        nombre = input("Nombre del periódico: ")
        year = int(input("year: "))
        editorial = input("Editorial: ")
        seccion_principal = input("Sección principal: ")
        if not (nombre and editorial and seccion_principal):
            print("Hay campos vacios. No puedes continuar")
        else:
            Poo.Periodico(nombre, year, editorial, seccion_principal)
    except ValueError as err:
        print(f"Se te esta pidiendo un entero: {err}")
    return "Creacion exitosa"

def buscar(title):
    if title != ("" and  " "):
        for x in Poo.Periodico.periodicos:
            if x.title == title:
                print("Los Datos son los siguientes: \n")
                print(f"El titulo es: {x.title}")
                print(f"El año es:  {x.year}")
                print(f"EL editorial es: {x.editorial}")
                print(f"La seccion principal es: {x.section}")
            else:
                print(f"No se encontro el titulo {title}")
    else:
        print("Tienes que poner algo")

def remover(title):
    if title != ("" and  " "):
        for periodic, mater in zip(Poo.Periodico.periodicos, Poo.Material.materiales):
            if periodic.title == title and mater.title == title:
                Poo.Periodico.periodicos.remove(periodic)
                Poo.Material.materiales.remove(mater)
                print("Se ha borrado correctamente")
            else:
                print(f"No se encontro el titulo: {title} por ende no se pudo borrar")
    else:
        print("Tienes que colocar un titulo")

def size():
    if len(Poo.Periodico.periodicos) == 1:
        return f"Tenemos: {len(Poo.Periodico.periodicos)} periodicos"
    else:
        return f"Hay {len(Poo.Periodico.periodicos)} periodico"
