from time import sleep

def contraseña1():
    
    contraseña = "password"
    ingreso = input("Contraseña: ")
    intentos = 4
    valida = False

    
    while ingreso != contraseña:
        ingreso = input("Contraseña incorrecta! Quedan {} intentos: ".format(intentos))
        intentos -= 1

        
        if intentos == 3:
            if contraseña == ingreso:
                valida = True
                print("Contraseña correcta")
                return(valida)
            print("Vuelva a intentar en 5 segundos.")
            sleep(5)

            
        elif intentos == 2:
            if contraseña == ingreso:
                valida = True
                print("Contraseña correcta")
                return(valida)
            print("Vuelva a intentar en 15 segundos.")
            sleep(15)

            
        elif intentos == 1:
            if contraseña == ingreso:
                valida = True
                print("Contraseña correcta")
                return(valida)
            print("Vuelva a intentar en 45 segundos.")
            sleep(45)

            
        if intentos == 0:
            valida = False
            print("No se puede volver a intentar")
            return(valida)

                
    if contraseña == ingreso:
        valida = True
        print("Contraseña correcta")
        return(valida)
            

contra = contraseña1()

if contra == True:
    print("La contraseña se ingreso correctamente")
