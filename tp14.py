import random

"""
    Esta serie de funciones tienen estos motivos:
    - generar un numero aleatorio que el usuario adivinara
    por medio de dos funciones
    - validar que el numero que ingrese el usuario no se repita
    - el juego en si, incluyendo los for que constituyen a las condiciones
    de acierto y coincidencias.
    La forma en la que la funcion principal valida si hay digitos repetidos
    en la serie de numeros que ingresaste, y el input esta atrapado dentro de
    un while, que lo va a hacer mientras que "repetido" este en "false". esto
    permite que el programa te pueda pedir el numero continuamente sin procesar
    ninguna de la informacion, es decir, que no continuara hasta que el numero que ingreses
    no este repetido. El resto utiliza los "for" para recorrer la cadena de numeros,
    validando si son iguales en la misma posicion o si simplemente ambos numeros contienen
    el otro, verificando que no se repitan las mismas condiciones con el mismo numero al
    mismo tiempo.
"""

# funcion que genera un numero aleatorio
def numeroaleatorio():
    num = 0  
    while len(set(str(num))) != 4:
        num = random.randint(1000, 9999)
    return num

num = str(numeroaleatorio())

def validar(numero):

    repetido = 1
    # valida numero iguales
    for x in range(0, len(numero)):
        for e in range(0, len(numero)):
            if numero[e] == numero[x] and e != x:
                repetido += 1
                #print("Numero {} repetido {} veces".format(numero[e], repetido))
                if (repetido > 1):
                    print("No pueden haber numeros repetidos en tu numero.")
                    return False
                repetido = 1
    return True
    
# funcion principal
def adivinaryigualdad():

    print("Adivina el numero secreto")
    ganaste = 0
    repetido = False
    
    while ganaste == 0:

        resultado = False

        while resultado == False:
            numero = input("Ingresa un numero de 4 digitos unicos: ")
            resultado = validacion(numero)   

        acierto = 0
        numacierto = 0
        listacierto = []

 
        if len(numero) == 4:


            # detector de aciertos
            for x in range(0, len(numero)):
                if numero[x] == num[x]:
                    acierto += 1
                    listacierto.append(numero[x])

                    
            # mensajes de adivinar
            if acierto > 0 and acierto < 4:
                print("Acertaste con: {}.".format(listacierto))
            elif acierto == 0:
                print("No hay aciertos.")
            elif acierto == 4:
                print("Ganaste! El numero era: {}".format(num))
                ganaste += 1
                return


            # comprobacion de datos iguales
            for e in range(0, len(numero)):
                for i in range (0, len(numero)):
                    if numero[e] in num[i] and numero[i] != num[i]:
                        numacierto = numero[e]
                        print("Tu numero coincide con el numero secreto con el numero {}".format(numacierto))
        else:
            print("Tu numero debe tener unicamente cuatro digitos.")
