import math
from NovoObjeto import *
from NovaTela import *
from Config import *

import pygame

pygame.init()

tela = Nova_tela('teste', (RESOLUCAO))
nave = Novo_objeto('arquivos/bola.jpg', 0,0)
nave.set_tamanho(50,50)
nave.set_posicao(550,550)


i = 0

jogoAtivo = True
while jogoAtivo:
    i+=0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogoAtivo = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jogoAtivo = False


    tela.fill(BLACK)
    nave.set_angulo_rotacao(i)
    naveRot = nave.rotacaoCentralizada(i)
    tela.blit(naveRot[0], naveRot[1])

    nave.criaPoligono_Propulsor(10,0,0)
    tela.set_fps(FPS)
    tela.flip()

    print("nave angulo rotacao :", nave.get_angulo_rotacao())
pygame.quit()

"""def rotatePolygon(self,angle):
   Rotates the given polygon which consists of corners represented as (x,y),
   around the ORIGIN, clock-wise, theta degrees

    angle = math.radians(angle)
    polygon = self
    rotatedPolygon = []
    for corner in polygon :
        rotatedPolygon.append(( corner[0]*math.cos(angle)-corner[1]*math.sin(angle) , corner[0]*math.sin(angle)+corner[1]*math.cos(angle)) )
    self = rotatedPolygon
    return"""