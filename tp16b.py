"""
    esto es igual que con el ejercicio de consonantes anterior, hago lo mismo pero
    con una lista de vocales.
"""


def vocal():
    palabra = input("Ingrese una sentencia: ")
    vocales = ""
    
    for x in range(0, len(palabra)):    # lee la palabra
        if palabra[x] in "aeiouAEIOU":
            vocales += palabra[x]  # le suma las vocales de nuestra palabra a la nueva palabra
        
    print(vocales)