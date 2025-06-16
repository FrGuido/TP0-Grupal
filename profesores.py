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
        else:
            print('No se encontro al profesor de ese DNI\n')
            return None


def modificar_profesor():
    if validar.valid_archivo(archivo):
        while True:
            print('Ingrese el dni del profesor a buscar')
            dni = validar.valid_formato_dni()
            prof = buscar_profesor(dni)
            if prof == None:
                print('Desea intentarlo de nuevo?')
                vl = menu_texto.confirmacion_user()
                if vl == 'n':
                    return
            else:
                break
            
        print('Este es el profesor que esta editando\n')
        menu_texto.imprimir_dic(prof)
        input('Ingrese enter para continuar')            

        with open(archivo,'r',encoding="UTF-8") as j:
            datos = json.load(j)
        for i in datos:
            if i['dni'] == dni:
                while True:
                    opcion = menu_texto.opcion_modificar_profesor()

                    if opcion == '0':
                        break
                    
                    elif opcion == '1':
                        print("\n" + "=" * 50)
                        print(f'{"~ Modificando nombre ~".center(50)}')
                        print(f"{"» Introduzca su nuevo nombre «".center(50)}")
                        print("-" * 50)
                        i['nombre'] = validar.valid_nombre()

                    elif opcion == '2':
                        print("\n" + "=" * 50)
                        print(f'{"~ Modificando apellido ~".center(50)}')
                        print(f"{"» Introduzca su nuevo apellido «".center(50)}")
                        print("-" * 50)
                        i['apellido'] = validar.valid_nombre()

                    elif opcion == '3':
                        print("\n" + "=" * 50)
                        print(f'{"~ Modificando fecha de nacimiento ~".center(50)}')
                        print(f"{"» Introduzca su nueva fecha «".center(50)}")
                        print("-" * 50)
                        i['fecha_nacimiento'] = validar.valid_fecha()

                    elif opcion == '4':
                        print("\n" + "=" * 50)
                        print(f'{"~ Modificando DNI ~".center(50)}')
                        print(f"{"» Introduzca su DNI «".center(50)}")
                        print("-" * 50)
                        i['dni'] = validar.valid_dni_inprof()

                    elif opcion == '5':
                        print("\n" + "=" * 50)
                        print(f'{"~ Modificando Email ~".center(50)}')
                        print(f"{"» Introduzca su nuevo Email «".center(50)}")
                        print("-" * 50)
                        i['mail'] = validar.valid_mail()

                    elif opcion == '6':
                        print("\n" + "=" * 50)
                        print(f'{"~ Modificando telefono ~".center(50)}')
                        print(f"{"» Introduzca su nuevo Telefono «".center(50)}")
                        print("-" * 50)
                        i['telefono'] = validar.valid_telefono()

                    elif opcion == '7':
                        print("\n" + "=" * 50)
                        print(f'{"~ Modificando Contraseña ~".center(50)}')
                        print(f"{"» Introduzca su nueva Contraseña «".center(50)}")
                        print("-" * 50)
                        i['pasw'] = validar.valid_pasw()

                registro.registrar_modificado("Profesor", i['nombre'],i['apellido'],i['dni'])
                break

        validar.cargar_archivo_json(archivo,datos)
    else:
        menu_texto.error_archivo()

    input('Volviendo al menu inicial, precione enter')


def eliminar_profesor():
    if validar.valid_archivo(archivo) or validar.valid_archivo(cursos.archivo):
        while True:
            try:
                print('Ingrese el DNI del profesor a eliminar')
                dni = validar.valid_formato_dni()
                menu_texto.imprimir_dic(buscar_profesor(dni))
                print('\nSeguro que desea eliminar este elemento?\n')
                seg = menu_texto.confirmacion_user()
                if seg == 's':
                    with open(archivo,'r',encoding="UTF-8") as j:
                        datos = json.load(j)
                    for i in datos:
                        if i['dni'] == dni:
                            registro.registrar_eliminado("Profesor", i['nombre'],i['apellido'],i['dni'])
                            break
                    datos = list(filter(lambda x: x['dni'] != dni, datos))
                    
                    validar.cargar_archivo_json(archivo,datos)

                    with open(cursos.archivo,"r",encoding="UTF-8") as j:
                        datos = json.load(j)
                    
                    for i in datos:
                        for j in i['materias']:
                            for g in j['profesores']:
                                if dni in g:
                                    j.remove(g)
                    print('='*50)
                    print('Se ha eliminado correctamente al profesor')
                    return

                else:
                    break

            except:
                print('Ingrese numeros\n--------------')

        input('Volviendo al menu inicial, presione Enter para continuar')
        return
    else:
        menu_texto.error_archivo()


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













