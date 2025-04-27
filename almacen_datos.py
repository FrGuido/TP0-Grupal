
notas = [] #matriz notas

alumnos = [] #lista alumnos

profesores = [] #lista profesores

materias = [] #lista materias con profesores

Registro = []

cursos = []

dias = ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes')

nros_cursos = ('1ero', '2do','3ero','4to','5to','6to') #tupla cursos

turnos = ('Mañana', 'Tarde')

des_nota = [str(), str(), str(), float(), int()] #profesor, curso, alumno, nota, fecha(100625)



#esqueleto cursos
curso = {
    'nombre':str(),
    'cantidad alumnos': int(),
    'alumnos':[], #cantidad alumnos, limite 35
    'materias':[], #materias por curso, limite 10
    'turno':str()
}


#esqueleto materias
materia = {
    'nombre':str(),
    'profesores': [], #matriz profesores por materia, limite 5
    'dias': [], #lunes,martes,etc.
    'turno': str()
}

#esqueleto alummnos
alumno = {
    'dni':int(),
    'nombre':str(),
    'apellido':str(),
    'fecha_nac':int(),
    'curso':str(),
    'truno':str(),
    'notas':[],
    'pasw':str()
}

#esqueleto profesores
profesor = {
    'dni':int(),
    'nombre':str(),
    'fecha_nac':int(),
    'apellido':str(),
    'pasw':str(),
    'mail':str(),
    'telefono':int()
}