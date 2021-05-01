def siguientevocal():

    # el usuario ingresa una palabra
    palabra = input("Ingresa una sentencia: ")
    
    # convierte a la lista de vocales en una lista
    vocales = "a e i o u A E I O U".split()

    # crea un diccionario usando zip()
    tupla = dict(zip(vocales, vocales[1:] + [vocales[0]])) 

    # crea una comprension de listas para hacer el reemplazo de vocales en la palabra.
    reemplazo = "".join([tupla.get(ele, ele) for ele in palabra]) 
    print("Tu palabra reemplazada: {}".format(reemplazo))
