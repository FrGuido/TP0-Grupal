def pedirFecha():
    while True: #bucle, termina cuando se ingrese una fecha valida
        fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")
        f = fecha.split("/")

        if len(f) == 3:
            try:
                dia = int(f[0]) 
                mes = int(f[1])
                ano = int(f[2])

                bisiesto = anoBisiesto(ano) #valido el ano bisisesto

                diasMes = [31, 29 if bisiesto else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #lista de dias de meses, con febrero arreglado

                if 1 <= mes <= 12 and 1 <= dia <= diasMes[mes - 1]:
                    print("Fecha válida.")
                    return dia, mes, ano
                else:
                    print("Fecha inválida. Día o mes fuera de rango.")
            except ValueError:
                print("Error: ingrese solo números en el formato correcto.")
        else:
            print("Formato incorrecto. Use dd/mm/aaaa.")

def anoBisiesto(ano): #verificacion si el ano es bisiesto o no
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
pedirFecha()



