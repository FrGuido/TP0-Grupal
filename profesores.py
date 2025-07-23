import validar
import menu_texto
import materias

import cursos
import registro

import json

archivo = 'profesores.json'


def cargar_esqueleto():
    prof = {}
    print("\n" + "=" * 50)
    print(f"{"» Introduzca su nombre «".center(50)}")
    print("-" * 50)
    prof['nombre'] = validar.valid_nombre()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca su apellido «".center(50)}")
    print("-" * 50)
    prof['apellido'] = validar.valid_nombre()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca su fecha de nacimiento «".center(50)}")
    print("-" * 50)
    prof['fecha_nacimiento'] = validar.valid_fecha()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca su DNI «".center(50)}")
    print("-" * 50)
    prof['dni'] = validar.valid_dni_inprof()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca su Email «".center(50)}")
    print("-" * 50)
    prof['mail'] = validar.valid_mail()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca su Telefono «".center(50)}")
    print("-" * 50)
    prof['telefono'] = validar.valid_telefono()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca su Contraseña «".center(50)}")
    print("-" * 50)
    prof['pasw'] = validar.valid_pasw()

    return prof


def añadir_profesor():

    if validar.valid_archivo(archivo):
        with open(archivo, "r", encoding="UTF-8") as j:
            try:
                datos = json.load(j)

            except json.JSONDecodeError:
                datos = []
        
        profe = cargar_esqueleto()
        datos.append(profe)
        registro.registrar_agregado("Profesor", profe['nombre'],profe['apellido'],profe['dni'])


        validar.cargar_archivo_json(archivo,datos)

        print('='*50)
        input('Se ha ingresado correctamente al profesor\nPresione una tecla para continuar')

    else:
        menu_texto.error_archivo()


def buscar_profesor(dni):
    with open(archivo,'r',encoding="UTF-8") as j:
        datos = json.load(j)
        for i in datos:
            if i['dni'] == dni:
                return i
        print('No se encontro al profesor de ese DNI\n')
        return None


def obtener_dni_profesor():
    #Obtiene y valida el DNI del profesor a buscar
    while True:
        print('Ingrese el dni del profesor a buscar')
        dni = validar.valid_formato_dni()
        prof = buscar_profesor(dni)
        if prof is not None:
            return dni, prof
        
        print('Desea intentarlo de nuevo?')
        if menu_texto.confirmacion_user() == 'n':
            return None, None


def procesar_modificacion_profesor(datos, dni):
    for i in datos:
        if i['dni'] != dni:
            continue
        opcion = menu_texto.opcion_modificar_profesor()
        while opcion != '0':
            modificaciones = {
                '1': lambda: modificar_campo(i, 'nombre', "~ Modificando nombre ~", "» Introduzca su nuevo nombre «", validar.valid_nombre),
                '2': lambda: modificar_campo(i, 'apellido', "~ Modificando apellido ~", "» Introduzca su nuevo apellido «", validar.valid_nombre),
                '3': lambda: modificar_campo(i, 'fecha_nacimiento', "~ Modificando fecha de nacimiento ~", "» Introduzca su nueva fecha «", validar.valid_fecha),
                '4': lambda: modificar_campo(i, 'dni', "~ Modificando DNI ~", "» Introduzca su DNI «", validar.valid_dni_inprof),
                '5': lambda: modificar_campo(i, 'mail', "~ Modificando Email ~", "» Introduzca su nuevo Email «", validar.valid_mail),
                '6': lambda: modificar_campo(i, 'telefono', "~ Modificando telefono ~", "» Introduzca su nuevo Telefono «", validar.valid_telefono),
                '7': lambda: modificar_campo(i, 'pasw', "~ Modificando Contraseña ~", "» Introduzca su nueva Contraseña «", validar.valid_pasw)
            }
            if opcion in modificaciones:
                modificaciones[opcion]()
            opcion = menu_texto.opcion_modificar_profesor()
        registro.registrar_modificado("Profesor", i['nombre'],i['apellido'],i['dni'])
        return


def modificar_campo(profesor, campo, titulo, mensaje, validador):
    #Modifica un campo específico del profesor
    print("\n" + "=" * 50)
    print(f'{titulo.center(50)}')
    print(f"{mensaje.center(50)}")
    print("-" * 50)
    profesor[campo] = validador()


def modificar_profesor():
    if not validar.valid_archivo(archivo):
        menu_texto.error_archivo()
        return
        
    dni, prof = obtener_dni_profesor()
    if dni is None:
        return
        
    print('Este es el profesor que esta editando\n')
    menu_texto.imprimir_dic(prof)
    input('Ingrese enter para continuar')            

    with open(archivo,'r',encoding="UTF-8") as j:
        datos = json.load(j)
    
    procesar_modificacion_profesor(datos, dni)
    validar.cargar_archivo_json(archivo,datos)
    input('Volviendo al menu inicial, precione enter')


def confirmar_y_eliminar_profesor(dni):
    #Confirma y elimina el profesor si el usuario confirma
    profesor = buscar_profesor(dni)
    if profesor is None:
        return False
        
    menu_texto.imprimir_dic(profesor)
    print('\nSeguro que desea eliminar este elemento?\n')
    
    if menu_texto.confirmacion_user() != 's':
        return False
    
    # Eliminar de profesores.json
    with open(archivo,'r',encoding="UTF-8") as j:
        datos = json.load(j)
    
    for i in datos:
        if i['dni'] == dni:
            registro.registrar_eliminado("Profesor", i['nombre'],i['apellido'],i['dni'])
            datos = list(filter(lambda x: x['dni'] != dni, datos))
            validar.cargar_archivo_json(archivo,datos)
            
            # Eliminar de cursos
            with open(cursos.archivo,"r",encoding="UTF-8") as j:
                datos_cursos = json.load(j)
            
            for curso in datos_cursos:
                for materia in curso['materias']:
                    materia['profesores'] = [prof for prof in materia['profesores'] if dni not in prof]
            
            print('='*50)
            print('Se ha eliminado correctamente al profesor')
            return True
    
    return False


def eliminar_profesor():
    if not (validar.valid_archivo(archivo) or validar.valid_archivo(cursos.archivo)):
        menu_texto.error_archivo()
        return
    try:
        print('Ingrese el DNI del profesor a eliminar')
        dni = validar.valid_formato_dni()
        confirmar_y_eliminar_profesor(dni)
    except:
        print('Ingrese numeros\n--------------')
    input('Volviendo al menu inicial, presione Enter para continuar')


def listar_profesores():
    with open(archivo, 'r', encoding="UTF-8") as j:
        datos = json.load(j)
    for i in datos:
        menu_texto.imprimir_dic(i)
    
    input('Ingrese enter para volver al menu anterior')


def ver_materias_profe(profe):
    with open(materias.archivo,'r',encoding="UTF-8") as j:
        datos = json.load(j)
    
    for i in datos:
        for j in i['profesores']:
            if profe['dni'] in j:
                menu_texto.imprimir_dic(i)