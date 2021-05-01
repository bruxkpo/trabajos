from time import sleep

def contraseña1():
    contraseña = "password"
    ingreso = input("Contraseña: ")
    intentos = 4
    while ingreso != contraseña:
        ingreso = input("Contraseña incorrecta! Quedan {} intentos: ".format(intentos))
        intentos -= 1
        if intentos == 3:
            if contraseña == ingreso:
                break
            print("Vuelva a intentar en 5 segundos.")
            sleep(5)
        elif intentos == 2:
            if contraseña == ingreso:
                break
            print("Vuelva a intentar en 15 segundos.")
            sleep(15)
        elif intentos == 1:
            if contraseña == ingreso:
                break
            print("Vuelva a intentar en 45 segundos.")
            sleep(45)
        if intentos == 0:
            print("No se puede volver a intentar")
            break

    if contraseña == ingreso:
        print("Contraseña correcta")

contraseña1()