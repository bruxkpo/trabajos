"""
en esta simplemente creo una funcion que valide si la palabra ingresada es
igual a la palabra dada vuelta. En ese caso, va a devolver True siempre y cuando
tu palabra sea un palindromo. Caso contrario, te indicara que no.
"""

def espalindromo(reverso):
    if reverso == reverso[::-1]: # revisa si la palabra es igual a la palabra en reversa
        return True
    else:
        return False

def palindromo():
    reverso = input("Ingresa un palindromo: ").replace(" ","") # quita los espacios
    validacion = espalindromo(reverso)

    if validacion is True:
        print("La palabra {} es un palindromo.".format(reverso))
    else:
        print("La palabra {} no es un palindromo.".format(reverso))
    