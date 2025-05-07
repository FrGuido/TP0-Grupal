import login
import cargar_leer
import almacen_datos
import menus
import random_test

def Bienvenida():
    print("""------------- Bienvenido al sistema de alumnado ------------- 
>Identifiquese
""")
    tipo, dni = login.login_users()

    if tipo == 'admin':
        print(f""" Bienvenido Administrador
    """)
        menus.menu_admin()

    elif tipo == 'p':
        nombre_profesor = cargar_leer.busqueda_nombre_profesores(dni)
        if nombre_profesor is None:
            print("Profesor no encontrado.")
        else:
            print(f""" Bienvenido {nombre_profesor}
    """)

    elif tipo == 'a':
        nombre_alumno = cargar_leer.busqueda_nombre_alumnos(dni)
        if nombre_alumno is None:
            print("Alumno no encontrado.")
        else:
            print(f""" Bienvenido {nombre_alumno}
    """)

almacen_datos.profesores = random_test.generar_profesores(20)
print(almacen_datos.profesores)
print('\n'*6)
Bienvenida()