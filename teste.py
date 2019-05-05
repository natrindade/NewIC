from visual import *
from Bola import Bola

sorvete = frame()

sphere(pos=vector(0,0,100),
                radius=10, color=color.red)

bola1 = Bola(sorvete)
bola1.posicao(vector(0,0,0))
bola1.cor(color.yellow)

bola2 = Bola(sorvete)
bola2.posicao(vector(150,0,0))
bola2.cor(color.orange)

casquinha = cone(frame=sorvete, pos=vector(100,0,0),
     axis=vector(0,-400,0),
     radius=120)


sorvete.pos = (1000, 0, 0)
sorvete.axis = (1,10,0)
