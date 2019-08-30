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
    elif ganador == None:
        print("Empatados!")


def cambiarJugador():

    return

def juegoTerminado():
    hayGanador()
    hayEmpate()


def hayGanador():

    return

def hayEmpate():

    return

def turnos(jugadorActual):

    #Tomar la posicion deseada por el jugador desde el teclado
    posicion = input("Ingrese un número del 1 al 9: ")
    #Definir la posicion segun el indice del arreglo
    posicion = int(posicion) -1

    #Marcar la jugada en el tablero
    tablero[posicion] = "X"
    #Mostrar el tablero actualizado
    mostrarTablero()

jugar()