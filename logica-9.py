"""
Se	requiere	diseñar	e	implementar	una	aplicación	para	la	asociaciones	de	tenis	profesional	
WTA	que	permita	ingresar	en	los	nombres	de	 las	8	jugadoras	y	genere	los	partidos	del	
torneo

El	programa	deberá	mostrar	por	cada	partido	los	nombres	de	las	jugadoras que	se	enfrentan	
y	deberá	permitir	ingresar	el	resultado	de	ese	partido.
Al	finalizar	se	mostrara	el	nombre	de la	campeona del	torneo
"""

jugadores, ganadores, finalistas = [], [], []
valor, valor2, valor3 = 0, 0, 0
for x in range(8):
    jugadores.append(input(f"ingresa jugador numero {x +1}: "))

print("-----------")
print("Inicia el torneo")
print("-----------")
for i in jugadores:
    if valor != -4:
        valor = valor - 1
        print(f"Primer juego es: {i} vs {jugadores[valor]}")
        puntuacion1 = int(input(f"Cual es la puntuacion del jugador {i}: "))
        puntuacion2 = int(input(f"Cual es la puntuacion del jugador {jugadores[valor]}: "))
        if puntuacion1 > puntuacion2:
            print(f"El juego lo gano {i}")
            ganadores.append(i)
        else:
            print(f"El juego lo gano {jugadores[valor]}")
            ganadores.append(jugadores[valor])
print("-----------")
print("Semi-final")
print("-----------")
for j in ganadores:
    if valor2 != -2:
        valor2 = valor2 - 1
        print(f"Primer juego es: {j} vs {ganadores[valor2]}")
        puntuacion1 = int(input(f"Cual es la puntuacion del jugador {j}: "))
        puntuacion2 = int(input(f"Cual es la puntuacion del jugador {ganadores[valor2]}: "))
        if puntuacion1 > puntuacion2:
            print(f"El juego lo gano {j}")
            finalistas.append(j)
        else:
            print(f"El juego lo gano {ganadores[valor2]}")
            finalistas.append(ganadores[valor2])
print("-----------")
print("final")
print("-----------")
print(f"El juego final se juega entre: {finalistas[0]} vs {finalistas[1]}")
puntuacion1 = int(input(f"Cual es la puntuacion del jugador {finalistas[0]}: "))
puntuacion2 = int(input(f"Cual es la puntuacion del jugador {finalistas[1]}: "))
if puntuacion1 > puntuacion2:
    print(f"El ganador del torneo es {finalistas[0]}")
else:
    print(f"El ganador del torneo es {finalistas[1]}")
