from abc import ABC, abstractclassmethod #se importa abstractclassmethod para usar abstrapcion

class Ave:#se define una clase abstracta la cual su funcion es ser una plantilla
    @abstractclassmethod
    def __init__(self, nom_ave, size_ala, color_dominante):
        self.nom_ave = nom_ave
        self.size_ala = size_ala
        self.color_dominante = color_dominante

    @abstractclassmethod#todas las que hereden de esta clase debe de tener este metodo
    def puedo_volar(self):
        pass

    @abstractclassmethod#todas las que hereden de esta clase debe de tener este metodo
    def presentar(self):
        pass

class Ave_No_Voladora(Ave):#se crea una clase de ave no voladora que hereda de la plantilla Ave
    def __init__(self, nom_ave, size_ala, color_dominante, principal_accion):
        super().__init__(nom_ave, size_ala, color_dominante)#hereda todos los atributos
        self.accion = principal_accion#se define una accion principal

    def puedo_volar(self):#se definen los metodos obligatorios
        return "No puedo volar"

    def presentar(self):#se define los metodos obligatorios
        return f"Hola, Mi nobre de especie es: {self.nom_ave} mi principal accion es: {self.accion}"

    def hacer_accion(self):#se crea un metodo adicional el cual solo lo tendra esta clase
        return f"Estoy por: {self.accion}"

class Ave_Voladora(Ave):#se crea una clase de ave voladora que hereda de la plantilla ave
    def __init__(self, nom_ave, size_ala, color_dominante, vel_vuelo):
        super().__init__(nom_ave, size_ala, color_dominante)#hereda los atributos de la plantilla
        self.speed = vel_vuelo#se declara el atributo speed que solo lo tendra las aves voladoras

    def puedo_volar(self):#se define los metodos obligatorios
        return "Si, puedo volar"

    def presentar(self):#se define los metodos obligatorios
        return f"Hola, mi nombre de especie es: {self.nom_ave} y soy ave voladora"

    def velocidad(self):#se crea un metodo adicional el cual solo lo tendra esta clase
        return f"Mi velocidad de vuelo es: {self.speed} km/h"


#se crea una instancia de la clase creando un objeto
pinguino = Ave_No_Voladora("pinguino", "100 cm", "blanco", "bucear")
azulejo = Ave_Voladora("azulejo", "10cm", "azul", 10)
#se imprime los metodos que tiene cada clase
print("--------------------------")
print("--------------------------")
print(pinguino.presentar())
print(pinguino.puedo_volar())
print(pinguino.hacer_accion())
print("--------------------------")
print("--------------------------")
print(azulejo.presentar())
print(azulejo.puedo_volar())
print(azulejo.velocidad())
print("--------------------------")
print("--------------------------")
