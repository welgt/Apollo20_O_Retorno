import pygame
from Config import *
class Nova_tela:
    def __init__(self, titulo, resolucao):
        self.__tela = pygame.display.set_mode(resolucao)
        self.__titulo = pygame.display.set_caption(titulo)
        self.__titulo_da_tela = titulo
        self.__clock = pygame.time.Clock()
        self.__fps = 0

        self.__milisegundos = 0
        self.__segundos = 0
        self.__minuto = 0
        self.__hora = 0

    def get_surface_tela(self):
        return self.__tela

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

    def set_fps(self, fps):
        self.__fps = fps
        clock = pygame.time.Clock()
        clock.tick(fps)

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

    def draw_line(self, cor, vertice_inicial, vertice_final, espessura):
        #pygame.draw.line(self.__tela, cor, lista_vertices, espessura_linha)
        pygame.draw.line(self.__tela, cor, vertice_inicial, vertice_final, espessura)

    def draw_lines(self, cor,lista, espessura):
        pygame.draw.lines(self.__tela, cor, True, lista, espessura)

    def cronometro(self):
        # RELOGIO
        if self.__milisegundos < self.get_fps():
            self.__milisegundos += 1
            #print("milisegundos  : ", self.__milisegundos)
        else:
            self.__segundos += 1
            #print("segundos :------------", self.__segundos)
            self.__milisegundos  = 0

        if self.__segundos == 60:
            self.__segundos = 0
            self.__minuto += 1

            if self.__minuto > 60:
                self.__minuto = 0
                self.__hora+=1

        #print(self.__hora, ":", self.__minuto, ".", self.__segundos)
        #return self.__hora, self.__minuto, self.__segundos

    def get_cronometro(self):
        return self.__hora, self.__minuto, self.__segundos