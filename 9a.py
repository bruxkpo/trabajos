def contraseña1():
    contraseña = "password"
    ingreso = input("Contraseña: ")
    intentos = 4
    while ingreso != contraseña and intentos > 0:
        ingreso = input("Contraseña incorrecta! Quedan {} intentos: ".format(intentos))
        intentos -= 1

    if intentos == 0:
        print("No se puede intentar.")
        
    if contraseña == ingreso:
        print("Contraseña correcta")

contraseña1()