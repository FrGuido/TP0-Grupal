import re
import json
import menu_texto
import materias
import profesores
import cursos


def cargar_archivo_json(ruta,datos):
    with open(ruta, "w", encoding="UTF-8") as j:
        json.dump(datos, j, indent=2, ensure_ascii=False)

#validacion dni simple
def valid_formato_dni():
    while True:
        try:
            dni = input('>>> ')
            print('-'*15)
            if len(dni) == 8 and dni.isdigit() and int(dni)>10000000: #El DNI debe tener 8 digitos
                return int(dni)
            else:
                print('Formato de DNI incorrecto, intente nuevamente')
        except:
            print('Ingrese los datos adecuados\n')

#validacion existencia dni en profesores
def valid_dni_inprof():

    tipo = tipo_archivo(profesores.archivo)

    while True:
        try:
            dni = input('>>> ')
            print('-'*15)
            if len(dni) == 8 and dni.isdigit(): #El DNI debe tener 8 digitos
                dni = int(dni)
                if tipo == 'json':
                    vl = 0
                    with open(profesores.archivo, "r", encoding="UTF-8") as j:
                        datos = json.load(j)
                        for i in datos:
                            if i['dni'] == dni:
                                vl = 1
                                print()
                                print('Ese DNI ya existe, pruebe otro o ingrese uno temporal para despues editarlo\n')
                                print('-'*15)
                                break
                        
                elif tipo == 'csv':
                    pass
                elif tipo == 'txt':
                    pass

                if vl == 0:
                    return dni
            
            else:
                print('Ingreso un DNI invalido, intente nuevamente, sin puntos, guiones ni espacios') #Mensaje de correccion
                print('-'*15)
        except ValueError:
            print('Ingrese numeros\n--------')

#validacion existencia dni en cursos/alumnos
def valid_dni_inalu():

    tipo = tipo_archivo(cursos.archivo)

    while True:
        try:
            dni = input('>>> ')
            print('-'*15)
            if len(dni) == 8 and dni.isdigit(): #El DNI debe tener 8 digitos
                dni = int(dni)
                if tipo == 'json':
                    vl = 0
                    with open(cursos.archivo, "r", encoding="UTF-8") as j:
                        datos = json.load(j)
                        for i in datos:
                            for j in i['alumnos']:
                                if j['dni'] == dni:
                                    vl = 1
                                    print()
                                    print('Ese DNI ya existe, pruebe otro o ingrese uno temporal para despues editarlo\n')
                                    print('-'*15)
                                    break
                        
                elif tipo == 'csv':
                    pass
                elif tipo == 'txt':
                    pass

                if vl == 0:
                    return dni
            
            else:
                print('Ingreso un DNI invalido, intente nuevamente, sin puntos, guiones ni espacios') #Mensaje de correccion
                print('-'*15)
        except ValueError:
            print('Ingrese numeros\n--------')


#validacion de mail
def valid_mail():
    while True:
        validez = r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑüÜ\.-]+@[a-zA-Z0-9\.-]+\.\w{2,4}$' #Caracteres validos para el mail
        mail = input(">>> ")
        if re.match(validez, mail) is not None:
            return mail
        else:
            print("Formato de mail inválido. Intente nuevamente.\n")

#validacion de contrsenia
def valid_pasw():
    print('La contraseña debe tener al menos un carcter en mayuscula,\nun numero, un simbolo y al menos 10 caracteres')
    while True:
        contra = input('>>> ')
        if len(contra) < 10 or not re.search(r'[A-Z]',contra) or not re.search(r'\d', contra) or not re.search(r'[^A-Za-z0-9]', contra):
            print('Contraseña no valida, intente de nuevo')
        else:
            #print('Contraseña valida')
            return contra

#validacion de fecha
def valid_telefono():   
    while True:
        validez = r'^11\d{8}$'
        tel = input(">>> ")
        if re.match(validez, tel) is not None:
            return tel
        else:
            print("Formato de telefono inválido. Intente nuevamente.\n")

#validcion de fecha
def valid_fecha():
    while True: #bucle, termina cuando se ingrese una fecha valida
        try:
            dia = int(input('Ingrese el dia\n>>>'))
            print('-'*15)
            mes = int(input('Ingrese el mes\n>>>'))
            print('-'*15)
            año = int(input('Ingrese el año\n>>>'))

            bisiesto = añoBisiesto(año) #valido el año bisisesto

            diasMes = [31, 29 if bisiesto else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #lista de dias de meses, con febrero arreglado

            if 1 <= mes <= 12 and 1 <= dia <= diasMes[mes - 1] and 1900 < año < 2025:
                #print("Fecha válida.")
                return (f'{dia}/{mes}/{año}')
            else:
                print("Fecha inválida. Día, mes o año fuera de rango.\n")
        except ValueError:
            print("Error: ingrese solo números en el formato correcto.\n")

def añoBisiesto(año): #verificacion si el año es bisiesto o no
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

#validacion nombre
def valid_nombre():
    while True:
        validez = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]+(?: [a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]+)*$'
        nombre = input(">>> ").title()
        if re.match(validez, nombre):
            return nombre
        else:
            print("Formato de nombre/apellido inválido. Intente nuevamente.\n")

def valid_cant_alumnos(max, cant_alumnos):
    if valid_archivo(cursos.archivo):
        try:
            print('-'*15)
            print('Cuantos alumnos desea que sean el maximo?')
            print(f'Actualmente hay {max} de maximo')
            print('-'*15)
            num = int(input('>>>'))
            with open(cursos.archivo, "r", encoding="UTF-8") as j:
                datos = json.load(j)
            if cant_alumnos > num:
                print(f'Hay mas alumnos ya ingresados ({cant_alumnos}) de lo que quiere establecer como maximo ({num})')
                input('Ingrese un numero mayor o elimine alumnos\nIngrese Enter para continuar')
            else:
                print(f'Se ha cambiado el maximo de {max} a {num}\n')
                input('Ingrese Enter para continuar')
                return num
        except:
            print('Ingrese numeros enteros, Intente nuevamente')
    else:
        menu_texto.error_archivo()

def valid_repeticion_nombre(nombre):
    with open(materias.archivo, "r", encoding="UTF-8") as j:
        datos = json.load(j)
    while True:
        for i in datos:
            if i['nombre'].lower().strip() == nombre.lower().strip():
                print('Ese nombre ya esta en uso, elija otro')
                nombre = valid_nombre()
                break
        else:
            break
    return nombre

def valid_repeticion_codigo(codigo):
    with open(materias.archivo, "r", encoding="UTF-8") as j:
        datos = json.load(j)
    for i in datos:
        if i['codigo'] == codigo:
            print('Ese codigo ya esta en uso, elija otro')
            return None
    else:
        return codigo

def valid_codigo_materia():
    while True:
        try:
            print('Ingrese 2 letras y un numero de 3 cifras (entre 100 y 999)')
            while True:
                letras = input('Letras >> ').upper()
                validez = r'^[A-ZÑ]{2}$'
                if not re.match(validez,letras):
                    print('Ingrese solo dos letras, sin simbolos ni nada mas')
                    continue
                else:
                    break
            while True:
                numeros = int(input('Numero >> '))
                if not (100 <= numeros <= 999):
                    print('Ingrese un numero acorde')
                else:
                    break
            
            codigo = (letras + str(numeros))
            if valid_repeticion_codigo(codigo):
                return codigo
            else:
                print('Ese codigo ya existe, ingrese uno diferente')

        except:
            print('Ingrese correctamente los datos') 

#validacion archivo usable
def valid_archivo(archivo):
    try:
        open(archivo, "r", encoding="UTF-8")
        return True
    except FileNotFoundError:
        print('El archivo no existe')
    except PermissionError:
        print('No se puede acceder al archivo')
    except OSError:
        print('Ha ocurrido un error al intentar abrir el archivo')
    return False

#que tipo de archivo es
def tipo_archivo(arch):
    if arch.endswith(".json"):
        return 'json'
    elif arch.endswith(".csv"):
        return 'csv'
    elif arch.endswith(".txt"):
        return 'txt'
    else:
        return None




