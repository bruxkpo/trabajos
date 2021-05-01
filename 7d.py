import datetime
from calendar import monthrange

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


def CuantoParaFinDeMes():
    """
    Se calcula cuantos dias faltan para fin de mes
    """
    date = ValidacionFecha()
    formato = "%d/%m/%Y"
    dateobj = datetime.datetime.strptime(date, formato)
    yearnow = dateobj.year
    monthnow = dateobj.month
    daynow = dateobj.day
    days = monthrange(yearnow, monthnow)[1]
    try:
        daysleft = days - daynow
        print("{} restantes para fin de mes".format(daysleft))
    except ValueError:
        print("ERROR")


CuantoParaFinDeMes()