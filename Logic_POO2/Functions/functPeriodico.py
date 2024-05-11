from POO import Poo
def crear():
    try:
        nombre = input("Nombre del periódico: ")
        year = int(input("year: "))
        editorial = input("Editorial: ")
        seccion_principal = input("Sección principal: ")
        lista = [nombre, year, editorial, seccion_principal]
        return lista
    except ValueError as Valerr:
        print(f"Cometiste un error: {Valerr}")
    except KeyboardInterrupt as KeyErr:
        print("Saliendo.....")

def buscar(title):
    for x in Poo.Periodico.periodicos:
        if x.title == title:
            print("Los Datos son los siguientes: \n")
            print(f"El titulo es: {x.title}")
            print(f"El año es:  {x.year}")
            print(f"EL editorial es: {x.editorial}")
            print(f"La seccion principal es: {x.section}")
