import cursos
import materias
import profesores
import json
import registro

import validar
import time
import alumnos

def bienvenida():
    print('\n'*10)
    print(f'{" Bienvenido al sistema de alumnado © ":-^58}')
    print(f'{"Trabajo Practico - Programacion 1":^58}')
    print(f'{"Grupo 10":^58}')
    print(f'{" - "*15:^58}')

def opciones_principal_profesor(contador = 0):
    if contador >= 5:
        print("Demasiados intentos inválidos. Cerrando programa...")
        exit()

    opciones = 2
    print()
    print("-" * 26)
    print("MENÚ PRINCIPAL")
    print("-" * 26)
    print("[1] Ver mis materias")
    print("[2] Modificar Notas Alumnos")
    print("-" * 26)
    print("[0] Salir del programa")
    print("-" * 26)
    print()

    opcion = input("Seleccione una opción: ")
    if opcion not in [str(i) for i in range(0, opciones + 1)]:
        input("Opción inválida. Presione ENTER para volver a seleccionar.")
        return opciones_principal_profesor(contador + 1)
    print()
    return opcion

def opciones_principal_alumno(contador = 0):
    if contador >= 5:
        print("Demasiados intentos inválidos. Cerrando programa...")
        exit()

    opciones = 1
    print()
    print("-" * 26)
    print("MENÚ PRINCIPAL")
    print("-" * 26)
    print("[1] Ver mis notas")
    print("-" * 26)
    print("[0] Salir del programa")
    print("-" * 26)
    print()

    opcion = input("Seleccione una opción: ")
    if opcion not in [str(i) for i in range(0, opciones + 1)]:
        input("Opción inválida. Presione ENTER para volver a seleccionar.")
        return opciones_principal_alumno(contador + 1)
    print()
    return opcion

def opciones_principal_admin(contador = 0):
    if contador >= 5:
        print("Demasiados intentos inválidos. Cerrando programa...")
        exit()

    opciones = 5
    print()
    print("-" * 26)
    print("MENÚ PRINCIPAL")
    print("-" * 26)
    print("[1] Gestión de profesores")
    print("[2] Gestión de alumnos")
    print("[3] Modificar Curso")
    print("[4] Gestion de materias")
    print("[5] Registro de cambios")
    print("-" * 26)
    print("[0] Salir del programa")
    print("-" * 26)
    print()

    opcion = input("Seleccione una opción: ")
    if opcion not in [str(i) for i in range(0, opciones + 1)]:
        input("Opción inválida. Presione ENTER para volver a seleccionar.")
        return opciones_principal_admin(contador + 1)
    print()
    return opcion


def opciones_profesores(intentos = 0, max_intentos = 5):
    opciones = 5
    print()
    print("---------------------------")
    print("MENÚ PRINCIPAL > GESTION DE PROFESORES")
    print("---------------------------")
    print("[1] Añadir Profesores")
    print("[2] Eliminar Profesor")
    print("[3] Modificar Profesor")
    print("[4] Lista Profesores")
    print("[5] Buscar datos Profesor")
    print("---------------------------")
    print("[0] Volver al menú anterior")
    print("---------------------------")
    print()

    opcion = input("Seleccione una opción: ")
    if opcion in [str(i) for i in range(0, opciones + 1)]:
        return opcion
    else:
        intentos += 1
        if intentos >= max_intentos:
            print("\nSe superó el número máximo de intentos. Volviendo al menú anterior.")
            return "0"
        print()
        input("Opción inválida. Presione ENTER para volver a seleccionar.")
        return opciones_profesores(intentos)  
        

def opciones_alumno():
    while True:
        opciones = 6
        print()
        print("---------------------------")
        print("MENÚ PRINCIPAL > GESTION DE ALUMNOS")
        print("---------------------------")
        print("[1] Añadir Alumno")
        print("[2] Eliminar Alumno")
        print("[3] Modificar Alumno")
        print("[4] Modificar Notas Alumno")
        print("[5] Listar Alumnos Curso")
        print("[6] Buscar datos alumno")
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
    return opcion

def opciones_materias():
    while True:
        opciones = 5
        print()
        print("---------------------------")
        print("MENÚ PRINCIPAL > GESTION DE MATERIAS")
        print("---------------------------")
        print("[1] Añadir Materia")
        print("[2] Eliminar Materia")
        print("[3] Modificar Materia")
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
    return opcion

def opcion_modificar_profesor():
    while True:
        opciones = 7
        print(f'Que desea modificar?')
        print("---------------------------")
        print("[1] Nombre")
        print("[2] Apellido")
        print("[3] Fecha de Nacimiento")
        print("[4] DNI")
        print("[5] Mail")
        print("[6] Telefono")
        print("[7] Contraseña")
        print("---------------------------")
        print("[0] Salir")
        print("---------------------------")
        print()
        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones + 1)]:
            return opcion
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")


def opcion_modificar_alumno():
    while True:
        opciones = 7
        print(f'Que desea modificar?')
        print("---------------------------")
        print("[1] Nombre")
        print("[2] Apellido")
        print("[3] Fecha de Nacimiento")
        print("[4] DNI")
        print("[5] Mail")
        print("[6] Telefono")
        print("[7] Contraseña")
        print("---------------------------")
        print("[0] Salir")
        print("---------------------------")
        print()
        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones + 1)]:
            return opcion
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")


def opcion_modificar_materia():
    while True:
        opciones = 2
        print(f'Que desea modificar?')
        print("---------------------------")
        print("[1] Nombre")
        print("[2] Profesores acargo")
        print("---------------------------")
        print("[0] Salir")
        print("---------------------------")
        print()
        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones + 1)]:
            return opcion
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")


def opcion_modificar_materias_profesores():
    while True:
        opciones = 2
        print(f'Que desea hacer?')
        print("---------------------------")
        print("[1] Añadir Profesor")
        print("[2] Eliminar Profesor")
        print("---------------------------")
        print("[0] Salir")
        print("---------------------------")
        print()
        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones + 1)]:
            return opcion
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")


def opciones_cursos():
    while True:
        opciones = 2
        print(f'Que desea modificar?')
        print("---------------------------")
        print("[1] Cantidad Maxima de Alumnos")
        print("[2] Materias")
        print("---------------------------")
        print("[0] Salir")
        print("---------------------------")
        print()
        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones + 1)]:
            return opcion
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")

def elegir_materia():
    with open(materias.archivo,"r",encoding="UTF-8") as j:
        datos = json.load(j)
    while True:
        opciones = len(datos)
        print("---------------------------")
        for i, valor in enumerate(datos):
            print(f"[{i+1}] {valor['nombre']}")
        print("---------------------------")
        print("[0] Salir")
        print("---------------------------")
        print()
        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(1, opciones + 1)]:
            return (datos[int(opcion)-1]['nombre'], datos[int(opcion)-1]['codigo']) 
        elif opcion == '0':
            return (None, None)
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")


def lista_profesores_disponibles():
    print('Esta es la lista de profesores disponibles')
    with open(profesores.archivo, "r", encoding="UTF-8") as j:
        datos_p = json.load(j)

    with open(materias.archivo, "r", encoding="UTF-8") as j:
        datos_m = json.load(j)

    disponibles = []

    for i in datos_p:
        contador = 0
        for j in datos_m:
            for h in j['profesores']:
                if i['dni'] == h[0]:
                    contador += 1
        if contador < 3:
            disponibles.append([i['dni'],i['nombre']])
            print('=' * 52)
            print(f"| {str(i['nombre']):<20} DNI {str(i['dni']):>25} |")
    print('=' * 52)
    return disponibles



def error_archivo():
    print()
    print('!','='*15,'!')
    print('No se ha podido acceder al archivo\nVerifique su integridad o existencia')
    print('!','='*15,'!')
    print()


def confirmacion_user():
    while True:
        rta = input('Ingrese "S" para si\nIngrese "N" para no\n>>')
        print()
        if rta.lower() == 's' or rta.lower() == 'n':
            return rta
        else:
            print('Ingrese uno de los valores indicados\n-----------------\n')


def imprimir_dic(dic):
    print('=' * 52)
    for key, valor in dic.items():
        a = f'| {str(key):<20} : {str(valor):>25} |'
        print(a)
    print('-' * 52)


def seleccion_turno():
    while True:
        print('Que turno desea?')
        print('-'*15)
        print('[1] Turno Mañana')
        print('[2] Turno Tarde')
        print('-'*15)
        turno = input('>')
        if turno == '1':
            return 'Mañana'
        elif turno == '2':
            return 'Tarde'
        else:
            print('Ingrese un valor valido, intente de nuevo\n-----------\n')


def seleccion_curso():
    while True:
        print('Que curso desea ingresar?')
        print('-'*15)
        print('[1] Primer Grado/Año')
        print('[2] Segundo Grado/Año')
        print('[3] Tercer Grado/Año')
        print('[4] Cuarto Grado/Año')
        print('[5] Quinto Grado/Año')
        print('[6] Sexto Grado/Año')
        print('-'*15)
        turno = input('>')
        if turno == '1':
            return '1ro'
        elif turno == '2':
            return '2do'
        elif turno == '3':
            return '3ro'
        elif turno == '4':
            return '4to'
        elif turno == '5':
            return '5to'
        elif turno == '6':
            return '6to'
        else:
            print('Ingrese una opcion valida\n-----------\n')


"""
def seleccion_etapa():
    while True:
        print('Que etapa desea?')
        print('-'*15)
        print('[1] Educacion Primaria')
        print('[2] Educacion Secundaria')
        print('-'*15)
        turno = input('>')
        if turno == '1':
            return 'Primario'
        elif turno == '2':
            return 'Secundario'
        else:
            print('Ingrese un valor valido, intente de nuevo\n-----------\n')
"""

def eleccion_notas():
    while True:
        opciones = 2
        print('Que desea hacer?')
        print('-'*15)
        print('[1] Añadir Nota')
        print('[2] Editar Nota')
        print('-'*15)
        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones + 1)]:
            return opcion
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")


# profesor(nombre - dni), curso, turno, alumno, nota, instancia,fecha
def añadir_nota(alumno = None, profe = None):
    nota = []
    valid = False
    try:
        with open(profesores.archivo, "r", encoding="UTF-8") as j:
            datos = json.load(j)
        with open(cursos.archivo, "r", encoding="UTF-8") as j:
            c = json.load(j)

        if datos:
            while True:
                if alumno == None:
                    print('Ingrese el dni del alumno a cargo de la nota')
                    aludni = validar.valid_formato_dni()
                    alumno = alumnos.buscar_alumno(aludni)

                for i in c:
                    for j in i['alumnos']:
                        if j['dni'] == alumno['dni']:
                            valid = True
                            curso = i['nombre']
                            turno = i['turno']
                            break
                    if valid:
                        break                   

                if not valid:
                    print('Desea intentarlo de nuevo?')
                    vl = confirmacion_user()
                    if vl == 'n':
                        return
                else:
                    valid = False
                    break
            for i in datos:
                imprimir_dic(i)
            while True:
                if profe == None:
                    print('Ingrese el dni del profesor a cargo de la nota')
                    profdni = validar.valid_formato_dni()
                    for i in datos:
                        if profdni == i['dni']:
                            nota.append(f'{i['nombre']} - {i['dni']}')
                            valid = True
                            break
                else:
                    nota.append(f'{profe['nombre']} - {profe['dni']}')
                    valid = True
                    break

                if not valid:
                    print('Profesor no encontrado, intente nuevamente')
                else:
                    valid = False
                    break
            instancia = alumnos.pedir_instancia()
            with open(alumnos.notas,"r",encoding="utf-8") as csv:
                datos = csv.readline().strip()
                while datos:
                    if datos.split(',')[0].split(" - ")[1] == profdni and datos.split(',')[3].split(" - ")[1] == alumno['dni'] and datos.split(',')[5] == instancia:
                        print('No se puede crear, ya que ya existe')
                        return
                    datos = csv.readline().strip()
                nota.append(curso)
                nota.append(turno)
                nota.append(f"{alumno['nombre']} - {alumno['dni']}")
                nota.append(str(alumnos.pedir_nota()))
                nota.append(instancia)
                nota.append(f'{time.ctime(time.time())}')

            with open(alumnos.notas,"a",encoding="utf-8") as csv:
                csv.write(','.join(nota)+"\n")
            registro.registrar_agregado("Nota", nota[0], nota[3],nota[4])
        else:
            print('No hay profesores/alumnos para crear una nota')
    except:
        error_archivo()


def editar_nota(alumno = None, profe = None):
    nueva_lista = []
    valid = False
    with open(profesores.archivo, "r", encoding="UTF-8") as j:
        datos = json.load(j)
    with open(cursos.archivo, "r", encoding="UTF-8") as j:
        c = json.load(j)

    if datos:
        while True:
            if alumno == None:
                print('Ingrese el dni del alumno a cargo de la nota')
                aludni = validar.valid_formato_dni()
                alumno = alumnos.buscar_alumno(aludni)
            for i in c:
                for j in i['alumnos']:
                    if j['dni'] == alumno['dni']:
                        valid = True

            if not valid:
                print('Desea intentarlo de nuevo?')
                vl = confirmacion_user()
                if vl == 'n':
                    return
            else:
                valid = False
                break
        for i in datos:
            imprimir_dic(i)
        while True:
            if profe == None:
                print('Ingrese el dni del profesor a cargo de la nota')
                profdni = validar.valid_formato_dni()
                for i in datos:
                    if profdni == i['dni']:
                        valid = True
                        break
            else:
                profdni = profe['dni']
                valid = True

            if not valid:
                print('Profesor no encontrado, intente nuevamente')
            else:
                break
        instancia = alumnos.pedir_instancia()
        with open(alumnos.notas, "r", encoding="utf-8") as archivo:
            arch = archivo.readline().strip()
            while arch:
                campos = arch.split(",")
                if campos[0].split(" - ")[1] == str(profdni) and campos[3].split(" - ")[1] == str(alumno['dni']) and campos[5] == instancia:
                    campos[4] = str(alumnos.pedir_nota())
                    campos[6] = time.ctime(time.time())
                    arch = ",".join(campos)
                    valid = True
                    registro.registrar_modificado("Nota", campos[0], campos[3],campos[4])
                nueva_lista.append(arch + "\n")
                arch = archivo.readline().strip()

            if not valid:
                print('El alumno no tiene notas creadas de esas caracteristicas, cree una para poder editarla')
        with open(alumnos.notas, "w", encoding="utf-8") as c:
            c.writelines(nueva_lista)






