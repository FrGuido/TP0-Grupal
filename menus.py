import cargar_leer, almacen_datos

def menu_admin():
    while True:
        while True:
            opciones = 5
            print()
            print("-"*26)
            print("MENÚ PRINCIPAL")
            print("-"*26)
            print("[1] Gestión de profesores")
            print("[2] Gestión de alumnos")
            print("[3] Gestión de materias")
            print("[4] Registro de cambios")
            print("[5] Opción 5")
            print("-"*26)
            print("[0] Salir del programa")
            print("-"*26)
            print()
            
            opcion = input("Seleccione una opción: ")
            if opcion in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0": # Opción salir del programa
            exit() 

        elif opcion == "1":   # Opción 1
            while True:
                while True:
                    opciones = 3
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > GESTION DE PROFESORES")
                    print("---------------------------")
                    print("[1] Añadir Profesores")
                    print("[2] Eliminar Profesor")
                    print("[3] Modificar Profesor")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcion = input("Seleccione una opción: ")
                    if opcion in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcion == "0": # Opción salir del submenú
                    break # No salimos del programa, volvemos al menú anterior
                elif opcion == "1":   # Opción 1
                    almacen_datos.profesores.append(cargar_leer.Carga_Profesores(almacen_datos.profesor))

                    print("Cargando Profesor en lista...")
                    input('Cargado! Ingrese "Enter" para volver al menu anterior')
                    
                elif opcion == "2":   # Opción 2
                    ...
                elif opcion == "3":   # Opción 3
                    ...
                elif opcion == "4":   # Opción 4
                    ...

        elif opcion == "2":   # Opción 2
            ...
        elif opcion == "3":   # Opción 3
            ...
        elif opcion == "4":   # Opción 4
            ...
        elif opcion == "5":   # Opción 5
            ...

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")

