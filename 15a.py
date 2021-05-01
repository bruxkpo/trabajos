def mayusculas():
    string = input("Ingrese su palabra: ")
    palab = string.split()
    palabra = ""
    inicio = ""

    
    for x in range(0, len(palab)):
        palabra = palab[x]
        if palab[x] == palabra:
            inicio += palabra[0].upper()
    print("Las iniciales son: {}".format(inicio))
    return(palabra)
mayusculas()
