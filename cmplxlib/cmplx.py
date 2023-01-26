def Sumcplx(c1, c2):
    """Realiza la suma de dos numeros complejos y retorna un numero complejo
    (array, array) -> array"""
    real = c1[0] + c2[0]
    imag = c1[1] + c2[1]
    c = (real,imag)
    return c

def PrettyPcplx(c):
    print("{} + {}i".format(c[0], c[1]))

def Multcplx(c1,c2):
    """Realiza la multiplicacion de dos numeros complejos y retorna un numero complejo
    (array, array) -> array"""
    real = c1[0] * c2[0] - c1[1] * c2[1]
    imag = c1[0] * c1[1] + c2[0] * c2[1]
    c = (real,imag)
    return c

def Divcplx(c1,c2):
    """Realiza la division de dos numeros complejos y retorna un numero complejo
    (array, array) -> array"""
    real = ((c1[0]*c2[0])+(c1[1]*c2[1]))/((c2[0]**2)+(c2[1]**2))
    imag = ((c2[0]*c1[1])-(c1[0]*c2[1]))/((c2[0]**2)+(c2[1]**2))
    c = (real, imag)
    return c




