import math
import random
from Config import *
from Tela import *
class Mapa_do_jogo:
    def __init__(self):
        self.__qtd_tuplas_terreno = 0
        self.__desenha = True
        self.__terreno = None
        self.__cont = 1
        self.__base_pouso = None
        self.__porcento_altura_terreno = None



    def desenha(self, tela):
        self.desenha_solo()

    def desenha_solo(self, tela):
        #print("desenhando solo")
        #retangulo = pygame.Rect(500, 300, 60, 60)
        #tela.draw_rect(WHITE, retangulo)
        #terreno = [(100, 100), (500, 100),(500, 500), (100, 500)]

        if self.__desenha == True:

            self.__terreno = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                              (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),

                              (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                              (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),

                              (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                              (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),







                              (1200, 1200), (0, 600))  # nao pode modificar, limite da tela!


            self.__qtd_tuplas_terreno = len(self.__terreno)


            novo_terreno = []
            x = 0
            for vertice in self.__terreno:

                # sorteia duas porcentagem de tela para que o morro do terreno alterne entre picos altos e baixos
                self.__porcento_altura_terreno = random.randint((RESOLUCAO[1] / 1000) * 200,
                                                                (RESOLUCAO[1] / 1000) * 300)  # 10% ou 20% da tela

                # faz outro sorteio que recebe como o parametro o sorteio anterior que pode ser 10 ou 20% da tela
                ramdom_alturas_diferentes = random.randint((RESOLUCAO[1] - self.__porcento_altura_terreno), (RESOLUCAO[1] - 10))

                #define a altura minima e maxima das montanhas do terrero
                #random_y = random.randint((RESOLUCAO[1] - self.__porcento_altura_terreno), (RESOLUCAO[1] - 50))

                # incrementa o valor do x que contem na tupla e em y adiciona randomicamente
                vertice_aux = ((vertice[0] + x), (vertice[1] + ramdom_alturas_diferentes))
                novo_terreno.append(vertice_aux)



                #print("qtd tuplas ",self.__qtd_tuplas_terreno)
                #print("ramdom_pouso_nave ", ramdom_pouso_nave)



                sort = random.randint(1, self.__qtd_tuplas_terreno)

                if self.__cont == sort:
                    # coleta a divisao da abstracao da malha do terreno em x
                    x_vertice_pouso = RESOLUCAO[0]/(self.__qtd_tuplas_terreno)

                    # pega o divisao e define o tamanho x e o centro do pouso. determina o vertice1 da direita.
                    x_fim_pouso = ((x_vertice_pouso + RESOLUCAO[0] / (self.__qtd_tuplas_terreno)) - TAMANHO_DA_NAVE_X)/2
                    # define o inicio do vertice2 da esquerda
                    x_inicio_pouso = x_fim_pouso/2

                    # se nao tiver no fim da lista, adiciona o pouso com  o retangulo
                    if self.__cont < len(self.__terreno):
                        novo_terreno.insert((self.__cont+1), ((vertice[0] + x + x_inicio_pouso), vertice[1] + 400))
                        novo_terreno.insert((self.__cont+1), ((vertice[0] + x + x_fim_pouso), vertice[1] + 400))
                        self.__cont+=1

                        retangulo = pygame.Rect((vertice[0] + x + x_inicio_pouso), 400, x_fim_pouso/2+3, 10)
                        self.__base_pouso = retangulo

                        #vertice_aux = (vertice[0] + x + x_inicio_pouso), (vertice[1] + 400)
                        #novo_terreno.append(vertice_aux)
                        #vertice_aux = (vertice[0] + x + x_fim_pouso), (vertice[1] + 400)
                        #novo_terreno.append(vertice_aux)

                #incrementa x e define a quantidade de pontos em x da tela
                x += RESOLUCAO[0]/(self.__qtd_tuplas_terreno)
                # captura a posicao das ultimas duas tuplas para realocar o valor que representa as medidas da resolucao
                self.__cont += 1


            print(RESOLUCAO[0]/(self.__qtd_tuplas_terreno))



            # preenche os valores das ultimas duas tuplas que nao deve ser mudado
            novo_terreno.insert((self.__cont-1), (RESOLUCAO[0], RESOLUCAO[1]))
            novo_terreno.insert((self.__cont), (0, RESOLUCAO[0]))
            self.__terreno = novo_terreno
            #print(self.__terreno)

            self.__desenha = False
        tela.draw_polygon(WHITE, self.__terreno)
        tela.draw_rect(LARANJA, self.__base_pouso)


