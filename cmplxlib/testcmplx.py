import unittest
import cmplx
import math


class TestLibComplejos(unittest.TestCase):
    c1, c2 = (5, -1), (1, -4)
    c3, c4 = (3, 7), (2, -3)
    c5, c6 = (1, 9), (-2, 1)
    c7, c8 = (5, 5), (5, 5)

    def test_complexsum(self):
        self.assertEqual(cplx.Sumcplx(self.c1, self.c2), (6, -5))
        self.assertEqual(cplx.Sumcplx(self.c3, self.c4), (5, 4))
        self.assertEqual(cplx.Sumcplx(self.c5, self.c6), (-1, 10))
        self.assertEqual(cplx.Sumcplx(self.c7, self.c8), (10, 10))

    def test_complexproduct(self):
        self.assertEqual(cplx.Multcplx(self.c1, self.c2), (1, -21))
        self.assertEqual(cplx.Multcplx(self.c3, self.c4), (27, 5))
        self.assertEqual(cplx.Multcplx(self.c5, self.c6), (-11, -17))
        self.assertEqual(cplx.Multcplx(self.c7, self.c8), (0, 50))

    def test_division(self):
        self.assertEqual(cplx.Divcplx(self.c1, self.c2), (9 / 17, 19 / 17))
        self.assertEqual(cplx.Divcplx(self.c3, self.c4), (-15 / 13, 23 / 13))
        self.assertEqual(cplx.Divcplx(self.c5, self.c6), (7 / 5, -19 / 5))
        self.assertEqual(cplx.Divcplx(self.c7, self.c8), (1, 0))

    def test_complexresta(self):
        self.assertEqual(cplx.Rescplx(self.c1, self.c2), (4, 3))
        self.assertEqual(cplx.Rescplx(self.c3, self.c4), (1, 10))
        self.assertEqual(cplx.Rescplx(self.c5, self.c6), (3, 8))
        self.assertEqual(cplx.Rescplx(self.c7, self.c8), (0, 0))

    def test_modulo(self):
        self.assertEqual(cplx.Modulocplx(self.c1), 5.099)
        self.assertEqual(cplx.Modulocplx(self.c3), 7.616)
        self.assertEqual(cplx.Modulocplx(self.c5), 9.055)
        self.assertEqual(cplx.Modulocplx(self.c7), 7.071)

    def test_conjugado(self):
        self.assertEqual(cplx.Conjugadocplx(self.c1), (5, 1))
        self.assertEqual(cplx.Conjugadocplx(self.c3), (3, -7))
        self.assertEqual(cplx.Conjugadocplx(self.c5), (1, -9))
        self.assertEqual(cplx.Conjugadocplx(self.c7), (5, -5))

    def test_polar(self):
        self.assertEqual(cplx.Polarcplx(self.c1), (5.099, round(math.radians(-11.310), 3)))
        self.assertEqual(cplx.Polarcplx(self.c3), (7.616, round(math.radians(66.801), 3)))
        self.assertEqual(cplx.Polarcplx(self.c5), (9.055, round(math.radians(83.660), 3)))
        self.assertEqual(cplx.Polarcplx(self.c7), (7.071, round(math.radians(45), 3)))

    def test_cartesianas(self):
        n9 = (4, pi/4)
        n10 = (3, pi/2)
        n11 = (-5, pi/6)
        self.assertEqual(cplx.Cartesiahascplx(c9), (2.828, 2.828))
        self.assertEqual(cplx.Cartesiahascplx(c10), (0, 3))
        self.assertEqual(cplx.Cartesiahascplx(c11), (-4.330, -2.5))

    def test_fase(self):
        self.assertEqual(cplx.Fasecplx(self.c1), round(math.radians(-11.310), 3))
        self.assertEqual(cplx.Fasecplx(self.c3), round(math.radians(66.801), 3))
        self.assertEqual(cplx.Fasecplx(self.c6), round(math.radians(-26.565) + pi, 3))
        self.assertEqual(cplx.Fasecplx(self.c7), round(math.radians(45), 3))


if __name__ == '__main__':
    unittest.main()
