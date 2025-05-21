import almacen_datos
from modif_objetos import eliminar
from validacion import validar
import re


# Carga de datos dentro del diccionario alumno

def Carga_Alumnos(alumno):

    #nombre
    print('Ingrese el nombre del alumno')
    alumno['nombre'] = (input('> ')).capitalize()
    print()

    #apellido
    print('Ingrese el apellido del alumno')
    alumno['apellido'] = (input('> ')).capitalize()
    print()

    #dni
    print('Ingrese el dni del alumno')
    while True:
        dni = validar.valid_dni()
        if not any(a['dni'] == dni for a in almacen_datos.alumnos): #ANY A CAMBIAR / ERROR TYPEERROR 'NONE TYPE'
            alumno['dni'] = dni
            break
        else:
            print('Ese dni ya existe en nuestra base de datos, ingrese un dni valido')
    print()

    #fecha naciemiento
    print('Ingrese la fecha de nacimiento del alumno')
    alumno['fecha_nac'] = validar.pedirFecha()

    #turno (mañana o tarde)
    print('Ingrese el turno del alumno')
    while True:
        turno = input('Ingrese M (para turno Mañana) o T (para turno Tarde): ').lower()
        if turno == 'm':
            alumno['turno'] = 'Mañana'
            break
        elif turno == 't':
            alumno['turno'] = 'Tarde'
            break
        else:
            print('Ingrese un valor valido, intente de nuevo')
    
    #curso
    print('Ingrese el curso del alumno')
    alumno['curso'] = elegir_curso()

    # Añadir el alumno a la lista
    almacen_datos.alumnos.append(alumno)
    print("Alumno añadido con éxito.")
    print("\nLista actual de alumnos:")
    for a in almacen_datos.alumnos:
        print("-" * 60)
        print(f"DNI: {alumno['dni']}")
        print(f"Nombre: {alumno['nombre']} {alumno['apellido']}")
        print(f"Fecha de nacimiento: {alumno['fecha_nac']}")
        print(f"Curso: {alumno['curso']}")
        print(f"Turno: {alumno['turno']}")
        print(f"Notas: {alumno['notas']}")
    print("-" * 60)

def busqueda_nombre_alumnos(dni):
    for alumno in almacen_datos.alumnos:
        if alumno['dni'] == dni:
            return f"{alumno['nombre']} {alumno['apellido']}"
    return None  # Devuelve None si no encuentra al alumno

def busqueda_datos_alumnos(dni):
    print("Buscando DNI:", dni)
    for alumno in almacen_datos.alumnos:
        print("Revisando alumno:", alumno)  # Depuración
        if isinstance(alumno, dict) and 'dni' in alumno:
            if alumno['dni'] == dni:
                print(f"---- Datos del Alumno {alumno['nombre']} {alumno['apellido']} ----")
                print(f"DNI: {alumno['dni']}")
                print(f"Fecha de Nacimiento: {alumno['fecha_nac']}")
                print(f"Curso: {alumno['curso']}")
                print(f"Turno: {alumno['turno']}")
                print('-'*20)
                return alumno
    print("Alumno no encontrado.")
    return None  # Devuelve None si no encuentra al alumno

def modif_alumno(dni):
    alumno = next((a for a in almacen_datos.alumnos if a['dni'] == dni), None)
    if not alumno:
        print("Alumno no encontrado.")
        return

    while True:
        print("\n¿Qué desea modificar?")
        print("[1] Nombre")
        print("[2] Apellido")
        print("[3] DNI")
        print("[4] Fecha de Nacimiento")
        print("[5] Turno")
        print("[6] Curso")
        print("[7] Contraseña")
        print("[0] Volver")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '0':
            break
            
        elif opcion == '1':
            print("Nombre actual:", alumno['nombre'])
            alumno['nombre'] = input("Nuevo nombre: ").capitalize()
            print("Nombre modificado con éxito.")
            
        elif opcion == '2':
            print("Apellido actual:", alumno['apellido'])
            alumno['apellido'] = input("Nuevo apellido: ").capitalize()
            print("Apellido modificado con éxito.")
            
        elif opcion == '3':
            print("DNI actual:", alumno['dni'])
            while True:
                nuevo_dni = validar.valid_dni()
                if not any(a['dni'] == nuevo_dni for a in almacen_datos.alumnos if a['dni'] != dni): #ANY A CAMBIAR
                    alumno['dni'] = nuevo_dni
                    print("DNI modificado con éxito.")
                    break
                else:
                    print("Este DNI ya está en uso. Intente con otro.")
                    
        elif opcion == '4':
            print("Fecha de nacimiento actual:", alumno['fecha_nac'])
            print("Ingrese la nueva fecha de nacimiento:")
            alumno['fecha_nac'] = validar.pedirFecha()
            print("Fecha de nacimiento modificada con éxito.")
            
        elif opcion == '5':
            print("Turno actual:", alumno['turno'])
            while True:
                nuevo_turno = input("Ingrese nuevo turno (Mañana/Tarde): ").capitalize()
                if nuevo_turno in almacen_datos.turnos:
                    alumno['turno'] = nuevo_turno
                    print("Turno modificado con éxito.")
                    break
                else:
                    print("Turno inválido. Intente nuevamente.")
                    
        elif opcion == '6':
            print("Curso actual:", alumno['curso'])
            print("Seleccione nuevo curso:")
            alumno['curso'] = elegir_curso()
            print("Curso modificado con éxito.")
            
        elif opcion == '7':
            print("Ingrese nueva contraseña:")
            alumno['pasw'] = validar.valid_pasw()
            print("Contraseña modificada con éxito.")
            
        else:
            print("Opción inválida.")

def ver_notas_alumno(dni):
    alumno = next((a for a in almacen_datos.alumnos if a['dni'] == dni), None) #NEXT A CAMBIAR
    if not alumno:
        print("Alumno no encontrado.")
        return
    
    print(f"\nNotas de {alumno['nombre']} {alumno['apellido']}:")
    if not alumno['notas']:
        print("El alumno no tiene notas cargadas.")
    else:
        for nota in alumno['notas']:
            print(f"Materia: {nota[1]} - Nota: {nota[3]} - Fecha: {nota[4]}")

def elegir_curso():
    print(almacen_datos.nros_cursos, sep=' | ') #FROMA DE ELECCION DE CURSO A CAMBIAR
    curso = input('> ').lower()
    while True:
        if curso not in almacen_datos.nros_cursos:
            print('Ingrese un curso valido')
        else:
            return curso

