import numpy as np
import math
import cmplx


def suma_vec_cplx(A, B):
    ''' Calcula el vector resultado de una suma entre vectores.
    '''
    res = []
    if len(A) == len(B):
        vector = [[0 for i in range(1)] for j in range(len(A))]
        for i in range(len(A)):
            for j in range(1):
                vector[i][j] = cmplx.Sumcplx(A[i][j], B[i][j])
        return vector
    else:
        print("Para realizar la operacion entre vectores, estos deben tener el mismo tamaño.")

    def resta_vectores_cplx(A, B):
        if len(A) == len(B):
            vector = [[0 for i in range(1)] for j in range(len(A))]
            for i in range(len(A)):
                for j in range(1):
                    vector[i][j] = cmplx.Restacplx(A[i][j], B[i][j])
            return vector
        else:
            print("Para realizar la operacion entre vectores, estos deben tener el mismo tamaño.")

    def inversovector(A):
        vector = [[0 for i in range(1)] for j in range(len(A))]
        for i in range(len(A)):
            for j in range(1):
                vector[i][j] = cmplx.Inversocplx(A[i][j])
        return vector

    def multescalarvector(C, A):
        vector = [[0 for i in range(1)] for j in range(len(A))]
        for i in range(len(A)):
            for j in range(1):
                vector[i][j] = cmplx.Multcplx(C, A[i][j])
        return vector

    def sumamatrices(A, B):
        if len(A) == len(B) and len(A[0]) == len(B[0]):
            matriz = [[0 for i in range(len(B[0]))] for j in range(len(A))]
            for i in range(len(A)):
                for j in range(len(B[0])):
                    matriz[i][j] = cmplx.Sumacplx(A[i][j], B[i][j])
            return matriz
        else:
            print("Debido A que las matrices no tienen tamaños compatibles, no es posible realizar la operación")



    def traspuesta(A):
        matriz = [[0 for i in range(len(A))] for j in range(len(A[0]))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                matriz[j][i] = A[i][j]
        return matriz

    def conjugadomatriz(A):
        matriz = [[0 for i in range(len(A[0]))] for j in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                matriz[i][j] = cmplx.Conjugadocplx(A[i][j])
        return matriz

    def adjuntamatriz(A):
        matriz = conjugadomatriz(A[:])
        return traspuesta(matriz)

    def multmatrices(A, B):
        if len(A[0]) == len(B):
            matriz = [[[0, 0] for i in range(len(B[0]))] for j in range(len(A))]
            for i in range(len(A)):
                for j in range(len(B[0])):
                    for k in range(len(B)):
                        matriz[i][j] = cmplx.Sumacplx(matriz[i][j], Multcplx(A[i][k], B[k][j]))
            return matriz
        else:
            print("Debido A que las matrices no tienen tamaños compatibles, no es posible realizar la operación")

    def productointerno(A, B):
        rta = [0, 0]
        adj = adjuntamatriz(A)
        matriz = multmatrices(adj, B)
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if i == j:
                    rta = cmplx.Sumacplx(rta, matriz[i][j])
                else:
                    rta = rta
        return rta




