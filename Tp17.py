#funcion principal
def telegram():

    costo_palabra_corta = 3
    costo_palabra_larga = 4.5
    total_costo = 0

    textoptimizado = ""
    print("Calculo de costo de telegrama")
    print("palabra corta: {}$".format(costo_palabra_corta))
    print("palabra larga: {}$".format(costo_palabra_larga))
    textoenviar = input("Ingresa el texto del telegrama a enviar: ")
    listapalabras = textoenviar.split()

    contador_palabras=0
    for x in listapalabras:
        contador_palabras +=1

        #cambia en la ultima palabra el punto para sacarselo
        if (contador_palabras == len(listapalabras)):
            x.replace(".", "")

        #Revisa si es mayor a 5 caracteres para acortarlo a 5 y dejarle un arroba al final
        #si es menor, directamente lo agrega
        if (len(x) > 5):
            total_costo += costo_palabra_larga
            textoptimizado += x[0:5] + "@" + " "
        else:            
            total_costo += costo_palabra_corta
            textoptimizado += x + " "
            
        #una vez agregado o acortado el texto, revisa si el texto que va formado hasta ahora tiene un punto para sustituirlo por STOP
        #pero verifica que no este en la ultima palara ya que es la ULTIMA palabra la que lleva STOPSTOP
        if ( x.find('.') > -1 and contador_palabras<len(listapalabras)):
            textoptimizado += "STOP" + " "

        #Le agrega STOPSTOP a la ultima palabra
        if (contador_palabras == len(listapalabras)):
            textoptimizado += "STOPSTOP"

    print("Texto a enviar por telegrama: ",textoptimizado)
    print("Costo del envio: {}$".format(total_costo))