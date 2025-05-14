import almacen_datos

def login_users():
    # Definir usuario admin
    admin = 'admin'
    adminpasww = 'admin'

    # Inicializo tipo de usuario a retornar y contador
    usertype = ''
    user = ''
    
    while True:
        user = input('Ingrese su DNI: ').strip()
        
        # Usuario administrador
        if user == admin:
            while True:
                pasww = input('Ingrese su contraseña: ')
                if pasww == adminpasww:
                    usertype = 'admin'
                    break
                else:
                    print('Contraseña incorrecta. Intente de nuevo')
            break

        # Validación de DNI
        if len(user) != 8 or not user.isdigit():
            print('Ha ingresado un DNI no válido, intente de nuevo\n')
            continue

        # Profesores
        profesor = None
        for x in almacen_datos.profesores:
            if x ['dni'] == user:
                profesor = x
                break

        if profesor:
            for _ in range(3):
                pasww = input('Ingrese su contraseña: ')
                if pasww == profesor['pasw']:
                    usertype = 'p'
                    break
                else:
                    print('Contraseña incorrecta. Intente de nuevo')
            else:
                print('Ha hecho muchos intentos, intente desde 0')
            if usertype: break

        # Alumnos
        alumno = None
        for x in almacen_datos.alumnos:
            if x['dni'] == user:
                alumno = x
                break
            
        if alumno:
            for _ in range(3):
                pasww = input('Ingrese su contraseña: ')
                if pasww == alumno['pasw']:
                    usertype = 'a'
                    break
                else:
                    print('Contraseña incorrecta. Intente de nuevo')
            else:
                print('Ha hecho muchos intentos, intente desde 0')
            if usertype: break

        # DNI no encontrado
        if not (profesor or alumno or user == admin):
            print('El DNI no está en nuestra base de datos\n')

    return usertype, user
