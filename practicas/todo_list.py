# Lista de tareas: Desarrolla un gestor de tareas simple. Permite al usuario agregar tareas, marcarlas como completadas y eliminarlas de la lista. También puedes agregar funcionalidades
# adicionales, como establecer fechas de vencimiento o prioridades para cada tarea.

from datetime import datetime, date, time, timedelta

dicc = {}
resultado = {}
completadas = {}
vencimiento = {}

def agregar_tarea(tarea, contenido):
    dicc.update({inp_tarea:inp_cont})
    return tarea, contenido

def mostrar_tareas(diccionario):
    diccionario = dict(diccionario)
    for keys, values, num in zip(diccionario.keys(), diccionario.values(), range(1, len(diccionario) + 1)):
        print(str(num) + ".", "Nombre tarea:", keys, "Contenido tarea:", values)

def marcar_completadas():
    eleccion = []
    eleccion.append(eleccion1)
    for nombre, keys, value in zip(eleccion, dicc.keys(), dicc.values()):
        completadas.update({keys:value})
        dicc.pop(nombre)
        print("\nSe ha marcardo como completada:", "Tarea: ", keys, "Contenido: ", value)

# def establecer_fecha():


try:
    while True:
        print("\nGestor de tareas")
        print("1. Agregar tarea")
        print("2. Marcar como completada/Mostrar tarea")
        print("3. Establecer fecha de vencimiento para una tarea")
        print("4. Salir")
        eleccion = input("Ingrese una opción: ")

        if eleccion == "1":
            print("\nIngrese una tarea")
            inp_tarea = input("Ingrese el nombre de la tarea: ")
            inp_cont = input("Ingrese el contenido de la tarea: ")
            tarea = agregar_tarea(inp_tarea, inp_cont)
            print("\n¡Tarea agregada con éxito!")
                
        if eleccion == "2":
            if len(completadas) == 0:
                print("\nListado de tareas completadas: ")
                print("No hay tareas completadas")
            if len(completadas) > 0:
                print("Tareas completadas: ")
                mostrar_tareas(completadas)
                print("")

            print("Listado de tareas: ")
            if len(dicc) == 0:
                print("\nNo hay tareas completadas")
            if len(dicc) > 0:
                mostrar_tareas(dicc)
                print("\nOpciones:")
                print("1. Marcar tarea como completada")
                print("2. Volver al menú principal")
                opcion = input("Ingrese una opción: ")
                if opcion == "1":
                    eleccion1 = input("Seleccione por su nombre, la tarea a completar: ")
                    marcar_completadas()
                elif opcion == "2":
                    continue

        if eleccion == "3":
            print("\nListado de tareas con vencimiento:")
            if len(vencimiento) == 0:
                print("No hay tareas por vencer")
            if len(vencimiento) > 0:
                for keys, values, num in zip(vencimiento.keys(), vencimiento.values(), range(1, len(vencimiento) + 1)):
                    print(str(num) + ".", "Nombre tarea:", keys, "Vence en:", values)
            print("\nListado de tareas:")
            if len(dicc) == 0:
                print("No hay tareas creadas")
            if len(dicc) > 0:
                mostrar_tareas(dicc)
                print("\nOpciones:")
                print("1. Asignar vencimiento a una tarea")
                print("2. Volver al menú principal")
                opcion = input("Ingrese una opción: ")
                if opcion == "1":
                    eleccion1 = input("\nSeleccione por su nombre, la tarea a establecer una fecha de vencimiento: ")
                    eleccion = []
                    eleccion.append(eleccion1)
                    for key, value in zip(eleccion, dicc.values()):
                        print("Seleccione la fecha y hora límite para completar la tarea: ")
                        dia = int(input("Día: "))
                        mes = int(input("Mes: "))
                        año = int(input("Año: "))
                        inp_fecha = datetime(año, mes, dia)
                        fecha_actual = datetime.today()
                        tiempo_restante = inp_fecha - fecha_actual
                        tiempo_restante = list([str(tiempo_restante)])
                        for key, tiempo in zip(eleccion, tiempo_restante):
                            vencimiento.update({key:tiempo})
                            print()
                        print(vencimiento)
                elif opcion == "2":
                    continue
                    # for vencim in vencimiento:
                    #     vencimiento.update()

        for nombre, keys, value in zip(eleccion, dicc.keys(), dicc.values()):
            completadas.update({keys:value})
                        
        if eleccion == "4":
            print("Saliendo...")
            break

except KeyboardInterrupt:
     print("\nSaliendo...")
