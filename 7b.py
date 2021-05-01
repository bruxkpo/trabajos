from calendar import monthrange
import datetime
def mes():
    """se utilizan las librerias de calendario y datetime para utilizar sus funciones y statements para conseguir el nombre de mes y la cantidad de dias de ese mes, y este numero de dias (esto varia si el año es biciesto)"""
    year = int(input("ingrese el año: "))
    month = int(input("Ingrese el mes (en numero): "))
    while month > 12 or year > 10000:
        print("Dato incorrecto, vuelva a ingresar el mes o el año")
        year = int(input("ingrese el año: "))
        month = int(input("Ingrese el mes (en numero): "))
    day = monthrange(year, month)[1]
    monthobj = datetime.datetime.strptime(str(month), "%m")
    monthname = monthobj.strftime("%b")
    print(day)
    print("El mes {} en el año {} tuvo un total de {} dias".format(monthname, year, day))
mes()
