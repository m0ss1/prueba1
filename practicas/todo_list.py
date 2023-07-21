# Lista de tareas: Desarrolla un gestor de tareas simple. Permite al usuario agregar tareas, marcarlas como completadas y eliminarlas de la lista. También puedes agregar funcionalidades
# adicionales, como establecer fechas de vencimiento o prioridades para cada tarea.

dicc = {}
resultado = {}
numeros = []

try:
    while True:
        print("Gestor de tareas")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Eliminar tarea de la lista")
        print("4. Mostrar tareas de la lista")
        eleccion = input("Ingrese una opción: ")

        if eleccion == "1":
            print("\nIngrese una tarea")
            inp_tarea = input("Ingrese el nombre de la tarea: ")
            inp_cont = input("Ingrese el contenido de la tarea: ")
            dicc.update({inp_tarea:inp_cont})
            for n, keys, values in zip(range(1, len(dicc) + 1), dicc.keys(), dicc.values()):
                resultado.update({str(n):{keys:values}})
            print(resultado)
            print("\n¡Tarea agregada con éxito!\n")
                
        if eleccion == "2":
            for var in dicc.values():
                dicc1 = var
            for num, tarea, cont in zip(dicc.keys(), dicc1.keys(), dicc1.values()):
                print(num + ".", "Tarea:", tarea, "contenido:", cont)
            for num in dicc:
                        eleccion = input("Ingrese el numero de tarea a remover: ")
                        elim = dicc.pop(eleccion)
                        print(dicc)
                        print(elim)
                        
        if eleccion == "3":
            print("Listado de tareas")
            for n, keys, values in zip(range(1, len(dicc) + 1), dicc.keys(), dicc.values()):
                print(str(n) + ".", "Tarea:", keys, "Contenido:", values)
                elim_inp = input("Seleccione por su número la tarea a eliminar: ")
                print("Se ha eliminado: " + elim_inp + ".", "Tarea:", keys, "Contenido:", values)
                elim = resultado.pop(elim_inp)
            print(resultado)
            print("")
        if eleccion == "4":
            print("Listado de tareas")
            for n, keys, values in zip(range(1, len(dicc) + 1), dicc.keys(), dicc.values()):
                print(str(n) + ".", "Tarea:", keys, "Contenido:", values)
                print("")
except ValueError: 
     print("hola")
