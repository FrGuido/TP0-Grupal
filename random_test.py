import random
import string
import json

def generar_profesores(cantidad=10):
    nombres = ['Juan', 'María', 'Luis', 'Ana', 'Carlos', 'Laura', 'Pedro', 'Lucía', 'José', 'Camila']
    apellidos = ['Gómez', 'Pérez', 'Fernández', 'López', 'Martínez', 'Díaz', 'Sánchez', 'Ramírez']
    
    profesores = []

    for _ in range(cantidad):
        dni = random.randint(10000000, 49999999)
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        fecha_nac = random.randint(19600101, 20050101)  # formato AAAAMMDD
        pasw = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        mail = f"{nombre.lower()}.{apellido.lower()}@mail.com"
        telefono = int("11"+ str(random.randint(10000000, 99999999)))

        profesor = {
            'dni': dni,
            'nombre': nombre,
            'fecha_nac': fecha_nac,
            'apellido': apellido,
            'pasw': pasw,
            'mail': mail,
            'telefono': telefono
        }

        profesores.append(profesor)

    with open("profesores.json", "w", encoding="utf-8") as j:
        json.dump(profesores,j ,indent=7, ensure_ascii=False)


def imprimir_json():
    with open("profesores.json","r",encoding="utf-8") as j:
        datos = json.load(j)
        for i in datos:
            print(i)
        

#generar_profesores()