from math import sqrt
from re import X
from tkinter import Y
from zlib import DEF_BUF_SIZE

from regex import B


class Punto:
    X = 0
    Y = 0
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y   
    def __str__(self):
        return "(X={},Y={}".format(self.X,self.Y)
    def cuadrante(self,X,Y):
        if X == 0 and Y != 0:
            print("El punto de coordenadas ({},{}) se sitúa sobre el eje Y")
        elif X != 0 and Y == 0:
            print("El punto de coordenadas ({},{}) se sitúa sobre el eje X")
        elif X == 0 and Y == 0:
            print("El punto de coordenadas ({},{}) está sobre el origen")
    def vector(self,punto):
        print("El vector entre {}) y {}) es ({},{})".format(self,punto,punto.X-self.X,punto.Y-self.Y))
    

A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto(0,0)

A.vector(B)
C.vector(D)

class Rectángulo:
    inicial = 0
    final = 0
    diagonal = (final - inicial)
    def __init__(self,inicial,final):
        self.inicial = inicial
        self.final = final
    def __str__(self):
        return "(punto1{},punto2{})".format(self.inicial,self.Y)
        