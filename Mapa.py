
import random
from Config import *
from Tela import *
class Mapa_do_jogo:
    def __init__(self):
        self.__qtd_tuplas_terreno = 0
        self.__desenha = True
        self.__terreno = None
        self.__cont = 1


    def desenha(self, tela):
        self.desenha_solo()

    def desenha_solo(self, tela):
        #print("desenhando solo")
        retangulo = pygame.Rect(500, 300, 60, 60)
        tela.draw_rect(WHITE, retangulo)
        #terreno = [(100, 100), (500, 100),(500, 500), (100, 500)]

        if self.__desenha == True:
            randon_1 = random.randint(400, 550)
            randon_2 = random.randint(400, 550)
            randon_3 = random.randint(400, 550)
            randon_4 = random.randint(400, 550)
            randon_5 = random.randint(400, 550)
            randon_6 = random.randint(400, 550)
            randon_7 = random.randint(400, 550)
            randon_8 = random.randint(400, 550)
            randon_9 = random.randint(400, 550)
            randon_10 = random.randint(400, 550)
            """ 
            self.__terreno = [(0, randon_1),

                              (240, randon_3), (360, randon_4), (480, randon_5), (600, randon_6), (720, randon_7), (840, randon_8),(950, randon_9), (1080, randon_8),(1200, randon_2),


                              (1200, 1200), (0, 600)] # nao pode modificar, limite da tela!
            self.__desenha = False"""
            #tela.draw_polygon(WHITE, self.__terreno)

            self.__terreno = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                              (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),

                              (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                              (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),


                              (1200, 1200), (0, 600))  # nao pode modificar, limite da tela!

            x = 0
            self.__qtd_tuplas_terreno = len(self.__terreno)

            porcento_h = (RESOLUCAO[1]/1000) * 200 # 20% da tela
            novo_terreno = []
            for vertice in self.__terreno:
                rand = random.randint((RESOLUCAO[1]-porcento_h), (RESOLUCAO[1]-10))
                vertice_aux = ((vertice[0] + x), (vertice[1] + rand))
                print("i :", self.__cont)
                print("x :", x)
                print(rand)
                x += RESOLUCAO[0]/(self.__qtd_tuplas_terreno-2)
                self.__cont += 1

                novo_terreno.append(vertice_aux)

            # preenche as valores das ultimas duas tuplas que nao deve ser mudado
            novo_terreno.insert ((self.__cont -1), (RESOLUCAO[0], RESOLUCAO[1]))
            novo_terreno.insert((self.__cont) , (0, RESOLUCAO[0]))
            self.__terreno = novo_terreno
            print(self.__terreno)

            self.__desenha = False
        tela.draw_polygon(WHITE, self.__terreno)

