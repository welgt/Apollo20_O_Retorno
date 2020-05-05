
import random
from Config import *
from Tela import *
class Mapa_do_jogo:
    def __init__(self):
        self.__desenha = True
        self.__terreno = None
        pass


    def desenha(self, tela):
        self.desenha_solo()

    def desenha_solo(self, tela):
        #print("desenhando solo")
        # poligono_propulsor = pygame.draw.polygon(gamePlay.tela, WHITE, [(300,600), (295,618), (824,407), (800,400)],0)



        retangulo = pygame.Rect(500, 300, 60, 60)
        tela.draw_rect(WHITE, retangulo)


        #terreno = [(100, 100), (500, 100),(500, 500), (100, 500)]


        if self.__desenha == True:
            randon_1 = random.randint(400, 550)
            randon_2 = random.randint(400, 550)
            self.__terreno = [(0, randon_1), (1200, randon_2),(1200, 1200), (0, 600)]
            self.__desenha = False

        tela.draw_polygon(WHITE, self.__terreno)
