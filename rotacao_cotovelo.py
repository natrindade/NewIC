from Cilindro import Cilindro
from Esfera import Esfera
from Cone import Cone
from visual import *

frame1=frame()#instancia, frame(objeto), frame() projeto do objeto,
frame2=frame()
frame3=frame()





Ombro=Esfera(frame1)

Ombro.posicao(2.5,0,0)
Ombro.raio(2.5)



Umero = Cilindro(frame1)

Umero.posicao(5,0,0)
Umero.eixo(1,0,0)
Umero.raio(1.5)

Umero = Cilindro(frame1)

Umero.posicao(3.5,0.1,0)
Umero.eixo(1,0,0)
Umero.raio(1.4)


Umero = Cilindro(frame1)

Umero.posicao(4.5,0.2,0)
Umero.eixo(1,0,0)
Umero.raio(1.3)


Umero = Cilindro(frame1)

Umero.posicao(5.5,0.3,0)
Umero.eixo(1,0,0)
Umero.raio(1.2)


Umero = Cilindro(frame1)

Umero.posicao(6.5,0.4,0)
Umero.eixo(1,0,0)
Umero.raio(1.1)

Umero = Cilindro(frame1)

Umero.posicao(7.5,0.5,0)
Umero.eixo(1,0,0)
Umero.raio(1.1)

Umero = Cilindro(frame1)

Umero.posicao(8.5,0.6,0)
Umero.eixo(1,0,0)
Umero.raio(1.1)

Umero = Cilindro(frame1)

Umero.posicao(9.5,0.7,0)
Umero.eixo(1,0,0)
Umero.raio(1.1)

Umero = Cilindro(frame1)

Umero.posicao(10.5,0.8,0)
Umero.eixo(1,0,0)
Umero.raio(1.1)

Umero = Cilindro(frame1)

Umero.posicao(11.5,0.9,0)
Umero.eixo(1,0,0)
Umero.raio(1.1)

Umero = Cilindro(frame1)

#-------------------------------------------------------------------------------------------------------------------------------
#2 parte do umero a partir dos 12.5cm


Umero.posicao(12.5,1,0)
Umero.eixo(1,0,0)
Umero.raio(1.1)



Umero = Cilindro(frame1)

Umero.posicao(13.5,1,0)
Umero.eixo(1,0,0)
Umero.raio(1.1)

Umero = Cilindro(frame1)

Umero.posicao(14.5,1,0)
Umero.eixo(1,0,0)
Umero.raio(1.1)


Umero = Cilindro(frame1)

Umero.posicao(15.5,0.9,0)
Umero.eixo(1,0,0)
Umero.raio(1.2)

Umero = Cilindro(frame1)

Umero.posicao(16.5,0.8,0)
Umero.eixo(1,0,0)
Umero.raio(1.3)

Umero = Cilindro(frame1)

Umero.posicao(17.5,0.7,0)
Umero.eixo(1,0,0)
Umero.raio(1.4)

Umero = Cilindro(frame1)

Umero.posicao(18.5,0.6,0)
Umero.eixo(1,0,0)
Umero.raio(1.5)

Umero = Cilindro(frame1)

Umero.posicao(19.5,0.5,0)
Umero.eixo(1,0,0)
Umero.raio(1.6)
#----------------------------------------------------------------------------------------------------------------------------------------
#Parte final do umero___articulacao

Umero= Cilindro(frame1)

Umero.posicao(20.5,0.5,0)
Umero.eixo(1,0,0)
Umero.raio(1.7)

#---------------------------------------------------------------------------------------------------------------------------------
#articulacao do cotovelo

capitulodoumero = Esfera(frame1)

capitulodoumero.posicao(22.7,-0.8,0)
capitulodoumero.raio(1.2)

trocleadoumero = Cone(frame1)

trocleadoumero.posicao(22.7,2.3,0)
trocleadoumero.eixo(0,-1.5,0)
trocleadoumero.raio(1)

trocleadoumero2 = Cone(frame1)

trocleadoumero2.posicao(22.7,-0.2,0)
trocleadoumero2.eixo(0,1.5,0)
trocleadoumero2.raio(1)

#Fim do umero
#----------------------------------------------------------------------------------------------------------------------------
#Ulna_parte1

ulna  = Cone(frame2)

ulna.posicao(23.7,1.15,0)
ulna.eixo(-1,0,0)
ulna.raio(1)

ulna = Cilindro(frame2)

ulna.posicao(23.7,1.15,0)
ulna.eixo(1,0,0)
ulna.raio(1.1)

ulna = Cilindro(frame2)

ulna.posicao(24.7,1.15,0)
ulna.eixo(1,0,0)
ulna.raio(1.1)

ulna = Cilindro(frame2)

ulna.posicao(25.7,1.2,0)
ulna.eixo(1,0,0)
ulna.raio(1.1)

ulna = Cilindro(frame2)

ulna.posicao(26.7,1.25,0)
ulna.eixo(1,0,0)
ulna.raio(1.1)

ulna = Cilindro(frame2)

ulna.posicao(27.7,1.3,0)
ulna.eixo(1,0,0)
ulna.raio(1.1)

ulna = Cilindro(frame2)

ulna.posicao(28.7,1.4,0)
ulna.eixo(1,0,0)
ulna.raio(1)

ulna = Cilindro(frame2)

ulna.posicao(29.7,1.5,0)
ulna.eixo(1.3,0,0)
ulna.raio(0.95)
#-----------------------------------------------------------------------------------------------------------------------------------------
#Ulna_Parte2

ulna = Cilindro(frame2)

ulna.posicao(31,1.55,0)
ulna.eixo(1,0,0)
ulna.raio(0.9)

ulna = Cilindro(frame2)

ulna.posicao(32,1.6,0)
ulna.eixo(1,0,0)
ulna.raio(0.85)

ulna = Cilindro(frame2)

ulna.posicao(33,1.65,0)
ulna.eixo(0.5,0,0)
ulna.raio(0.8)

#------------------------------------------------------------------------------------------------------------------------------------
#Ulna_parte3

ulna = Cilindro(frame2)

ulna.posicao(33.5,1.7,0)
ulna.eixo(1,0,0)
ulna.raio(0.8)

ulna = Cilindro(frame2)

ulna.posicao(34.5,1.75,0)
ulna.eixo(1,0,0)
ulna.raio(0.8)

ulna = Cilindro(frame2)

ulna.posicao(35.5,1.8,0)
ulna.eixo(1,0,0)
ulna.raio(0.8)

ulna = Cilindro(frame2)

ulna.posicao(36.5,1.85,0)
ulna.eixo(1,0,0)
ulna.raio(0.8)

ulna = Cilindro(frame2)

ulna.posicao(37.5,1.85,0)
ulna.eixo(1,0,0)
ulna.raio(0.8)

#----------------------------------------------------------------------------------------------------------------------------------
#Ulna_parte4

ulna = Cilindro(frame2)

ulna.posicao(38.5,1.8,0)
ulna.eixo(1,0,0)
ulna.raio(0.8)

ulna = Cilindro(frame2)

ulna.posicao(37.5,1.85,0)
ulna.eixo(1,0,0)
ulna.raio(0.75)

ulna = Cilindro(frame2)

ulna.posicao(38.5,1.9,0)
ulna.eixo(1,0,0)
ulna.raio(0.7)

ulna = Cilindro(frame2)

ulna.posicao(39.5,1.9,0)
ulna.eixo(1,0,0)
ulna.raio(0.7)

ulna = Cilindro(frame2)

ulna.posicao(40.5,1.95,0)
ulna.eixo(1,0,0)
ulna.raio(0.7)

ulna = Cilindro(frame2)

ulna.posicao(41.5,1.9,0)
ulna.eixo(1,0,0)
ulna.raio(0.7)

ulna = Cilindro(frame2)

ulna.posicao(42.5,1.85,0)
ulna.eixo(1,0,0)
ulna.raio(0.7)

ulna = Cilindro(frame2)

ulna.posicao(43.5,1.8,0)
ulna.eixo(1,0,0)
ulna.raio(0.7)

ulna = Cilindro(frame2)

ulna.posicao(44.5,1.75,0)
ulna.eixo(1,0,0)
ulna.raio(0.70)

ulna = Cilindro(frame2)

ulna.posicao(45.5,1.7,0)
ulna.eixo(1.2,0,0)
ulna.raio(0.70)

#---------------------------------------------------------------------------------------------------------------------------------------
#Radio_parte1

radio = Cilindro(frame3)

radio.posicao(23.7,-0.8,0)
radio.eixo(1,0,0)
radio.raio(1.2)

radio = Cilindro(frame3)

radio.posicao(24.7,-0.85,0)
radio.eixo(1,0,0)
radio.raio(1.15)

radio = Cilindro(frame3)

radio.posicao(25.7,-0.9,0)
radio.eixo(1,0,0)
radio.raio(1)

radio = Cilindro(frame3)

radio.posicao(26.7,-0.95,0)
radio.eixo(1,0,0)
radio.raio(0.95)

radio = Cilindro(frame3)

radio.posicao(27.7,-1,0)
radio.eixo(1,0,0)
radio.raio(0.9)

radio = Cilindro(frame3)

radio.posicao(28.7,-1.05,0)
radio.eixo(1,0,0)
radio.raio(0.95)

radio = Cilindro(frame3)

radio.posicao(29.7,-1.1,0)
radio.eixo(1,0,0)
radio.raio(0.9)

radio = Cilindro(frame3)

radio.posicao(30.7,-1.15,0)
radio.eixo(1,0,0)
radio.raio(0.85)

radio = Cilindro(frame3)

radio.posicao(31.7,-1.2,0)
radio.eixo(1,0,0)
radio.raio(0.8)
#-------------------------------------------------------------------------------------------------------------------------------------
#Radio_parte2

radio = Cilindro(frame3)

radio.posicao(32.7,-1.25,0)
radio.eixo(1,0,0)
radio.raio(0.75)

radio = Cilindro(frame3)

radio.posicao(33.7,-1.3,0)
radio.eixo(1,0,0)
radio.raio(0.7)

#--------------------------------------------------------------------------------------------------------------------------------------
#Radio_Parte3

radio = Cilindro(frame3)

radio.posicao(34.7,-1.25,0)
radio.eixo(1,0,0)
radio.raio(0.75)

radio = Cilindro(frame3)

radio.posicao(35.7,-1.2,0)
radio.eixo(1,0,0)
radio.raio(0.8)

radio = Cilindro(frame3)

radio.posicao(36.7,-1.15,0)
radio.eixo(1,0,0)
radio.raio(0.85)
#--------------------------------------------------------------------------------------------------------------------------------------
#Radio_Parte4

radio = Cilindro(frame3)

radio.posicao(37.7,-1.2,0)
radio.eixo(1,0,0)
radio.raio(0.9)

radio = Cilindro(frame3)

radio.posicao(38.7,-1.25,0)
radio.eixo(1,0,0)
radio.raio(0.95)

radio = Cilindro(frame3)

radio.posicao(39.7,-1.3,0)
radio.eixo(1,0,0)
radio.raio(1)

radio = Cilindro(frame3)

radio.posicao(40.7,-1.35,0)
radio.eixo(1,0,0)
radio.raio(1.05)

radio = Cilindro(frame3)

radio.posicao(41.7,-1.3,0)
radio.eixo(1,0,0)
radio.raio(1.1)

radio = Cilindro(frame3)

radio.posicao(42.7,-1.25,0)
radio.eixo(1,0,0)
radio.raio(1.15)

radio = Cilindro(frame3)

radio.posicao(43.7,-1.2,0)
radio.eixo(1,0,0)
radio.raio(1.2)

radio = Cilindro(frame3)

radio.posicao(44.7,-1.15,0)
radio.eixo(1,0,0)
radio.raio(1.25)

radio = Cilindro(frame3)

radio.posicao(45.7,-1.1,0)
radio.eixo(1,0,0)
radio.raio(1.4)
#------------------------------------------------------------------------------------------------------------------------------------

frame1.pos = (0,0,0)
frame1.axis = (23.7,0,0)

frame2.pos=(0,0,0)
frame2.axis=(22.5,0,0)


x=0.1

while 2:

  rate(10)
  frame3.rotate(angle=x, axis=(x,0,0), origin=(23.7,-0.8,0))
  print(x)
  x += 0.1
  if x >= 0.8:
    x = 0
    break

