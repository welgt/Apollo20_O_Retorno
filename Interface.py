import pygame
from Tela import *


class Nova_interface:
    def __init__(self):
        self.__botao = self
        self.__cor_botao = 0
        self.__botao_posicao_x = 0
        self.__botao_posicao_y = 0
        self.__botao_largura = 0
        self.__botao_altura = 0

        self.__qtd_botao = 0


        self.__painel = None
        self.__cor_painel = 0
        self.__painel_posicao_x = 0
        self.__painel_posicao_y = 0
        self.__painel_largura = 0
        self.__painel_altura = 0




    def cria_painel(self, tela, posicao_x, posicao_y, largura, altura):

        self.__painel_posicao_x = posicao_x + RESOLUCAO[0]/2 - self.__painel_largura/2
        self.__painel_posicao_y = posicao_y + RESOLUCAO[1]/2 - self.__painel_altura/2
        self.__painel_largura = (RESOLUCAO[0]/1000)* (largura*10)
        self.__painel_altura = (RESOLUCAO[1]/1000)* (altura*10)

        return self

    def criar_botao(self, tela, posicao_x, posicao_y, largura, altura):

        self.__botao_posicao_x = posicao_x + self.__painel_posicao_x + self.__painel_largura/2 - self.__botao_largura/2
        self.__botao_posicao_y = posicao_y + self.__painel_posicao_y + self.__painel_altura/2 - self.__botao_altura/2
        self.__botao_largura = (self.__painel_largura/1000)* (largura*10)
        self.__botao_altura = (self.__painel_altura/1000)* (altura*10)

        return self

    def draw_painel(self, tela, cor):
        self.__painel = pygame.Rect(self.__painel_posicao_x, self.__painel_posicao_y, self.__painel_largura, self.__painel_altura)
        tela.draw_rect(cor, self.__painel)

    def draw_borda_painel(self, tela, cor):

        borda = [(self.__painel_posicao_x, self.__painel_posicao_y),
                 (self.__painel_posicao_x+self.__painel_largura, self.__painel_posicao_y),
                 (self.__painel_posicao_x+ self.__painel_largura, self.__painel_posicao_y+self.__painel_altura),
                 (self.__painel_posicao_x ,self.__painel_posicao_y+ self.__painel_altura)]

        tela.draw_lines(cor, borda, 3)


    def draw_botao(self, tela, cor):
        self.__botao = pygame.Rect(self.__botao_posicao_x, self.__botao_posicao_y, self.__botao_largura, self.__botao_altura)
        tela.draw_rect(cor, self.__botao)

    def draw_borda_botao(self, tela, cor):
        borda = [(self.__botao_posicao_x, self.__botao_posicao_y),
                 (self.__botao_posicao_x+self.__botao_largura, self.__botao_posicao_y),
                 (self.__botao_posicao_x+ self.__botao_largura, self.__botao_posicao_y+self.__botao_altura),
                 (self.__botao_posicao_x ,self.__botao_posicao_y+ self.__botao_altura)]

        tela.draw_lines(cor, borda, 3)




    def get_botao(self):
        return self

    def set_cor_botao(self, cor):
        self.__cor_botao = cor


    def get_qtd_botoes(self):
        return self.__qtd_botao

    def set_qtd_botoes(self, qtd):
        self.__qtd_botao = qtd

    def get_largura_botao(self):
        return self.__botao_largura

    def get_altura_botao(self):
        return  self.__botao_altura

    def get_posicao_x_botao(self):
        return self.__botao_posicao_x

    def set_posicao_x_botao(self, posicao_x):
        self.__botao_posicao_x = posicao_x

    def get_posicao_y_botao(self):
        return self.__botao_posicao_y

    def get_tamanho_painel(self):
        return self.__painel_largura, self.__painel_altura

    def get_tamanho_botao(self):
        return self.__botao_largura, self.__botao_altura