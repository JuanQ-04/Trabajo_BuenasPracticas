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

    def juego():

        opcion_jugador = PiedraPapelTijeras.opcionJugador()
        opcion_maquina = PiedraPapelTijeras.opcionMaquina()

        jugador = PiedraPapelTijeras.opcionesDelJuego(opcion_jugador)
        maquina = PiedraPapelTijeras.opcionesDelJuego(opcion_maquina)

        print("-"*15)
        print("Calculando el resultado....")
        print("-"*15)
        time.sleep(0.3)

        resultado = ""
        if jugador == maquina:
            resultado = f"Tu elección: {jugador}\nElección de la máquina: {maquina}\n\n¡Es un empate!"
        elif (jugador == "Piedra" and maquina == "Tijeras") or (jugador == "Papel" and maquina == "Piedra") or (jugador == "Tijeras" and maquina == "Papel"):
            resultado = f"Tu elección: {jugador}\nElección de la máquina: {maquina}\n¡Ganaste!"
        else:
            resultado = f"Tu elección: {jugador}\nElección de la máquina: {maquina}\n¡Perdiste!"

        print("\n")
        print("-"*15)
        print (resultado)
        print("-"*15)



class Adivina():

    def adivina_el_numero():
        numero_secreto = random.randint(1, 100)
        intentos = 0
        print("¡Bienvenido al juego de adivinanza!")
        print("He pensado en un número entre 1 y 100. ¿Puedes adivinar cuál es?")
        
        while True:
            try:
                intento = int(input("Introduce tu número: "))
                intentos += 1
                
                if intento < numero_secreto:
                    print("Demasiado bajo. Intenta de nuevo.")
                elif intento > numero_secreto:
                    print("Demasiado alto. Intenta de nuevo.")
                else:
                    print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                    break
            except ValueError:
                print("Por favor, introduce un número válido.")

if __name__ == "__main__":

    while True:
        print("\nSeleccione un juego:")
        print("1. Piedra, Papel o Tijeras")
        print("2. Adivina el número")
        print("3. Salir")
        opcion = input("Ingrese el número del juego que desea jugar: ")

        if opcion == "1":
            print("-"*15)
            print("¡Bienvenido a Piedra, Papel o Tijeras!")
            print("-"*15)
            while True:
                PiedraPapelTijeras.juego()
                jugar_otra = input("\n¿Quieres jugar otra ronda? (s/n): ").lower()
                if jugar_otra != "s":
                    print("Gracias por jugar, hasta la próxima")
                    break
                time.sleep(0.5)

        elif opcion == "2":
            Adivina.adivina_el_numero()

        elif opcion == "3":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

        else:
            print("Opción no válida, por favor elige 1, 2 o 3.")