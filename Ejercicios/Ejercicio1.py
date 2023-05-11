# 1. Crea un programa en Python que acepte una fecha como cadena de caracteres en formato `"dd/mm/aaaa"` y devuelva la fecha en formato 
# `"aaaa-mm-dd"`, con el año primero. 
from datetime import datetime, timedelta
def principal():
        op = "s"
        while op == "s":
                print("Programa Formato Fecha")
                date=input("Introduce la fecha con el formato dd/mm/aaaa :")
                dateobj=date
                try:
                        dateobj= datetime.strptime(dateobj, '%d/%m/%Y')
                except:
                        print("Formato de fecha introducido erroneo")
                else: 
                        
                        print(dateobj.strftime("%Y-%m-%d"))
                finally:
                        print("Fin del programa")
                choose = input("Si  quieres continuar teclea 's', sino pulse cualquier otra tecla: ")
                op = choose.lower()

if __name__ == "__main__":
    principal() 