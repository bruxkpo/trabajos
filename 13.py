def comparacionUpper():
    string1 = input("Digite una palabra: ")
    string2 = input("Digite una segunda palabra: ")
    verdadero = False
    if string1 == string2.upper(): 
        verdadero = True
        print("La palabra 1 es la version en mayuscula de la segunda? {}".format(verdadero))
    elif string1.upper() == string2:
        verdadero = False
        print("La palabra 1 es la version en mayuscula de la segunda? {}".format(verdadero))
comparacionUpper()