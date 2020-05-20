import pygame
import math
from Config import *

class Nova_nave:
    def __init__(self, surface, posicao_x, posicao_y):
        self.__surface = pygame.image.load(surface)
        self.__tamanho_x = self.__surface.get_rect()[2]
        self.__tamanho_y = self.__surface.get_rect()[3]
        self.__posicao_x = posicao_x
        self.__posicao_y = posicao_y
        #self.__centro_surface = self.__posicao_x + (self.__tamanho_x / 2), self.get_posicao_y + self.__tamanho_y / 2
        self.__velocidade_x = 0
        self.__velocidade_y = 0
        self.__potencia_propulsor = 0
        self.__friccao = 0
        self.__angulo_rotacao = 0
        self.__velocidade_rotacao = 0
        self.__rect =self.__surface.get_rect()
        self.__propulsor = False
        self.__colidiu_tela = False
        self.__rotacionou_dir = False
        self.__rotacionou_esq = False


    def get_surface(self):
        return self.__surface

    def set_surface(self, nova_surface):
        self.__surface = pygame.image.load(nova_surface)

    def get_posicao_x(self):
        return self.__posicao_x

    def set_posicao_x(self, posicao_x):
        self.__posicao_x = posicao_x

    def get_posicao_y(self):
        return self.__posicao_y

    def set_posicao_y(self, posicao_y):
        self.__posicao_y = posicao_y

    def get_posicao(self):
        return self.__posicao_x, self.__posicao_y

    def set_posicao(self, nova_posicao_x, nova_posicao_y):
        self.__posicao_x = nova_posicao_x
        self.__posicao_y =  nova_posicao_y

    def get_posicao(self):
        return self.__posicao_x, self.__posicao_y

    def set_velocidade_x(self, velocidade):
        self.__velocidade_x = velocidade

    def get_velocidade_x(self):
        return self.__velocidade_x

    def set_velocidade_y(self, velocidade):
        self.__velocidade_y = velocidade

    def get_velocidade_y(self):
        return self.__velocidade_y

    def get_potencia_propulsor(self):
         return self.__potencia_propulsor

    def set_potencia_propulsor(self, potencia_propulsor):
        self.__potencia_propulsor = potencia_propulsor

    def get_tamanho_y(self):
        return self.__tamanho_y

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

    def get_rotacionou_dir(self):
        return self.__rotacionou_dir

    def set_rotacionou_dir(self, booleana):
        self.__rotacionou_dir = booleana

    def get_rotacionou_esq(self):
        return self.__rotacionou_esq

    def set_rotacionou_esq(self, booleana):
        self.__rotacionou_esq = booleana


    def rotacaoCentralizada(self,angulo):

        surface = pygame.transform.rotate(self.get_surface(), angulo)
        nova_posicao = surface.get_rect(center=self.get_centro_surface())
        nova_posicao[0] += self.get_posicao()[0]
        nova_posicao[1] += self.get_posicao()[1]

        return surface ,nova_posicao


    def criaPoligono_Propulsor(self, largura_poligono, posicao_horizontal, ponto_acelerador_poligono):

        ponto_direito = largura_poligono + self.__posicao_x + self.__tamanho_x / 2 + posicao_horizontal
        ponto_esquerdo = -largura_poligono + self.__posicao_x + self.__tamanho_x / 2 + posicao_horizontal
        ponto_acelerador_poligono += self.__posicao_y + self.__tamanho_y
        altura_base = self.__tamanho_y

        vertices_propulsor = ((ponto_direito, altura_base + self.__posicao_y),  # (0,3),
                              (self.__posicao_x + self.__tamanho_x / 2 + posicao_horizontal, ponto_acelerador_poligono),  # (3,-3)
                              (ponto_esquerdo, altura_base + self.__posicao_y))  # (-3,-3)

        return self.__rotacionaPoligono_propulsor(vertices_propulsor)


    def __rotacionaPoligono_propulsor(self, vertices_propulsor):

        origem_nave = self.__posicao_x + self.__tamanho_x / 2, self.__posicao_y + self.__tamanho_y / 2
        angulo_rotacao = math.radians(-self.get_angulo_rotacao())

        poligono_rotacionado = []

        for vertice in vertices_propulsor:
            vertice_aux = vertice[0] - origem_nave[0], vertice[1] - origem_nave[1]
            vertice_aux = (vertice_aux[0] * math.cos(angulo_rotacao) - vertice_aux[1] * math.sin(angulo_rotacao),
                           vertice_aux[0] * math.sin(angulo_rotacao) + vertice_aux[1] * math.cos(angulo_rotacao))
            vertice_aux = vertice_aux[0] + origem_nave[0], vertice_aux[1] + origem_nave[1]
            poligono_rotacionado.append(vertice_aux)

        return poligono_rotacionado


    def __colisao(self, posEixoObjeto, tamanho, resolucaoTela):
        if posEixoObjeto >= 0 and posEixoObjeto <= resolucaoTela - tamanho:
            #self.colidiu = False
            self.set_colidiu_tela(False)
        else:
            #print("colidiu")
            self.set_colidiu_tela(True)
            if posEixoObjeto < resolucaoTela / 2:
                #print(self.posicao_y)
                posEixoObjeto = 0
            else:
                posEixoObjeto = resolucaoTela - tamanho
        return posEixoObjeto


    def verifica_colisao_tela(self):
        self.__posicao_x = self.__colisao(self.__posicao_x, self.__tamanho_x, RESOLUCAO[0])
        self.__posicao_y = self.__colisao(self.__posicao_y, self.__tamanho_y, RESOLUCAO[1])




    # ACELERACAO do propulsor
    def aceleracao_propulsor(self, tempo):

        if self.get_propulsor_ativo() == True:
            self.__velocidade_y-= (VELOCIDADE_ACELERACAO_LUA / FPS) * tempo * self.get_friccao()

            # permite aumentar o tamanho do propulsor ate 1
            if self.__potencia_propulsor < 1:
                self.__potencia_propulsor += (VELOCIDADE_ACELERACAO_LUA / FPS) * tempo * self.get_friccao()

            if self.get_velocidade_y() <= VELOCIDADE_ACELERACAO_LUA:
                tempo = 0

                # define nova direcao caso a nave esteja inclinada pra direita e propulsor ativo
                if self.get_angulo_rotacao()<=1 and self.get_propulsor_ativo():
                    self.__velocidade_x += self.get_angulo_rotacao()*-1 /360

                # define nova direcao caso a nave esteja inclinada pra esquerda e propulsor ativo
                if self.__angulo_rotacao >= 1 and self.get_propulsor_ativo():
                    self.__velocidade_x -= self.get_angulo_rotacao()/360



    def gravidade(self, tempo):

        # GRAVIDADE
        if self.get_propulsor_ativo() == False:

            self.__velocidade_y += (VELOCIDADE_ACELERACAO_LUA / FPS) * tempo * self.get_friccao()

            # diminiu o tamanho do propulsor
            self.__potencia_propulsor -= (VELOCIDADE_ACELERACAO_LUA / FPS) * tempo * self.get_friccao()

            # caso ele for menor que zero, fique em zero.
            if self.get_potencia_propulsor() < 0:
                self.set_potencia_propulsor(0)
            if self.get_velocidade_y() >= VELOCIDADE_ACELERACAO_LUA:
                tempo = 0
