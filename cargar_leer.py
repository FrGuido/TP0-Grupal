import almacen_datos
import eliminar
import validar
import pedirFecha
import re

def Carga_Profesores(profe):

    print('Ingrese el nombre del profesor')
    print('vvv')
    profe['nombre'] = (input('> ')).capitalize()
    print()

    print('Ingrese el apellido del profesor')
    print('vvv')
    profe['apellido'] = (input('> ')).capitalize()
    print()

    print('Ingrese la fecha de nacimiento del profesor')
    print('vvv')
    profe['fecha_nac'] = pedirFecha.pedirFechaNac()

    print('Ingrese el dni del profesor')
    print('ejemplo --> 22334455')
    print('vvv')
    while True:
        dni = validar.valid_dni()
        if not any(almacen_datos.profesor['dni'] == dni for x in almacen_datos.profesores):
            profe['dni'] = dni
            break
        else:
            print('Ese dni ya existe en nuestra base de datos, ingrese un dni valido')
    print()

    print('Ingrese el mail del profesor')
    print('ejemplo --> nombreprofe@ejemplo.com')
    print('vvv')
    profe['mail'] = validar.valid_mail()

    print('Ingrese el telefono del profesor')
    print('ejemplo --> 1122334455')
    print('vvv')
    profe['telefono'] = validar.valid_telefono()

    print('Ingrese una contraseña para el profesor')
    print('vvv')
    profe['pasw'] = validar.valid_pasw()
    print()


    return profe

def busqueda_nombre_profesores(dni):
    for profesor in almacen_datos.profesores:
        if profesor['dni'] == dni:
            return f"{profesor['nombre']} {profesor['apellido']}"
    return None  # Devuelve None si no encuentra al profesor

def busqueda_datos_profesores(dni):
    for profesor in almacen_datos.profesores:
        if profesor['dni'] == dni:
            print(f"---- Datos Profesor del {profesor['nombre']} {profesor['apellido']} ----")
            print(f"Fecha de Nacimiento : {profesor['fecha_nac']}")
            print(f"Mail : {profesor['mail']}")
            print(f"Telefono : {profesor['telefono']}")
            listar_materias_prof(profesor['dni'])
            print('-'*20)
            break

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

def modif_prof(elemento):
    while True:
        for prof in almacen_datos.profesores:
            if prof['dni'] == elemento:
                profesor = prof

        while True:
            opciones = 7
            print(f'Que desea modificar?')
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
            if opcion in [str(i) for i in range(0, opciones + 1)]:
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        while True:

            if opcion == '0':
                break

            elif opcion == '1':
                print()
                print('Modificando el Nombre del profesor:')
                profesor['nombre'] = input('> ').capitalize()
                print('Nombre cambiado con exito!')
                print('-'*15)
                break

            elif opcion == '2':
                print()
                print('Modificando el Apellido del profesor:')
                profesor['apellido'] = input('> ').capitalize()
                print('Apellido cambiado con exito!')
                print('-'*15)
                break

            elif opcion == '3':
                print()
                print('Modificando el DNI del profesor:')
                while True:
                    dni = validar.valid_dni()
                    if not any(almacen_datos.profesor['dni'] == dni for x in almacen_datos.profesores):
                        profesor['dni'] = dni
                        break
                    else:
                        print('Ese dni ya existe en nuestra base de datos, ingrese un dni valido')
                        print()
                print('DNI cambiado con exito!')
                print('-'*15)
                break

            elif opcion == '4':
                print()
                print('Modificando la Fecha de Nacimiento del profesor:')
                profesor['fecha_nac'] = pedirFecha.pedirFechaNac()
                print('Fecha de Nacimiento cambiado con exito!')
                print('-'*15)
                break
            
            elif opcion == '5':
                print()
                print('Modificando el Mail del profesor:')
                profesor['mail'] = validar.valid_mail()
                print('Mail cambiado con exito!')
                print('-'*15)
                break

            elif opcion == '6':
                print()
                print('Modificando el Telefono del profesor:')
                profesor['telefono'] = validar.valid_telefono()
                print('Telefono cambiado con exito!')
                print('-'*15)
                break

            elif opcion == '7':
                print()
                print('Modificando la Contraseña del profesor:')
                profesor['pasw'] = validar.valid_pasw()
                print('Contraseña cambiado con exito!')
                print('-'*15)
                break
        
        if opcion == '0':
            for prof in almacen_datos.profesores:
                if prof['dni'] == elemento:
                    prof = profesor
                    break
            break

def modif_materias(nombre, turno):
    # Buscar la materia a modificar
    materia_mod = None
    for mat in almacen_datos.materias:
        if mat['nombre'] == nombre and mat['turno'] == turno:
            materia_mod = mat
            break
    
    if materia_mod is None:
        print("Materia no encontrada.")
        return
    
    while True:
        print("\nDatos actuales de la materia:")
        print(f"Nombre: {materia_mod['nombre']}")
        print(f"Turno: {materia_mod['turno']}")
        print(f"Días: {', '.join(materia_mod['dias'])}")
        print(f"Profesores: {len(materia_mod['profesores'])}")
        
        print("\n¿Qué desea modificar?")
        print("[1] Nombre")
        print("[2] Turno")
        print("[3] Días de cursada")
        print("[4] Profesores")
        print("[0] Volver")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '0':
            break
            
        elif opcion == '1':
            nuevo_nombre = input("Ingrese el nuevo nombre de la materia: ").capitalize()
            # Verificar que no exista otra materia con mismo nombre y turno
            existe = any(m for m in almacen_datos.materias 
                        if m['nombre'] == nuevo_nombre and 
                        m['turno'] == materia_mod['turno'] and 
                        m != materia_mod)
            if existe:
                print("Ya existe una materia con ese nombre y turno.")
            else:
                materia_mod['nombre'] = nuevo_nombre
                print("Nombre modificado con éxito.")
                
        elif opcion == '2':
            nuevo_turno = input("Ingrese el nuevo turno (Mañana/Tarde): ").capitalize()
            if nuevo_turno not in almacen_datos.turnos:
                print("Turno inválido.")
            else:
                # Verificar que no exista otra materia con mismo nombre y nuevo turno
                existe = any(m for m in almacen_datos.materias 
                            if m['nombre'] == materia_mod['nombre'] and 
                            m['turno'] == nuevo_turno and 
                            m != materia_mod)
                if existe:
                    print("Ya existe una materia con ese nombre en el turno seleccionado.")
                else:
                    materia_mod['turno'] = nuevo_turno
                    print("Turno modificado con éxito.")
                    
        elif opcion == '3':
            print("Días actuales:", ', '.join(materia_mod['dias']))
            materia_mod['dias'] = []
            while True:
                dia = input(f"Ingrese un día a añadir ({', '.join(almacen_datos.dias)}): ").capitalize()
                if dia in almacen_datos.dias:
                    if dia not in materia_mod['dias']:
                        materia_mod['dias'].append(dia)
                        print(f"Día {dia} añadido.")
                    else:
                        print("Este día ya está asignado.")
                else:
                    print("Día inválido.")
                
                if len(materia_mod['dias']) >= 4:
                    print("Límite de días alcanzado (4).")
                    break
                    
                resp = input("¿Desea añadir otro día? (s/n): ").lower()
                if resp != 's':
                    break
                    
        elif opcion == '4':
            print("\nGestión de profesores para esta materia:")
            while True:
                print("\n[1] Añadir profesor")
                print("[2] Eliminar profesor")
                print("[0] Volver")
                
                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == '0':
                    break
                    
                elif sub_opcion == '1':
                    dni = validar.valid_dni()
                    profesor = next((p for p in almacen_datos.profesores if p['dni'] == dni), None)
                    if profesor:
                        if dni not in [p[0] for p in materia_mod['profesores']]:
                            materia_mod['profesores'].append([dni, profesor['nombre'], profesor['apellido']])
                            print(f"Profesor {profesor['nombre']} {profesor['apellido']} añadido.")
                        else:
                            print("Este profesor ya está asignado a la materia.")
                    else:
                        print("Profesor no encontrado.")
                        
                elif sub_opcion == '2':
                    if not materia_mod['profesores']:
                        print("No hay profesores asignados.")
                        continue
                        
                    print("\nProfesores asignados:")
                    for i, prof in enumerate(materia_mod['profesores'], 1):
                        print(f"{i}. {prof[1]} {prof[2]} (DNI: {prof[0]})")
                    
                    try:
                        num = int(input("Seleccione el número de profesor a eliminar (0 para cancelar): "))
                        if num == 0:
                            continue
                        if 1 <= num <= len(materia_mod['profesores']):
                            removed = materia_mod['profesores'].pop(num-1)
                            print(f"Profesor {removed[1]} {removed[2]} eliminado.")
                        else:
                            print("Número inválido.")
                    except ValueError:
                        print("Ingrese un número válido.")
                
                else:
                    print("Opción inválida.")
                    
        else:
            print("Opción inválida.")



def Carga_Alumnos(alumno):
    print('Ingrese el nombre del alumno')
    alumno['nombre'] = (input('> ')).capitalize()
    print()

    print('Ingrese el apellido del alumno')
    alumno['apellido'] = (input('> ')).capitalize()
    print()

    print('Ingrese el dni del alumno')
    while True:
        dni = validar.valid_dni()
        if not any(a['dni'] == dni for a in almacen_datos.alumnos):
            alumno['dni'] = dni
            break
        else:
            print('Ese dni ya existe en nuestra base de datos, ingrese un dni valido')
    print()

    print('Ingrese la fecha de nacimiento del alumno')
    alumno['fecha_nac'] = pedirFecha.pedirFechaNac()

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

    print('Ingrese el curso del alumno')
    alumno['curso'] = elegir_curso()

    # Añadir el alumno a la lista
    almacen_datos.alumnos.append(alumno)
    print("Alumno añadido con éxito.")
    print("\nLista actual de alumnos:")
    for a in almacen_datos.alumnos:
        print("-" * 60)
        print(f"DNI: {alumno['dni']}")
        print(f"Nombre: {alumno['nombre']} {alumno['apellido']}")
        print(f"Fecha de nacimiento: {alumno['fecha_nac']}")
        print(f"Curso: {alumno['curso']}")
        print(f"Turno: {alumno['turno']}")
        print(f"Notas: {alumno['notas']}")
    print("-" * 60)


def busqueda_nombre_alumnos(dni):
    for alumno in almacen_datos.alumnos:
        if alumno['dni'] == dni:
            return f"{alumno['nombre']} {alumno['apellido']}"
    return None  # Devuelve None si no encuentra al alumno

def busqueda_datos_alumnos(dni):
    print("Buscando DNI:", dni)
    for alumno in almacen_datos.alumnos:
        print("Revisando alumno:", alumno)  # Depuración
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
    return None  # Devuelve None si no encuentra al alumno

def modif_alumno(dni):
    alumno = next((a for a in almacen_datos.alumnos if a['dni'] == dni), None)
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
                if not any(a['dni'] == nuevo_dni for a in almacen_datos.alumnos if a['dni'] != dni):
                    alumno['dni'] = nuevo_dni
                    print("DNI modificado con éxito.")
                    break
                else:
                    print("Este DNI ya está en uso. Intente con otro.")
                    
        elif opcion == '4':
            print("Fecha de nacimiento actual:", alumno['fecha_nac'])
            print("Ingrese la nueva fecha de nacimiento:")
            alumno['fecha_nac'] = pedirFecha.pedirFechaNac()
            print("Fecha de nacimiento modificada con éxito.")
            
        elif opcion == '5':
            print("Turno actual:", alumno['turno'])
            while True:
                nuevo_turno = input("Ingrese nuevo turno (Mañana/Tarde): ").capitalize()
                if nuevo_turno in almacen_datos.turnos:
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

def ver_notas_alumno(dni):
    alumno = next((a for a in almacen_datos.alumnos if a['dni'] == dni), None)
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
    print(almacen_datos.nros_cursos, sep=' | ')
    curso = input('> ').lower()
    while True:
        if curso not in almacen_datos.nros_cursos:
            print('Ingrese un curso valido')
        else:
            return curso



def Carga_Materias(materia):
    while True:
        t = None
        print('Ingrese el nombre de la materia:')
        materia['nombre'] = input('> ').capitalize()
        existe = False
        for i in almacen_datos.materias:
            if i['nombre'] == materia['nombre']:
                if not existe:
                    print(f'Esa materia ya existe, debera incluirla con un turno distinto')
                    existe = True
                t = i['turno']

        print()
        print('Ingrese el turno de esta materia (Mañana o Tarde)')
        while True:
            materia['turno'] = input('> ').capitalize()
            if materia['turno'] not in almacen_datos.turnos:
                print('Ingrese un turno valido\n')
            else:
                break
        if materia['turno'] == t:
            print('Esta materia en este turno ya existe, intente de nuevo')
        else:
            break
    print('Ingrese los dias que esta materia se va a cursar, limite 4')
    while True:
        dia = input(f'Ingrese el dia a añadir\n{almacen_datos.dias}').capitalize()
        if dia in almacen_datos.dias:
            materia['dias'].append(dia)
            while True:
                print('Desea añadir mas dias? (y o n)')
                elec = input('> ').lower()
                if elec == 'y':
                    break
                elif elec == 'n':
                    print('-'*20,'\n')
                    break
                else:
                    print('Por favor ingrese una de las dos letras indicadas')
                    elec = input('(Ingrese Y o N): ').lower()
        else:
            print('Ingrese un dia valido por favor')
            print('-'*10)
        
        if elec == 'n':
            break
    
    return materia.copy()

def buscar_materia():
    while True:
        elec = ''
        materia = None
        nombre = input('Ingrese la materia\n> ').capitalize()
        turno = input('Ingrese el turno \n>').capitalize()

        for mat in almacen_datos.materias:
            if mat['nombre'] == nombre and mat['turno'] == turno:
                materia = mat
                break
        if materia is None:
            print(f'La materia {nombre} del turno {turno}, no existe. Desea salir o intentar nuevamente?')
            while True:
                elec = input('Ingrese "Y" para salir y "N" para intentar de nuevo').lower()
                if elec == 'y':
                    nombre,turno = None,None
                    break
                elif elec == 'n':
                    break
                else:
                    print('Ingrese un valor adecuado')
        
        if elec == 'y':
            break

        if materia is not None:
            for k, valor in materia.items():
                print(f"{(k.capitalize()):<15}{str(valor):>30}")
            return nombre,turno
    
    return nombre,turno
    
def modif_materias(nombre,turno):
    while True:
        for x in almacen_datos.materias:
            if x['nombre'] == nombre and x['turno'] == turno:
                mat = x

        while True:
            opciones = 3
            print(f'Que desea modificar?')
            print("[1] Nombre y Turno")
            print("[2] Profesores")
            print("[3] Dias")
            print("---------------------------")
            print("[0] Salir")
            print("---------------------------")
            print()
            opcion = input("Seleccione una opción: ")
            if opcion in [str(i) for i in range(0, opciones + 1)]:
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        while True:

            if opcion == '0':
                break

            elif opcion == '1':
                while True:
                    t = None
                    print('Ingrese el nombre de la materia para cambiar:')
                    mat['nombre'] = input('> ').capitalize()
                    for i in almacen_datos.materias:
                        if i['nombre'] == mat['nombre']:
                            print(f'Esa materia ya existe, y se encuentra en el turno {i["turno"]}\nDesea continuar igualmente, debera incluirla con un turno distinto')
                            t = i['turno']
                    print()
                    print('Ingrese el turno a cambiar de esta materia (Mañana o Tarde)')
                    while True:
                        mat['turno'] = input('> ').capitalize()
                        if mat['turno'] not in almacen_datos.turnos:
                            print('Ingrese un turno valido\n')
                        else:
                            break
                    if mat['turno'] == t:
                        print('Esta materia en este turno ya existe, intente de nuevo')
                    else:
                        break

            elif opcion == '2':
                while True:
                    print()
                    print('Modificando lista de profesores de la materia:')
                    print('Estas son las materias:')
                    print(mat['profesores'])
                    print('Quieres añadir o eliminar alguna?')
                    deci = input('Ingresa A para añadir o E para eliminar').lower()
                    if deci == 'a':
                        while True:
                            print('Ingrese el dni del profesor a agregar')
                            dni = validar.valid_dni()
                            nombre, apellido = busqueda_nombre_profesores(dni)
                            if nombre is not None:
                                mat['profesores'].append(nombre)
                                break
                            else:
                                print('Ingrese un DNI que exista')
                    elif deci == 'e':
                        while True:
                            break
                    print('Apellido cambiado con exito!')
                    print('-'*15)
                    break

            elif opcion == '3':
                print()
                print('Modificando el DNI del profesor:')
                while True:
                    dni = validar.valid_dni()
                    if not any(almacen_datos.profesor['dni'] == dni for x in almacen_datos.profesores):
                        mat['dni'] = dni
                        break
                    else:
                        print('Ese dni ya existe en nuestra base de datos, ingrese un dni valido')
                        print()
                print('DNI cambiado con exito!')
                print('-'*15)
                break

        
        if opcion == '0':
            for x in almacen_datos.materias:
                if x['nombre'] == nombre and x['turno'] == turno:
                    x = mat
                    break
            break