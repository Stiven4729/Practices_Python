"""
Descripción: Desarrolla un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
El programa debe solicitar al usuario que ingrese su peso en kilogramos y su altura en metros
luego calcular el IMC utilizando la fórmula IMC = peso / (altura * altura). 
Finalmente, el programa debe mostrar el IMC calculado y una interpretación del resultado
según la siguiente tabla:

IMC < 18.5: Bajo peso
18.5 >= IMC < 25: Peso normal
25 <= IMC < 30: Sobrepeso
IMC >= 30: Obesidad

"""

def Calculo_IMC(Kg, Alt):
    IMC = Alt*Alt
    IMC = round(Kg / IMC, 2)
    return(IMC)

def Clasificador(IMC):
    if IMC < 18.5:
        print("peso bajo")
    elif 18.5 <= IMC < 25:
        print("Peso normal")
    elif 25 <= IMC < 30:
        print("Sobrepeso")
    else:
        print("Obesidad")
    print(f"{IMC}")

Valor = Calculo_IMC(int(input("Digita tu peso: ")), float(input("Digita tu altura en metros: ")))
Clasificador(Valor)
