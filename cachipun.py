#realizar el juego de piedra, papel o tijeras (cachipun)
from random import choice as elegir

def WIN(movimiento, lista):
    gana = False
    if movimiento in lista:
        PC = elegir(lista)
        print("PC usa: ",PC)
        print("Jugador usa:", M)

        if movimiento == "Piedra" and PC == "Papel":
            print("Ha ganado PC.\n")
            gana = True

        elif movimiento == "Piedra" and PC == "Tijeras":
            print("Ha ganado el jugador.\n")
            gana = True
        
        elif movimiento == "Piedra" and PC == "Piedra":
            print("No hay ganador.\n")
            gana = False

        if movimiento == "Papel" and PC == "Tijeras":
            print("Ha ganado PC.\n")
            gana = True

        elif movimiento == "Papel" and PC == "Piedra":
            print("Ha ganado el jugador.\n")
            gana  = True

        elif movimiento == "Papel" and PC == "Papel":
            print("No hay ganador.\n")
            gana  = False

        if movimiento == "Tijeras" and PC == "Piedra":
            print("Ha ganado PC.\n")
            gana = True

        elif movimiento == "Tijeras" and PC == "Papel":
            print("Ha ganado el jugador.\n")
            gana = True

        elif movimiento == "Tijeras" and PC == "Tijeras":
            print("No hay ganador.\n")
            gana  = False

    else:
        print("Se ingresó movimiento/objeto inválido.\n")
        gana = False
    
    return(gana)

objeto = ["Piedra","Papel","Tijeras"]

ternima = False
while ternima == False:
    print("Piedra, Papel o Tijeras")
    M = input("Ingresa tu movimiento :").capitalize()

    if WIN(M,objeto) == True:
        ternima = True
