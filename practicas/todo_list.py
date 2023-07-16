# Lista de tareas: Desarrolla un gestor de tareas simple. Permite al usuario agregar tareas, marcarlas como completadas y eliminarlas de la lista. También puedes agregar funcionalidades
# adicionales, como establecer fechas de vencimiento o prioridades para cada tarea.

import time

tareas = {}
numeros = []

try: 
    while True:
        print("\nGestor de tareas")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Eliminar tarea de la lista")
        print("4. Mostrar tareas de la lista")
        eleccion = input("Ingrese una opción: ")

        if eleccion == "1":
            print("\nIngrese una tarea")
            inp_tarea = input("Ingrese el nombre de la tarea: ")
            cont_tarea = input("Ingrese el contenido de la tarea: ")
            tareas.update({inp_tarea:cont_tarea})
            numero = len(tareas)
            numeros.append(numero)
            print("\n¡Tarea agregada con éxito!")
        if eleccion == "4":
            print("\nListado de tareas")
            for tarea in tareas:
                print(tarea + ":", tareas[tarea])
except ValueError:
    print("Error de ingreso")
except KeyboardInterrupt:
    print("\nSaliendo...")
    time.sleep(1)