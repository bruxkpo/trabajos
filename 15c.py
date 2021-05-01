"""
En este ejercicio se quiere que el usuario dijite una frase conformada por uno o varios
strings, que de esta, se logren sacar aquellas palabras que empienzan con a (y mostrarlas).
"""

def HallarA():
    string = input("Escriba una frase: ")
    palabra = string.split()
    a = ""
    b = ""


    for x in range(0, len(palabra)):
        a = palabra[x]
        if a[0] in "Aa":
            b += a
        else:
            print("En la frase no hay palabras que empiencen con a 'A'.")
    print("Las palabras encontradas que empiencen con a son: {}".format(b))

HallarA()
    