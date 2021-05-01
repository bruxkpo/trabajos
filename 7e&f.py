from calendar import monthrange
import datetime

"""
En este codigo, utilizando la funcion previamente establecida, se calculan 2 datos, el primero cuanto falta para fin de año, y despues se calcula cuantos dias pasaron en el año
"""
def ValidacionFecha():
    date = input("Ingresa una fecha en numeros separadas en barras (Dia/Mes/Año ): ")

    dia,mes,año = date.split('/')

    valida = True
    try:
        datetime.datetime(int(año),int(mes),int(dia))
    except ValueError:
        valida = False

    if valida == True:
        print("{} es valida.".format(date))
        return date
    else:
        print("Dato ingreso invalido")
        exit



def diasaño():
    diastotal = 0
    diashastafecha = 0
    diasrestantes = 0
    date = ValidacionFecha()
    formato = "%d/%m/%Y"
    fechaobjeto = datetime.datetime.strptime(date, formato)
    año = fechaobjeto.year
    mes = fechaobjeto.month
    dia = fechaobjeto.day
    tr = monthrange(año,mes)[1]
    diames = tr - dia
    
    for i in range(1,13):
        dias = monthrange(año, i)[1]
        diastotal = diastotal + dias
    for i in range(1,13):
        if i <= mes:
            dias2 = monthrange(año, i)[1]
            diashastafecha = diashastafecha + dias2
    try:
        diashastafecha = diashastafecha - diames
        diasrestantes = diastotal - diashastafecha
        print("Faltan {} dias para que termine el año. y han pasado {} dias del año.".format(diasrestantes, año, diashastafecha))
        return diasrestantes,diastotal,diashastafecha,diames
    except ValueError:
        print("Error de formateo.")


diasaño()