import pygame
import math

# falta arrumar a def get_centro_surface e adicionala na funcao de rotacionar

class Novo_objeto:
    def __init__(self, surface, posicao):
        self.__surface = pygame.image.load(surface)
        self.__tamanho = self.__surface.get_rect()[2], self.__surface.get_rect()[3]
        self.__posicao = posicao[0], posicao[1]
        self.__centro_surface = self.get_posicao()[0]+self.__tamanho[0]/2, self.get_posicao()[1] + self.__tamanho[1]/2
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

    def get_posicao(self):
        return self.__posicao

    def set_posicao(self, nova_posicao):
        self.__posicao = nova_posicao

    def get_tamanho(self):
        return self.__tamanho

    def set_tamanho(self, novo_tamanho):
        self.__surface = pygame.transform.scale(self.__surface, (novo_tamanho))
        novo_centro = novo_tamanho[0]/2, novo_tamanho[1]/2
        self.set_centro(novo_centro)
        self.__tamanho = novo_tamanho


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

    def rotacaoCentralizada(self,angulo):

        surface = pygame.transform.rotate(self.get_surface(), angulo)
        nova_posicao = surface.get_rect(center=self.get_centro_surface())
        nova_posicao[0] += self.get_posicao()[0]
        nova_posicao[1] += self.get_posicao()[1]

        return surface ,nova_posicao

    def criaPoligono_Propulsor(self, largura_poligono, posicao_x, ponto_acelerador_poligono):


        ponto_direito = largura_poligono + self.get_posicao()[0] +self.__tamanho[0]/2 + posicao_x
        ponto_esquerdo = -largura_poligono + self.get_posicao()[0] +self.__tamanho[0]/2+ posicao_x
        ponto_acelerador_poligono += self.get_posicao()[1]+ self.get_tamanho()[1]
        altura_base = self.get_tamanho()[1]

        vertices_propulsor = ((ponto_direito, altura_base + self.get_posicao()[1]),  # (0,3),
                              (self.get_posicao()[0] +self.__tamanho[0]/2+ posicao_x, ponto_acelerador_poligono),  # (3,-3)
                              (ponto_esquerdo, altura_base + self.get_posicao()[1]))  # (-3,-3)

        return self.__rotacionaPoligono_propulsor(vertices_propulsor)



    def __rotacionaPoligono_propulsor(self, vertices_propulsor):

        origem_nave = self.get_posicao()[0]+self.__tamanho[0]/2, self.get_posicao()[1] + self.__tamanho[1]/2
        angulo_rotacao = math.radians(-self.__angulo_rotacao)

        poligono_rotacionado = []

        for vertice in vertices_propulsor:
            vertice_aux = vertice[0] - origem_nave[0], vertice[1] - origem_nave[1]
            vertice_aux = (vertice_aux[0] * math.cos(angulo_rotacao) - vertice_aux[1] * math.sin(angulo_rotacao),
                           vertice_aux[0] * math.sin(angulo_rotacao) + vertice_aux[1] * math.cos(angulo_rotacao))
            vertice_aux = vertice_aux[0] + origem_nave[0], vertice_aux[1] + origem_nave[1]
            poligono_rotacionado.append(vertice_aux)

        return poligono_rotacionado

