import cargar_leer
import almacen_datos
import eliminar
import validar

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
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > GESTION DE PROFESORES")
                    print("---------------------------")
                    print("[1] Añadir Profesores")
                    print("[2] Eliminar Profesor")
                    print("[3] Modificar Profesor")
                    print("[4] Modificar Materias Profesor")
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
                    while True:
                        print('Busque al Profesor por su DNI: ')
                        dni = validar.valid_dni()
                        cargar_leer.busqueda_datos_profesores(dni)
                        print('Este es el que deseea eliminar?')
                        elec = input('(Ingrese Y o N): ').lower()
                        while True:
                            if elec == 'y':
                                almacen_datos.profesores = eliminar.eliminar_diccionario_lista_alu_prof(almacen_datos.profesores,dni)
                                break
                            elif elec == 'n':
                                print('-'*20,'\n')
                                break
                            else:
                                print('Por favor ingrese una de las dos letras indicadas')
                                elec = input('(Ingrese Y o N): ').lower()
                        if elec == 'y':
                            print('Desea eliminar otro?')
                            elec = input('(Ingrese Y o N): ').lower()
                            if elec == 'n':
                                break
                        
                elif opcion == "3":   # Opción 3
                    while True:
                        print('Busque al Profesor por su DNI: ')
                        dni = validar.valid_dni()
                        cargar_leer.busqueda_datos_profesores(dni)
                        print('Este es el que deseea modificar?')
                        elec = input('(Ingrese Y o N): ').lower()
                        while True:
                            if elec == 'y':
                                cargar_leer.modif_prof(dni)
                                break
                            elif elec == 'n':
                                print('-'*20,'\n')
                                break
                            else:
                                print('Por favor ingrese una de las dos letras indicadas')
                                elec = input('(Ingrese Y o N): ').lower()
                        if elec == 'y':
                            print('Desea modificar otro?')
                            elec = input('(Ingrese Y o N): ').lower()
                            if elec == 'n':
                                break

                elif opcion == "4":   # Opción 4
                    pass

        elif opcion == "2":   # Opción 2
            ...
        elif opcion == "3":   # Opción 3
            while True:
                while True:
                    opciones = 3
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > GESTION DE MATERIAS")
                    print("---------------------------")
                    print("[1] Añadir Materias")
                    print("[2] Eliminar Materias")
                    print("[3] Modificar Materias")
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

                if opcion == '0':
                    break
                
                elif opcion == '1':
                    almacen_datos.materias.append(cargar_leer.Carga_Materias(almacen_datos.materia))
    
                    print("Cargando Materia en lista...")
                    input('Cargado! Ingrese "Enter" para volver al menu anterior')
                
                elif opcion == '2':
                    while True:
                        print('Busque la Materia por nombre y turno')
                        nombre,turno = cargar_leer.buscar_materia()
                        if nombre != None:
                            print('Este es el que deseea eliminar?')
                            elec = input('(Ingrese Y o N): ').lower()
                            while True:
                                if elec == 'y':
                                    eliminar.eliminar_diccionario_lista_alu_prof(nombre,turno)
                                    break
                                elif elec == 'n':
                                    print('-'*20,'\n')
                                    break
                                else:
                                    print('Por favor ingrese una de las dos letras indicadas')
                                    elec = input('(Ingrese Y o N): ').lower()
                            if elec == 'y':
                                print('Desea eliminar otro?')
                                elec = input('(Ingrese Y o N): ').lower()
                                if elec == 'n':
                                    break
                        else:
                            break
                
                elif opcion == '3':
                    while True:
                        print('Busque la Materia por nombre y turno')
                        nombre,turno = cargar_leer.buscar_materia()
                        if nombre != None:
                            print('Este es el que deseea modificar?')
                            elec = input('(Ingrese Y o N): ').lower()
                            while True:
                                if elec == 'y':
                                    eliminar.eliminar_diccionario_lista_alu_prof(nombre,turno)
                                    break
                                elif elec == 'n':
                                    print('-'*20,'\n')
                                    break
                                else:
                                    print('Por favor ingrese una de las dos letras indicadas')
                                    elec = input('(Ingrese Y o N): ').lower()
                            if elec == 'y':
                                print('Desea eliminar otro?')
                                elec = input('(Ingrese Y o N): ').lower()
                                if elec == 'n':
                                    break
                        else:
                            break

        elif opcion == "4":   # Opción 4
            ...
        elif opcion == "5":   # Opción 5
            ...

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")

