import os
import time 
import random
from Funciones.questions_bank import questions_bank
from Funciones.start import start
from Funciones.admin import admin

def main():

    print("----------Bienvenid@ a este juego---------")
    while True:
        option=input("\nPresiona X para comenzar\nPresiona Y para salir\n")
        if option=="X":
            print("Iniciando...")
            results=start()
            print("Juego terminado\n")
            print("Su resultado fue:\nPreguntas Acertadas: ",results[0],"\n","Preguntas Fallidas: ",results[1])
        elif option=="Y":
            print("Saliendo...")
            break
        elif option=="Z":
            print("Modo admin")
            admin()
        else:
            pass

main()





