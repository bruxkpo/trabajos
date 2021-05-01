def bisiesto():
    """Calcula si un año es bisiesto o no a travez de modulos."""
    año = input("Ingresar año: ")
    if len(año) > 5:
        print("Ingrese una fecha mas cercana.")
    if int(año) % 4 == 0 or int(año) % 400 == 0 and int(año) % 100 > 0:
        print("El año es bisiesto.".format(año))
    else:
        print("El año NO es bisiesto.".format(año))

bisiesto()
