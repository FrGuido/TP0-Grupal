import main

def login():

    #definir usuario admin
    admin = 'admin'
    adminpasww = 'admin'

    #inicializo tipo de usuario a retornar
    usertype = ''

    while True:
        user = input('Ingrese su DNI: ')
        if user == admin:
            usertype = 'admin'

        elif any(x ['dni'] == user for x in main.profesores):
                usertype = 'p'
                break
        
        elif any(x ['dni'] == user for x in main.alumnos):
            break

        else:
             print('Ha ingresado un DNI no valido, intente de nuevo\n')

    while True:
        pasww = input('Ingrese su contraseña: ')
        if user == admin:
            usertype = 'admin'

        elif any(x ['pasw'] == user for x in main.profesores):
                usertype = 'p'
                break
        
        elif any(x ['pasw'] == user for x in main.alumnos):
            break

        else:
             print('Ha ingresado un DNI no valido, intente de nuevo\n')
    return