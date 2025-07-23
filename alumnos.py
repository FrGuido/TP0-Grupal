import menu_texto
import validar
import registro

import cursos
import materias

import json

notas = "notas.csv"


def cargar_esqueleto():
    alu = {}
    print("\n" + "=" * 50)
    print(f"{"» Introduzca su nombre «".center(50)}")
    print("-" * 50)
    alu['nombre'] = validar.valid_nombre()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca su apellido «".center(50)}")
    print("-" * 50)
    alu['apellido'] = validar.valid_nombre()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca su fecha de nacimiento «".center(50)}")
    print("-" * 50)
    alu['fecha_nacimiento'] = validar.valid_fecha()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca su DNI «".center(50)}")
    print("-" * 50)
    alu['dni'] = validar.valid_dni_inalu()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca un Telefono «".center(50)}")
    print(f"{"para la comunicacion con los padres".center(50)}")
    print("-" * 50)
    alu['telefono'] = validar.valid_telefono()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca su Contraseña «".center(50)}")
    print("-" * 50)
    alu['pasw'] = validar.valid_pasw()

    return alu

def añadir_alumno():
    if validar.valid_archivo(cursos.archivo):
        with open(cursos.archivo, "r", encoding="UTF-8") as j:
            datos = json.load(j)
        for i in datos:
            if len(i['alumnos']) <= i['max alumnos']:
                print("\n" + "=" * 50)
                print(f"{"» Introduzca el curso donde desea añadir «".center(50)}")
                print("-" * 50)
                curso = menu_texto.seleccion_curso()
                turno = menu_texto.seleccion_turno()
                for i in datos:
                    if curso == i['nombre'] and turno == i['turno']:
                        alumno = cargar_esqueleto()
                        i['alumnos'].append(alumno)
                        registro.registrar_agregado("Alumno", alumno['nombre'], alumno['apellido'], alumno['dni'])
                        validar.cargar_archivo_json(cursos.archivo,datos)
                        print('='*50)
                        input('Se ha ingresado correctamente al alumno\nPresione Enter para continuar')
                        return
                # Si no se encontró el curso, no hace nada
                return
            else:
                print('Se ha alcanzado el tope de alumnos establecidos')
                print('Elimine algun alumno o cambie el limite')
                input('Ingrese Enter para continuar')
                return
    else:
        menu_texto.error_archivo()

def buscar_alumno(dni):
    with open(cursos.archivo,'r',encoding="UTF-8") as j:
        datos = json.load(j)
        for i in datos:
            for j in i['alumnos']:
                if j['dni'] == dni:
                    return j
        else:
            print('No se encontro al alumno de ese DNI\n')
            return None

def modificar_alumno():
    if not validar.valid_archivo(cursos.archivo):
        menu_texto.error_archivo()
        return
    while True:
        print('Ingrese el dni del alumno que desea modificar')
        dni = validar.valid_formato_dni()
        alu = buscar_alumno(dni)
        if alu is None:
            print('Desea intentarlo de nuevo?')
            vl = menu_texto.confirmacion_user()
            if vl == 'n':
                return
        else:
            break
    print('Este es el alumno que esta editando\n')
    menu_texto.imprimir_dic(alu)
    input('Ingrese enter para continuar')
    with open(cursos.archivo,'r',encoding="UTF-8") as j:
        datos = json.load(j)
    for i in datos:
        for j in i['alumnos']:
            if j['dni'] == dni:
                opcion = menu_texto.opcion_modificar_alumno()
                while opcion != '0':
                    if opcion == '1':
                        print("\n" + "=" * 50)
                        print(f'{"~ Modificando nombre ~".center(50)}')
                        print(f"{"» Introduzca su nuevo nombre «".center(50)}")
                        print("-" * 50)
                        j['nombre'] = validar.valid_nombre()
                    elif opcion == '2':
                        print("\n" + "=" * 50)
                        print(f'{"~ Modificando apellido ~".center(50)}')
                        print(f"{"» Introduzca su nuevo apellido «".center(50)}")
                        print("-" * 50)
                        j['apellido'] = validar.valid_nombre()
                    elif opcion == '3':
                        print("\n" + "=" * 50)
                        print(f'{"~ Modificando fecha de nacimiento ~".center(50)}')
                        print(f"{"» Introduzca su nueva fecha «".center(50)}")
                        print("-" * 50)
                        j['fecha_nacimiento'] = validar.valid_fecha()
                    elif opcion == '4':
                        print("\n" + "=" * 50)
                        print(f'{"~ Modificando DNI ~".center(50)}')
                        print(f"{"» Introduzca su DNI «".center(50)}")
                        print("-" * 50)
                        j['dni'] = validar.valid_dni_inalu()
                    elif opcion == '5':
                        print("\n" + "=" * 50)
                        print(f'{"~ Modificando Email ~".center(50)}')
                        print(f"{"» Introduzca su nuevo Email «".center(50)}")
                        print("-" * 50)
                        j['mail'] = validar.valid_mail()
                    elif opcion == '6':
                        print("\n" + "=" * 50)
                        print(f'{"~ Modificando telefono ~".center(50)}')
                        print(f"{"» Introduzca su nuevo Telefono «".center(50)}")
                        print("-" * 50)
                        j['telefono'] = validar.valid_telefono()
                    elif opcion == '7':
                        print("\n" + "=" * 50)
                        print(f'{"~ Modificando Contraseña ~".center(50)}')
                        print(f"{"» Introduzca su nueva Contraseña «".center(50)}")
                        print("-" * 50)
                        j['pasw'] = validar.valid_pasw()
                    opcion = menu_texto.opcion_modificar_alumno()
                registro.registrar_modificado("Alumno", j['nombre'],j['apellido'],j['dni'])
                break
    validar.cargar_archivo_json(cursos.archivo,datos)
    input('Volviendo al menu inicial, precione enter')

def eliminar_alumno():
    if not validar.valid_archivo(cursos.archivo):
        menu_texto.error_archivo()
        return
    try:
        dni = int(input('Ingrese el DNI del alumno a eliminar\n>> '))
        with open(cursos.archivo,'r',encoding="UTF-8") as j:
            datos = json.load(j)
        print('ESTA POR ELIMINAR EL ALUMNO')
        for i in datos:
            for j in i['alumnos']:
                if j['dni'] == dni:
                    print(f'DEL CURSO {i["nombre"]}')
                    print('='*10)
                    menu_texto.imprimir_dic(j)
                    print('\nSeguro que desea eliminar este elemento?\n')
                    seg = menu_texto.confirmacion_user()
                    if seg == 's':
                        registro.registrar_eliminado("Alumno", j['nombre'],j['apellido'],j['dni'])
                        i['alumnos'] = list(filter(lambda x: x['dni'] != dni, i['alumnos']))
                        validar.cargar_archivo_json(cursos.archivo,datos)
                        print('='*50)
                        input('Se ha eliminado correctamente al alumno\nPresione Enter para continuar')
                        return
                    else:
                        input('Volviendo al menu inicial, precione enter')
                        return
    except:
        print('Ingrese numeros\n--------------')

def modificar_notas(profe = None):
    if validar.valid_archivo(cursos.archivo):
        while True:
            print('Ingrese el dni del alumno el cual quiere modificar sus notas')
            dni = validar.valid_formato_dni()
            alu = buscar_alumno(dni)
            if alu == None:
                print('Desea intentarlo de nuevo?')
                vl = menu_texto.confirmacion_user()
                if vl == 'n':
                    return
            else:
                break
            
        print('Este es el alumno del que esta editando/viendo sus notas\n')
        menu_texto.imprimir_dic(alu)
        input('Ingrese enter para continuar')
        opcion = menu_texto.eleccion_notas()
        if opcion == '0':
            return
        elif opcion == '1':
            menu_texto.añadir_nota(alu,profe)
        elif opcion == '2':
            menu_texto.editar_nota(alu,profe)
    else:
        menu_texto.error_archivo()
    input('Volviendo al menu inicial, presione enter')


def listar_alumnos():
    paso = False
    curso,turno = cursos.buscar_curso()
    with open(cursos.archivo,'r',encoding="UTF-8") as j:
        datos = json.load(j)
    for i in datos:
        if i['nombre'] == curso and i['turno'] == turno:
            paso = True
            for j in i['alumnos']:
                menu_texto.imprimir_dic(j)
            break
    if not paso:
        print(f'No hay alumnos en el curso {curso} del turno {turno}')

def pedir_nota():
    print('Ingrese la nota (Entre 0 y 10)\n ~ si ingresa con decimales que sea con . y no con , ~')
    while True:
        try:
            nota = float(input('>>'))
            if 0 <= nota <= 10:
                return round(nota,2)
            else:
                print('Ingrese un valor en el rango e intente nuevamente')
        except:
            print('Ingrese valores numericos y los decimales con .')


def pedir_instancia():
    print('Ingrese la instancia deseada')
    print('-'*15)
    print('[1] 1er Cuatrimestre')
    print('[2] 2do Cuatrimestre')
    print('[3] Final')
    opcion = input('Ingrese la opcion: ')
    if opcion == '1':
        return '1er Cuatrimestre'
    elif opcion == '2':
        return '2do Cuatrimestre'
    elif opcion == '3':
        return 'Final'


def ver_notas_alumno(alumno):
    with open('notas.csv','r',encoding="UtF-8") as csv:
        for datos in csv:
            datos = datos.strip()
            if not datos:
                continue
            campos = datos.split(',')
            if campos[3].split(" - ")[1] == str(alumno['dni']):
                print('='*20)
                print(f'Profesor : {campos[3]}')
                print(f'Nota : {campos[4]}')
                print(f'Instancia : {campos[5]}')
                print('='*20)






