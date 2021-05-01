def calificacionesProm():

    """
    Lo que se quiere realizar en este ejercicios, es una vez conociendo las respuestas de un examen y la cantidad respondida por los alumnos
    sacar un promedio y al mismo tiempo, decir si este aprobo o desaprobo (e indicar cuantos ejercicios hizo).
    """
    ejer = int(input("Ingresa la cantidad de ejercicios totales: "))
    listaexamen = [
        (int(input("Ejercicios hechos? :")), tot),
        (int(input("Ejercicios hechos? :")), tot),
        (int(input("Ejercicios hechos? :")), tot),
        (int(input("Ejercicios hechos? :")), tot),
        (int(input("Ejercicios hechos? :")), tot)]
    print(listaexamen)

    resueltos = 0
    por = 0
    cantidad = 1
    
    for i, x in listaexamen:
        if i < x:
            res = i
            por = float((resueltos / tot) * 100)
            if por >= 60:
                print("Examen n´. {}: tiene un porcentaje de {}% | APROBADO | {} de {} ejercicios hechos.".format(cantidad, por, i , x))
            else:
                print("Examen n´. {}: tiene un porcentaje de {}% | DESAPROBADO | {} de {} ejercicios hechos. ".format(cantidad, por, i, x))
        else:
            print("Error de ingreso. Vuelva a ingresar los datos.")
            exit
        cantidad += 1
calificacionesProm()
    
