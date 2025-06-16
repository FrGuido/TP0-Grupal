import validar

import menu_texto
import alumnos
import materias


import json

nros_cursos = ('1ero', '2do','3ero','4to','5to','6to')

archivo = 'cursos.json'

def modificar_curso():
    if validar.valid_archivo(archivo):
        print('Que curso desea editar?')
        c = menu_texto.seleccion_curso()
        print('-'*15,'\n')
        t = menu_texto.seleccion_turno()

        with open(archivo, 'r', encoding="UTF-8") as j:
            datos = json.load(j)
        
        for i in datos:
            if i['nombre'] == c and i['turno'] == t:
                while True:
                    opcion = menu_texto.opciones_cursos()

                    if opcion == '0':
                        break
                    
                    elif opcion == '1':
                        print("\n" + "=" * 50)
                        print(f'{"~ Modificando Cantidad Alumnos ~".center(50)}')
                        print("-" * 50)
                        i['max alumnos'] = validar.valid_cant_alumnos(i['max alumnos'], len(i['alumnos']))

                    elif opcion == '2':
                        print("\n" + "=" * 50)
                        print(f'{"~ Modificando Materias ~".center(50)}')
                        print("-" * 50)
                        i['materias'] = modificar_materias(i['materias'])
                
                validar.cargar_archivo_json(archivo, datos)


    else:
        menu_texto.error_archivo()





def modificar_materias(lista):

    with open(materias.archivo,"r",encoding="UTF-8") as j:
        datos = json.load(j)

    if len(datos) == 0:
        print('No hay materias creadas, crea alguna para poder añadir\n------------------------\n\n')
        return lista
    while True:
        verif = False
        print('Desea [1] añadir o [2] eliminar una materia?')
        print('Ingrese 0 para salir')
        opcion = input('>>')
        if opcion == '0':
            return lista
        if opcion == '1':
            if len(lista) < 10:
                while True:
                    nombre,codigo = menu_texto.elegir_materia()
                    if nombre != None:
                        for i in lista:
                            if codigo in i:
                                print('Esta materia ya esta en este Curso, elija otra')
                                verif = True
                        if not verif:
                            lista.append([codigo,nombre])
                            print('Materia cargada con exito')
                            break
                    else:
                        print('Volviendo al menu anterior')
                        input('Ingrese Enter para continuar')
                        break
            else:
                print('Se ha llegado al tope de materias, elimine una para poder añadir')
                
        
        elif opcion == '2':
            if len(lista) > 0:
                while True:
                    print('Este es el listado de materias de este curso')
                    print('-'*20)
                    for i in lista:
                        print(f'Materia: {i[0]} | Codigo: {i[1]}')
                    print('-'*20)
                    print('Ingrese el codigo de alguna materia de la lista para eliminar')
                    codigo = input('O Ingrese 0 para salir\n>>')
                    if codigo == '0':
                        break
                    for i in lista:
                        if codigo in i:
                            lista = list(filter(lambda x: x[0] != codigo, lista))
                            print('Materia eliminada con exito')
                            return lista
                    else:
                        print('No ha ingresado un codigo correcto')
            else:
                print('No hay materias en este curso, ingrese alguna para poder eliminar')



def buscar_curso():
    curso = menu_texto.seleccion_curso()
    turno = menu_texto.seleccion_turno()
    return curso,turno







