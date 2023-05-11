#2. Crea un programa que le pregunte al usuario su zona horaria y le muestre la hora actual en esa zona. 

from datetime import datetime, timedelta

from pytz import timezone
import pytz
def principal():
        op = "s"
        while op == "s":
                print("Zonas Horarias Disponibles:")
                print (*pytz.all_timezones,sep='\n')
                zona=input("Introduce la zona horaria que deseas ver, con el formato Continente/Localizacion: ")
                try:
                        zonatiempo=timezone(zona)
                        
                        print(datetime.now(timezone(zona)).strftime("%H:%M"))
                except pytz.exceptions.UnknownTimeZoneError:
                        print("Debe ser una zona horaria valida")
                        
                choose = input("Si  quieres continuar teclea 's', sino pulse cualquier otra tecla: ")
                op = choose.lower()
