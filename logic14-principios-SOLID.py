from abc import ABC, abstractmethod

class Actividad(ABC):#se hereda de ABC para garantizar que es clase abstracta
    _id_counter = 1  # Variable de clase para contar los IDs

    @abstractmethod#se define atributos abstractos
    def __init__(self, nom_activity, date, start_hour, finish_hour):
        self.nom_activity = nom_activity
        self.date = date
        self.start_hour = start_hour
        self.finish_hour = finish_hour
        self.__id = Actividad._id_counter
        Actividad._id_counter += 1

    @abstractmethod#se define metodos abstractos
    def info_activity(self):
        pass

    @property#se indica que son setters o getters
    def identificador(self):
        return self.__id

class PresupuestoActividad(Actividad):
    def __init__(self, nom_activity, date, start_hour, finish_hour, spectation_cash, presupuesto):
        super().__init__(nom_activity, date, start_hour, finish_hour)
        self.spectation_cash = spectation_cash
        self.presupuesto = presupuesto

    def info_activity(self):
        resultado = self.spectation_cash - self.presupuesto
        faltante = f"Tu tiempo límite es hasta la fecha: {self.date} para ahorrar: {resultado}"
        return f"Tu presupuesto es: {self.presupuesto} dólares. {faltante}"

class ReunionActividad(Actividad):
    def __init__(self, nom_activity, date, start_hour, finish_hour, modality):
        super().__init__(nom_activity, date, start_hour, finish_hour)
        self.modality = modality

    def info_activity(self):
        modality_info = f"Tienes una reunión, su modalidad es: {self.modality}"
        if self.modality == "virtual":
            return f"{modality_info}. Su fecha es: {self.date} y su hora de inicio es {self.start_hour}"
        elif self.modality == "presencial":
            return f"{modality_info}. Necesitas presupuesto. Su fecha es: {self.date} y su hora de inicio es {self.start_hour}"
        else:
            return "Coloca una modalidad correctamente"

# Crear instancias de las clases
number1 = PresupuestoActividad("Salida", "24/05/2024", "2:00pm", "4:00pm", 3000, 1500)
number2 = ReunionActividad("Salida", "24/05/2024", "2:00pm", "4:00pm", "virtual")
number3 = ReunionActividad("Salida", "24/05/2024", "2:00pm", "4:00pm", "presencial")

# Imprimir resultados
print("---------------------------")
print(number1.info_activity())
print("---------------------------")
print(number2.info_activity())
print("---------------------------")
print(number3.info_activity())
print("---------------------------")
