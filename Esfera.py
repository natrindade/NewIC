from visual import *

class Esfera:

    forma = None



    def __init__(self,frame):
        self.forma = sphere(frame=frame) # frame esta passando os parametros necessarios de posicao

    def posicao(self, x, y, z):
        self.forma.pos = (x, y, z)


    def raio(self, r):
        self.forma.radius = r

    def cor(self, cor):
        self.forma.color = cor

