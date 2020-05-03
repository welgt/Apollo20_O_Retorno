import pygame

class Novo_objeto:
    def __init__(self, surface, posicao):
        self.__surface = pygame.image.load(surface)
        self.__tamanho = self.__surface.get_rect()[2], self.__surface.get_rect()[3]
        self.__posicao = posicao[0], posicao[1]
        self.__centro = (self.__posicao[0] + (self.__tamanho[0]/2)), (self.__posicao[1] + (self.__tamanho[1]/2))
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


    def get_centro(self):
        return self.__centro

    def set_centro(self, novo_centro):
        self.__centro = novo_centro



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
        nova_posicao = surface.get_rect(center=self.get_centro())
        nova_posicao[0] += self.get_posicao()[0]
        nova_posicao[1] += self.get_posicao()[1]

        return surface ,nova_posicao

