from re import X
from tkinter import Y


class Punto:
    X = 0
    Y = 0
    def __init__(self,X):
        self.X = X
        return X
    def __init__(self,Y):
        self.Y = Y
        return Y
    def __str__(self):
        return +str(self.X)+","+str(self.Y)
    def cuadrante():
        if X == 0 and Y != 0:
            print("Se encuentra en el eje Y")
        elif X != 0 and Y == 0:
            print("Se encuentra en el eje X")
        elif X == 0 and Y == 0:
            print("Se encuentra en el origen")
Punto.cuadrante()


