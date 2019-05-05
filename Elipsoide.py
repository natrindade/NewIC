from visual import *

class Elipsoide:
    forma = None

    def __init__(self):
        self.forma = cylinder()

    def posicao(self, x, y, z):
        self.forma.pos = (x, y, z)

    def largura(self, valor):
        self.forma.width = valor

    def altura(self, valor):
        self.forma.height = valor

    def comprimento(self, valor):
        self.forma.length = valor

    def cor(self, vermelho, verde, azul):
        self.forma.color = (self.convertCor(vermelho), self.convertCor(verde), self.convertCor(azul))

    def convertCor(self, cor):
        return ((cor * 100.0) / 255.0) / 100.0