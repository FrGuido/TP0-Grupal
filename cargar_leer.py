import almacen_datos

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

    while True:
        año = int(input('Ingrese el año\n> '))
        if año < 1920 or año > 2010:
            print('Ingrese un año de nacimiento valido')
        else:
            break
    while True:
        mes = int(input('Ingrese el mes\n> '))
        if mes < 1 or mes > 12:
            print('Ingrese un mes de nacimiento valido')
        else:
            break
    while True:
        dia = int(input('Ingrese el dia\n> '))
        if dia < 1 or dia > 31:
            print('Ingrese un dia de nacimiento valido')
        else:
            break
    profe['fecha_nac'] = (f'{año}/{mes}/{dia}')

    print('Ingrese el dni del profesor')
    while True:
        dni = (input('> ')).strip()
        if len(dni) == 8 and dni.isdigit() and not any(x['dni'] == dni for x in almacen_datos.profesores):
            profe['dni'] = int(dni)
            break
        else:
            print('Ingreso un DNI invalido, intente nuevamente')     
    print()

    print('Ingrese una contraseña para el profesor')
    print('vvv')
    profe['pasw'] = (input('> '))
    print()

    return profe

def Carga_Alumnos(alumno):

    print('Ingrese el nombre del alumno')
    alumno['nombre'] = (input('> '))
    print()

    print('Ingrese el apellido del alumno')
    alumno['apellido'] = (input('> '))
    print()

    print('Ingrese el dni del alumno')
    while True:
        alumno['dni'] = (input('> '))
        if len(alumno['dni']) == 8 and alumno['dni'].isdigit():
            break
        else:
            print('Ingreso un DNI invalido, intente nuevamente')
    print()

    print('Ingrese la fecha de nacimiento del alumno')
    print('vvv')

    while True:
        año = int(input('Ingrese el año\n> '))
        if año < 1920 or año > 2010:
            print('Ingrese un año de nacimiento valido')
        else:
            break
    while True:
        mes = int(input('Ingrese el mes\n> '))
        if mes < 1 or mes > 12:
            print('Ingrese un mes de nacimiento valido')
        else:
            break
    while True:
        dia = int(input('Ingrese el dia\n> '))
        if dia < 1 or dia > 31:
            print('Ingrese un dia de nacimiento valido')
        else:
            break
    alumno['fecha_nac'] = (f'{año}/{mes}/{dia}')


def cargar_en_lista(elemento,lista):
    almacen_datos.lista.append(elemento)

def busqueda_nombre_alumnos(dni):
    for alumno in almacen_datos.alumnos:
        if alumno['dni'] == dni:
            return alumno['nombre'] + alumno['apellido']
            break

def busqueda_nombre_profesores(dni):
    for profesor in almacen_datos.profesores:
        if profesor['dni'] == dni:
            return profesor['nombre'] + profesor['apellido']
            break            

