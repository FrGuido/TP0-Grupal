import almacen_datos
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
    while True:
        dni = valid_dni()
        if not any(almacen_datos.profesor['dni'] == dni for x in almacen_datos.profesores):
            profe['dni'] = dni
            break
        else:
            print('Ese dni ya existe en nuestra base de datos, ingrese un dni valido')
    print()

    print('Ingrese el mail del profesor')
    profe['mail'] = valid_mail()

    print('Ingrese una contraseña para el profesor')
    print('vvv')
    profe['pasw'] = valid_pasw()
    print()


    return profe

def Carga_Alumnos(alumno):

    print('Ingrese el nombre del alumno')
    alumno['nombre'] = (input('> ')).capitalize()
    print()

    print('Ingrese el apellido del alumno')
    alumno['apellido'] = (input('> ')).capitalize()
    print()

    print('Ingrese el dni del alumno')
    while True:
        dni = valid_dni()
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

    


def valid_dni():
    while True:
        dni = (input('> '))
        if len(dni) == 8 and dni.isdigit():
            return int(dni)
        else:
            print('Ingreso un DNI invalido, intente nuevamente')

def busqueda_nombre_alumnos(dni):
    for alumno in almacen_datos.alumnos:
        if alumno['dni'] == dni:
            return alumno['nombre'] + alumno['apellido']

def busqueda_nombre_profesores(dni):
    for profesor in almacen_datos.profesores:
        if profesor['dni'] == dni:
            return profesor['nombre'] + profesor['apellido']

def busqueda_datos_profesores(dni):
    for profesor in almacen_datos.profesores:
        if profesor['dni'] == dni:
            print(f'---- Datos Profesor del {profesor['nombre']} {profesor['apellido']} ----')
            print(f'Fecha de Nacimiento : {profesor['fecha_nac']}')
            print(f'Mail : {profesor['mail']}')
            listar_materias_prof(profesor['dni'])
            print('-'*20)
            break

def eliminar_diccionario_lista(dic,elemento):
    return list(filter(lambda x: x.get('dni') != elemento, dic))

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

def valid_mail():
    while True:
        validez = r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑüÜ\.-]+@[a-zA-Z0-9\.-]+\.\w{2,4}$'
        mail = input("> ")
        if re.match(validez, mail) is not None:
            return mail
        else:
            print("Formato inválido. Intente nuevamente.\n")

def valid_pasw():
    print('La contraseña debe tener al menos un carcter en mayuscula,\nun numero, un simbolo y al menos 10 caracteres')
    while True:
        contra = input('> ')
        if len(contra) < 10 or not re.search(r'[A-Z]',contra) or not re.search(r'\d', contra) or not re.search(r'\d', contra):
            print('Contraseña no valida, intente de nuevo')
        else:
            print('Contraseña valida')
            return contra

def elegir_curso():
    print(almacen_datos.cursos, sep=' | ')
    curso = input('> ').lower()
    while True:
        if curso not in almacen_datos.cursos:
            print('Ingrese un curso valido')
        else:
            return curso