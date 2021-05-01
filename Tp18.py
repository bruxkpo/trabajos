#usando dos listas
def listainvertida():


    frase = input("Ingrese una frase: ")
    lista = frase.split() # se crea un array a partir del split
    listainvertida = [None]*len(lista) # se crea un nuevo array con tamaño del arreglo anterior

    #se recorre el arreglo original y en forma decreciente se agrega en el nuevo array, asi se construye la lista invertida
    for i in range(len(lista)):        
        listainvertida[(len(lista)-1)-i] = lista[i]

    #se crea una variable en la que se acumula la informacion de la lista invertida para imprimirlo como una frase alreves
    fraseinvertida=""
    print("Frase invertida: ")
    for i in range(len(listainvertida)):        
        fraseinvertida +=listainvertida[i]+" "
    print(fraseinvertida)

#usando una lista y una variable temporal
def listainvertidatemporal():

    frase = input("Ingrese una frase: ")
    lista = frase.split() # se crea un array a partir del split
    variabletemporal = ""
    mitad  = int(len(lista)/2) #Para recorrer la mitad del arreglo para invertir en el recorrido del for    

    for i in range(mitad):        
        variabletemporal =  lista[i]
        lista[i] = lista[(len(lista)-1)-i]
        lista[(len(lista)-1)-i] = variabletemporal
       
    fraseinvertida=""
    print("Frase invertida: ")
    for i in range(len(lista)):        
        fraseinvertida +=lista[i]+" "
    print(fraseinvertida) 