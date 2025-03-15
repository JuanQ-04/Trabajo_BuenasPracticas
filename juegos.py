import random
import time

class PiedraPapelTijeras():


    def opcionesDelJuego(opcion):
        if opcion == 1:
            return "Piedra"
        elif opcion == 2:
            return "Papel"
        elif opcion == 3:
            return "Tijeras"
    
    def opcionMaquina():
        opcion = random.randint(1,3)
        return opcion

    def opcionJugador():
        while True:
            print("\nOpciones de juego\nPiedra (1)\nPapel (2)\nTijeras (3)\n")
            try:
                opcion = int(input("Ingrese su opcion: "))
                if opcion > 0 and opcion < 4:
                    return opcion
                else:
                    print( f"El valor '{opcion}' es invalido")
            except ValueError:
                print("Por favor, ingresa un número válido.")