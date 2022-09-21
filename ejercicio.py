from math import sqrt
from re import X
from tkinter import Y

from regex import B


class Punto:
    X = 0
    Y = 0
    def __init__(self,X):
        X = input()
        self.X = X
        return X
    def __init__(self,Y):
        Y = input()
        self.Y = Y
        return Y
    def __str__(self):
        return +str(self.X)+","+str(self.Y)
    def cuadrante(self,X,Y):
        if X == 0 and Y != 0:
            print("Se sitúa sobre el eje Y")
        elif X != 0 and Y == 0:
            print("Se sitúa sobre el eje X")
        elif X == 0 and Y == 0:
            print("Está sobre el origen")
    def vector(self,punto):
        print("El vector entre los dos puntos es".format(self,punto,punto.X-self.X,punto.Y-self.Y))

A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto(0,0)

A.vector(B)
C.vector(D)