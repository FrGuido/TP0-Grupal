from validar import añoBisiesto
import registroPU

def test_año_bisiesto():
    assert añoBisiesto(2020) == True
    assert añoBisiesto(1900) == False
    assert añoBisiesto(2000) == True
    assert añoBisiesto(2023) == False

def limpiar_archivoPU():
    with open("RegistroPU.txt", "w") as f:
        pass

def test_registrar_agregado():
    limpiar_archivoPU()
    registroPU.registrar_agregadoPU("Alumno", "Juan", "Pérez", 12345678)
    
    with open("RegistroPU.txt", "r") as archivo:
        lineas = archivo.readlines()
        assert len(lineas) == 1
        assert "AGREGADO" in lineas[0]
        assert "Juan" in lineas[0]
        assert "12345678" in lineas[0]

def test_registrar_eliminado():
    limpiar_archivoPU()
    registroPU.registrar_eliminadoPU("Profesor", "Ana", "Gómez", 87654321)
    
    with open("RegistroPU.txt", "r") as archivo:
        contenido = archivo.read()
        assert "ELIMINADO" in contenido
        assert "Ana" in contenido
        assert "87654321" in contenido

def test_registrar_modificado():
    limpiar_archivoPU()
    registroPU.registrar_modificadoPU("Alumno", "Luis", "Martínez", 11223344)
    
    with open("RegistroPU.txt", "r") as archivo:
        contenido = archivo.read()
        assert "MODIFICADO" in contenido
        assert "Luis" in contenido
        assert "11223344" in contenido