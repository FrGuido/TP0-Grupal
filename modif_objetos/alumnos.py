import json
from validacion import validar

# --- Funciones para cargar y guardar alumnos ---
def cargar_alumnos():
    with open('alumnos.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def guardar_alumnos(alumnos):
    with open('alumnos.json', 'w', encoding='utf-8') as f:
        json.dump(alumnos, f, ensure_ascii=False, indent=4)

# --- Función para agregar un alumno ---
def Carga_Alumnos():
    alumnos = cargar_alumnos()
    alumno = {}

    # nombre
    print('Ingrese el nombre del alumno')
    alumno['nombre'] = (input('> ')).capitalize()
    print()

    # apellido
    print('Ingrese el apellido del alumno')
    alumno['apellido'] = (input('> ')).capitalize()
    print()

    # dni
    print('Ingrese el dni del alumno')
    while True:
        dni = validar.valid_dni()
        if not any(a['dni'] == dni for a in alumnos):
            alumno['dni'] = dni
            break
        else:
            print('Ese dni ya existe en nuestra base de datos, ingrese un dni valido')
    print()

    # fecha nacimiento
    print('Ingrese la fecha de nacimiento del alumno')
    alumno['fecha_nac'] = validar.pedirFecha()

    # turno
    print('Ingrese el turno del alumno')
    while True:
        turno = input('Ingrese M (para turno Mañana) o T (para turno Tarde): ').lower()
        if turno == 'm':
            alumno['turno'] = 'Mañana'
            break
        elif turno == 't':
            alumno['turno'] = 'Tarde'
            break
        else:
            print('Ingrese un valor valido, intente de nuevo')

    # curso
    print('Ingrese el curso del alumno')
    alumno['curso'] = elegir_curso()

    # notas y pasw
    alumno['notas'] = []
    print('Ingrese la contraseña del alumno')
    alumno['pasw'] = validar.valid_pasw()

    alumnos.append(alumno)
    guardar_alumnos(alumnos)
    print("Alumno añadido con éxito.")
    print("\nLista actual de alumnos:")
    for a in alumnos:
        print("-" * 60)
        print(f"DNI: {a['dni']}")
        print(f"Nombre: {a['nombre']} {a['apellido']}")
        print(f"Fecha de nacimiento: {a['fecha_nac']}")
        print(f"Curso: {a['curso']}")
        print(f"Turno: {a['turno']}")
        print(f"Notas: {a['notas']}")
    print("-" * 60)

# --- Funciones de búsqueda y modificación ---
def busqueda_nombre_alumnos(dni):
    alumnos = cargar_alumnos()
    for alumno in alumnos:
        if alumno['dni'] == dni:
            return f"{alumno['nombre']} {alumno['apellido']}"
    return None

def busqueda_datos_alumnos(dni):
    alumnos = cargar_alumnos()
    print("Buscando DNI:", dni)
    for alumno in alumnos:
        if isinstance(alumno, dict) and 'dni' in alumno:
            if alumno['dni'] == dni:
                print(f"---- Datos del Alumno {alumno['nombre']} {alumno['apellido']} ----")
                print(f"DNI: {alumno['dni']}")
                print(f"Fecha de Nacimiento: {alumno['fecha_nac']}")
                print(f"Curso: {alumno['curso']}")
                print(f"Turno: {alumno['turno']}")
                print('-'*20)
                return alumno
    print("Alumno no encontrado.")
    return None

def modif_alumno(dni):
    alumnos = cargar_alumnos()
    alumno = next((a for a in alumnos if a['dni'] == dni), None)
    if not alumno:
        print("Alumno no encontrado.")
        return

    while True:
        print("\n¿Qué desea modificar?")
        print("[1] Nombre")
        print("[2] Apellido")
        print("[3] DNI")
        print("[4] Fecha de Nacimiento")
        print("[5] Turno")
        print("[6] Curso")
        print("[7] Contraseña")
        print("[0] Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == '0':
            break

        elif opcion == '1':
            print("Nombre actual:", alumno['nombre'])
            alumno['nombre'] = input("Nuevo nombre: ").capitalize()
            print("Nombre modificado con éxito.")

        elif opcion == '2':
            print("Apellido actual:", alumno['apellido'])
            alumno['apellido'] = input("Nuevo apellido: ").capitalize()
            print("Apellido modificado con éxito.")

        elif opcion == '3':
            print("DNI actual:", alumno['dni'])
            while True:
                nuevo_dni = validar.valid_dni()
                if not any(a['dni'] == nuevo_dni for a in alumnos if a['dni'] != dni):
                    alumno['dni'] = nuevo_dni
                    print("DNI modificado con éxito.")
                    break
                else:
                    print("Este DNI ya está en uso. Intente con otro.")

        elif opcion == '4':
            print("Fecha de nacimiento actual:", alumno['fecha_nac'])
            print("Ingrese la nueva fecha de nacimiento:")
            alumno['fecha_nac'] = validar.pedirFecha()
            print("Fecha de nacimiento modificada con éxito.")

        elif opcion == '5':
            print("Turno actual:", alumno['turno'])
            while True:
                nuevo_turno = input("Ingrese nuevo turno (Mañana/Tarde): ").capitalize()
                if nuevo_turno in ['Mañana', 'Tarde']:
                    alumno['turno'] = nuevo_turno
                    print("Turno modificado con éxito.")
                    break
                else:
                    print("Turno inválido. Intente nuevamente.")

        elif opcion == '6':
            print("Curso actual:", alumno['curso'])
            print("Seleccione nuevo curso:")
            alumno['curso'] = elegir_curso()
            print("Curso modificado con éxito.")

        elif opcion == '7':
            print("Ingrese nueva contraseña:")
            alumno['pasw'] = validar.valid_pasw()
            print("Contraseña modificada con éxito.")

        else:
            print("Opción inválida.")

    guardar_alumnos(alumnos)

def ver_notas_alumno(dni):
    alumnos = cargar_alumnos()
    alumno = next((a for a in alumnos if a['dni'] == dni), None)
    if not alumno:
        print("Alumno no encontrado.")
        return

    print(f"\nNotas de {alumno['nombre']} {alumno['apellido']}:")
    if not alumno['notas']:
        print("El alumno no tiene notas cargadas.")
    else:
        for nota in alumno['notas']:
            print(f"Materia: {nota[1]} - Nota: {nota[3]} - Fecha: {nota[4]}")

def elegir_curso():
    cursos = ('1ero', '2do','3ero','4to','5to','6to')
    print(cursos, sep=' | ')
    while True:
        curso = input('> ')
        if curso not in cursos:
            print('Ingrese un curso valido')
        else:
            return curso

# --- Funciones de utilidad ya están abajo ---
def buscar_alumno_por_dni(dni):
    alumnos = cargar_alumnos()
    for alumno in alumnos:
        if alumno['dni'] == dni:
            return alumno
    return None

def agregar_alumno(nuevo_alumno):
    alumnos = cargar_alumnos()
    alumnos.append(nuevo_alumno)
    guardar_alumnos(alumnos)

