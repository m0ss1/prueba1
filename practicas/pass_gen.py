# Generador de contraseñas: Crea un programa que genere contraseñas aleatorias.
# Permite al usuario especificar la longitud de la contraseña y los tipos de
# caracteres que desea incluir (letras mayúsculas, minúsculas, números 
# y símbolos).

import random
import math
import time

lista = []
list = []
contraseña = []
eleccion = []
abeced_min = ["a", "b", "c", "d", "e", "f", "g", "h"]
abeced_may = ["A", "B", "C", "D", "E", "F", "G", "H"]
numeros = ["1", "2", "3", "4", "5", "6", "7", "8"]
simbolos = ["+", "×", "÷", "=", "/", "_", "<", ">"]
try: 
    while True:
        try:
            print("\nGenerador de contraseña")
            longitud = int(input("Ingrese la longitud de la contraseña: "))
            while longitud < 6:
                print("\nError: la longitud debe ser mayor o igual a 6\n")
                longitud = int(input("Ingrese nuevamente la longitud de la contraseña: "))
            print("")
            print('Seleccione por su numero, los caracteres que desea incluir separados por una coma (,): ')
            print("1. Minusculas")
            print("2. Mayusculas")
            print("3. Numeros")
            print("4. Simbolos")
            print('Ej. "1, 2, 3"')
            eleccion = input("Caracteres a incluir: ")
            # eleccion = input("Ingrese nuevamente la cantidad de caracteres: ")
            eleccion_num = eleccion.split(", ")

        #Agrupar en un diccionario el numero y caracter
            dicc = {}
            for elemento in eleccion_num:
                if elemento == "1":
                    dicc.update({"1": abeced_min})
                elif elemento == "2":
                    dicc.update({"2": abeced_may})
                elif elemento == "3":
                    dicc.update({"3": numeros})
                elif elemento == "4":
                    dicc.update({"4": simbolos})

        # Definir el largo del diccionario
            len_dicc = len(dicc)
        # Definir el modulo de la longitud por el largo dicc
            modulo = longitud % len_dicc
        # Dividir la longitud por el largo del diccionario
            division = longitud / len_dicc
            division_int = int(division)
            contraseña1 = []
            if modulo == 0:
                list.extend(random.sample(dicc[elemento], modulo))
                for elemento in dicc:
                    list.extend(random.sample(dicc[elemento], division_int))
                    random.shuffle(list)
                for elemento in list:
                    contraseña1.append(elemento)
                    contraseña = ''.join(contraseña1)
                print("\nSu contraseña es:", contraseña)
            elif modulo == 1:
                list.extend(random.sample(dicc[elemento], modulo))
                for elemento in dicc:
                    list.extend(random.sample(dicc[elemento], division_int))
                    random.shuffle(list)
                for elemento in list:
                    contraseña1.append(elemento)
                    contraseña = ''.join(contraseña1)
                print("\nSu contraseña es:", contraseña)
            elif modulo == 2:
                list.extend(random.sample(dicc[elemento], modulo))
                for elemento in dicc:
                    list.extend(random.sample(dicc[elemento], division_int))
                    random.shuffle(list)
                for elemento in list:
                    contraseña1.append(elemento)
                    contraseña = ''.join(contraseña1)
                print("\nSu contraseña es:", contraseña)
            elif modulo == 3:
                list.extend(random.sample(dicc[elemento], modulo))
                for elemento in dicc:
                    list.extend(random.sample(dicc[elemento], division_int))
                    random.shuffle(list)
                for elemento in list:
                    contraseña1.append(elemento)
                    contraseña = ''.join(contraseña1)
                print("\nSu contraseña es:", contraseña)
        except ValueError:
            print("\nIngrese un caracter válido")
        except ZeroDivisionError:
            print("\nError de ingreso")
except KeyboardInterrupt:
        print("\nSaliendo...")
        time.sleep(1)