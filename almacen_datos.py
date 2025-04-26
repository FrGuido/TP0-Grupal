
notas = [] #matriz notas

alumnos = [] #lista alumnos

profesores = [] #lista profesores

materias = [] #lista materias con profesores

cursos = [] #lista cursos

des_nota = [str(), str(), str(), float(), int()] #profesor, curso, alumno, nota, fecha(100625)



#esqueleto cursos
curso = {
    'nombre':str(),
    'cantidad alumnos': int(),
    'alumnos':[], #cantidad alumnos, limite 35
    'materias':[], #materias por curso, limite 12
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
    'curso':int(),
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
    'mail':str()
}

#esqueleto administrador
administrador = {
    'dni':int(),
    'nombre':str(),
    'edad':int(),
    'apellido':str()
}