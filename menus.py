from modif_objetos import profesores,alumnos,materias,eliminar
import almacen_datos
from validacion import validar

def menu_admin():
    while True:
        while True:
            opciones = 4
            print()
            print("-" * 26)
            print("MENÚ PRINCIPAL")
            print("-" * 26)
            print("[1] Gestión de profesores")
            print("[2] Gestión de alumnos")
            print("[3] Gestión de materias")
            print("[4] Registro de cambios")
            print("-" * 26)
            print("[0] Salir del programa")
            print("-" * 26)
            print()

            opcion = input("Seleccione una opción: ")
            if opcion in [str(i) for i in range(0, opciones + 1)]:
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0":
            exit()

        elif opcion == "1":
            # Gestión de Profesores
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
                    if opcion in [str(i) for i in range(0, opciones + 1)]:
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcion == "0":
                    break

                elif opcion == "1":
                    almacen_datos.profesores.append(profesores.Carga_Profesores(almacen_datos.profesor))
                    input('Cargado! Ingrese "Enter" para volver al menú anterior')

                elif opcion == "2":
                    while True:
                        print('Busque al Profesor por su DNI: ')
                        dni = validar.valid_dni()
                        profesores.busqueda_datos_profesores(dni)
                        print('¿Este es el que desea eliminar?')
                        elec = input('(Ingrese Y o N): ').lower()
                        if elec == 'y':
                            eliminar.eliminar_diccionario_lista_alu_prof(almacen_datos.profesores, dni)
                            print('Profesor eliminado.')
                        if elec == 'n' or elec == 'y':
                            break

                elif opcion == "3":
                    while True:
                        print('Busque al Profesor por su DNI: ')
                        dni = validar.valid_dni()
                        profesores.busqueda_datos_profesores(dni)
                        print('¿Este es el que desea modificar?')
                        elec = input('(Ingrese Y o N): ').lower()
                        if elec == 'y':
                            profesores.modif_prof(dni)
                            print('Profesor modificado.')
                        if elec == 'n' or elec == 'y':
                            break

                elif opcion == "4":
                    print('Busque al Profesor por su DNI: ')
                    dni = validar.valid_dni()
                    profesores.modif_materias_prof(dni)

        elif opcion == "2":
            # Gestión de Alumnos
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > GESTION DE ALUMNOS")
                    print("---------------------------")
                    print("[1] Añadir Alumnos")
                    print("[2] Eliminar Alumno")
                    print("[3] Modificar Alumno")
                    print("[4] Ver Notas/Alumno")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()

                    opcion = input("Seleccione una opción: ")
                    if opcion in [str(i) for i in range(0, opciones + 1)]:
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcion == "0":
                    break

                elif opcion == "1":
                    nuevo_alumno = almacen_datos.alumno.copy()
                    almacen_datos.alumnos.append(alumnos.Carga_Alumnos(nuevo_alumno))
                    input('Cargado! Ingrese "Enter" para volver al menú anterior')

                elif opcion == "2":
                    print('Busque al Alumno por su DNI: ')
                    dni = validar.valid_dni()
                    alumno = alumnos.busqueda_datos_alumnos(dni)
                    if alumno is None:  # Verifica si no se encontró el alumno
                        print('No se encontró un alumno con ese DNI.')
                    else:
                        print('¿Este es el alumno que desea eliminar?')
                        elec = input('(Ingrese Y o N): ').lower()
                        if elec == 'y':
                            eliminar.eliminar_diccionario_lista_alu_prof(almacen_datos.alumnos, dni)
                            print('Alumno eliminado.')

                elif opcion == "3":
                    print("Lista actual de alumnos:", almacen_datos.alumnos)  # Depuración
                    print('Busque al Alumno por su DNI: ')
                    dni = validar.valid_dni()
                    alumno = alumnos.busqueda_datos_alumnos(dni)
                    if alumno is None:
                        print('No se encontró un alumno con ese DNI.')
                    else:
                        print('¿Este es el alumno que desea modificar?')
                        elec = input('(Ingrese Y o N): ').lower()
                        if elec == 'y':
                            alumnos.modif_alumno(dni)
                            print('Alumno modificado.')

                elif opcion == "4":
                    print('Busque al Alumno por su DNI: ')
                    dni = validar.valid_dni()
                    alumnos.ver_notas_alumno(dni)

        elif opcion == "3":
            # Gestión de Materias
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
                    if opcion in [str(i) for i in range(0, opciones + 1)]:
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcion == '0':
                    break

                elif opcion == '1':
                    almacen_datos.materias.append(materias.Carga_Materias(almacen_datos.materia))
                    input('Cargado! Ingrese "Enter" para volver al menú anterior')

                elif opcion == '2':
                    print('Busque la Materia por nombre y turno')
                    nombre, turno = materias.buscar_materia()
                    if nombre is not None:
                        print('¿Desea eliminar esta materia?')
                        elec = input('(Ingrese Y o N): ').lower()
                        if elec == 'y':
                            eliminar.eliminar_diccionario_lista_materias(nombre, turno)
                            print('Materia eliminada.')

                elif opcion == '3':
                    print('Busque la Materia por nombre y turno')
                    nombre, turno = materias.buscar_materia()
                    if nombre is not None:
                        print('¿Desea modificar esta materia?')
                        elec = input('(Ingrese Y o N): ').lower()
                        if elec == 'y':
                            materias.modif_materias(nombre, turno)
                            print('Materia modificada.')

        elif opcion == "4":
            # Registro de cambios (por ahora no implementado)
            print("Funcionalidad de registro de cambios aún no implementada.")
        
        input("\nPresione ENTER para volver al menú.")
        print("\n\n")
