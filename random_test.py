import random
import string

def generar_profesores(cantidad=20):
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

    return profesores