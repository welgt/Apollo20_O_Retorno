import pygame
import math
from Config import *

# falta arrumar a def get_centro_surface e adicionala na funcao de rotacionar

class Novo_objeto:
    def __init__(self, surface, posicao_x,posicao_y):
        self.__surface = pygame.image.load(surface)
        self.__tamanho_x = self.__surface.get_rect()[2]
        self.__tamanho_y = self.__surface.get_rect()[3]
        self.__posicao_x = posicao_x
        self.__posicao_y = posicao_y
        #self.__centro_surface = self.__posicao_x + (self.__tamanho_x / 2), self.get_posicao_y + self.__tamanho_y / 2
        self.__velocidade = 0, 0
        self.__friccao = 0
        self.__angulo_rotacao = 0
        self.__velocidade_rotacao = 0
        self.__rect =self.__surface.get_rect()
        self.__propulsor = False
        self.__colidiu_tela = False
        self.__rotacionou = False, False

    def get_surface(self):
        return self.__surface

    def set_surface(self, nova_surface):
        self.__surface = pygame.image.load(nova_surface)

    def get_posicao_x(self):
        return self.__posicao_x

    def get_posicao_y(self):
        return self.__posicao_y

    def get_posicao_x(self):
        return self.__posicao_x, self.__posicao_y

    def set_posicao(self, nova_posicao_x, nova_posicao_y):
        self.__posicao_x = nova_posicao_x
        self.__posicao_y =  nova_posicao_y

    def get_posicao(self):
        return self.__posicao_x, self.__posicao_y

    def get_tamanho_x(self):
        return self.__tamanho_x

    def get_tamanho_y(self):
        return self.__tamanho_y

    def set_tamanho(self, novo_tamanho_x, novo_tamanho_y):
        self.__surface = pygame.transform.scale(self.__surface, (novo_tamanho_x, novo_tamanho_y))
        novo_centro = novo_tamanho_x/2, novo_tamanho_y/2
        self.set_centro(novo_centro)
        self.__tamanho_x = novo_tamanho_x
        self.__tamanho_y = novo_tamanho_y


    def get_centro_surface(self):
        return self.__centro_surface

    def set_centro(self, novo_centro):
        self.__centro_surface = novo_centro



    def get_velocidade(self):
        return self.__velocidade

    def set_velocidade(self, nova_velocidade):
        self.__velocidade = nova_velocidade

    def get_rect(self):
        return self.__rect

    def get_friccao(self):
        return self.__friccao

    def set_friccao(self, nova_friccao):
        self.__friccao = nova_friccao

    def get_angulo_rotacao(self):
        return self.__angulo_rotacao

    def set_angulo_rotacao(self, novo_angulo_rotacao):
        self.__angulo_rotacao = novo_angulo_rotacao

    def get_velocidade_rotacao(self):
        return self.__velocidade_rotacao

    def set_velocidade_rotacao(self, nova_velocidade_rotacao):
        self.__velocidade_rotacao = nova_velocidade_rotacao

    def get_propulsor_ativo(self):
        return self.__propulsor

    def set_propulsor_ativo(self, booleana):
        self.__propulsor = booleana

    def get_colidiu_tela(self):
        return self.__colidiu_tela

    def set_colidiu_tela(self, booleana):
        self.__colidiu_tela = booleana

    def get_rotacionou(self):
        return self.__rotacionou

    def set_rotacionou(self, booleana):
        self.__rotacionou = booleana

    def rotacaoCentralizada(self,angulo):

        surface = pygame.transform.rotate(self.get_surface(), angulo)
        nova_posicao = surface.get_rect(center=self.get_centro_surface())
        nova_posicao[0] += self.get_posicao()[0]
        nova_posicao[1] += self.get_posicao()[1]

        return surface ,nova_posicao


    def criaPoligono_Propulsor(self, largura_poligono, posicao_x, ponto_acelerador_poligono):


        ponto_direito = largura_poligono + self.__posicao_x + self.__tamanho_x / 2 + posicao_x
        ponto_esquerdo = -largura_poligono + self.__posicao_x + self.__tamanho_x / 2 + posicao_x
        ponto_acelerador_poligono += self.__posicao_y + self.__tamanho_y
        altura_base = self.__tamanho_y

        vertices_propulsor = ((ponto_direito, altura_base + self.__posicao_y),  # (0,3),
                              (self.__posicao_x + self.__tamanho_x / 2 + posicao_x, ponto_acelerador_poligono),  # (3,-3)
                              (ponto_esquerdo, altura_base + self.__posicao_y))  # (-3,-3)

        return self.__rotacionaPoligono_propulsor(vertices_propulsor)



    def __rotacionaPoligono_propulsor(self, vertices_propulsor):

        origem_nave = self.__posicao_x + self.__tamanho_x / 2, self.__posicao_y + self.__tamanho_x / 2
        angulo_rotacao = math.radians(-self.get_angulo_rotacao())

        poligono_rotacionado = []

        for vertice in vertices_propulsor:
            vertice_aux = vertice[0] - origem_nave[0], vertice[1] - origem_nave[1]
            vertice_aux = (vertice_aux[0] * math.cos(angulo_rotacao) - vertice_aux[1] * math.sin(angulo_rotacao),
                           vertice_aux[0] * math.sin(angulo_rotacao) + vertice_aux[1] * math.cos(angulo_rotacao))
            vertice_aux = vertice_aux[0] + origem_nave[0], vertice_aux[1] + origem_nave[1]
            poligono_rotacionado.append(vertice_aux)

        return poligono_rotacionado


    def colisao(self, posEixoObjeto, tamanho, resolucaoTela):                # considerando novo centro da imagem  - (tamanho/2)
        if posEixoObjeto >= 0 and posEixoObjeto <= resolucaoTela - tamanho/2:
            #self.colidiu = False
            self.set_colidiu_tela(False)
        else:
            #print("colidiu")
            #self.colidiu = True
            self.set_colidiu_tela(True)
            if posEixoObjeto < resolucaoTela / 2:
                #print(self.posicao_y)
                posEixoObjeto = 0
            else:                                         # considerando novo centro da imagem  - (tamanho/2)
                posEixoObjeto = resolucaoTela - tamanho/2
        return posEixoObjeto


    def verifica_colisao_tela(self):
        #self.posicao_x = self.colisao(self.posicao_x, self.tamanho_x, RESOLUCAO[0])
        self.get_posicao()[0] = self.colisao(self.get_posicao()[0], self.get_tamanho()[0], RESOLUCAO[0])
        #self.posicao_y = self.colisao(self.posicao_y, self.tamanho_y, RESOLUCAO[1])
        self.get_posicao()[1] = self.colisao(self.get_posicao()[1], self.get_tamanho()[1], RESOLUCAO[1])