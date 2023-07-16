try:
    while True:
        try: 
            print("Calculadora")
            num_a = int(input("Ingrese un número: "))
            num_b = int(input("Ingrese otro número: "))

            operacion = input("Ingrese el tipo de operación que quiere realizar: ")

            if operacion == "sumar" or operacion == "+":
                resultado = num_a + num_b
                print(f"El resultado de la operación es: {resultado}")
                print("")
            elif operacion == "restar" or operacion == "-":
                resultado = num_a - num_b
                print(f"El resultado de la operación es: {resultado}")
                print("")
            elif operacion == "multiplicar" or operacion == "*":
                resultado = num_a * num_b
                print(f"El resultado de la operación es: {resultado}")
                print("")
            elif operacion == "dividir" or operacion == "/":
                resultado = num_a / num_b
                print(f"El resultado de la operación es: {resultado}")
                print("")
            else:
                print("Error en el ingreso")
                print("")
        except ValueError:
            print("Error de ingreso")
            print("")
        except ZeroDivisionError:
            print("No se puede dividir por 0")
            print("")
except KeyboardInterrupt:
    print("")