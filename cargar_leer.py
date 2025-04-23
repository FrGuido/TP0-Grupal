

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
        if año < 1920 and año > 2010:
            print('Ingrese un año de nacimiento valido')
        else:
            break
    while True:
        mes = int(input('Ingrese el mes\n> '))
        if mes < 1 and mes > 12:
            print('Ingrese un mes de nacimiento valido')
        else:
            break
    while True:
        dia = int(input('Ingrese el dia\n> '))
        if dia < 1 and dia > 31:
            print('Ingrese un dia de nacimiento valido')
        else:
            break
    profe['fecha_nac'] = (f'{año}/{mes}/{dia}')

    print('Ingrese el dni del profesor')
    while True:
        profe['dni'] = (input('> '))
        if len(profe['dni']) == 8 and profe['dni'].isdigit():
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