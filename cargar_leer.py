import almacen_datos
import eliminar
import validar
import pedirFecha
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
    profe['fecha_nac'] = pedirFecha.pedirFechaNac()

    print('Ingrese el dni del profesor')
    print('ejemplo --> 22334455')
    print('vvv')
    while True:
        dni = eliminar.valid_dni()
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
            return profesor['nombre'] + profesor['apellido']

def busqueda_datos_profesores(dni):
    for profesor in almacen_datos.profesores:
        if profesor['dni'] == dni:
            print(f"---- Datos Profesor del {profesor['nombre']} {profesor['apellido']} ----")
            print(f"Fecha de Nacimiento : {profesor['fecha_nac']}")
            print(f"Mail : {profesor['mail']}")
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
                    dni = eliminar.valid_dni()
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
                profesor['fecha_nac'] = pedirFecha.pedirFechaNac()
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



def Carga_Alumnos(alumno):

    print('Ingrese el nombre del alumno')
    alumno['nombre'] = (input('> ')).capitalize()
    print()

    print('Ingrese el apellido del alumno')
    alumno['apellido'] = (input('> ')).capitalize()
    print()

    print('Ingrese el dni del alumno')
    while True:
        dni = eliminar.valid_dni()
        if not any(almacen_datos.alumno['dni'] == dni for x in almacen_datos.alumnos):
            alumno['dni'] = dni
            break
        else:
            print('Ese dni ya existe en nuestra base de datos, ingrese un dni valido')
    print()

    print('Ingrese la fecha de nacimiento del alumno')
    print('vvv')

    alumno['fecha_nac'] = pedirFecha.pedirFechaNac()

    print('Ingrese el turno del alumno')
    print('vvv')
    while True:
        input('Ingrese M (para turno Mañana) o T (para turno tarde)')
        turno = input('> ').lower()
        if turno == 'm':
            alumno['turno'] = 'Mañana'
            break
        elif turno == 't':
            alumno['turno'] = 'Tarde'
            break
        else:
            print('Ingrese un valor valido, intente de nuevo')
    
    print('Ingrese el curso del alumno')
    print('vvv')
    alumno['curso'] = elegir_curso()

def busqueda_nombre_alumnos(dni):
    for alumno in almacen_datos.alumnos:
        if alumno['dni'] == dni:
            return alumno['nombre'] + alumno['apellido']

def elegir_curso():
    print(almacen_datos.nros_cursos, sep=' | ')
    curso = input('> ').lower()
    while True:
        if curso not in almacen_datos.nros_cursos:
            print('Ingrese un curso valido')
        else:
            return curso



def Carga_Materias(materia):
    while True:
        print('Ingrese el nombre de la materia:')
        materia['nombre'] = input('> ').capitalize()
        for i in almacen_datos.materias:
            if i['nombre'] == materia['nombre']:
                print(f'Esa materia ya existe, y se encuentra en el turno {i["turno"]}\nDesea continuar igualmente, debera incluirla con un turno distinto')
                t = i['turno']
        print()
        print('Ingrese el turno de esta materia (Mañana o Tarde)')
        while True:
            materia['turno'] == input('> ').capitalize()
            if materia['turno'] not in almacen_datos.turnos:
                print('Ingrese un turno valido\n')
            else:
                break
        if materia['turno'] == t:
            print('Esta materia en este turno ya existe, intente de nuevo')
        else:
            break
    print('Ingrese los dias que esta materia se va a cursar, limite 4')
    while True:
        dia = input(f'Ingrese el dia a añadir\n{almacen_datos.dias}').capitalize()
        if dia in almacen_datos.dias:
            materia['dias'].append(dia)
            while True:
                print('Desea añadir mas dias? (y o n)')
                elec = input('> ').lower()
                if elec == 'y':
                    break
                elif elec == 'n':
                    print('-'*20,'\n')
                    break
                else:
                    print('Por favor ingrese una de las dos letras indicadas')
                    elec = input('(Ingrese Y o N): ').lower()
        else:
            print('Ingrese un dia valido por favor')
            print('-'*10)
        
        if elec == 'n':
            break
    
    return materia

def buscar_materia():
    while True:
        nombre = input('Ingrese la materia\n> ').capitalize()
        turno = input('Ingrese el turno \n>').capitalize()
        for mat in almacen_datos.materias:
            if mat['nombre'] == nombre and mat['turno'] == turno:
                materia = mat
                break
            else:
                materia = None
        if materia == None:
            print(f'La materia {nombre} del turno {turno}, no existe. Desea salir o intentar nuevamente?')
            while True:
                elec = input('Ingrese "Y" para salir y "N" para intentar de nuevo').lower()
                if elec == 'y':
                    nombre,turno = None,None
                    break
                elif elec == 'n':
                    break
                else:
                    print('Ingrese un valor adecuado')
        
        if elec == 'y':
            break

    if materia != None:
        for k, valor in materia():
            print(f"{(k.capitalize()):<15}{str(valor):>30}")
        return nombre,turno
    
    return nombre,turno
    
