from validacion from validacion import login
from modif_objetos import profesores,alumnos
import almacen_datos
import menus
import random_test

def Bienvenida():

    almacen_datos.menu_bien()

    tipo, dni = login.login_users()

#validacion segun usuario
    if tipo == 'admin':
        menus.menu_admin()

#usuarios no encontrados
    elif tipo == 'p':
        nombre_profesor = profesores.busqueda_nombre_profesores(dni)
        if nombre_profesor is None:
            print("Profesor no encontrado.")
        else:
            print(f""" Bienvenido {nombre_profesor}
    """)

    elif tipo == 'a':
        nombre_alumno = alumnos.busqueda_nombre_alumnos(dni)
        if nombre_alumno is None:
            print("Alumno no encontrado.")
        else:
            print(f""" Bienvenido {nombre_alumno}
    """)

random_test.imprimir_json()
print('\n'*6)
Bienvenida()