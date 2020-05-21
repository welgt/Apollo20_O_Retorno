import pygame
from Tela import *


class painel:
    def __init__(self):
        self.__painel = None
        self.__cor = 0
        self.__posicao_x = 0
        self.__posicao_y = 0
        self.__largura = 0
        self.__altura = 0

    def cria_painel(self, tela, posicao_x, posicao_y, largura, altura):
        self.__posicao_x = posicao_x + RESOLUCAO[0] / 2 - self.__largura / 2
        self.__posicao_y = posicao_y + RESOLUCAO[1] / 2 - self.__altura / 2
        self.__largura = (RESOLUCAO[0] / 1000) * (largura * 10)
        self.__altura = (RESOLUCAO[1] / 1000) * (altura * 10)

       

    def draw_painel(self, tela, cor):
        self.__painel = pygame.Rect(self.__posicao_x, self.__posicao_y, self.__largura,
                                    self.__altura)
        tela.draw_rect(cor, self.__painel)

    def draw_borda_painel(self, tela, cor):
        borda = [(self.__posicao_x, self.__posicao_y),
                 (self.__posicao_x + self.__largura, self.__posicao_y),
                 (self.__posicao_x + self.__largura, self.__posicao_y + self.__altura),
                 (self.__posicao_x, self.__posicao_y + self.__altura)]
        tela.draw_lines(cor, borda, 3)


    def get_cor(self):
        return self.__cor

    def set_cor(self, cor):
        self.__cor = cor

    def get_posicao_x(self):
        return self.__posicao_x

    def set_posicao_x(self, posicao_x):
        self.__posicao_x = posicao_x

    def get_posicao_y(self):
        return self.__posicao_y

    def set_posicao_y(self, posicao_y):
        self.__posicao_y = posicao_y

    def get_largura(self):
        return self.__largura

    def set_largura(self, largura):
        self.__largura = largura

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura

    def get_painel(self):
        return self.__painel



class botao:

    def __init__(self):
        self.__botao = None
        self.__cor = 0
        self.__posicao_x = 0
        self.__posicao_y = 0
        self.__largura = 0
        self.__altura = 0
        self.__qtd_botao = 0
        self.__clicou = False



    def criar_botao(self, painel, posicao_x, posicao_y, largura, altura):


        self.__posicao_x = posicao_x + painel.get_posicao_x() + painel.get_largura() / 2 - self.__largura / 2
        self.__posicao_y = posicao_y + painel.get_posicao_y() + painel.get_altura() / 2 - self.__altura / 2
        self.__largura = (painel.get_largura() / 1000) * (largura * 10)
        self.__altura = (painel.get_altura()/1000)* (altura*10)



    def draw_botao(self, tela, cor):
        self.__botao = pygame.Rect(self.__posicao_x, self.__posicao_y, self.__largura, self.__altura)
        tela.draw_rect(cor, self.__botao)

    def draw_borda_botao(self, tela, cor):
        borda = [(self.__posicao_x, self.__posicao_y),
                 (self.__posicao_x+self.__largura, self.__posicao_y),
                 (self.__posicao_x+ self.__largura, self.__posicao_y+self.__altura),
                 (self.__posicao_x ,self.__posicao_y+ self.__altura)]

        tela.draw_lines(cor, borda, 3)

    def get_cor(self):
        return self.__cor

    def set_cor(self, cor):
        self.__cor = cor

    def get_posicao_x(self):
        return self.__posicao_x

    def set_posicao_x(self, posicao_x):
        self.__posicao_x = posicao_x

    def get_posicao_y(self):
        return self.__posicao_y

    def set_posicao_y(self, posicao_y):
        self.__posicao_y = posicao_y

    def get_largura(self):
        return self.__largura

    def set_largura(self, largura):
        self.__largura = largura

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura

    def get_botao(self):
        return self.__botao

    def __verifica_colisao(self, botao):
        if pygame.mouse.get_pos()[0] >= botao.get_posicao_x() and \
                pygame.mouse.get_pos()[0] <= botao.get_posicao_x() + botao.get_largura() and \
                pygame.mouse.get_pos()[1] >= botao.get_posicao_y() and \
                pygame.mouse.get_pos()[1] <= botao.get_posicao_y() + botao.get_altura():
            print("colidiu")
            self.__clicou = True
        else:
            print("nao colidiu")
            self.__clicou = False

    def evento(self, evento, botao):

        #captura o click do mouse caso ele for apertado
        if evento.type == pygame.MOUSEBUTTONDOWN:
            #print(evento)
            #print("fucionou o click")
            #print("posicao mouse x ", pygame.mouse.get_pos()[0])
            #print("posicao botao x ", botao.get_posicao_x())
            #print("posicao mouse y ", pygame.mouse.get_pos()[1])
            #print("posicao botao y ", botao.get_posicao_y())
            self.__verifica_colisao(botao)
            #calcula a area de colisao do botao que chamou a funcao
            #if pygame.mouse.get_pos()[0] >= botao.get_posicao_x() and \
             #       pygame.mouse.get_pos()[0] <= botao.get_posicao_x() + botao.get_largura() and \
              #      pygame.mouse.get_pos()[1] >= botao.get_posicao_y() and \
               #     pygame.mouse.get_pos()[1] <= botao.get_posicao_y() + botao.get_altura():
                #print("colidiu")

            #elif evento.type == pygame.MOUSEBUTTONUP:
             #   print("passei o mouse por cima")



