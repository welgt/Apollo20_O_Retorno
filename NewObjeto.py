import pygame

class New_objeto:
    def __init__(self, surface, posicao):
        self.__surface = pygame.image.load(surface)
        self.__posicao = posicao
        self.__tamanho = self.__surface.get_rect()[2], self.__surface.get_rect()[3]
        self.__velocidade = 0, 0
        self.__friccao = 0
        self.__angulo_rotacao = 0
        self.__velocidade_rotacao = 0
        #self.__rect =self.__surface.get_rect()
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
        self.__tamanho = novo_tamanho

    def get_velocidade(self):
        return self.__velocidade

    def set_velocidade(self, nova_velocidade):
        self.__velocidade = nova_velocidade

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