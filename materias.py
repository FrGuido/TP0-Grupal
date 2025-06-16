import validar
import menu_texto
import registro



import json




archivo  = "materias.json"


def cargar_esqueleto():
    mat={}
    print("\n" + "=" * 50)
    print(f"{"» Introduzca el nombre «".center(50)}")
    print("-" * 50)
    mat['nombre'] = validar.valid_repeticion_nombre(validar.valid_nombre())

    print("\n" + "=" * 50)
    print(f"{"» Introduzca los profesores a cargo «".center(50)}")
    print("-" * 50)
    mat['profesores'] = prof_acargo()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca el codigo de identificacion de la materia «".center(50)}")
    print("-" * 50)
    mat['codigo'] = validar.valid_codigo_materia()

    return mat

def crear_materia():
    if validar.valid_archivo(archivo):
        with open(archivo, "r", encoding="UTF-8") as j:
            try:
                datos = json.load(j)
            except json.JSONDecodeError:
                datos = []
        mat = cargar_esqueleto()
        registro.registrar_agregado("Materia", mat['nombre'],'--',mat['codigo'])
        datos.append(mat)

        validar.cargar_archivo_json(archivo, datos)
        print('='*50)
        input('Se ha ingresado correctamente la materia\nPresione una tecla para continuar')

    else:
        menu_texto.error_archivo()

def modificar_materia():
    if validar.valid_archivo(archivo):
        with open(archivo, "r", encoding="UTF-8") as j:
            datos = json.load(j)
        
        print('='*20)
        for i in datos:
            print(f'{(i['codigo']).ljust(20)}  {i['nombre'].rjust(20)}')
        print('='*20)
        while True:
            try:
                print('Ingrese el codigo de la materia que desea modificar')
                cod = input('>>')
                for i in datos:
                    if cod == i['codigo']:
                        while True:
                            opcion = menu_texto.opcion_modificar_materia()

                            if opcion == '0':
                                registro.registrar_modificado("Materia", i['nombre'],'--',i['codigo'])
                                validar.cargar_archivo_json(archivo,datos)
                                return

                            elif opcion == '1':
                                print("\n" + "=" * 50)
                                print(f'{"~ Modificando Nombre ~".center(50)}')
                                print("-" * 50)
                                i['nombre'] = validar.valid_repeticion_nombre(validar.valid_nombre())

                            elif opcion == '2':
                                print("\n" + "=" * 50)
                                print(f'{"~ Modificando Profesores a Cargo ~".center(50)}')
                                print("-" * 50)
                                i['profesores'] = modificar_prof_acargo(i['profesores'])
                else:
                    print('Codigo no encontrado, Intente nuevamente')


            except ValueError:
                print('Ingrese numeros')
                print('\n----------\n')
    else:
        menu_texto.error_archivo()




def prof_acargo():
    if validar.valid_archivo(archivo):
        print('(Solo se pueden añadir profesores con menos de 3 materias asignadas)')
        profes = []
        disp = menu_texto.lista_profesores_disponibles()
        contador = 0
        if disp != []:
            while True:
                try:
                    if contador == 5:
                        print('Ha llegado al limite de profesores')
                        input('Presione Enter para salir')
                        break
                    verif = False
                    print('\nIngresa el DNI del profesor que deseas añadir')
                    p = validar.valid_formato_dni()
                    for i in profes:
                        if p in i:
                            print('Ese profe ya se encuentra en esta materia, elija otro')
                            verif = True
                            break
                    if not verif:
                        for i in disp:
                            if p in i:
                                profes.append(i)
                                contador += 1
                                break
                        else:
                            print('Ingrese un profesor disponible')
                        print('Desea ingresar un profesor nuevo?')
                        if menu_texto.confirmacion_user() == 'n':
                            break

                except:
                    print('Ingrese numeros')      

            return profes
    
        else:
            print('No se han encontrado profesores disponibles\nlibere a alguno y edite la materia')
            return []
    else:
        menu_texto.error_archivo()


def modificar_prof_acargo(asignados):
    print('(Solo se pueden añadir profesores con menos de 3 materias asignadas)')
    disp = menu_texto.lista_profesores_disponibles()
    print('Los profesores ya asignados son')
    for i in asignados:
        print('=' * 52)
        print(f'| {str(i[1]):<20} DNI {str(i[0]):>25} |')

    while True:
        try:
            opcion = menu_texto.opcion_modificar_materias_profesores()
            if opcion == '0':
                break
            elif opcion == '1':
                if disp != []:
                    if len(asignados) >= 5:
                        print('Ha llegado al limite de profesores en esta materia')
                        print('Elimine alguno e intente nuevamente')
                        input('-----------------------\nIngrese Enter para continuar')
                        break
                    else:
                        verif = False
                        print('\nIngresa el DNI del profesor que deseas añadir')
                        dni = validar.valid_formato_dni()
                        for i in asignados:
                            if dni in i:
                                print('Ese profe ya se encuentra en esta materia, elija otro')
                                verif = True
                                break
                        if not verif:
                            for i in disp:
                                if dni in i:
                                    asignados.append(i)
                                    return asignados
                            else:
                                print('Ingrese un profesor disponible')
                            print('Desea ingresar un profesor nuevo?')
                            if menu_texto.confirmacion_user() == 'n':
                                break
                else:
                    print('No se han encontrado profesores disponibles\nlibere a alguno y edite la materia')

            elif opcion == '2':
                if len(asignados) == 0:
                        print('No hay profesores en esta materia')
                        print('Añada alguno e intente nuevamente')
                        input('-----------------------\nIngrese Enter para continuar')
                        break
                else:
                    verif = False
                    print('\nIngresa el DNI del profesor que deseas eliminar')
                    dni = validar.valid_formato_dni()
                    for i in asignados:
                        if dni in i:
                            for j in disp:
                                if dni in j:
                                    asignados.remove(j)
                                    print('Profesor eliminado correctamente')
                                    return asignados
                    print('Proesor no encontrado')



        except:
            print('Ingrese correctamente los datos\nIntente nuevamente')
            input('Ingrese Enter para continuar')


def elimiar_materia():
    if validar.valid_archivo(archivo):
        with open(archivo, "r", encoding="UTF-8") as j:
            datos = json.load(j)
        
        print('='*20)
        for i in datos:
            print(f'{(i['codigo']).ljust(20)}  {i['nombre'].rjust(20)}')
        print('='*20)
        while True:
                print('Ingrese el codigo de la materia que desea eliminar')
                print('O ingrese 0 para salir')
                cod = input('>>')
                if cod == '0':
                    return
                for i in datos:
                    if cod == i['codigo']:
                        print('Esta es la materia que va a eliminar')
                        menu_texto.imprimir_dic(i)
                        print('Seguro que desea eliminarla?')
                        if menu_texto.confirmacion_user() == 's':
                            registro.registrar_eliminado("Materia", i['nombre'],'--',i['codigo'])
                            datos = list(filter(lambda x : x['codigo'] != cod, datos))
                            validar.cargar_archivo_json(archivo,datos)
                            return
                        else:
                            return
    else:
        menu_texto.error_archivo()


















