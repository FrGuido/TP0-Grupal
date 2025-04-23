
notas = [] #matriz notas

alumnos = [] #lista alumnos

profesores = [] #lista

des_nota = [str(), str(), str(), float(), int()] #profesor, curso, alumno, nota, fecha(100625)


#esqueleto cursos
curso = {
    'nombre':str(),
    'cantidad alumnos': int(),
    'alumnos':[], #cantidad alumnos, limite 35
    'materias':[], #materias por curso, limite ?
    'turno':str()
}


#esqueleto materias
materia = {
    'nombre':str(),
    'profesores': [], #profesores por materia, limite 3
    'dias': [], #lunes,martes,etc.
    'turno': str()
}

#esqueleto alummnos
alumno = {
    'dni':int(),
    'nombre':str(),
    'edad':int(),
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
    'edad':int(),
    'apellido':str(),
    'materias':[],
    'pasw':str()
}

#esqueleto administrador
administrador = {
    'dni':int(),
    'nombre':str(),
    'edad':int(),
    'apellido':str()
}



def Bienvenida():
    print("""------------- Bienvenido al sistema de alumnado -------------
>Identifiquese
""")
#    tipo,dni = login()

#    if tipo=='admin':
#        print(f""" Bienvenido Administrador)
#    """)
#    elif tipo=='p':
#        print(f""" Bienvenido {profesor.nombre})
#    """)
#    else:
#        print(f""" Bienvenido {alumno.nombre})
#    """)

Bienvenida()