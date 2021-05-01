listnum = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def romanos():
    """
    esta funcion funciana con un list que contiene la tabla de conversion entre numeros
    decimales a  romanos. la funcion utiliza un for con dos variables
    que recorren a ambos valores de la lista, y en el for hay un while que agrega los valores
    correspondientes en romano solo cuando nuestra variable "num" es mayor o igual a su correspondiente "i".
    luego, se le resta "i" a "num" y sigue  hasta que se consigan todos los valores en romano. """
    
    
    romano = ""
    num = int(input("Ingrese un año: "))
    num = num
    if num > 0 and num < 10000:
        for i, x in listnum:
            while num >= i:
                romano = romano + x
                num = num - i
        print("El año {} es {} en numeros romanos.".format(num, romano))
    else:
        print("Ingrese un año.");
