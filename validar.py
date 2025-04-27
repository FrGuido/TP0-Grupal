import re

def valid_dni():
    while True:
        dni = (input('> '))
        if len(dni) == 8 and dni.isdigit():
            return int(dni)
        else:
            print('Ingreso un DNI invalido, intente nuevamente')

def valid_mail():
    while True:
        validez = r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑüÜ\.-]+@[a-zA-Z0-9\.-]+\.\w{2,4}$'
        mail = input("> ")
        if re.match(validez, mail) is not None:
            return mail
        else:
            print("Formato de mail inválido. Intente nuevamente.\n")

def valid_pasw():
    print('La contraseña debe tener al menos un carcter en mayuscula,\nun numero, un simbolo y al menos 10 caracteres')
    while True:
        contra = input('> ')
        if len(contra) < 10 or not re.search(r'[A-Z]',contra) or not re.search(r'\d', contra) or not re.search(r'\d', contra):
            print('Contraseña no valida, intente de nuevo')
        else:
            print('Contraseña valida')
            return contra

def valid_telefono():   
    while True:
        validez = r'^11\d{8}$'
        tel = input("> ")
        if re.match(validez, tel) is not None:
            return tel
        else:
            print("Formato de telefono inválido. Intente nuevamente.\n")