notas = [] #matriz notas

alumnos = [] #lista alumnos

profesores = [] #lista profesores

materias = [] #lista materias con profesores

Registro = []

cursos = []

# --- Constantes y estructuras base ---

dias = ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes')
nros_cursos = ('1ero', '2do','3ero','4to','5to','6to')
turnos = ('Mañana', 'Tarde')
des_nota = [str(), str(), str(), float(), int()] #profesor, curso, alumno, nota, fecha(100625)

# Esqueleto cursos
curso = {   
    'nombre': str(),
    'cantidad alumnos': int(),
    'alumnos': [], # hasta 35
    'materias': [], # hasta 10
    'turno': str()
}

# Esqueleto materias
materia = {
    'nombre': str(),
    'profesores': [], # hasta 5
    'dias': [],
    'turno': str()
}

# Esqueleto alumnos
alumno = {
    'dni': int(),
    'nombre': str(),
    'apellido': str(),
    'fecha_nac': int(),
    'curso': str(),
    'turno': str(),
    'notas': [],
    'pasw': str()
}

# Esqueleto profesores
profesor = {
    'dni': int(),
    'nombre': str(),
    'fecha_nac': int(),
    'apellido': str(),
    'pasw': str(),
    'mail': str(),
    'telefono': int()
}

def menu_bien():
    print('\n'*10)
    print(f'{" Bienvenido al sistema de alumnado © ":-^58}')
    print(f'{"Trabajo Practico - Programacion 1":^58}')
    print(f'{"Grupo 10":^58}')
    print(f'{" - "*15:^58}')
    print('\n'*5)
