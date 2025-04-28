import almacen_datos

# Elimina profesores o alumnos de una lista, basado en el DNI


# Elimina materias de la lista global de materias, basado en nombre y turno
def eliminar_diccionario_lista_materias(nombre, turno):
    almacen_datos.materias[:] = [
        x for x in almacen_datos.materias 
        if not (x.get('nombre') == nombre and x.get('turno') == turno)
    ]
