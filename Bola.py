from visual import *

class Bola:

    bola = None

    def __init__(self, frame):
        self.bola = sphere(frame=frame, radius=100)

    def posicao(self, posicao):
        self.bola.pos = posicao

    def cor(self, cor):
        self.bola.color = cor