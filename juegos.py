import random
import time

#Se inicia la clase del primer juego
class PiedraPapelTijeras():

    #Funcion que transforma los numeros a las opciones del juego
    def opcionesDelJuego(opcion):
        if opcion == 1:
            return "Piedra"
        elif opcion == 2:
            return "Papel"
        elif opcion == 3:
            return "Tijeras"
    
    #Funcion que trae un numero al azar para escoger la opcion de la maquina
    def opcionMaquina():
        opcion = random.randint(1,3)
        return opcion

    #Funcion que pregunta la opcion que va a tomar el jugador
    def opcionJugador():
        while True:
            print("\nOpciones de juego\nPiedra (1)\nPapel (2)\nTijeras (3)\n")
            try:
                opcion = int(input("Ingrese su opcion: "))
                if opcion > 0 and opcion < 4:   #Condicional para que la opcion tomada este dentro de los parametros
                    return opcion
                else:
                    print( f"El valor '{opcion}' es invalido")
            except ValueError:
                print("Por favor, ingresa un número válido.")

    #Funcion donde se da inicio al juego
    def juego():

        opcion_jugador = PiedraPapelTijeras.opcionJugador()
        opcion_maquina = PiedraPapelTijeras.opcionMaquina()

        jugador = PiedraPapelTijeras.opcionesDelJuego(opcion_jugador)
        maquina = PiedraPapelTijeras.opcionesDelJuego(opcion_maquina)

        print("-"*15)
        print("Calculando el resultado....")
        print("-"*15)
        time.sleep(0.3)

        #Condicionales de victoria, derrota y empate
        resultado = ""
        if jugador == maquina:
            resultado = f"Tu elección: {jugador}\nElección de la máquina: {maquina}\n\n¡Es un empate!"
        elif (jugador == "Piedra" and maquina == "Tijeras") or (jugador == "Papel" and maquina == "Piedra") or (jugador == "Tijeras" and maquina == "Papel"):
            resultado = f"Tu elección: {jugador}\nElección de la máquina: {maquina}\n¡Ganaste!"
        else:
            resultado = f"Tu elección: {jugador}\nElección de la máquina: {maquina}\n¡Perdiste!"

        #Retorna el mensaje final
        print("\n")
        print("-"*15)
        print (resultado)
        print("-"*15)

#Clase del segundo juego
class Adivina():

    def adivina_el_numero():
        numero_secreto = random.randint(1, 100) #Escoge de manera aleatoria el numero a encontrar
        intentos = 0
        print("¡Bienvenido al juego de adivinanza!")
        print("He pensado en un número entre 1 y 100. ¿Puedes adivinar cuál es?")
        
        while True:
            try:
                while True:
                    intento = int(input("Introduce tu número: "))
                    if intento <= 100 and intento >= 0:
                        intentos += 1   #Inicia una variable con la cual se van a captar los intentos
                        if intento < numero_secreto:    #Condicional si el intento del jugador es menor al numero
                            print("Demasiado bajo. Intenta de nuevo.")
                        elif intento > numero_secreto:  #Condicional si el intento del jugador es mayor al numero
                            print("Demasiado alto. Intenta de nuevo.")
                        else:       #Condicional si el jugador finalmente halla el numero secreto
                            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                            break
                    else:
                        print(f"El numero ingresado {intento} no esta dentro de los parametros establecidos.")
            except ValueError:
                print("Por favor, introduce un número válido.")

if __name__ == "__main__":

    #Menu de inicio
    while True:
        print("\nSeleccione un juego:")
        print("1. Piedra, Papel o Tijeras")
        print("2. Adivina el número")
        print("3. Salir")
        opcion = input("Ingrese el número del juego que desea jugar: ")

        #Menu del juego Piedra Papel o Tijera
        if opcion == "1":
            print("-"*15)
            print("¡Bienvenido a Piedra, Papel o Tijeras!")
            print("-"*15)
            while True: #Bucle para repetir el juego
                PiedraPapelTijeras.juego()
                jugar_otra = input("\n¿Quieres jugar otra ronda? (s/n): ").lower()  #Pregunta al jugador si quiere salirse del juego
                if jugar_otra != "s": 
                    print("Gracias por jugar, hasta la próxima")
                    break
                time.sleep(0.5)

        #Menu del juego de adivinanza
        elif opcion == "2":
            Adivina.adivina_el_numero()

        #Opcion de Salir
        elif opcion == "3":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

        else:
            print("Opción no válida, por favor elige 1, 2 o 3.")