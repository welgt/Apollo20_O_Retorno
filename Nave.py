import random

import pygame
import math
from Config import *

class Nova_nave:
    def __init__(self, surface, posicao_x, posicao_y):
        self.__surface = pygame.image.load(surface)
        self.__tamanho_x = self.__surface.get_rect()[2]
        self.__tamanho_y = self.__surface.get_rect()[3]
        self.__posicao_x = posicao_x
        self.__posicao_y = posicao_y
        #self.__centro_surface = self.__posicao_x + (self.__tamanho_x / 2), self.get_posicao_y + self.__tamanho_y / 2
        self.__velocidade_x = 0
        self.__velocidade_y = 0
        self.__potencia_propulsor = 0
        self.__friccao = 0
        self.__angulo_rotacao = 0
        self.__velocidade_rotacao = 0
        self.__rect =self.__surface.get_rect()
        self.__propulsor = False
        self.__colidiu_tela = False
        self.__colidiu_pouso = False
        self.__colidiu_terreno = False
        self.__rotacionou_dir = False
        self.__rotacionou_esq = False
        self.__nova_lista_colisores_terreno = []

    def get_lista_colisores_terreno(self):
        return self.__nova_lista_colisores_terreno

    def get_surface(self):
        return self.__surface

    def get_posicao_x(self):
        return self.__posicao_x

    def set_posicao_x(self, posicao_x):
        self.__posicao_x = posicao_x

    def get_posicao_y(self):
        return self.__posicao_y

    def set_posicao_y(self, posicao_y):
        self.__posicao_y = posicao_y

    def get_posicao(self):
        return self.__posicao_x, self.__posicao_y

    def set_posicao(self, nova_posicao_x, nova_posicao_y):
        self.__posicao_x = nova_posicao_x
        self.__posicao_y =  nova_posicao_y

    def get_posicao(self):
        return self.__posicao_x, self.__posicao_y


    def set_velocidade_x(self, velocidade):
        self.__velocidade_x = velocidade

    def get_velocidade_x(self):
        return self.__velocidade_x

    def set_velocidade_y(self, velocidade):
        self.__velocidade_y = velocidade

    def get_velocidade_y(self):
        return self.__velocidade_y

    def get_potencia_propulsor(self):
         return self.__potencia_propulsor

    def set_potencia_propulsor(self, potencia_propulsor):
        self.__potencia_propulsor = potencia_propulsor

    def get_tamanho_x(self):
        return self.__tamanho_x

    def get_tamanho_y(self):
        return self.__tamanho_y

    def set_tamanho(self, novo_tamanho_x, novo_tamanho_y):
        self.__surface = pygame.transform.scale(self.__surface, (novo_tamanho_x, novo_tamanho_y))
        novo_centro = novo_tamanho_x/2, novo_tamanho_y/2
        self.set_centro(novo_centro)
        self.__tamanho_x = novo_tamanho_x
        self.__tamanho_y = novo_tamanho_y


    def get_centro_surface(self):
        return self.__centro_surface

    def set_centro(self, novo_centro):
        self.__centro_surface = novo_centro

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

    def get_colidiu_area_pouso(self):
        return self.__colidiu_pouso

    def set_colidiu_area_pouso(self, booleana):
        self.__colidiu_pouso = booleana

    def get_colidiu_terreno(self):
        return self.__colidiu_terreno

    def set_colidiu_terreno(self, booleana):
        self.__colidiu_terreno = booleana

    def get_rotacionou_dir(self):
        return self.__rotacionou_dir

    def set_rotacionou_dir(self, booleana):
        self.__rotacionou_dir = booleana

    def get_rotacionou_esq(self):
        return self.__rotacionou_esq

    def set_rotacionou_esq(self, booleana):
        self.__rotacionou_esq = booleana


    def rotacaoCentralizada(self):

        surface = pygame.transform.rotate(self.get_surface(), self.get_angulo_rotacao())
        nova_posicao = surface.get_rect(center=self.get_centro_surface())
        nova_posicao[0] += self.get_posicao()[0]
        nova_posicao[1] += self.get_posicao()[1]

        return surface ,nova_posicao


    def criaPoligono_Propulsor(self, largura_poligono, posicao_horizontal, ponto_acelerador_poligono):

        ponto_direito = largura_poligono + self.__posicao_x + self.__tamanho_x / 2 + posicao_horizontal
        ponto_esquerdo = -largura_poligono + self.__posicao_x + self.__tamanho_x / 2 + posicao_horizontal
        ponto_acelerador_poligono += self.__posicao_y + self.__tamanho_y
        altura_base = self.__tamanho_y

        vertices_propulsor = ((ponto_direito, altura_base + self.__posicao_y),  # (0,3),
                              (self.__posicao_x + self.__tamanho_x / 2 + posicao_horizontal, ponto_acelerador_poligono),  # (3,-3)
                              (ponto_esquerdo, altura_base + self.__posicao_y))  # (-3,-3)

        return self.__rotacionaPoligono_propulsor(vertices_propulsor)


    def __rotacionaPoligono_propulsor(self, vertices_propulsor):

        origem_nave = self.__posicao_x + self.__tamanho_x / 2, self.__posicao_y + self.__tamanho_y / 2
        angulo_rotacao = math.radians(-self.get_angulo_rotacao())

        poligono_rotacionado = []

        for vertice in vertices_propulsor:
            vertice_aux = vertice[0] - origem_nave[0], vertice[1] - origem_nave[1]
            vertice_aux = (vertice_aux[0] * math.cos(angulo_rotacao) - vertice_aux[1] * math.sin(angulo_rotacao),
                           vertice_aux[0] * math.sin(angulo_rotacao) + vertice_aux[1] * math.cos(angulo_rotacao))
            vertice_aux = vertice_aux[0] + origem_nave[0], vertice_aux[1] + origem_nave[1]
            poligono_rotacionado.append(vertice_aux)

        return poligono_rotacionado


    def verifica_colisao_tela(self):

        # se for diferente disso é porque esta fora da tela
        if self.get_posicao_x()>= 0 and self.__posicao_x <= RESOLUCAO[0] - self.get_tamanho_x()\
            and self.get_posicao_y()>= 0 and self.__posicao_y <= RESOLUCAO[1] - self.get_tamanho_y():
            #print("nao colidiu")
            self.set_colidiu_tela(False)
        else:
            #print("colidiu")
            self.set_colidiu_tela(True)
            # pega a posicao do momento da colisao e deixa a nave travada nela
            self.set_posicao(self.get_posicao_x(),self.get_posicao_y())
            #self.set_velocidade_x(0)
            #self.set_velocidade_y(0)




    def verifica_colisao_area_pouso(self, mapa):


        if mapa.get_existe_area_pouso() == True:

            #pega o vertice inicial horizontal da area de pouso do terreno
            inicio_area_pouso_horizontal = mapa.get_pouso_nave_line()[0]

            # pega o vertice final horizontal da area de pouso do terreno
            fim_area_pouso_horizontal = mapa.get_pouso_nave_line()[2]

            # verifica a colisao entre a nave e a area de pouso
            if self.get_posicao_x() >= inicio_area_pouso_horizontal \
                    and self.get_posicao_x() + self.get_tamanho_x() <= fim_area_pouso_horizontal \
                    and self.get_posicao_y() + self.get_tamanho_y() >= mapa.get_altura_pouso_nave() - mapa.get_espessura_line_pouso_nave()/2:
                self.set_colidiu_area_pouso(True)
                print("COLIDIU COM A AREA DE POUSO")
                #se colidiu zere o propulsor
                self.set_potencia_propulsor(0)
                self.set_rotacionou_dir(False)
                self.set_rotacionou_esq(False)
                self.set_velocidade_x(0)
                self.set_velocidade_y(0)
                #self.set_angulo_rotacao(0)
                self.set_posicao(self.get_posicao_x(), (self.get_posicao_y()))
            else:
                self.set_colidiu_area_pouso(False)

        #else:
            #print("NAO FOI POSSIVEL SORTEAR UMA AREA DE POUSO, REDESENHANDO TERRENO")
            # se caso nao tiver sorteado a area de pouso manda desenhar o terreno denovo
            #mapa.desenha_terreno(tela)



    # ACELERACAO do propulsor
    def aceleracao_propulsor(self, tempo):

        if self.get_propulsor_ativo() == True and self.get_colidiu_tela() == False and self.get_colidiu_area_pouso() == False:
            self.__velocidade_y-= (VELOCIDADE_ACELERACAO_LUA/FPS) * tempo  * self.get_friccao()

            # permite aumentar o tamanho do propulsor ate 1
            if self.__potencia_propulsor < 1:
                self.__potencia_propulsor += (VELOCIDADE_ACELERACAO_LUA/FPS)* tempo  * self.get_friccao()

            if self.get_velocidade_y() <= VELOCIDADE_ACELERACAO_LUA:
                tempo = 0

                # define nova direcao caso a nave esteja inclinada pra direita e propulsor ativo
                if self.get_angulo_rotacao()<=1 and self.get_propulsor_ativo():
                    self.__velocidade_x += self.get_angulo_rotacao()*-1 /180

                # define nova direcao caso a nave esteja inclinada pra esquerda e propulsor ativo
                if self.__angulo_rotacao >= 1 and self.get_propulsor_ativo():
                    self.__velocidade_x -= self.get_angulo_rotacao()/180



    def gravidade(self, tempo):

        # GRAVIDADE
        # se nao tiver acelerando e nao tiver colidido com a tela ou com a area de pouso executa a gravidade
        if self.get_propulsor_ativo() == False and self.get_colidiu_tela() == False \
            and self.get_colidiu_area_pouso() == False:

            self.__velocidade_y += (VELOCIDADE_ACELERACAO_LUA/FPS) * tempo * self.get_friccao()
            # diminiu o tamanho do propulsor
            self.__potencia_propulsor -= (VELOCIDADE_ACELERACAO_LUA/FPS) * tempo * self.get_friccao()

            # caso ele for menor que zero, fique em zero.
            if self.get_potencia_propulsor() < 0:
                self.set_potencia_propulsor(0)
            if self.get_velocidade_y() >= VELOCIDADE_ACELERACAO_LUA:
                tempo = 0





    # for vertice in self.__terreno:
    def verifica_colisao_terreno(self, mapa, tela):

        self.set_colidiu_terreno(False)

        lista_vertice = mapa.get_terreno()
        lista_aux = []
        #nova_lista_colisores = []

        i = 0
        j = 1
        qtd_novos_numeros = 8
        # junta os valores das tuplas do terreno e as torna uma lista de valores ao inves de lista de tupla
        for vertice in lista_vertice:

            lista_aux.append(vertice[0])
            lista_aux.append(vertice[1])
            self.__nova_lista_colisores_terreno.append((vertice[0], vertice[1]))



            ponto_principal_x1 = lista_vertice[i][0]
            ponto_principal_y1 = lista_vertice[i][1]
            ponto_principal_x2 = lista_vertice[j][0]
            ponto_principal_y2 = lista_vertice[j][1]




            #distancia_entre_ponto_principal_x1_y1_x2_y2 = math.sqrt((abs(abs(ponto_principal_x2 - ponto_principal_x1)**2) + abs(ponto_principal_y1 - ponto_principal_y2)**2))
            #print(print("distancia_entre_ponto_principal_x1_y1_x2_y2 :",distancia_entre_ponto_principal_x1_y1_x2_y2))
            #distancia_entre_ponto_principal_x1_y1_x2_y2/=2

            incremento_x = abs(ponto_principal_x1-ponto_principal_x2)/  (len(lista_vertice)/6)
            incremento_y = abs(ponto_principal_y1-ponto_principal_y2)/ (len(lista_vertice)/6)




            #SO FALTA ACERTAR O CALCULO DESSES NOVOS PONTOS
            if ponto_principal_y1>ponto_principal_y2:
                pontos_intermediarios_entre_pontos_principais_p1 = (int(ponto_principal_x1 + (incremento_x * 1)), int(ponto_principal_y1 - (incremento_y * 1)))
                pontos_intermediarios_entre_pontos_principais_p2 = (int(ponto_principal_x1 + (incremento_x * 2)), int(ponto_principal_y1 - (incremento_y * 2)))
                pontos_intermediarios_entre_pontos_principais_p3 = (int(ponto_principal_x1 + (incremento_x * 3)), int(ponto_principal_y1 - (incremento_y * 3)))
                pontos_intermediarios_entre_pontos_principais_p4 = (int(ponto_principal_x1 + (incremento_x * 4)), int(ponto_principal_y1 - (incremento_y * 4)))
                pontos_intermediarios_entre_pontos_principais_p5 = (int(ponto_principal_x1 + (incremento_x * 5)), int(ponto_principal_y1 - (incremento_y * 5)))

            else:
                pontos_intermediarios_entre_pontos_principais_p1 = (int(ponto_principal_x1 + (incremento_x * 1)), int(ponto_principal_y1 + (incremento_y * 1)))
                pontos_intermediarios_entre_pontos_principais_p2 = (int(ponto_principal_x1 + (incremento_x * 2)), int(ponto_principal_y1 + (incremento_y * 2)))
                pontos_intermediarios_entre_pontos_principais_p3 = (int(ponto_principal_x1 + (incremento_x * 3)), int(ponto_principal_y1 + (incremento_y * 3)))
                pontos_intermediarios_entre_pontos_principais_p4 = (int(ponto_principal_x1 + (incremento_x * 4)), int(ponto_principal_y1 + (incremento_y * 4)))
                pontos_intermediarios_entre_pontos_principais_p5 = (int(ponto_principal_x1 + (incremento_x * 5)), int(ponto_principal_y1 + (incremento_y * 5)))


            lista_aux.append(pontos_intermediarios_entre_pontos_principais_p1[0])
            lista_aux.append(pontos_intermediarios_entre_pontos_principais_p1[1])
            #self.__nova_lista_colisores_terreno.append(("x","y"))
            self.__nova_lista_colisores_terreno.append(pontos_intermediarios_entre_pontos_principais_p1)

            #lista_aux.append(pontos_intermediarios_entre_pontos_principais_p2[0])
            #lista_aux.append(pontos_intermediarios_entre_pontos_principais_p2[1])
            #self.__nova_lista_colisores_terreno.append(("x", "y"))
            self.__nova_lista_colisores_terreno.append(pontos_intermediarios_entre_pontos_principais_p2)

            #lista_aux.append(pontos_intermediarios_entre_pontos_principais_p3[0])
            #lista_aux.append(pontos_intermediarios_entre_pontos_principais_p3[1])
            #self.__nova_lista_colisores_terreno.append(("x", "y"))
            self.__nova_lista_colisores_terreno.append(pontos_intermediarios_entre_pontos_principais_p3)

            #lista_aux.append(pontos_intermediarios_entre_pontos_principais_p4[0])
            #lista_aux.append(pontos_intermediarios_entre_pontos_principais_p4[1])
            #nova_lista_colisores.append(("x", "y"))
            self.__nova_lista_colisores_terreno.append(pontos_intermediarios_entre_pontos_principais_p4)

            #lista_aux.append(pontos_intermediarios_entre_pontos_principais_p4[0])
            #lista_aux.append(pontos_intermediarios_entre_pontos_principais_p4[1])
            #self.__nova_lista_colisores_terreno.append(("x", "y"))
            self.__nova_lista_colisores_terreno.append(pontos_intermediarios_entre_pontos_principais_p5)

            # pegando o centro de baixo da nave
            p_nave = self.get_posicao_x()+ self.get_tamanho_x()/2,   self.get_posicao_y() + self.get_tamanho_y()
            #print(p_nave)

            # so falta replicar com os outros pontos(fazer uma funcao)
            distancia_entre_ponto_colisor_nave_ponto_principal = \
                math.sqrt((abs(abs(ponto_principal_x2 - p_nave[0]) ** 2) + abs(p_nave[1] - ponto_principal_y2) ** 2))

            distancia_entre_ponto_colisor_nave_ponto_intermediario_01 = \
                math.sqrt((abs(abs(pontos_intermediarios_entre_pontos_principais_p1[0] - p_nave[0]) ** 2)
                             + abs(p_nave[1] - pontos_intermediarios_entre_pontos_principais_p1[1]) ** 2))

            distancia_entre_ponto_colisor_nave_ponto_intermediario_02 = \
                math.sqrt((abs(abs(pontos_intermediarios_entre_pontos_principais_p2[0] - p_nave[0]) ** 2)
                           + abs(p_nave[1] - pontos_intermediarios_entre_pontos_principais_p2[1]) ** 2))

            distancia_entre_ponto_colisor_nave_ponto_intermediario_03 = \
                math.sqrt((abs(abs(pontos_intermediarios_entre_pontos_principais_p3[0] - p_nave[0]) ** 2)
                           + abs(p_nave[1] - pontos_intermediarios_entre_pontos_principais_p3[1]) ** 2))

            distancia_entre_ponto_colisor_nave_ponto_intermediario_04 = \
                math.sqrt((abs(abs(pontos_intermediarios_entre_pontos_principais_p4[0] - p_nave[0]) ** 2)
                           + abs(p_nave[1] - pontos_intermediarios_entre_pontos_principais_p4[1]) ** 2))

            distancia_entre_ponto_colisor_nave_ponto_intermediario_05 = \
                math.sqrt((abs(abs(pontos_intermediarios_entre_pontos_principais_p5[0] - p_nave[0]) ** 2)
                           + abs(p_nave[1] - pontos_intermediarios_entre_pontos_principais_p5[1]) ** 2))

            if distancia_entre_ponto_colisor_nave_ponto_principal < 10:
                self.set_colidiu_terreno(True)
                #print("COLIDIU PONTO PRINCIPAL")


            if distancia_entre_ponto_colisor_nave_ponto_intermediario_01 < 5 \
                    or distancia_entre_ponto_colisor_nave_ponto_intermediario_02 < 5 \
                    or distancia_entre_ponto_colisor_nave_ponto_intermediario_03 < 5 \
                    or distancia_entre_ponto_colisor_nave_ponto_intermediario_04 < 5 \
                    or distancia_entre_ponto_colisor_nave_ponto_intermediario_05 < 5 :
                #print("COLIDIU PONTO INTERMEDIARIO")
                self.set_colidiu_terreno(True)





            #print("ponto_principal_x1:",ponto_principal_x1)
            #print("ponto_principal_y1:",ponto_principal_y1)

            #print("ponto_principal_x2:",ponto_principal_x2)
            #print("ponto_principal_y2:",ponto_principal_y2)
            #print("dividido por 4 :",distancia_entre_ponto_principal_x1_y1_x2_y2)


            if j < len(lista_vertice)-1:#6
                i+=1
                j+=1

        #tela.draw_lines((RED), self.get_lista_colisores_terreno(), 2)





















"""    # for vertice in self.__terreno:
    def verifica_colisao_terreno(self, mapa, tela):

        lista_vertice = mapa.get_terreno()
        lista_aux = []

        i = 0
        j = 1
        # junta os valores das tuplas do terreno e as torna uma lista de valores ao inves de lista de tupla
        for vertice in lista_vertice:

            lista_aux.append(vertice[0])
            lista_aux.append(vertice[1])

            x1 = lista_vertice[0][0]
            y1 = lista_vertice[0][1]
            x2 = lista_vertice[1][0]
            y2 = lista_vertice[1][1]

            lista_aux.append("x")
            lista_aux.append("y")
            lista_aux.append("x")
            lista_aux.append("y")
            lista_aux.append("x")
            lista_aux.append("y")
            lista_aux.append("x")
            lista_aux.append("y")


            i+=1
            j+=1
"""














"""    # for vertice in self.__terreno:
    def verifica_colisao_terreno(self, mapa, tela):

        lista_vertice = mapa.get_terreno()
        lista_aux = []
        cont = 0
        # junta os valores das tuplas do terreno e as torna uma lista de valores ao inves de lista de tupla
        for vertice in lista_vertice:
            lista_aux.append(vertice[0])
            lista_aux.append(vertice[1])

        #print("oficial:", lista_vertice)
        # print("aux :",lista_aux)

        # impede o stouro do indice
        stop = len(lista_aux) - 3
        # incrementa os indices para definir o inicio e fim da colisao em x e o inicio e fim da colisao em y
        x_inicio = 0
        x_fim = 2
        y_inicio = 1
        y_fim = 3

        for vertice in lista_aux:

            x_vertice_inicio = lista_aux[x_inicio]
            x_vertice_fim = lista_aux[x_fim]
            y_vertice_inicio = lista_aux[y_inicio]
            y_vertice_fim = lista_aux[y_fim]

            # desenha_colisao = pygame.Rect((x_vertice_inicio, x_vertice_fim), (y_vertice_inicio, y_vertice_fim))
            # desenha_colisao = pygame.Rect((x_vertice_inicio, y_vertice_fim), (x_vertice_inicio, y_vertice_fim))
            # tela.draw_rect(pygame.Color(255, 0, 0, 10), desenha_colisao)

            # padroniza a colisao retangular de acordo com o vertice y mais  baixo
            # if y_vertice_inicio <= y_vertice_fim:
            #   temp = y_vertice_inicio
            #   y_vertice_inicio = y_vertice_fim
            #   y_vertice_fim = temp

            # padroniza a colisao retangular de acordo com o vertice y mais  alto
            if y_vertice_inicio >= y_vertice_fim:
                temp = y_vertice_inicio
                y_vertice_inicio = y_vertice_fim
                y_vertice_fim = temp

            # calcula a distancia entre as duas alturas sorteadas no terreno e divide por 2 ignorando o sinal(-ou+)
            y_vertice_intermediario_central = abs((y_vertice_inicio - y_vertice_fim) / 2)
            # soma  a altura do y do terreno com o  centro do retangulo maior da geometria para criar a altura do retangulo menor no centro
            y_vertice_intermediario_central += y_vertice_inicio

            x_vertice_intermediario_central = abs((x_vertice_inicio - x_vertice_fim) /2 )
            x_vertice_intermediario_central += x_vertice_inicio

            tamanho_x_colisor_maior = abs(x_vertice_inicio - x_vertice_fim)
            tamanho_y_colisor_maior = abs(y_vertice_inicio - RESOLUCAO[1])

            cremento_tamanho_y = tamanho_y_colisor_maior/6



            print("oficial:", lista_vertice)
            print("tamanho_y", tamanho_y_colisor_maior)
            print("cremento ", cremento_tamanho_y)



            # desenha retangulos do tamanho da volumetria da area de colisao para eu ter um feedback visual de onde esta ativado a colisao retangular
            retangulo_colisor_maior_01 = pygame.Surface((tamanho_x_colisor_maior, tamanho_y_colisor_maior))
            retangulo_colisor_maior_01.set_alpha(80)  # alpha level
            retangulo_colisor_maior_01.fill(AMARELO)  # this fills the entire surface
            tela.blit(retangulo_colisor_maior_01, ((abs(x_vertice_inicio), abs(y_vertice_fim))))

            retangulo_colisor_maior_02 = pygame.Surface((tamanho_x_colisor_maior, tamanho_y_colisor_maior))
            retangulo_colisor_maior_02.set_alpha(80)  # alpha level
            retangulo_colisor_maior_02.fill(CYAN)  # this fills the entire surface
            tela.blit(retangulo_colisor_maior_02,((abs(x_vertice_inicio), abs(y_vertice_fim - cremento_tamanho_y))))


            # veifica a colisao retangular maior da geometria  dinamicamente
            # e tambem a geometria retangular fragmentada (y_vertice_intermediario_central gera de fato retangulos menores)
            if self.get_posicao_x() + self.get_tamanho_x() >= x_vertice_inicio \
                    and self.get_posicao_x() <= x_vertice_fim \
                    and self.get_posicao_y() + self.get_tamanho_y() >= y_vertice_fim:
                # onde a nave colidiu, pinte este retangulo de amarelo
                retangulo_colisor_maior_01.set_alpha(180)  # alpha level
                retangulo_colisor_maior_01.fill((AMARELO))  # this fills the entire surface
                tela.blit(retangulo_colisor_maior_01, ((abs(x_vertice_inicio), abs(y_vertice_fim))))

                self.set_colidiu_terreno(True)
                print("COLIDIU COM O TERRENO")

            else:
                self.set_colidiu_terreno(False)

            if self.get_posicao_x() + self.get_tamanho_x() >= x_vertice_inicio \
                    and self.get_posicao_x() <= x_vertice_fim \
                    and self.get_posicao_y() + self.get_tamanho_y() >= y_vertice_fim - cremento_tamanho_y:
                retangulo_colisor_maior_02.set_alpha(180)  # alpha level
                retangulo_colisor_maior_02.fill((CYAN))  # this fills the entire surface
                tela.blit(retangulo_colisor_maior_02,((abs(x_vertice_inicio), abs(y_vertice_fim - cremento_tamanho_y))))

                self.set_colidiu_terreno(True)
                print("COLIDIU COM O TERRENO")

            else:
                self.set_colidiu_terreno(False)

            # impede o stouro do indice
            # incremento (atualizacao)da posicao de verificacao de colisao
            if y_fim < stop:
                x_inicio += 2
                x_fim += 2
                y_inicio += 2
                y_fim += 2
            else:
                break

            cont += 1

            #print("x inicio :", x_vertice_inicio)
            #print("x fim :", x_vertice_fim)
            #print('x intermediario ', x_vertice_intermediario_central)
            # print("y inicio: ", y_vertice_inicio)
            # print("y fim :",y_vertice_fim)
            # print("intermediario: ", y_vertice_intermediario_central)"""