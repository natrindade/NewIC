from time import clock
from vis.graph import gcurve, gdisplay
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
Ombro.cor(color.white)


Umero1 = Cilindro(frame1)

Umero1.posicao(4.5,0,0)
Umero1.eixo(1,0,0)
Umero1.raio(1.5)

Umero2 = Cilindro(frame1)

Umero2.posicao(5.5,0.1,0)
Umero2.eixo(1,0,0)
Umero2.raio(1.4)


Umero3 = Cilindro(frame1)

Umero3.posicao(6.5,0.2,0)
Umero3.eixo(1,0,0)
Umero3.raio(1.3)


Umero4 = Cilindro(frame1)

Umero4.posicao(7.5,0.3,0)
Umero4.eixo(1,0,0)
Umero4.raio(1.2)


Umero5 = Cilindro(frame1)

Umero5.posicao(8.5,0.4,0)
Umero5.eixo(1,0,0)
Umero5.raio(1.1)

Umero6 = Cilindro(frame1)

Umero6.posicao(9.5,0.5,0)
Umero6.eixo(1,0,0)
Umero6.raio(1.1)

Umero7 = Cilindro(frame1)

Umero7.posicao(10.5,0.6,0)
Umero7.eixo(1,0,0)
Umero7.raio(1.1)


Umero8 = Cilindro(frame1)

Umero8.posicao(11.5,0.7,0)
Umero8.eixo(1,0,0)
Umero8.raio(1.1)

Umero9 = Cilindro(frame1)

#-------------------------------------------------------------------------------------------------------------------------------
#2 parte do umero a partir dos 12.5cm


Umero9.posicao(12.5,0.8,0)
Umero9.eixo(1,0,0)
Umero9.raio(1.1)



Umero10 = Cilindro(frame1)

Umero10.posicao(13.5,0.9,0)
Umero10.eixo(1,0,0)
Umero10.raio(1.1)

Umero11 = Cilindro(frame1)

Umero11.posicao(14.5,0.9,0)
Umero11.eixo(1,0,0)
Umero11.raio(1.1)


Umero12 = Cilindro(frame1)

Umero12.posicao(15.5,0.9,0)
Umero12.eixo(1,0,0)
Umero12.raio(1.2)

Umero13 = Cilindro(frame1)

Umero13.posicao(16.5,0.8,0)
Umero13.eixo(1,0,0)
Umero13.raio(1.3)

Umero14 = Cilindro(frame1)

Umero14.posicao(17.5,0.7,0)
Umero14.eixo(1,0,0)
Umero14.raio(1.4)

Umero15 = Cilindro(frame1)

Umero15.posicao(18.5,0.6,0)
Umero15.eixo(1,0,0)
Umero15.raio(1.5)

Umero16 = Cilindro(frame1)

Umero16.posicao(19.5,0.5,0)
Umero16.eixo(1,0,0)
Umero16.raio(1.6)
#----------------------------------------------------------------------------------------------------------------------------------------
#Parte final do umero___articulacao

Umero17= Cilindro(frame1)

Umero17.posicao(20.5,0.5,0)
Umero17.eixo(1,0,0)
Umero17.raio(1.7)

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

ulna18 = Cone(frame2)

ulna18.posicao(23.7,1.15,0)
ulna18.eixo(-1,0,0)
ulna18.raio(1)

ulna19 = Cilindro(frame2)

ulna19.posicao(23.7,1.15,0)
ulna19.eixo(1,0,0)
ulna19.raio(1.1)

ulna20 = Cilindro(frame2)

ulna20.posicao(24.7,1.15,0)
ulna20.eixo(1,0,0)
ulna20.raio(1.1)

ulna21= Cilindro(frame2)

ulna21.posicao(25.7,1.2,0)
ulna21.eixo(1,0,0)
ulna21.raio(1.1)

ulna22 = Cilindro(frame2)

ulna22.posicao(26.7,1.25,0)
ulna22.eixo(1,0,0)
ulna22.raio(1.1)

ulna23 = Cilindro(frame2)

ulna23.posicao(27.7,1.3,0)
ulna23.eixo(1,0,0)
ulna23.raio(1.1)

ulna24 = Cilindro(frame2)

ulna24.posicao(28.7,1.4,0)
ulna24.eixo(1,0,0)
ulna24.raio(1)

ulna25 = Cilindro(frame2)

ulna25.posicao(29.7,1.5,0)
ulna25.eixo(1.3,0,0)
ulna25.raio(0.95)
#-----------------------------------------------------------------------------------------------------------------------------------------
#Ulna_Parte2

ulna26 = Cilindro(frame2)

ulna26.posicao(31,1.55,0)
ulna26.eixo(1,0,0)
ulna26.raio(0.9)

ulna27 = Cilindro(frame2)

ulna27.posicao(32,1.6,0)
ulna27.eixo(1,0,0)
ulna27.raio(0.85)

ulna28 = Cilindro(frame2)

ulna28.posicao(33,1.65,0)
ulna28.eixo(0.5,0,0)
ulna28.raio(0.8)

#------------------------------------------------------------------------------------------------------------------------------------
#Ulna_parte3

ulna29 = Cilindro(frame2)

ulna29.posicao(33.5,1.7,0)
ulna29.eixo(1,0,0)
ulna29.raio(0.8)

ulna30 = Cilindro(frame2)

ulna30.posicao(34.5,1.75,0)
ulna30.eixo(1,0,0)
ulna30.raio(0.8)

ulna31 = Cilindro(frame2)

ulna31.posicao(35.5,1.8,0)
ulna31.eixo(1,0,0)
ulna31.raio(0.8)

ulna32 = Cilindro(frame2)

ulna32.posicao(36.5,1.85,0)
ulna32.eixo(1,0,0)
ulna32.raio(0.8)

ulna33 = Cilindro(frame2)

ulna33.posicao(37.5,1.85,0)
ulna33.eixo(1,0,0)
ulna33.raio(0.8)

#----------------------------------------------------------------------------------------------------------------------------------
#Ulna_parte4

ulna34 = Cilindro(frame2)

ulna34.posicao(38.5,1.85,0)
ulna34.eixo(1,0,0)
ulna34.raio(0.8)

ulna35 = Cilindro(frame2)

ulna35.posicao(37.5,1.85,0)
ulna35.eixo(1,0,0)
ulna35.raio(0.75)

ulna36 = Cilindro(frame2)

ulna36.posicao(38.5,1.9,0)
ulna36.eixo(1,0,0)
ulna36.raio(0.7)

ulna37 = Cilindro(frame2)

ulna37.posicao(39.5,1.95,0)
ulna37.eixo(1,0,0)
ulna37.raio(0.7)

ulna38 = Cilindro(frame2)

ulna38.posicao(40.5,1.95,0)
ulna38.eixo(1,0,0)
ulna38.raio(0.7)

ulna39 = Cilindro(frame2)

ulna39.posicao(41.5,1.9,0)
ulna39.eixo(1,0,0)
ulna39.raio(0.7)

ulna40 = Cilindro(frame2)

ulna40.posicao(42.5,1.85,0)
ulna40.eixo(1,0,0)
ulna40.raio(0.7)

ulna41 = Cilindro(frame2)

ulna41.posicao(43.5,1.8,0)
ulna41.eixo(1,0,0)
ulna41.raio(0.7)

ulna42 = Cilindro(frame2)

ulna42.posicao(44.5,1.75,0)
ulna42.eixo(1,0,0)
ulna42.raio(0.70)

ulna43 = Cilindro(frame2)

ulna43.posicao(45.5,1.7,0)
ulna43.eixo(1.2,0,0)
ulna43.raio(0.70)

#---------------------------------------------------------------------------------------------------------------------------------------
#Radio_parte1

radio44 = Cilindro(frame2)

radio44.posicao(23.7,-0.8,0)
radio44.eixo(1,0,0)
radio44.raio(1.2)

radio45 = Cilindro(frame2)

radio45.posicao(24.7,-0.85,0)
radio45.eixo(1,0,0)
radio45.raio(1.15)

radio46 = Cilindro(frame2)

radio46.posicao(25.7,-0.9,0)
radio46.eixo(1,0,0)
radio46.raio(1)

radio47 = Cilindro(frame2)

radio47.posicao(26.7,-0.95,0)
radio47.eixo(1,0,0)
radio47.raio(0.95)

radio48 = Cilindro(frame2)

radio48.posicao(27.7,-1,0)
radio48.eixo(1,0,0)
radio48.raio(0.9)

radio49 = Cilindro(frame2)

radio49.posicao(28.7,-1.05,0)
radio49.eixo(1,0,0)
radio49.raio(0.9)

radio50 = Cilindro(frame2)

radio50.posicao(29.7,-1.1,0)
radio50.eixo(1,0,0)
radio50.raio(0.9)

radio51 = Cilindro(frame2)

radio51.posicao(30.7,-1.15,0)
radio51.eixo(1,0,0)
radio51.raio(0.85)

radio52 = Cilindro(frame2)

radio52.posicao(31.7,-1.2,0)
radio52.eixo(1,0,0)
radio52.raio(0.8)
#------------------------------------------------------------------------------------------------------------------------------------
#Radio_parte2

radio53 = Cilindro(frame2)

radio53.posicao(32.7,-1.25,0)
radio53.eixo(1,0,0)
radio53.raio(0.75)

radio54 = Cilindro(frame2)

radio54.posicao(33.7,-1.3,0)
radio54.eixo(1,0,0)
radio54.raio(0.7)

#--------------------------------------------------------------------------------------------------------------------------------------
#Radio_Parte3

radio55 = Cilindro(frame2)

radio55.posicao(34.7,-1.25,0)
radio55.eixo(1,0,0)
radio55.raio(0.75)

radio56 = Cilindro(frame2)

radio56.posicao(35.7,-1.2,0)
radio56.eixo(1,0,0)
radio56.raio(0.8)

radio57 = Cilindro(frame2)

radio57.posicao(36.7,-1.15,0)
radio57.eixo(1,0,0)
radio57.raio(0.85)
#--------------------------------------------------------------------------------------------------------------------------------------
#Radio_Parte4

radio58 = Cilindro(frame2)

radio58.posicao(37.7,-1.2,0)
radio58.eixo(1,0,0)
radio58.raio(0.9)

radio59 = Cilindro(frame2)

radio59.posicao(38.7,-1.25,0)
radio59.eixo(1,0,0)
radio59.raio(0.95)

radio60 = Cilindro(frame2)

radio60.posicao(39.7,-1.3,0)
radio60.eixo(1,0,0)
radio60.raio(1)

radio61 = Cilindro(frame2)

radio61.posicao(40.7,-1.35,0)
radio61.eixo(1,0,0)
radio61.raio(1.05)

radio62 = Cilindro(frame2)

radio62.posicao(41.7,-1.3,0)
radio62.eixo(1,0,0)
radio62.raio(1.1)

radio63 = Cilindro(frame2)

radio63.posicao(42.7,-1.25,0)
radio63.eixo(1,0,0)
radio63.raio(1.15)

radio64 = Cilindro(frame2)

radio64.posicao(43.7,-1.2,0)
radio64.eixo(1,0,0)
radio64.raio(1.2)

radio65 = Cilindro(frame2)

radio65.posicao(44.7,-1.15,0)
radio65.eixo(1,0,0)
radio65.raio(1.25)

radio66 = Cilindro(frame2)

radio66.posicao(45.7,-1.1,0)
radio66.eixo(1,0,0)
radio66.raio(1.4)
#------------------------------------------------------------------------------------------------------------------------------------
#uniao das partes para movimentacao conjunta, semelhante a movimentacao do braco

frame1.pos = (0,0,0)
frame1.axis = (23.7,0,0)

frame2.pos=(0,0,0)
frame2.axis=(22.5,0,0)

#-------------------------------------------------------------------------------------------------------------------------------------
#calculo do centro de massa e sua representacao

CentroMassa=Esfera(frame2)

CentroMassa.posicao(55.596,0.135,0)
CentroMassa.raio(1.5)
CentroMassa.cor(color.red)


#-------------------------------------------------------------------------------------------------------------------------------------
#melhorando a obsevacao da movimentacao do braco

frame1.rotate(angle=pi/2, axis=(1, 0, 0), origin=(0, 0, 0))
frame2.rotate(angle=pi/2, axis=(1, 0, 0), origin=(0, 0, 0))

#--------------------------------------------------------------------------------------------------------------------------------------
#grafico de posicao


# ___ Tempo ___
tempo_a = 10  # [s] : Tempo de amostragem
N_pontos = tempo_a * 100.
dt = 0.01
temp = 0.
t = [0.]

for i in range(int(N_pontos)):
    temp = temp + dt
    t.append(temp)


graph1 = gdisplay(x=386, y=25, width=439, height=237, #parece que x e y sao o tamanho da janela
                  title='Movimentacao do Centro de Massa [cm]', xtitle='Movimentacao Horizontal [cm]',
                  ytitle='Movimentacao Vertical[cm]',
                  xmax=30, xmin=-30, ymax=30, ymin=-30,
                  foreground=color.black, background=color.white)




# ___ Loop ___
finished = False
rate_time = 1.3 * N_pontos / tempo_a
start = clock()


tempo = 0.
cont = 0
w = 1.61*pi/(2*tempo_a)
#w = pi/(2*tempo_a)
d_teta = w*dt

grafico = gcurve(gdisplay=graph1,color=color.blue)

flag = false
valorAnterior = 0

def plataGrafico(grafico, pos_CM):
    global flag
    global valorAnterior

    print(str(pos_CM.x) + " - " + str(pos_CM.z))
    if(valorAnterior > pos_CM.x):
        flag = true

    cor = color.red
    if (flag):
        cor = color.blue
    grafico.plot(pos=(pos_CM.x, pos_CM.z * -1), color=cor)

    valorAnterior = pos_CM.x


while not finished:
    rate(rate_time)

    tempo = t[cont]

    frame2.rotate(angle=d_teta, axis=(0,0,1), origin=(23.7, 0, 0))

    pos_CM = frame2.frame_to_world(frame2.pos)

    frame_pos = frame2.world_to_frame(pos_CM)

    ponto = 23
    plataGrafico(grafico, pos_CM)

    cont = cont + 1

    if tempo >= t[t.__len__() - 1]:
      finished = True

print ''
print '__Processamento__'
print 'Foram realizadas %i iteracoes' % (cont)
tempo_gasto = clock() - start
print 'Tempo gasto: %f segundos' % tempo_gasto
print 'Tempo plotado: %f segundos' % tempo