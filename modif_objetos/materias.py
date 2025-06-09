import json
from modif_objetos import profesores
from validacion import validar
import almacen_datos

# --- Funciones para cargar y guardar materias ---
def cargar_materias():
    try:
        with open('materias.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_materias(materias):
    with open('materias.json', 'w', encoding='utf-8') as f:
        json.dump(materias, f, ensure_ascii=False, indent=4)

# --- Carga de materias ---
def Carga_Materias():
    print("\n--- Alta de Materia ---")
    materias = cargar_materias()
    materia = {
        'nombre': '',
        'profesores': [],
        'dias': [],
        'turno': ''
    }

    materias_comunes = ['Matemática', 'Lengua', 'Historia', 'Geografía', 'Biología', 'Física', 'Química', 'Inglés', 'Arte']
    print('Seleccione una materia del listado:')
    for indice, nombre in enumerate(materias_comunes, 1):
        print(f"{indice}. {nombre}")

    while True:
        try:
            opcion = int(input('Ingrese el número de la materia: '))
            if 1 <= opcion <= len(materias_comunes):
                materia['nombre'] = materias_comunes[opcion - 1]
                break
            else:
                print("❌ Opción inválida. Intente de nuevo.")
        except ValueError:
            print("❌ Entrada no válida. Ingrese un número.")

    print('\nIngrese el turno de esta materia (Mañana o Tarde)')
    while True:
        materia['turno'] = input('Turno: ').capitalize()
        if materia['turno'] not in almacen_datos.turnos:
            print('❌ Ingrese un turno válido (Mañana/Tarde).')
        elif any(m['nombre'] == materia['nombre'] and m['turno'] == materia['turno'] for m in materias):
            print('❌ Esta materia ya existe en ese turno, intente de nuevo.')
        else:
            break

    print('\nIngrese los días que esta materia se va a cursar (máximo 4).')
    print(f"Días disponibles: {', '.join(almacen_datos.dias)}")
    while len(materia['dias']) < 4:
        dia = input('Día a añadir (ENTER para terminar): ').capitalize()
        if not dia:
            if len(materia['dias']) == 0:
                print("⚠️ Debe ingresar al menos un día.")
                continue
            else:
                break
        if dia in almacen_datos.dias and dia not in materia['dias']:
            materia['dias'].append(dia)
            print(f"✔️ Día '{dia}' añadido.")
        else:
            print('❌ Ingrese un día válido y que no esté repetido.')
        if len(materia['dias']) < 4:
            elec = input('¿Desea añadir más días? (y/n): ').lower()
            if elec == 'n':
                break

    print('\nIngrese los DNI de los profesores para esta materia (ENTER para terminar):')
    while True:
        dni_input = input('DNI profesor: ')
        if not dni_input.strip():
            if len(materia['profesores']) == 0:
                print("⚠️ Debe ingresar al menos un profesor.")
                continue
            else:
                break
        try:
            dni = int(dni_input)
            nombre_prof = profesores.busqueda_nombre_profesores(dni)
            if nombre_prof:
                if nombre_prof not in materia['profesores']:
                    materia['profesores'].append(nombre_prof)
                    print(f"✔️ Profesor '{nombre_prof}' añadido.")
                else:
                    print('❌ Ese profesor ya está agregado.')
            else:
                print('❌ No existe un profesor con ese DNI.')
        except ValueError:
            print('❌ Ingrese un DNI válido.')

    materias.append(materia)
    guardar_materias(materias)
    print('\n✅ Materia añadida con éxito.')
    print(f"Materia: {materia['nombre']} | Turno: {materia['turno']}")
    print(f"Profesores: {', '.join(materia['profesores'])}")
    print(f"Días: {', '.join(materia['dias'])}")

# --- Buscar materia ---
def buscar_materia():
    print("\n--- Buscar Materia ---")
    materias = cargar_materias()
    while True:
        nombre = input('Ingrese el nombre de la materia: ').capitalize()
        turno = input('Ingrese el turno (Mañana/Tarde): ').capitalize()
        materia = next((m for m in materias if m['nombre'] == nombre and m['turno'] == turno), None)
        if materia:
            print("\n--- Datos de la Materia ---")
            for k, valor in materia.items():
                if isinstance(valor, list):
                    print(f"{k.capitalize():<15}: {', '.join(valor)}")
                else:
                    print(f"{k.capitalize():<15}: {valor}")
            return nombre, turno
        else:
            print(f'❌ La materia {nombre} del turno {turno} no existe.')
            elec = input('¿Desea salir? (Y para salir, N para intentar de nuevo): ').lower()
            if elec == 'y':
                return None, None

# --- Modificar materia ---
def modif_materias(nombre, turno):
    materias = cargar_materias()
    mat = next((m for m in materias if m['nombre'] == nombre and m['turno'] == turno), None)
    if not mat:
        print('❌ Materia no encontrada.')
        return

    while True:
        print("\n--- Modificar Materia ---")
        print(f"Materia actual: {mat['nombre']} | Turno: {mat['turno']}")
        print("[1] Nombre y Turno")
        print("[2] Profesores")
        print("[3] Días")
        print("---------------------------")
        print("[0] Salir")
        print("---------------------------")
        opcion = input("Seleccione una opción: ")
        if opcion not in ['0', '1', '2', '3']:
            input("❌ Opción inválida. Presione ENTER para volver a seleccionar.")
            continue

        if opcion == '0':
            print("Saliendo de la modificación de materia.")
            break

        # Opción 1: Nombre y Turno
        elif opcion == '1':
            while True:
                nuevo_nombre = input('Ingrese el nuevo nombre de la materia: ').capitalize()
                nuevo_turno = input('Ingrese el nuevo turno (Mañana/Tarde): ').capitalize()
                if nuevo_turno not in almacen_datos.turnos:
                    print('❌ Ingrese un turno válido.')
                elif any(m['nombre'] == nuevo_nombre and m['turno'] == nuevo_turno and m is not mat for m in materias):
                    print('❌ Ya existe una materia con ese nombre y turno.')
                else:
                    mat['nombre'] = nuevo_nombre
                    mat['turno'] = nuevo_turno
                    print('✔️ Nombre y turno modificados con éxito.')
                    break

        # Opción 2: Profesores
        elif opcion == '2':
            while True:
                print(f"Profesores actuales: {', '.join(mat['profesores'])}")
                deci = input('¿Quieres añadir (A) o eliminar (E) un profesor? (A/E): ').lower()
                if deci == 'a':
                    dni = validar.valid_dni()
                    nombre_prof = profesores.busqueda_nombre_profesores(dni)
                    if nombre_prof and nombre_prof not in mat['profesores']:
                        mat['profesores'].append(nombre_prof)
                        print(f"✔️ Profesor '{nombre_prof}' añadido.")
                    else:
                        print('❌ Profesor no encontrado o ya agregado.')
                elif deci == 'e':
                    elimina = input('Ingrese el nombre del profesor a eliminar: ').capitalize()
                    if elimina in mat['profesores']:
                        mat['profesores'].remove(elimina)
                        print(f"✔️ Profesor '{elimina}' eliminado.")
                    else:
                        print('❌ Ese profesor no está en la materia.')
                else:
                    print('❌ Ingrese un valor válido (A/E).')
                if input('¿Desea modificar más profesores? (y/n): ').lower() != 'y':
                    break

        # Opción 3: Días
        elif opcion == '3':
            while True:
                print(f"Días actuales: {', '.join(mat['dias'])}")
                deci = input('¿Quieres añadir (A) o eliminar (E) un día? (A/E): ').lower()
                if deci == 'a':
                    dia = input('Ingrese el día a añadir: ').capitalize()
                    if dia in almacen_datos.dias and dia not in mat['dias']:
                        mat['dias'].append(dia)
                        print(f"✔️ Día '{dia}' añadido.")
                    else:
                        print('❌ Día inválido o ya agregado.')
                elif deci == 'e':
                    dia = input('Ingrese el día a eliminar: ').capitalize()
                    if dia in mat['dias']:
                        mat['dias'].remove(dia)
                        print(f"✔️ Día '{dia}' eliminado.")
                    else:
                        print('❌ Ese día no está en la materia.')
                else:
                    print('❌ Ingrese un valor válido (A/E).')
                if input('¿Desea modificar más días? (y/n): ').lower() != 'y':
                    break

        guardar_materias(materias)
        print('✅ Materia modificada con éxito.')

# --- Eliminar materia ---
def eliminar_materia():
    print("\n--- Eliminar Materia ---")
    materias = cargar_materias()
    nombre = input('Ingrese el nombre de la materia a eliminar: ').capitalize()
    turno = input('Ingrese el turno (Mañana/Tarde): ').capitalize()
    materia = next((m for m in materias if m['nombre'] == nombre and m['turno'] == turno), None)
    if not materia:
        print(f"❌ No se encontró la materia '{nombre}' en el turno '{turno}'.")
        return
    print("\nMateria encontrada:")
    for k, valor in materia.items():
        if isinstance(valor, list):
            print(f"{k.capitalize():<15}: {', '.join(valor)}")
        else:
            print(f"{k.capitalize():<15}: {valor}")
    confirm = input("¿Está seguro que desea eliminar esta materia? (Y/N): ").lower()
    if confirm == 'y':
        materias.remove(materia)
        guardar_materias(materias)
        print("✅ Materia eliminada con éxito.")
    else:
        print("Operación cancelada.")

