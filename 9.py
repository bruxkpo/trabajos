def contraseña1():
    contraseña = "password"
    ingreso = input("Contraseña: ")
    while ingreso != contraseña:
        ingreso = input("Contraseña incorrecta! Quedan {} intentos: ".format(intentos))
    
    if contraseña == ingreso:
        print("Contraseña correcta")

contraseña1()