import json
from validacion import validar
import almacen_datos
from modif_objetos import eliminar

# --- Funciones para cargar y guardar profesores ---
def cargar_profesores():
    with open('profesores.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def guardar_profesores(profesores):
    with open('profesores.json', 'w', encoding='utf-8') as f:
        json.dump(profesores, f, ensure_ascii=False, indent=4)

# --- Función para agregar un profesor ---
def Carga_Profesores():
    profesores = cargar_profesores()
    profe = {}

    print('Ingrese el nombre del profesor')
    profe['nombre'] = validar.valid_nombre()
    print()

    print('Ingrese el apellido del profesor')
    profe['apellido'] = (input('> ')).capitalize()
    print()

    print('Ingrese la fecha de nacimiento del profesor')
    profe['fecha_nac'] = validar.pedirFecha()

    print('Ingrese el dni del profesor')
    print('ejemplo --> 22334455')
    while True:
        dni = validar.valid_dni()
        if not any(p['dni'] == dni for p in profesores):
            profe['dni'] = dni
            break
        else:
            print('Ese dni ya existe en nuestra base de datos, ingrese un dni valido')
    print()

    print('Ingrese el mail del profesor')
    print('ejemplo --> nombreprofe@ejemplo.com')
    profe['mail'] = validar.valid_mail()

    print('Ingrese el telefono del profesor')
    print('ejemplo --> 1122334455')
    profe['telefono'] = validar.valid_telefono()

    print('Ingrese una contraseña para el profesor')
    profe['pasw'] = validar.valid_pasw()
    print()

    profe['materias'] = []
    profe['cursos'] = []

    profesores.append(profe)
    guardar_profesores(profesores)
    print("Profesor añadido con éxito.")

def busqueda_nombre_profesores(dni):
    profesores = cargar_profesores()
    for profesor in profesores:
        if profesor['dni'] == dni:
            return f"{profesor['nombre']} {profesor['apellido']}"
    return None  # Devuelve None si no encuentra al profesor

def busqueda_datos_profesores(dni):
    profesores = cargar_profesores()
    for profesor in profesores:
        if profesor['dni'] == dni:
            print(f"---- Datos Profesor del {profesor['nombre']} {profesor['apellido']} ----")
            print(f"Fecha de Nacimiento : {profesor['fecha_nac']}")
            print(f"Mail : {profesor['mail']}")
            print(f"Telefono : {profesor['telefono']}")
            print('-'*20)
            return profesor
    print("Profesor no encontrado.")
    return None

def listar_materias_prof(dni):
    mat = buscar_materias_prof(dni)
    print('Materias:')
    for i in mat:
        print(f'> {i}')

def buscar_materias_prof(dni):
    materias = []
    for materia in almacen_datos.materias:
        for fila in almacen_datos.materia['profesores']:
            if dni in fila:
                materias.append(materia['nombre'])
                break
    return materias

def modif_prof(dni):
    profesores = cargar_profesores()
    profesor = next((p for p in profesores if p['dni'] == dni), None)
    if not profesor:
        print("Profesor no encontrado.")
        return

    while True:
        print(f'¿Qué desea modificar?')
        print("[1] Nombre")
        print("[2] Apellido")
        print("[3] DNI")
        print("[4] Fecha de Nacimiento")
        print("[5] Mail")
        print("[6] Telefono")
        print("[7] Contraseña")
        print("---------------------------")
        print("[0] Salir")
        print("---------------------------")
        print()
        opcion = input("Seleccione una opción: ")

        if opcion == '0':
            break

        elif opcion == '1':
            print('Modificando el Nombre del profesor:')
            profesor['nombre'] = input('> ').capitalize()
            print('Nombre cambiado con exito!')

        elif opcion == '2':
            print('Modificando el Apellido del profesor:')
            profesor['apellido'] = input('> ').capitalize()
            print('Apellido cambiado con exito!')

        elif opcion == '3':
            print('Modificando el DNI del profesor:')
            while True:
                nuevo_dni = validar.valid_dni()
                if not any(p['dni'] == nuevo_dni for p in profesores if p['dni'] != dni):
                    profesor['dni'] = nuevo_dni
                    print('DNI cambiado con exito!')
                    break
                else:
                    print('Ese dni ya existe en nuestra base de datos, ingrese un dni valido')

        elif opcion == '4':
            print('Modificando la Fecha de Nacimiento del profesor:')
            profesor['fecha_nac'] = validar.pedirFecha()
            print('Fecha de Nacimiento cambiado con exito!')

        elif opcion == '5':
            print('Modificando el Mail del profesor:')
            profesor['mail'] = validar.valid_mail()
            print('Mail cambiado con exito!')

        elif opcion == '6':
            print('Modificando el Telefono del profesor:')
            profesor['telefono'] = validar.valid_telefono()
            print('Telefono cambiado con exito!')

        elif opcion == '7':
            print('Modificando la Contraseña del profesor:')
            profesor['pasw'] = validar.valid_pasw()
            print('Contraseña cambiado con exito!')

        else:
            print("Opción inválida.")

        guardar_profesores(profesores)

def modif_materias_prof(dni):
    mats = []
    lista = buscar_materias_prof(dni)
    if not lista:
        print('El profesor no posee materias')
    else:
        print('El profesor posee la siguientes materias:')
        print(" | ".join(map(str, lista)))
    
    print('')
    for materia in almacen_datos.materias:
        for fila in almacen_datos.materia['nombre']:
            print (materia['nombre']+ ' | ')
            mats.append(materia['nombre'])