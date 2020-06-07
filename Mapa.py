import math
import random
from Config import *
from Tela import *
class Mapa_do_jogo:
    def __init__(self):
        self.__qtd_tuplas_terreno = 0
        self.__desenha = True
        self.__terreno = None
        self.__cor_terreno =0
        self.__novo_terreno = []

        self.__cor_terreno_borda = 0
        self.__desenha_contorno = (0,0),(0,0)
        self.__random_alturas_diferentes = 0
        self.__ramdom_pouso_nave = 0
        self.__cont = 1
        self.__base_pouso_retangulo = None
        self.__base_pouso_line = None
        self.__porcento_altura_terreno = None
        self.__existe_area_pouso = False
        self.__altura_base_pouso = None
        self.__espessura_base_pouso_line = 6
        self.__qualidade_terreno =60
        self.__sort1 = 0
        self.__sort2 = 0
        self.__sort3 = 0

        self.__copia_terreno_vertices_terreno = []
        self.__copiou = False
        self.__copia_base_pouso_line = None


    def get_copia_vertices_terreno(self):
        return self.__copia_terreno_vertices_terreno


    def set_copia_vertices_terreno(self, copia):
        self.__copia_terreno_vertices_terreno = copia

    def set_copia_base_pouso_line(self, lista):
        self.__copia_base_pouso_line = lista






    def set_qualidade_terreno(self, int):
        self.__qualidade_terreno = int

    def get_qualidade_terreno(self):
        return self.__qualidade_terreno
    def set_cor_terreno(self, cor):
        self.__cor_terreno = cor

    def get_cor_terreno(self):
        return self.__cor_terreno

    def set_cor_borda_terreno(self, cor):
        self.__cor_terreno_borda = cor

    def get_cor_terreno_borda(self):
        return self.__cor_terreno_borda

    def get_terreno(self):
        return self.__terreno

    def set_terreno(self, lista_vertices):
        self.__terreno = lista_vertices


    def get_pouso_nave_line(self):
        return self.__base_pouso_line

    def set_pouso_nave_line(self, vertice):
        self.__base_pouso_line = vertice

    def get_pouso_nave_retangulo(self):
        if self.__existe_area_pouso == False:
            return self.__base_pouso_retangulo
        else:
            print("NAO FOI SORTEADO UMA AREA DE POUSO")
            return 0

    def get_espessura_line_pouso_nave(self):
        if self.__existe_area_pouso == True:
            return self.__espessura_base_pouso_line
        else:
            print("NAO FOI SORTEADO UMA AREA DE POUSO")

    def get_altura_pouso_nave(self):
        return self.__altura_base_pouso

    def get_existe_area_pouso(self):
        return self.__existe_area_pouso

    def set_existe_area_pouso(self, existe):
        self.__existe_area_pouso = existe

    def get_redesenha_terreno(self):
        return self.__desenha

    def set_redesenha_terreno(self, boleana):
        self.__desenha = boleana


    def get_qtd_tuplas_terreno(self):
        return self.__qtd_tuplas_terreno

    def set_qtd_tuplas_terreno(self, qtd):
        self.__qtd_tuplas_terreno = qtd

    def get_desenha(self):
        return self.__desenha

    def set_desenha(self, booleana):
        self.__desenha = booleana

    def get_novo_terreno(self):
        return self.__novo_terreno

    def set_novo_terreno(self, novo_terreno):
        self.__novo_terreno = novo_terreno

    def get_desenha_contorno(self):
        return self.__desenha_contorno

    def set_desenha_contorno(self, vertices):
        self.__desenha_contorno = vertices

    def get_random_alturas_diferentes(self):
        return self.__random_alturas_diferentes

    def set_random_alturas_diferentes(self, altura):
        self.__random_alturas_diferentes = altura

    def get_random_pouso_nave(self):
        return self.__ramdom_pouso_nave

    def set_ramdom_pouso_nave(self, random):
        self.__ramdom_pouso_nave = random

    def get_cont(self):
        return self.__cont

    def set_cont(self, cont):
        self.__cont = cont

    def get_porcento_altura_terreno(self):
        return self.__porcento_altura_terreno

    def set_porcento_altura_terreno(self, porcentagem):
        self.__porcento_altura_terreno = porcentagem

    def get_altura_base_pouso(self):
        return self.__altura_base_pouso

    def set_altura_base_pouso(self, altura):
        self.__altura_base_pouso = altura

    def get_espessura_base_pouso_line(self):
        return self.__espessura_base_pouso_line

    def set_espessura_base_pouso_line(self, espessura):
        self.__espessura_base_pouso_line = espessura


    def reiniciar(self):

        self.__qtd_tuplas_terreno = 0
        self.__desenha = True
        self.__terreno = None
        self.__cor_terreno = self.get_cor_terreno()
        self.__cor_terreno_borda = 0
        self.__novo_terreno = []
        self.__desenha_contorno = (0,0),(0,0)
        self.__random_alturas_diferentes = 0
        self.__ramdom_pouso_nave = 0
        self.__cont = 1
        self.__base_pouso_retangulo = None
        self.__base_pouso_line = None
        self.__porcento_altura_terreno = None
        self.__existe_area_pouso = False
        self.__altura_base_pouso = None
        self.__espessura_base_pouso_line = 6
        self.__qualidade_terreno =60
        self.__sort1 = 0
        self.__sort2 = 0
        self.__sort3 = 0


    def salvar(self):

        self.__s_qtd_tuplas_terreno = self.get_qtd_tuplas_terreno()
        self.__s_desenha = self.get_desenha()
        self.__s_terreno = self.get_terreno()
        self.__s_cor = self.get_cor_terreno()
        self.__s_novo_terreno = self.get_novo_terreno()
        self.__s_cor_borda_terreno = self.get_cor_terreno_borda()
        self.__s_desenha_contorno = self.get_desenha_contorno()
        self.__s_random_alturas_diferentes = self.get_random_alturas_diferentes()
        self.__s_random_pouso_nave = self.get_random_pouso_nave()
        self.__s_cont = self.get_cont()
        self.__s_base_pouso_line = self.get_pouso_nave_line()
        self.__s_porcento_altura_terreno = self.get_porcento_altura_terreno()
        self.__s_existe_area_pouso = self.get_existe_area_pouso()
        self.__s_altura_base_pouso = self.get_altura_base_pouso()
        self.__s_espessura_base_pouso_line = self.get_espessura_base_pouso_line()
        self.__s_qualidade_terreno = self.get_qualidade_terreno()
        self.__s_sort1 = random.randint(0, 255)
        self.__sort2 = random.randint(0, 255)








    def carregar_save(self):


        self.set_qtd_tuplas_terreno(self.__s_qtd_tuplas_terreno)
        self.set_desenha(self.__s_desenha)

        self.set_terreno(self.__s_terreno)
        self.set_cont(self.__s_cor)
        self.set_novo_terreno(self.__s_novo_terreno)
        self.set_cor_borda_terreno(self.__s_cor_borda_terreno)
        self.set_desenha_contorno(self.__s_desenha_contorno)
        self.set_random_alturas_diferentes(self.__s_random_alturas_diferentes)
        self.set_ramdom_pouso_nave(self.__s_random_pouso_nave)
        self.set_cont(self.__s_cont)
        self.set_pouso_nave_line(self.__s_base_pouso_line)
        self.set_porcento_altura_terreno(self.__s_porcento_altura_terreno)
        self.set_existe_area_pouso(self.__s_existe_area_pouso)
        self.set_altura_base_pouso(self.__s_altura_base_pouso)
        self.set_espessura_base_pouso_line(self.__s_espessura_base_pouso_line)
        self.set_qualidade_terreno(self.__s_qualidade_terreno)


        self.__sort1 = random.randint(0, 255)
        self.__sort2 = random.randint(0, 255)








    def copia(self, tela):

        self.set_terreno(self.__copia_terreno_vertices_terreno)
        tela.draw_polygon(self.get_cor_terreno(), self.__terreno)
        tela.draw_lines((self.get_cor_terreno_borda()), self.__copia_terreno_vertices_terreno, 4)

        self.__sort1 = random.randint(0, 255)
        self.__sort2 = random.randint(0, 255)

        if (self.__existe_area_pouso):
            tela.draw_line((self.__sort1, self.__sort2, 0), (self.__copia_base_pouso_line[0], self.__copia_base_pouso_line[1]),
                           (self.__copia_base_pouso_line[2], self.__copia_base_pouso_line[3]),
                           self.get_espessura_line_pouso_nave())




    def desenha_terreno(self, tela, nave):

        if self.get_redesenha_terreno() == True:


            # a quantidade de tupla (0, 0) define a qualidade e quantidade de pontos ao logo do horizonte do terreno
            self.__terreno =[(0,0)]* self.get_qualidade_terreno()

            #self.__terreno =  [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                              #(0, 0), (0, 0), (0, 0), (0, 0), (0, 0),

                              #(0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                              #(0, 0), (0, 0), (0, 0), (0, 0), (0, 0),

                              #(0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                              #(0, 0), (0, 0), (0, 0),(0, 0), (0, 0)]

                            #(0, 0), (0, 0), (0, 0), (1200, 600), (0, 600)]  # nao pode modificar, limite da tela!

            # começa com -2 pra esconder a line do terreno na tela do lado esquerdo
            x = -2

            # preenche os valores reais das tuplas com as posicoes dos vertices
            for vertice in self.__terreno:

                # captura a quantidade e define o tamanho da lista que vou trabalhar, esta for pra sempre ser atualizada.
                self.__qtd_tuplas_terreno = len(self.__terreno)

                # sorteia duas porcentagem de tela para que o morro do terreno alterne entre picos altos e baixos
                self.__porcento_altura_terreno = random.randint((tela.get_resolucao()[1] / 1000) * 200, #200
                                                                (tela.get_resolucao()[1] / 1000) * 300) #300    # 10% ou 20% da tela

                # faz outro sorteio que recebe como o parametro o sorteio anterior que pode ser 10 ou 20% da tela
                self.__random_alturas_diferentes = random.randint((tela.get_resolucao()[1] - self.__porcento_altura_terreno), (tela.get_resolucao()[1] - 50))

                # incrementa o valor do x que contem na tupla e em y adiciona randomicamente
                vertice_aux = ((vertice[0] + x), (vertice[1] + self.__random_alturas_diferentes))
                self.__novo_terreno.append(vertice_aux)

                # sorteia numeros entre 1 e a quantidade de tuplas-1 da lista de vertices do terreno
                self.__ramdom_pouso_nave = random.randint(1, self.__qtd_tuplas_terreno-1)
                teste = random.randint(1, self.__qtd_tuplas_terreno-1)

                #define o local de pouso
                if self.__ramdom_pouso_nave == self.__cont or teste == self.__cont:

                    self.set_existe_area_pouso(True)
                    # coleta a divisao da abstracao da malha do terreno em x
                    x_largura_pouso = tela.get_resolucao()[0] / (self.__qtd_tuplas_terreno)
                    if nave.get_largura_x()< x_largura_pouso:
                        x_largura_pouso = nave.get_largura_x()


                    # faz o rebaixo do pouso da nave no terreno
                    self.__novo_terreno.append((vertice[0] + x, vertice[1] + self.__random_alturas_diferentes))
                    self.__novo_terreno.append((vertice[0] + x + x_largura_pouso, vertice[1] + self.__random_alturas_diferentes ))

                    # desenha o feedback da area de pouso com uma line
                    self.__base_pouso_line =   [(vertice[0] + x),
                                                (vertice[1] + self.__random_alturas_diferentes),

                                                (vertice[0] + x + x_largura_pouso),
                                                (vertice[1] + self.__random_alturas_diferentes)]

                    if self.__copiou == False:
                        self.set_copia_base_pouso_line(self.__base_pouso_line)

                    # desenha o feedback da area de pouso com um retangulo
                    self.__base_pouso = pygame.Rect(((vertice[0] + x)), self.__random_alturas_diferentes, ((x_largura_pouso/2)), 10)

                    self.__cont+=2

                    # captura a altura do pouso pra usar na colisao entre nave e terreno
                    self.__altura_base_pouso = self.__random_alturas_diferentes


                    #quando é sorteado um local de pouso(rebaixo do terreno ou feedback) tem que atualizar o tamanho do for
                    # para que continue desenhando os vertices ate o fim da tela
                    self.__qtd_tuplas_terreno+=2;
                    x += tela.get_resolucao()[0] / (self.__qtd_tuplas_terreno)

                #incrementa x e define a quantidade de pontos em x da tela
                x += tela.get_resolucao()[0]/(self.__qtd_tuplas_terreno)

                # captura a posicao das ultimas duas tuplas para realocar o valor que representa as medidas da resolucao
                self.__cont += 1

            # repreenche os valores das ultimas duas tuplas que nao deve ser mudado, pois representam as bordas da tela
            self.__novo_terreno.insert((self.__cont), (tela.get_resolucao()[0]+5, tela.get_resolucao()[1]))
            self.__novo_terreno.insert((self.__cont), (-5, tela.get_resolucao()[1]))
            self.__cont += 2
            self.__qtd_tuplas_terreno+=2
            self.__terreno = self.__novo_terreno

            if self.__copiou == False:
                self.set_copia_vertices_terreno(self.__terreno)

            # permite randomizar e desenhar o terreno apenas uma vez somente no primeiro frame.
            self.set_redesenha_terreno(False)
            self.__copiou = True


        self.__debug()

        tela.draw_polygon(self.get_cor_terreno(), self.__terreno)

        self.__sort1 = random.randint(0, 255)
        self.__sort2 = random.randint(0, 255)
        #self.__sort3 = random.randint(0, 255)
        #tela.draw_lines((self.__sort1 ,0,self.__sort2 ), self.__novo_terreno, 4)

        tela.draw_lines(( self.get_cor_terreno_borda()), self.__terreno, 4)


        # só desenha a area de pouso se ela existir, ou seja se caiu no if #define o local de pouso.
        if(self.__existe_area_pouso):
            tela.draw_line((self.__sort1,self.__sort2,0), (self.__base_pouso_line[0], self.__base_pouso_line[1]),
                                    (self.__base_pouso_line[2], self.__base_pouso_line[3]), self.get_espessura_line_pouso_nave())

    def get_line_terreno(self):
        return self.__novo_terreno

    def __debug(self):
        #print("qtd tuplas ",self.__qtd_tuplas_terreno)
        #print("ramdom_pouso_nave ", self.__ramdom_pouso_nave)
        #print("self.__cont ", self.__cont)
        #print("distacia entre vertices ", RESOLUCAO[0] / (self.__qtd_tuplas_terreno))
        #print("self.__terreno ", len(self.__terreno))
        #print("self.__novo_terreno ", len(self.__novo_terreno))
        #print(self.__novo_terreno)
        pass


