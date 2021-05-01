from calendar import monthrange
from datetime import date
from dateutil import relativedelta
import datetime

"""
    Se calcula diferencia entre dos fechas ingresadas por el usuario.
"""

def ValidacionFecha():
    date1 = input("Ingresa su primera fecha (Dia/Mes/Años ): ")
    date2 = input("Ingresa su segunda fecha (Dia/Mes/Años ): ")

    dia1,mes1,año1 = date1.split('/')
    dia2,mes2,año2 = date2.split('/')

    valida = True
    try:
        datetime.datetime(int(año1),int(mes1),int(dia1))
        datetime.datetime(int(año2),int(mes2),int(dia2))
    except ValueError:
        valida = False

    if valida == True:
        print("Ambas fechas {} & {} son validas.".format(date1,date2))
        return date1,date2
    else:
        print("Datos invalidos")
        exit

def diasaño():
    date1,date2 = ValidacionFecha()
    formato = "%d/%m/%Y"
    fecha1 = datetime.datetime.strptime(date1, formato)
    fecha2 = datetime.datetime.strptime(date2, formato)
    try:
        diferencia = relativedelta.relativedelta(fecha1,fecha2)
        años = diferencia.years
        meses = diferencia.months
        dias = diferencia.days
        print("Hay un diferencia entre ambas fechas de: {} años/{} meses/{}".format(años,meses,dias))
    except ValueError:
        print("Error de formato.")
diasaño()