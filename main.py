tareas = []

while True:
    opcion = input("1. Crear --- 2. Filtrar --- 3. Salir")

    if opcion == "1":
        titulo = input("Titulo: ")
        descripcion = input("Descripcion: ")
        estadotarea = input("Ingrese el estado de la tarea (si/no): ").lower()

        completada = False

        if estadotarea == "si":
            completada = True

        tarea = {
            "titulo": titulo,
            "descripcion": descripcion,
            "completada": completada
        }

        tareas.append(tarea)

        print("Tarea guardada")

    elif opcion == "2":
        filtro = input("completadas / no completadas: ")

        for tarea in tareas:
            if filtro == "completadas" and tarea["completada"] == True:
                print(tarea)

            if filtro == "no completadas" and tarea["completada"] == False:
                print(tarea)

    elif opcion == "3":
        print("Fin")
        break

    else:
        print("Opcion invalida")
