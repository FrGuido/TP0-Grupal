import almacen_datos
from modif_objetos import eliminar
from validacion import validar
import re


def Carga_Profesores(profe):

    print('Ingrese el nombre del profesor')
    print('vvv')
    profe['nombre'] = (input('> ')).capitalize()
    print()

    print('Ingrese el apellido del profesor')
    print('vvv')
    profe['apellido'] = (input('> ')).capitalize()
    print()

    print('Ingrese la fecha de nacimiento del profesor')
    print('vvv')
    profe['fecha_nac'] = validar.pedirFecha()

    print('Ingrese el dni del profesor')
    print('ejemplo --> 22334455')
    print('vvv')
    while True:
        dni = validar.valid_dni()
        if not any(almacen_datos.profesor['dni'] == dni for x in almacen_datos.profesores):
            profe['dni'] = dni
            break
        else:
            print('Ese dni ya existe en nuestra base de datos, ingrese un dni valido')
    print()

    print('Ingrese el mail del profesor')
    print('ejemplo --> nombreprofe@ejemplo.com')
    print('vvv')
    profe['mail'] = validar.valid_mail()

    print('Ingrese el telefono del profesor')
    print('ejemplo --> 1122334455')
    print('vvv')
    profe['telefono'] = validar.valid_telefono()

    print('Ingrese una contraseña para el profesor')
    print('vvv')
    profe['pasw'] = validar.valid_pasw()
    print()


    return profe

def busqueda_nombre_profesores(dni):
    for profesor in almacen_datos.profesores:
        if profesor['dni'] == dni:
            return f"{profesor['nombre']} {profesor['apellido']}"
    return None  # Devuelve None si no encuentra al profesor

def busqueda_datos_profesores(dni):
    for profesor in almacen_datos.profesores:
        if profesor['dni'] == dni:
            print(f"---- Datos Profesor del {profesor['nombre']} {profesor['apellido']} ----")
            print(f"Fecha de Nacimiento : {profesor['fecha_nac']}")
            print(f"Mail : {profesor['mail']}")
            print(f"Telefono : {profesor['telefono']}")
            listar_materias_prof(profesor['dni'])
            print('-'*20)
            break

def listar_materias_prof(dni):
    mat = buscar_materias_prof(dni)
    print('Materias:')
    for i in mat:
        print(f'> {i}')

def buscar_materias_prof(dni):
    materias = []
    for materia in almacen_datos.materias:
        for fila in almacen_datos.materia['profesores']:
            if dni in fila:
                materias.append(materia['nombre'])
                break
    return materias

def modif_prof(elemento):
    while True:
        for prof in almacen_datos.profesores:
            if prof['dni'] == elemento:
                profesor = prof

        while True:
            opciones = 7
            print(f'Que desea modificar?')
            print("[1] Nombre")
            print("[2] Apellido")
            print("[3] DNI")
            print("[4] Fecha de Nacimiento")
            print("[5] Mail")
            print("[6] Telefono")
            print("[7] Contraseña")
            print("---------------------------")
            print("[0] Salir")
            print("---------------------------")
            print()
            opcion = input("Seleccione una opción: ")
            if opcion in [str(i) for i in range(0, opciones + 1)]:
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        while True:

            if opcion == '0':
                break

            elif opcion == '1':
                print()
                print('Modificando el Nombre del profesor:')
                profesor['nombre'] = input('> ').capitalize()
                print('Nombre cambiado con exito!')
                print('-'*15)
                break

            elif opcion == '2':
                print()
                print('Modificando el Apellido del profesor:')
                profesor['apellido'] = input('> ').capitalize()
                print('Apellido cambiado con exito!')
                print('-'*15)
                break

            elif opcion == '3':
                print()
                print('Modificando el DNI del profesor:')
                while True:
                    dni = validar.valid_dni()
                    if not any(almacen_datos.profesor['dni'] == dni for x in almacen_datos.profesores):
                        profesor['dni'] = dni
                        break
                    else:
                        print('Ese dni ya existe en nuestra base de datos, ingrese un dni valido')
                        print()
                print('DNI cambiado con exito!')
                print('-'*15)
                break

            elif opcion == '4':
                print()
                print('Modificando la Fecha de Nacimiento del profesor:')
                profesor['fecha_nac'] = validar.pedirFecha()
                print('Fecha de Nacimiento cambiado con exito!')
                print('-'*15)
                break
            
            elif opcion == '5':
                print()
                print('Modificando el Mail del profesor:')
                profesor['mail'] = validar.valid_mail()
                print('Mail cambiado con exito!')
                print('-'*15)
                break

            elif opcion == '6':
                print()
                print('Modificando el Telefono del profesor:')
                profesor['telefono'] = validar.valid_telefono()
                print('Telefono cambiado con exito!')
                print('-'*15)
                break

            elif opcion == '7':
                print()
                print('Modificando la Contraseña del profesor:')
                profesor['pasw'] = validar.valid_pasw()
                print('Contraseña cambiado con exito!')
                print('-'*15)
                break
        
        if opcion == '0':
            for prof in almacen_datos.profesores:
                if prof['dni'] == elemento:
                    prof = profesor
                    break
            break

def modif_materias_prof(dni):
    mats = []
    lista = buscar_materias_prof(dni)
    if not lista:
        print('El profesor no posee materias')
    else:
        print('El profesor posee la siguientes materias:')
        print(" | ".join(map(str, lista)))
    
    print('')
    for materia in almacen_datos.materias:
        for fila in almacen_datos.materia['nombre']:
            print (materia['nombre']+ ' | ')
            mats.append(materia['nombre'])