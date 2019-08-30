#Variables Globales

#Estado del juego
enPartida = True

#quien gano?
ganador = None

#De quien es el turno?

jugadorActual = "X"

#Definir el tablero de juego
tablero = ["-", "-", "-",
           "-", "-", "-",
           "-", "-", "-"]
#Método que muestra el tablero en pantalla
def mostrarTablero():
    print(tablero[0] + " | " + tablero[1] + " | " + tablero[2])
    print(tablero[3] + " | " + tablero[4] + " | " + tablero[5])
    print(tablero[6] + " | " + tablero[7] + " | " + tablero[8])

def jugar():

    #Mostrar el tablero inicial
    mostrarTablero()

    while enPartida:
        #Maneja el turno del jugador
        turnos(jugadorActual)
        #Chekea si se terminó el juego
        juegoTerminado()
        #Cambia el turno del jugador
        cambiarJugador()
    if ganador == "X" or ganador == "O":
        print("Ganaron las: " + ganador)
        volverAJugar()
    elif ganador == None:
        print("Empatados!")
        volverAJugar()

def volverAJugar():
    #Definicion de variable para acceso
    global tablero
    #Captación de respuesta del usuario
    respuesta = input("Desea volver a jugar? s/n ")
    while respuesta not in ["s","n"]:
        respuesta = input("Desea volver a jugar? s/n")
    #Si decide volver a jugar, blanquea el tablero y vuelve a jugar
    if respuesta == "s":
        reiniciar()
        jugar()
    #No quiere volver a jugar y termina el programa.
    else:
        return

def reiniciar():
    global enPartida, ganador, jugadorActual, tablero
    # Estado del juego
    enPartida = True

    # quien gano?
    ganador = None

    # De quien es el turno?

    jugadorActual = "X"

    # Definir el tablero de juego
    tablero = ["-", "-", "-",
               "-", "-", "-",
               "-", "-", "-"]


def cambiarJugador():
    #Definicion de la variable para acceso
    global jugadorActual
    #Si el jugador actual era X lo cambia a O
    if jugadorActual == "X":
        jugadorActual = "O"
    #Si el jugador actual era O lo cambia a X
    elif jugadorActual == "O":
        jugadorActual ="X"
    return

def juegoTerminado():
    hayGanador()
    hayEmpate()


def hayGanador():
    #Definicion de global para poder acceder
    global ganador
    #Chekear filas
    ganadorPorFilas = checkFilas()
    #Chekear columnas
    ganadorPorColumnas = checkColumnas()
    #Chekear diagonales
    ganadorPorDiagonales = checkDiagonales()
    if ganadorPorFilas:
        #Hubo victoria
        ganador = ganadorPorFilas
    elif ganadorPorColumnas:
        #Hubo victoria
        ganador = ganadorPorColumnas
    elif ganadorPorDiagonales:
        #Hubo victoria
        ganador = ganadorPorDiagonales
    else:
        #Hubo Empate
        ganador = None
    return

def checkFilas():
    #Definicion de variable para acceso
    global enPartida
    #Chekeo si alguna fila ganó
    fila1 = tablero[0] == tablero[1] == tablero[2] != "-"
    fila2 = tablero[3] == tablero[4] == tablero[5] != "-"
    fila3 = tablero[6] == tablero[7] == tablero[8] != "-"
    #Si alguna ganó
    if fila1 or fila2 or fila3:
        enPartida = False
    #Retornar el ganador
    if fila1:
        return tablero[0]
    elif fila2:
        return tablero[3]
    elif fila3:
        return tablero[6]
    return

def checkColumnas():
    # Definicion de variable para acceso
    global enPartida
    # Chekeo si alguna columna ganó
    col1 = tablero[0] == tablero[3] == tablero[6] != "-"
    col2 = tablero[1] == tablero[4] == tablero[7] != "-"
    col3 = tablero[2] == tablero[5] == tablero[8] != "-"
    # Si alguna ganó
    if col1 or col2 or col3:
        enPartida = False
    # Retornar el ganador
    if col1:
        return tablero[0]
    elif col2:
        return tablero[1]
    elif col3:
        return tablero[2]
    return

def checkDiagonales():
    # Definicion de variable para acceso
    global enPartida
    # Chekeo si alguna diagonal ganó
    diag1 = tablero[0] == tablero[4] == tablero[8] != "-"
    diag2 = tablero[6] == tablero[4] == tablero[2] != "-"

    # Si alguna ganó
    if diag1 or diag2:
        enPartida = False
    # Retornar el ganador
    if diag1:
        return tablero[0]
    elif diag2:
        return tablero[6]
    return


def hayEmpate():
    #Definicion de la variable para acceso
    global enPartida
    #Si no hay mas "-" no hay mas lugar para moverse
    if "-" not in tablero:
        enPartida = False

    return

def turnos(jugadorActual):

    #Mostrar de quien es el turno
    print("Es el turno de: " + jugadorActual)
    #Tomar la posicion deseada por el jugador desde el teclado
    posicion = input("Ingrese un número del 1 al 9: ")

    casilleroValido = False
    while not casilleroValido:
        #Validar input del jugador (una RegEx era matar una hormiga con un lanzacohetes)
        while posicion not in ["1","2","3","4","5","6","7","8","9"]:
            posicion = input("Ingrese un número del 1 al 9: ")
        #Definir la posicion segun el indice del arreglo
        posicion = int(posicion) -1
        #Si hay un "-", el casillero está libre y es un movimiento válido
        if tablero[posicion] == "-":
            casilleroValido = True
        #Hay otra ficha en el casillero!
        else:
            print("Elegiste un casillero ocupado! Intentá de nuevo!")

    #Marcar la jugada en el tablero
    tablero[posicion] = jugadorActual
    #Mostrar el tablero actualizado
    mostrarTablero()

jugar()