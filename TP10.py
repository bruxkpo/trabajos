from random import randrange

def adivinar():
    secreto = randrange(1,1000)
    num = int(input("Adivina el numero: "))

    while num > 0:
        if num > secreto:
            num = int(input("Tu numero es mayor a el numero oculto. intenta denuevo: "))
        elif num < secreto:
            num = int(input("Tu numero es menor a el numero oculto. intenta de nuevo: "))

        if num == secreto:
            print("Adivinaste, El numero es: {}".format(secreto))
            break