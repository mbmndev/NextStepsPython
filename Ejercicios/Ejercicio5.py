#5. Crea un programa en Python que acepte una cadena de caracteres y devuelva la cadena invertida (por ejemplo, "hola" se convertiría en "aloh"). 
def principal():
    op = "s"
    while op == "s":
        print("Programa invertir Cadena")
        cadena=input("Introduce la cadena de texto :")

        cadena_invertida= ""
        for char in  cadena:
            cadena_invertida= char + cadena_invertida;

        print(cadena_invertida)
        choose = input("Si  quieres continuar teclea 's', sino pulse cualquier otra tecla: ")
        op = choose.lower()
    