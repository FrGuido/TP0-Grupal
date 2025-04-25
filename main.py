import login
import cargar_leer
import almacen_datos
import menus

def Bienvenida():
    print("""------------- Bienvenido al sistema de alumnado -------------
>Identifiquese
""")
    tipo,dni = login.login_users()

    if tipo=='admin':
        print(f""" Bienvenido Administrador
    """)
        menus.menu_admin()
        
    elif tipo=='p':
        print(f""" Bienvenido {cargar_leer.busqueda_nombre_profesores(dni)})
    """)
    elif tipo=='a':
        print(f""" Bienvenido {cargar_leer.busqueda_nombre_alumnos(dni)})
    """)

Bienvenida()