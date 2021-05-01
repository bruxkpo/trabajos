import datetime
def ValidacionFecha():
    """Datatime de nuevo, se hace un un try-except para verificar si un dato string se puede pasar tipo datetime. Si la variable devuelve true la validacion se hizo correctamente, de lo contrario  queda en false"""
    fecha = input("ingrese fecha (Dia/Mes/Año ): ")

    dia,mes,año = fecha.split('/')

    valida = True
    try:
        datetime.datetime(int(año),int(mes),int(dia))
    except ValueError:
        valida = False

    if valida == True:
        print("{} es valida.".format(fecha))
    else:
        print("Los datos ingresador son incorrectos.")

    
ValidacionFecha()