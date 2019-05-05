from visual import *

class Cone:

    forma = None


    def __init__(self,frame):
        self.forma = cone(frame=frame)

    def posicao(self, x, y, z):
        self.forma.pos = (x, y, z)

    def eixo(self, comprimento, rotacionarVertical, rotacionarHorizontal):
        self.forma.axis = (comprimento, rotacionarVertical, rotacionarHorizontal)


    def raio(self, r):
        self.forma.radius = r
