import main

def login():

    #definir usuario admin
    admin = 'admin'
    adminpasww = 'admin'

    #inicializo tipo de usuario a retornar y contador
    usertype = ''
    count = 0

    #verificacion login
    while True:
        user = input('Ingrese su DNI: ')
        if user == admin:
            while True:
                pasww = input('Ingrese su contraseña: ')
                if pasww == adminpasww:
                    usertype = 'admin'
                    break
                else:
                    print('Intente de nuevo')

        elif any(x ['dni'] == user for x in main.profesores):
            while True:
                count = count + 1
                pasww = input('Ingrese su contraseña: ')
                if any(x ['pasw'] == user for x in main.profesores):
                    usertype = 'p'
                    break
                elif count == 3:
                    print('Ha hecho muchos intentos, intente desde 0')
                    break
        
        elif any(x ['dni'] == user for x in main.alumnos):
            while True:
                count = count + 1
                pasww = input('Ingrese su contraseña: ')
                if any(x ['pasw'] == user for x in main.alumnos):
                    usertype = 'a'
                    break
                elif count == 3:
                    print('Ha hecho muchos intentos, intente desde 0')
                    break

                else:
                     print('Ha ingresado una contraseña no valida, intente de nuevo\n')

        else:
             print('Ha ingresado un DNI no valido, intente de nuevo\n')

        if usertype != '':
             break