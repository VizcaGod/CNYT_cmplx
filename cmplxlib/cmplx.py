import math

def Sumcplx(c1, c2):
    """ Funcion que realiza la suma de dos numeros complejos y retorna
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
    """ Funcion que realiza la multiplicacion de dos numeros complejos
    y retorna un numero complejo
    (tuple, tuple) -> tuple"""
    real = c1[0] * c2[0] - c1[1] * c2[1]
    imag = c1[0] * c1[1] + c2[0] * c2[1]
    c = (real,imag)
    return c

def Divcplx(c1,c2):
    """ Funcion que realiza la division de dos numeros complejos
    y retorna un numero complejo
    (tuple, tuple) -> tuple"""
    real = ((c1[0]*c2[0])+(c1[1]*c2[1]))/((c2[0]**2)+(c2[1]**2))
    imag = ((c2[0]*c1[1])-(c1[0]*c2[1]))/((c2[0]**2)+(c2[1]**2))
    c = (real, imag)
    return c

def Modulocplx(c):
    """ Funcion que calcula el modulo de un numero complejo
    (tuple) -> float"""
    modul = float(math.sqrt(c[0]**2+c[1]**2)
    return modul

def Conjugadocplx(c):
    """ Funcion que calcula el conjugado de un numero complejo
    (tuple) -> float"""
    n = (c[0], c[1]*-1)
    return n

def Polarcplx(c):
    """ Funcion que obtiene las coordenadas polares de un numero complejo
    tuple -> tuple"""
    norma = math.sqrt(c[0]**2+c[1]**2)
    angulo = math.atan2(c[1], c[0])
    return norma, angulo

def Cartesianascplx(c):
    """ Funcion que obtiene las coordenadas polares de un numero complejo
    tuple -> tuple"""
    a = c[0] * math.cos(c[1])
    b = c[0] * math.sin(c[1])
    return a, b

def Fasecplx(c):
    """funcion que obtiene la fase de numeros complejos
    tuple -> tuple"""
    angulo = math.atan2(c[1], c[0])
    return angulo

def Inversocplx(A):
    real = -1 * (A[0])
    img = -1 * (A[1])
    c = (real, img)
    return c

def Restacplx(A, B):
    real = A[0] - B[0]
    img = A[1] - B[1]
    c = (real, img)
    return c


