import menu_texto
import profesores
import alumnos
import materias
import cursos
import validar
import registro
import json


login_admin = 99999999
contraseña_admin = "admin"

def login():
    intentos = 4
    print('Ingrese su dni')
    dni = validar.valid_formato_dni()
    if dni != login_admin:
        try:
            with open(profesores.archivo,"r",encoding="UTF-8") as j:
                datos = json.load(j)
            for i in datos:
                if i['dni'] == dni:
                    print(f'Bienvenido profesor {i['nombre']} {i['apellido']}')
                    contra = input('Ingrese su contraseña, si la ha olvidado consulte con el admin\n>>')
                    while True:
                        if contra == i['pasw']:
                            print('Ha ingresado correctamente, bienvenido')
                            menu_profesor(i)
                            break
                        elif intentos == 1:
                            print('Demasiados intentos, saliendo del programa')
                            exit()
                        else:
                            intentos -= 1
                            print(f'Contraseña incorrecta, le quedan {intentos} intentos')
                    break
            
            with open(cursos.archivo,"r",encoding="UTF-8") as j:
                datos = json.load(j)
            
            for i in datos:
                for j in i['alumnos']:
                    if j['dni'] == dni:
                        print(f'Bienvenido alumno {j['nombre']} {j['apellido']}')
                    contra = input('Ingrese su contraseña, si la ha olvidado consulte con el admin\n>>')
                    while True:
                        if contra == j['pasw']:
                            print('Ha ingresado correctamente, bienvenido')
                            menu_alumno(j)
                            break
                        elif intentos == 1:
                            print('Demasiados intentos, saliendo del programa')
                            exit()
                        else:
                            intentos -= 1
                            print(f'Contraseña incorrecta, le quedan {intentos} intentos')
                    break
        except:
            menu_texto.error_archivo()            
    else:
        print(f'Bienvenido admin')
        while True:
            contra = input('Ingrese su contraseña\n>>')
            if contra == contraseña_admin:
                menu_admin()
                break
            elif intentos == 1:
                print('Demasiados intentos, saliendo del programa')
                exit()
            else:
                intentos -= 1
                print('Contraseña incorrecta, intente nuevamente')



def menu_admin():
    while True:

        #menu principal admin
        opcion = menu_texto.opciones_principal_admin()

        #salir del programa
        if opcion == "0":
            exit()

        #gestion profesores
        if opcion == "1":
            while True: 
                opcion = menu_texto.opciones_profesores()

                if opcion == "0":
                    break
                
                #añadir profesor
                elif opcion == "1":
                    profesores.añadir_profesor()

                #eliminar profesor
                elif opcion == "2":
                    profesores.eliminar_profesor()
                
                #modificar profesor
                elif opcion == "3":
                    profesores.modificar_profesor()

                #lista profesores
                elif opcion == "4":
                    profesores.listar_profesores()
                
                elif opcion == "5":
                    print('Ingrese el DNI del profesor a buscar')
                    a = profesores.buscar_profesor(validar.valid_formato_dni())
                    if a == None:
                        print('No existe ese profesor')
                    else:
                        menu_texto.imprimir_dic(a)
                    input('Presione Enter para volver al menu anteriro')

        #gestion alumnos
        elif opcion == "2":
            while True: 
                opcion = menu_texto.opciones_alumno()

                if opcion == "0":
                    break
                
                #añadir alumno
                elif opcion == "1":
                    alumnos.añadir_alumno()

                #eliminar alumnos
                elif opcion == "2":
                    alumnos.eliminar_alumno()
                
                #modificar alumnos
                elif opcion == "3":
                    alumnos.modificar_alumno()
                
                #modificar notas alumno
                elif opcion == "4":
                    alumnos.modificar_notas()

                #listar alumnos por curso
                elif opcion == "5":
                    print('Ingrese curso y turno para listar los alumnos')
                    alumnos.listar_alumnos()
                    input('Presione Enter para volver al menu')

                #buscar alumno
                elif opcion == "6":
                    print('Ingrese el DNI del alumno a buscar')
                    a = alumnos.buscar_alumno(validar.valid_formato_dni())
                    if a == None:
                        print('No existe ese alumno')
                    else:
                        menu_texto.imprimir_dic(a)
                    input('Presione Enter para volver al menu anterior')
    
        #gestion cursos
        elif opcion == "3":
            cursos.modificar_curso()
        
        #gestion de materias
        elif opcion == '4':
            while True: 
                opcion = menu_texto.opciones_materias()

                if opcion == "0":
                    break
                
                #añadir materia
                elif opcion == "1":
                    materias.crear_materia()

                #eliminar materia
                elif opcion == "2":
                    materias.elimiar_materia()

                #modificar materia
                elif opcion == "3":
                    materias.modificar_materia()

        elif opcion == '5':
            registro.leer_modificaciones()
            input('Presione Enter para volver')


def menu_profesor(profe):
    while True:
        opcion = menu_texto.opciones_principal_profesor()
        if opcion == "0":
            break
        #Ver mis materias
        elif opcion == "1":
            profesores.ver_materias_profe(profe)
            input('Presione Enter para continuar')

        #Modificar Notas
        elif opcion == "2":
            alumnos.modificar_notas(profe)

def menu_alumno(alumno):
    while True:
        opcion = menu_texto.opciones_principal_alumno()
        if opcion == "0":
            break
        #Ver mis notas
        elif opcion == "1":
            alumnos.ver_notas_alumno(alumno)
                


