import pygame
from Config import *
class Nova_tela:
    def __init__(self, titulo, resolucao):
        self.__tela = pygame.display.set_mode(resolucao)
        self.__titulo = pygame.display.set_caption(titulo)
        self.__titulo_da_tela = titulo
        self.__clock = pygame.time.Clock()
        self.__fps = FPS

    def get_resolucao_tela(self):
        return self.__tela

    def set_resolucao_tela(self, nova_resolucao):
        self.__tela = pygame.display.set_mode(nova_resolucao)

    def get_titulo_tela(self):
        return self.__titulo_da_tela

    def set_titulo_tela(self, novo_titulo):
        self.__titulo_da_tela = novo_titulo

    def get_fps(self):
        return self.__fps

    def blit(self, surface_obj, posicao_obj):
        self.__tela.blit(surface_obj, posicao_obj)

    def fill(self, cor):
        self.__tela.fill(cor)

    def flip(self):
        pygame.display.flip()

    def draw_polygon(self, cor, lista_vertice):
        pygame.draw.polygon(self.__tela, cor, lista_vertice)

    def draw_rect(self, cor, retangulo):
        pygame.draw.rect(self.__tela, cor, retangulo)