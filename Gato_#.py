#1 mostrar tablero, designando los espacios
#2 indicar turno del jugador1 y jugador2
#3 al ingresar el número de la celda, mostrar fichero juego
def dibujarTablero():   #Dibuja el tablero de juego
    print(ubicacion[1],ubicacion[2],ubicacion[3], sep ="|")
    print(ubicacion[4],ubicacion[5],ubicacion[6], sep ="|")
    print(ubicacion[7],ubicacion[8],ubicacion[9], sep ="|")

def marca(celda, jugador): #Registra la celda indicada por el jugador
    
    if celda > 0 and celda < 7:
        ubicacion[celda] = jugador

    elif celda >= 7 and celda < 10: #Da formato especial para las ultimas 3 celdas
        if jugador =="_X_":
            jugador = " X "
            ubicacion[celda] = jugador
            jugador ="_X_"

        elif jugador == "_O_":
            jugador = " O "
            ubicacion[celda] = jugador
            jugador = "_O_"

    return(jugador)

def win(jugador, gano = False): #revisa si se cumple la combinación ganadora al registrar la celda del jugador comparando solo el valor interno

    if ubicacion[1][1] == ubicacion[2][1] and ubicacion[1][1] == ubicacion[3][1]:
        jugador
        gano = True

    elif ubicacion[4][1] == ubicacion[5][1] and ubicacion[4][1] == ubicacion[6][1]:
        jugador
        gano = True

    elif ubicacion[7][1] == ubicacion[8][1] and ubicacion[7][1] == ubicacion[9][1]:
        jugador
        gano = True

    elif ubicacion[1][1] == ubicacion[4][1] and ubicacion[1][1] == ubicacion[7][1]:
        jugador
        gano = True 
    
    elif ubicacion[2][1] == ubicacion[5][1] and ubicacion[2][1] == ubicacion[7][1]:
        jugador
        gano = True 

    elif ubicacion[3][1] == ubicacion[6][1] and ubicacion[3][1] == ubicacion[9][1]:
        jugador
        gano = True 

    elif ubicacion[1][1] == ubicacion[5][1] and ubicacion[1][1] == ubicacion[9][1]:
        jugador
        gano = True 

    elif ubicacion[3][1] == ubicacion[5][1] and ubicacion[3][1] == ubicacion[7][1]:
        jugador
        gano = True 

    return(gano)
        

ubicacion = {   1 : "_1_",  #diccionario de juego
                2 : "_2_",
                3 : "_3_",
                4 : "_4_",
                5 : "_5_",
                6 : "_6_",
                7 : " 7 ",
                8 : " 8 ",
                9 : " 9 "
                }

print("Inicia el juego jugador 1")
dibujarTablero()

correcto = False
while correcto == False : #Fuerza que solo se pueda asignar el valor de X u O
    P1 = input("Jugador 1 selecciona tu marca. Ingresa X u O :").upper()
    if P1 == "X":
        P1 = "_X_"
        P2 = "_O_"
        correcto = True
    elif P1 =="O":
        P1 = "_O_"
        P2 = "_X_"
        correcto = True
    else:
        print("Ingresó una marca inválida.")

Turno = 1
contador = 1
while contador <= 9:

    if Turno == 1:
        try:

            Celda = int(input("Jugador1 indique número de la celda a marcar: "))
            if Celda > 0 and Celda < 10:
                if ubicacion[Celda][1] != "O" and ubicacion[Celda][1] != "X":
                    marca(Celda,P1)
                    contador += 1
                    Turno = 2
                    dibujarTablero()
                else:
                    print("No se puede usar celda, ingrese de nuevo.")

                if win(P1) == True:
                    print("Ha ganado el jugador 1.")
                    break
            
            else:
                print("No se puede registrar en la celda", Celda)
        
        except ValueError:
            print("No ha ingresado un número.")

    elif Turno == 2 :
        try:

            Celda = int(input("Jugador2 indique número de la celda a marcar: "))
            if Celda > 0 and Celda < 10:
                if ubicacion[Celda][1] != "O" and ubicacion[Celda][1] != "X":
                    marca(Celda,P2)
                    contador += 1
                    Turno = 1
                    dibujarTablero()
                else:
                    print("No se puede usar celda, ingrese de nuevo.")

                if win(P2) == True:
                    print("Ha ganado el jugador 2.")
                    break
            else:
                print("No se puede registrar en la celda", Celda)

        except ValueError:
            print("No ha ingresado un número.")

if win(P1) == False:
    print("No hay ganador.")

#hola
print("prueba")