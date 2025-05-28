import almacen_datos 

def eliminar_diccionario_lista_alu_prof(dic,elemento):
    return list(filter(lambda x: x.get('dni') != elemento, dic)) #Elimina el elemento de la lista y devuelve una nueva lista

def eliminar_diccionario_lista_materias(nombre, turno): 
    almacen_datos.materias[:] = [
        x for x in almacen_datos.materias #recorre la lista "Materias"
        if not (x.get('nombre') == nombre and x.get('turno') == turno) #Verifica si los datos coinciden y se actualiza la lista
    ]
