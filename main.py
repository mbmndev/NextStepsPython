import os
import platform
from prettytable import PrettyTable
from termcolor import colored
from Ejercicios import Ejercicio1
from Ejercicios import Ejercicio2
from Ejercicios import Ejercicio3
from Ejercicios import Ejercicio4
from Ejercicios import Ejercicio5
from Ejercicios import Ejercicio6
from Ejercicios import Ejercicio7
from Ejercicios import Ejercicio8
from Ejercicios import Ejercicio9
from Ejercicios import Ejercicio10
from Ejercicios import Ejercicio11


while True:
    if platform.system() == "Windows":
        os.system("cls")
        print("Estás en Windows")

    elif platform.system() == "Darwin" :
        os.system("clear")
        print("Estás en MacOS")

    elif platform.system() == "Linux" :
        os.system("clear")
        print("Estás en Linux")
   
    tabla = PrettyTable()
    tabla.field_names = ["#", "OPCIONES"]
    tabla.align["OPCIONES"] = "l"
    tabla.add_row([colored("1", "blue"), colored("Fecha como cadena de caracteres", "blue")])
    tabla.add_row([colored("2", "blue"), colored("Busca tu zona horaria y la hora.", "blue")])
    tabla.add_row([colored("3", "blue"), colored("Calcula el número de palabras que contiene una cadena.", "blue")])
    tabla.add_row([colored("4", "blue"), colored("Convertir la hora en 24 horas.", "blue")])
    tabla.add_row([colored("5", "blue"), colored("Invierte una cadena", "blue")])
    tabla.add_row([colored("6", "blue"), colored("Calcular del numero ingresado hasta 1.", "blue")])
    tabla.add_row([colored("7", "blue"), colored("Imprime cada caracter en una cadena separada.", "blue")])
    tabla.add_row([colored("8", "blue"), colored("Seleccionar las cadenas que tiene más de 5 caracteres.", "blue")])
    tabla.add_row([colored("9", "blue"), colored("Reemplazar palabras.", "blue")])
    tabla.add_row([colored("10", "blue"), colored("Crea una lista con cadenas que tengan vocales.", "blue")])
    tabla.add_row([colored("0", "blue"), colored("Salir", "blue")])
    print(colored(tabla.get_string(), "white"))

    opcion = input("Seleccione una opción:")
    if opcion == "1":
        Ejercicio1.principal()
    elif opcion == "2":
        Ejercicio2.principal()
    elif opcion == "3":
        Ejercicio3.principal()
    elif opcion == "4":
        Ejercicio4.principal()
    elif opcion == "5":
        Ejercicio5.principal()
    elif opcion == "6":
        Ejercicio6.principal()
    elif opcion == "7":
        Ejercicio7.principal()
    elif opcion == "8":
        Ejercicio8.principal()
    elif opcion == "9":
        Ejercicio9.principal()
    elif opcion == "10":
        Ejercicio10.principal()
    elif opcion == "11":
        Ejercicio11.principal()
    elif opcion == "0":
        break
    continuar=input("Presione la tecla enter para continuar.")