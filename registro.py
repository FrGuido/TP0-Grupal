import time

def registrar_agregado(tipo, nombre, apellido, dni):
    fecha_hora = time.ctime()
    tupla = ("AGREGADO", tipo, nombre, apellido, dni, fecha_hora)
    try:
        with open("Registro.txt", "a") as archivo:
            archivo.write(f"{tupla}\n")
        print("Registro de agregado guardado.")
    except Exception as e:
        print(f"Ocurrió un error al escribir el archivo: {e}")

def registrar_eliminado(tipo, nombre, apellido, dni):
    fecha_hora = time.ctime()
    tupla = ("ELIMINADO", tipo, nombre, apellido, dni, fecha_hora)
    try:
        with open("Registro.txt", "a") as archivo:
            archivo.write(f"{tupla}\n")
        print("Registro de eliminación guardado.")
    except Exception as e:
        print(f"Ocurrió un error al escribir el archivo: {e}")

def registrar_modificado(tipo, nombre, apellido, dni):
    fecha_hora = time.ctime()
    tupla = ("MODIFICADO", tipo, nombre, apellido, dni, fecha_hora)
    try:
        with open("Registro.txt", "a") as archivo:
            archivo.write(f"{tupla}\n")
        print("Registro de modificación guardado.")
    except Exception as e:
        print(f"Ocurrió un error al escribir el archivo: {e}")

def leer_modificaciones():
    try:
        with open("Registro.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.readlines()
            for linea in contenido:
                linea = linea.strip()

                if linea.startswith("(") and linea.endswith(")"):
                    linea = linea[1:-1]

                partes = linea.split(",", 5)

                if len(partes) == 6:
                    accion   = partes[0].strip().strip("'")
                    tipo     = partes[1].strip().strip("'")
                    campo_1  = partes[2].strip().strip("'")
                    campo_2  = partes[3].strip().strip("'")
                    campo_3  = partes[4].strip().strip("'")
                    fecha    = partes[5].strip().strip("'")

                    if tipo == "Nota":
                        print(f"""
Acción     : {accion}
Tipo       : {tipo}
Profesor   : {campo_1}
Alumno     : {campo_2}
Nota       : {campo_3}
Fecha      : {fecha}
                        """)
                    elif tipo == "Materia":
                        print(f"""
Acción     : {accion}
Tipo       : {tipo}
Materia    : {campo_1}
Código     : {campo_3}
Fecha      : {fecha}
                        """)
                    else:
                        print(f"""
Acción     : {accion}
Tipo       : {tipo}
Nombre     : {campo_1}
Apellido   : {campo_2}
DNI        : {campo_3}
Fecha      : {fecha}
                        """)
                else:
                    print(f"Línea malformada: {linea}")
    except FileNotFoundError:
        print("No hay modificaciones registradas todavía.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")