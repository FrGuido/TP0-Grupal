def pedirFecha():
    while True: #bucle, termina cuando se ingrese una fecha valida
        fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")
        f = fecha.split("/")

        if len(f) == 3:
            try:
                dia = int(f[0]) 
                mes = int(f[1])
                año = int(f[2])

                bisiesto = añoBisiesto(año) #valido el año bisisesto

                diasMes = [31, 29 if bisiesto else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #lista de dias de meses, con febrero arreglado

                if 1 <= mes <= 12 and 1 <= dia <= diasMes[mes - 1]:
                    print("Fecha válida.")
                    return (f'{dia}/{mes}/{año}')
                else:
                    print("Fecha inválida. Día o mes fuera de rango.")
            except ValueError:
                print("Error: ingrese solo números en el formato correcto.")
        else:
            print("Formato incorrecto. Use dd/mm/aaaa.")

def añoBisiesto(año): #verificacion si el año es bisiesto o no
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False