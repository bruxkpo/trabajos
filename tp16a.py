"""
 con un simple for analiza la palabra y con un if el programa
 verifica si hay una consonante utilizando una lista que contiene a todas
 las consonantes en minuscula y mayuscula. luego le agrego las consonantes
 que se consiguieron a una variable vacia.
"""
def consonante():
    palabra = input("Ingrese una sentencia: ")
    consonantes = ""
    
    for x in range(0, len(palabra)):    # recorre la palabra
        if palabra[x] in "bdfghjklmnñpqrstvxyzBDFGHJKLMNÑPQRSTVXYZ":
            consonantes += palabra[x]  # le suma las consonantes de nuestra palabra a la nueva palabra
        
    print(consonantes)