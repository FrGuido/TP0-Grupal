import re

#validacion de dni
def valid_dni():
    while True:
        dni = (input('> '))
        if len(dni) == 8 and dni.isdigit(): #El DNI debe tener 8 digitos
            return int(dni)
        else:
            print('Ingreso un DNI invalido, intente nuevamente') #Mensaje de correccion

#validacion de mail
def valid_mail():
    while True:
        validez = r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑüÜ\.-]+@[a-zA-Z0-9\.-]+\.\w{2,4}$' #Caracteres validos para el mail
        mail = input("> ")
        if re.match(validez, mail) is not None:
            return mail
        else:
            print("Formato de mail inválido. Intente nuevamente.\n")

#validacion de contrsenia
def valid_pasw():
    print('La contraseña debe tener al menos un carcter en mayuscula,\nun numero, un simbolo y al menos 10 caracteres')
    while True:
        contra = input('> ')
        if len(contra) < 10 or not re.search(r'[A-Z]',contra) or not re.search(r'\d', contra) or not re.search(r'[^A-Za-z0-9]', contra):
            print('Contraseña no valida, intente de nuevo')
        else:
            print('Contraseña valida')
            return contra

#validacion de fecha
def valid_telefono():   
    while True:
        validez = r'^11\d{8}$'
        tel = input("> ")
        if re.match(validez, tel) is not None:
            return tel
        else:
            print("Formato de telefono inválido. Intente nuevamente.\n")

#validcion de fecha
def pedirFecha():
    while True: #bucle, termina cuando se ingrese una fecha valida
        fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")
        f = fecha.split("/")

        if len(f) == 3:
            try:
                dia = int(f[0]) 
                mes = int(f[1])
                año = int(f[2])

                bisiesto = añoBisiesto(año) #valido el año bisisesto

                diasMes = [31, 29 if bisiesto else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #lista de dias de meses, con febrero arreglado

                if 1 <= mes <= 12 and 1 <= dia <= diasMes[mes - 1]:
                    #print("Fecha válida.")
                    return (f'{dia}/{mes}/{año}')
                else:
                    print("Fecha inválida. Día o mes fuera de rango.")
            except ValueError:
                print("Error: ingrese solo números en el formato correcto.")
        else:
            print("Formato incorrecto. Use dd/mm/aaaa.")

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
        return 
    
def valid_nombre():
    while True:
        validez = r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑüÜ]'
        nombre = input("> ")
        if re.match(validez, nombre) is not None:
            return nombre
        else:
            print("Formato de nombre inválido. Intente nuevamente.\n")