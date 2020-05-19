import math
import random
from Config import *
from Tela import *
class Mapa_do_jogo:
    def __init__(self):
        self.__qtd_tuplas_terreno = 0
        self.__desenha = True
        self.__terreno = None
        self.__novo_terreno = []
        self.__desenha_contorno = (0,0),(0,0)
        self.__random_alturas_diferentes = 0
        self.__ramdom_pouso_nave = 0
        self.__cont = 1
        self.__base_pouso = None
        self.__porcento_altura_terreno = None
        self.__existe_area_pouso = False




    def desenha(self, tela):
        self.desenha_solo()

    def desenha_solo(self, tela):
        #print("desenhando solo")
        #retangulo = pygame.Rect(500, 300, 60, 60)
        #tela.draw_rect(WHITE, retangulo)
        #terreno = [(100, 100), (500, 100),(500, 500), (100, 500)]

        if self.__desenha == True:

            # a quantidade de tupla (0, 0) define a qualidade e quantidade de pontos do terreno
            self.__terreno = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                              (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),

                              (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                              (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),






                              (0, 0), (0, 0), (0, 0),(1200, 600), (0, 600)]  # nao pode modificar, limite da tela!

            # captura a quantidade e define o tamanho da lista que vou trabalhar
            self.__qtd_tuplas_terreno = len(self.__terreno)


            #novo_terreno = []
            x = 0

            # preenche os valores reais das tuplas com as posicoes dos vertices
            for vertice in self.__terreno:

                # sorteia duas porcentagem de tela para que o morro do terreno alterne entre picos altos e baixos
                self.__porcento_altura_terreno = random.randint((RESOLUCAO[1] / 1000) * 200,
                                                                (RESOLUCAO[1] / 1000) * 300)  # 10% ou 20% da tela

                # faz outro sorteio que recebe como o parametro o sorteio anterior que pode ser 10 ou 20% da tela
                self.__random_alturas_diferentes = random.randint((RESOLUCAO[1] - self.__porcento_altura_terreno), (RESOLUCAO[1] - 10))

                #define a altura minima e maxima das montanhas do terrero
                #random_y = random.randint((RESOLUCAO[1] - self.__porcento_altura_terreno), (RESOLUCAO[1] - 50))

                # incrementa o valor do x que contem na tupla e em y adiciona randomicamente
                vertice_aux = ((vertice[0] + x), (vertice[1] + self.__random_alturas_diferentes))
                self.__novo_terreno.append(vertice_aux)
                #tela.draw_line(LARANJA,  (798,0), (798,598),     2)

                # sorteia numeros entre 1 e a quantidade de tuplas-1 da lista de vertices do terreno
                self.__ramdom_pouso_nave = random.randint(1, self.__qtd_tuplas_terreno)
                #self.__ramdom_pouso_nave = 30



                #define o local de pouso

                if self.__ramdom_pouso_nave == self.__cont:

                    self.__existe_area_pouso = True
                    # coleta a divisao da abstracao da malha do terreno em x
                    x_vertice_pouso = RESOLUCAO[0]/(self.__qtd_tuplas_terreno)

                    # pega o divisao e define o tamanho x e o centro do pouso. determina o vertice1 da direita.
                    x_fim_pouso = ((x_vertice_pouso + RESOLUCAO[0] / (self.__qtd_tuplas_terreno)) - TAMANHO_DA_NAVE_X)/2
                    # define o inicio do vertice2 da esquerda
                    x_inicio_pouso = x_fim_pouso/2

                    # faz o rebaixo do pouso da nave no terreno
                    self.__novo_terreno.insert((self.__cont), ((vertice[0] + x + x_inicio_pouso), vertice[1] + self.__random_alturas_diferentes))
                    self.__novo_terreno.insert((self.__cont), ((vertice[0] + x),                  vertice[1] + self.__random_alturas_diferentes))
                    self.__cont+=2
                    #self.__terreno.append((0, 0))
                    #self.__terreno.append((0, 0))

                    # desenha o feedback da area de pouso
                    self.__base_pouso = pygame.Rect(((vertice[0] + x)), self.__random_alturas_diferentes, ((x_fim_pouso/2)), 10)

                    #quando é sorteado um local de pouso(rebaixo do terreno ou feedback) tem que atualizar o tamanho do for
                    # para que continue desenhando os vertices ate o fim da tela
                    self.__qtd_tuplas_terreno+=1;
                    x += RESOLUCAO[0] / (self.__qtd_tuplas_terreno)

                    #vertice_aux = (vertice[0] + x + x_inicio_pouso), (vertice[1] + 400)
                    #novo_terreno.append(vertice_aux)

                #incrementa x e define a quantidade de pontos em x da tela
                x += RESOLUCAO[0]/(self.__qtd_tuplas_terreno)

                # captura a posicao das ultimas duas tuplas para realocar o valor que representa as medidas da resolucao
                self.__cont += 1



            # repreenche os valores das ultimas duas tuplas que nao deve ser mudado
            self.__novo_terreno.insert((self.__cont), (1200, RESOLUCAO[1]))
            self.__novo_terreno.insert((self.__cont), (0, RESOLUCAO[1]))
            self.__terreno = self.__novo_terreno


            #permite desenhar o terreno apenas uma vez no primeiro frame.
            self.__desenha = False
        self.debug()

        tela.draw_polygon(WHITE, self.__terreno)
        #tela.draw_line(LARANJA, (798, 0), (798, 598), 2)

        lista = [(325, 200), (355, 200), (355, 250), (325, 250)]
        #tela.draw_lines(LARANJA, lista)
        tela.draw_lines(LARANJA, self.__novo_terreno, 2)

        # só desenha a area de pouso se ela existir, ou seja se caiu no if #define o local de pouso.
        if(self.__existe_area_pouso):
            tela.draw_rect(GREEN, self.__base_pouso)


    def debug(self):
        print("qtd tuplas ",self.__qtd_tuplas_terreno)
        print("ramdom_pouso_nave ", self.__ramdom_pouso_nave)
        print("self.__cont ", self.__cont)
        print("distacia entre vertices ", RESOLUCAO[0] / (self.__qtd_tuplas_terreno))
        print("terreno ", len(self.__terreno))
