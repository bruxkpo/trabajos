numeros = []
def multiplicar():
    """esta funcion pide cuatro numeros, y de los cuatro, multiplicar dos de ellos y ver cual da un mayor resultado entre todas las opciones"""
    for i in range(0, 4):
            num = int(input("Ingrese cuatro numeros: "))
            numeros.append(num)
    mayor = 0
    resultado = 0
    for i in range(0, 4):
        print(numeros[i])
        a = numeros[i]
    """aca hay un doble for. mientras i se para en un numero de la lista, el segundo for  pasa por el resto de los numeros de la lista, y despues chequea que ambos numeros no sean iguales a si no se multiplican entre si."""
        for x in range(0, 4):
            resultado = abs(a * numeros[x])
            if resultado > mayor and numeros[i] != numeros[x]:
                mayor = resultado

    print("El mayor valor es: ", mayor)


multiplicar()