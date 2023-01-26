import math

def Sumcplx(c1, c2):
    """Funcion que realiza la suma de dos numeros complejos y retorna
    un numero complejo
    (tuple, tuple) -> tuple"""
    real = c1[0] + c2[0]
    imag = c1[1] + c2[1]
    c = (real,imag)
    return c

def PrettyPcplx(c):
    """ Funcion que toma los componentes de un numero complejo y los retorna de
    forma ordenada """
    print("{} + {}i".format(c[0], c[1]))

def Multcplx(c1,c2):
    """Funcion que realiza la multiplicacion de dos numeros complejos
    y retorna un numero complejo
    (tuple, tuple) -> tuple"""
    real = c1[0] * c2[0] - c1[1] * c2[1]
    imag = c1[0] * c1[1] + c2[0] * c2[1]
    c = (real,imag)
    return c

def Divcplx(c1,c2):
    """Funcion que realiza la division de dos numeros complejos
    y retorna un numero complejo
    (tuple, tuple) -> tuple"""
    real = ((c1[0]*c2[0])+(c1[1]*c2[1]))/((c2[0]**2)+(c2[1]**2))
    imag = ((c2[0]*c1[1])-(c1[0]*c2[1]))/((c2[0]**2)+(c2[1]**2))
    c = (real, imag)
    return c

def Modulocplx(c):
    """Funcion que calcula el modulo de un numero complejo
    (tuple) -> float"""
    modul = float(math.sqrt(c[0]**2+c[1]**2)
    return modul

def conjugadocplx(c):
    """Funcion que calcula el conjugado de un numero complejo
    (tuple) -> float"""
    n = (c[0], c[1]*-1)
    return n

def polarcplx(c):
    norma = round(math.sqrt(c[0]**2+c[1]**2), 3)
    angulo = round(math.atan2(c[1], c[0]), 3)
    return norma, angulo

if __name__ == "__main__":
    #test enviar cmplx, test, readme, gitignore
