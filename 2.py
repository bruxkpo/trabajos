from math import pi
from math import sqrt 
def perimetro_rectangulo (base,altura):
    return ((base * 2)+(altura * 2))

def area_rectangulo (base,altura):
    return (base * altura)

def cordenadas_rectangulo (x1,x2,y1,y2):
    return ((abs(x2) - abs(x1)) * (abs(y2) - abs(y1)))

def perimetro_circulo (radio):
    return (2 * pi * radio)

def area_circulo (radio):
    return (pi * radio**2)

def volumen_esfera (radio):
   return ((4/3) * pi * radio**3)

def hipotenusa (cateto1,cateto2):
    return sqrt((cateto1**2) + (cateto2**2))
