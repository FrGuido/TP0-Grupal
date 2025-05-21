import almacen_datos
from modif_objetos import profesores,eliminar
from validacion import validar
import re



def Carga_Materias(m):
    materia = m
    while True:
        t,ma = None,None
        print('Ingrese el nombre de la materia:')
        materia['nombre'] = input('> ').capitalize()
        for i in almacen_datos.materias:
            if i['nombre'] == materia['nombre']:
                if i['turno'] == 'Mañana':
                    ma = i['turno']
                elif i['turno'] == 'Tarde':
                    t = i['turno']

        print()
        print('Ingrese el turno de esta materia (Mañana o Tarde)')
        while True:
            materia['turno'] = input('> ').capitalize()
            if materia['turno'] not in almacen_datos.turnos:
                print('Ingrese un turno valido\n')
            else:
                break
        if materia['turno'] == t and materia['turno'] == ma:
            print('Esta materia ya existe en ambos turnos, intente de nuevo')
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
        elec = ''
        materia = None
        nombre = input('Ingrese la materia\n> ').capitalize()
        turno = input('Ingrese el turno \n>').capitalize()

        for mat in almacen_datos.materias:
            if mat['nombre'] == nombre and mat['turno'] == turno:
                materia = mat
                break
        if materia is None:
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

        if materia is not None:
            for k, valor in materia.items():
                print(f"{(k.capitalize()):<15}{str(valor):>30}")
            return nombre,turno
    
    return nombre,turno
    
def modif_materias(nombre,turno):
    while True:
        for x in almacen_datos.materias:
            if x['nombre'] == nombre and x['turno'] == turno:
                mat = x

        while True:
            opciones = 3
            print(f'Que desea modificar?')
            print("[1] Nombre y Turno")
            print("[2] Profesores")
            print("[3] Dias")
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
                while True:
                    t = None
                    print('Ingrese el nombre de la materia para cambiar:')
                    mat['nombre'] = input('> ').capitalize()
                    for i in almacen_datos.materias:
                        if i['nombre'] == mat['nombre']:
                            print(f'Esa materia ya existe, y se encuentra en el turno {i["turno"]}\nDesea continuar igualmente, debera incluirla con un turno distinto')
                            t = i['turno']
                    print()
                    print('Ingrese el turno a cambiar de esta materia (Mañana o Tarde)')
                    while True:
                        mat['turno'] = input('> ').capitalize()
                        if mat['turno'] not in almacen_datos.turnos:
                            print('Ingrese un turno valido\n')
                        else:
                            break
                    if mat['turno'] == t:
                        print('Esta materia en este turno ya existe, intente de nuevo')
                    else:
                        break

            elif opcion == '2':
                while True:
                    print()
                    print('Modificando lista de profesores de la materia:')
                    print('Estas son los profesores de la materia:')
                    print(mat['profesores'])
                    print('Quieres añadir o eliminar alguna?')
                    deci = input('Ingresa A para añadir o E para eliminar').lower()
                    while True:
                        if deci == 'a':
                            while True:
                                print('Ingrese el dni del profesor a agregar')
                                dni = validar.valid_dni()
                                nombre, apellido = profesores.busqueda_nombre_profesores(dni)
                                if nombre is not None:
                                    mat['profesores'].append(nombre)
                                    break
                                else:
                                    print('Ingrese un DNI que exista')
                        elif deci == 'e':
                            while True:
                                elimina=input('Ingrese el que quiere eliminar\n> ').capitalize()
                                if elimina in mat['profesores']:
                                    mat['profesores'].remove(elimina)
                                    break
                                else:
                                    print('Ese profesor no se encuentra en esa materia')
                        else:
                            print('Ingrese un valor valido')

                        if deci=='a' or deci=='e':
                            break
                    print('Profesores cambiado con exito!')
                    print('-'*15)
                    break

            elif opcion == '3':
                while True:
                    print()
                    print('Estos son los dias que tiene la materia:')
                    print(mat['dias'])
                    print('Quieres añadir o eliminar alguna?')
                    deci = input('Ingresa A para añadir o E para eliminar').lower()
                    if deci == 'a':
                        while True:
                            dia = input('Ingrese el dia a añadir\n> ').capitalize()
                            if dia in almacen_datos.dias and dia not in mat['dias']:
                                mat['dias'].append(dia)
                                break
                            else:
                                print('Ingrese un dia adecuado o que no tenga la materia ya')
                
                    elif deci == 'e':
                        while True:
                            dia = input('Ingrese el dia a eliminar\n> ').capitalize()
                            if dia in almacen_datos.dias and dia in mat['dias']:
                                mat['dias'].remove(dia)
                                break
                            else:
                                print('Ingrese un dia adecuado o que no tenga la materia ya')
                    else:
                        print('Ingrese un valor adecuado')
                        print('-'*15)
        
        if opcion == '0':
            for x in almacen_datos.materias:
                if x['nombre'] == nombre and x['turno'] == turno:
                    x = mat
                    break
            break