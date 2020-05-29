import random

import pygame
import math
from Config import *

class Nova_nave:
    def __init__(self, surface, posicao_x, posicao_y):
        self.__surface = pygame.image.load(surface)
        self.__largura_x = self.__surface.get_rect()[2]
        self.__altura_y = self.__surface.get_rect()[3]
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
        self.__combustivel = 1000
        self.__gravidade_lua = 1.6

    def get_gravidade_lua(self):
        return self.__gravidade_lua

    def set_gravidade_lua(self, gravidade):
        self.__gravidade_lua = gravidade

    def get_combustivel(self):
        return self.__combustivel

    def set_combustivel(self, combustivel):
        self.__combustivel = combustivel

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

    def get_largura_x(self):
        return self.__largura_x

    def get_altura_y(self):
        return self.__altura_y

    def set_tamanho(self, novo_tamanho_x, novo_tamanho_y):
        self.__surface = pygame.transform.scale(self.__surface, (novo_tamanho_x, novo_tamanho_y))
        novo_centro = novo_tamanho_x/2, novo_tamanho_y/2
        self.set_centro(novo_centro)
        self.__largura_x = novo_tamanho_x
        self.__altura_y = novo_tamanho_y


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

        ponto_direito = largura_poligono + self.get_posicao_x() + self.get_largura_x() / 2 + posicao_horizontal
        ponto_esquerdo = -largura_poligono + self.get_posicao_x() + self.get_largura_x() / 2 + posicao_horizontal
        ponto_acelerador_poligono += self.get_posicao_y() + self.get_altura_y()
        altura_base = self.get_altura_y()

        vertices_propulsor = ((ponto_direito, altura_base + self.get_posicao_y()),  # (0,3),
                              (self.get_posicao_x() + self.get_largura_x() / 2 + posicao_horizontal, ponto_acelerador_poligono),  # (3,-3)
                              (ponto_esquerdo, altura_base + self.get_posicao_y()))  # (-3,-3)

        return self.__rotacionaPoligono_propulsor(vertices_propulsor)


    def __rotacionaPoligono_propulsor(self, vertices_propulsor):

        origem_nave = self.__posicao_x + self.get_largura_x() / 2, self.get_posicao_y() + self.get_altura_y() / 2
        angulo_rotacao = math.radians(-self.get_angulo_rotacao())

        poligono_rotacionado = []

        for vertice in vertices_propulsor:
            vertice_aux = vertice[0] - origem_nave[0], vertice[1] - origem_nave[1]
            vertice_aux = (vertice_aux[0] * math.cos(angulo_rotacao) - vertice_aux[1] * math.sin(angulo_rotacao),
                           vertice_aux[0] * math.sin(angulo_rotacao) + vertice_aux[1] * math.cos(angulo_rotacao))
            vertice_aux = vertice_aux[0] + origem_nave[0], vertice_aux[1] + origem_nave[1]
            poligono_rotacionado.append(vertice_aux)

        return poligono_rotacionado


    def verifica_colisao_tela(self, tela):

        # se for diferente disso é porque esta fora da tela
        if self.get_posicao_x() >= 0 and self.__posicao_x <= tela.get_resolucao()[0] - self.get_largura_x()\
            and self.get_posicao_y() >= 0 and self.__posicao_y <= tela.get_resolucao()[1] - self.get_altura_y():
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

            # verifica a colisao entre a nave e a area de pouso, permite pousar ate na metade da nave em colisao
            if self.get_posicao_x()+ self.get_largura_x()/2 >= inicio_area_pouso_horizontal \
                    and self.get_posicao_x() + self.get_largura_x()/2 <= fim_area_pouso_horizontal \
                    and self.get_posicao_y() + self.get_altura_y() >= mapa.get_altura_pouso_nave() - mapa.get_espessura_line_pouso_nave()/2:
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
    def aceleracao_propulsor(self, tempo, tela):

        if self.get_propulsor_ativo() == True and self.get_colidiu_tela() == False and self.get_colidiu_area_pouso() == False:
            self.__velocidade_y-= (self.get_gravidade_lua() / tela.get_fps()) * tempo  * self.get_friccao()

            self.set_combustivel(self.get_combustivel()-1)
            print("acelerei")

            # permite aumentar o tamanho do propulsor baseado no tamanho dela "%"
            if self.__potencia_propulsor < self.get_altura_y()/1000*10:
                self.__potencia_propulsor += (self.get_gravidade_lua() / tela.get_fps())* tempo  * self.get_friccao()

            if self.get_velocidade_y() <= self.get_gravidade_lua():
                tempo = 0

                # define nova direcao caso a nave esteja inclinada pra direita e propulsor ativo
                if self.get_angulo_rotacao()<=1 and self.get_propulsor_ativo():
                    self.__velocidade_x += self.get_angulo_rotacao()*-1 /180

                # define nova direcao caso a nave esteja inclinada pra esquerda e propulsor ativo
                if self.__angulo_rotacao >= 1 and self.get_propulsor_ativo():
                    self.__velocidade_x -= self.get_angulo_rotacao()/180



    def gravidade(self, tempo, tela):

        # GRAVIDADE
        # se nao tiver acelerando e nao tiver colidido com a tela ou com a area de pouso executa a gravidade
        if self.get_propulsor_ativo() == False and self.get_colidiu_tela() == False \
            and self.get_colidiu_area_pouso() == False:

            self.__velocidade_y += (self.get_gravidade_lua() / tela.get_fps()) * tempo * self.get_friccao()
            # diminiu o tamanho do propulsor
            self.__potencia_propulsor -= (self.get_gravidade_lua() / tela.get_fps()) * tempo * self.get_friccao()

            # caso ele for menor que zero, fique em zero.
            if self.get_potencia_propulsor() < 0:
                self.set_potencia_propulsor(0)
            if self.get_velocidade_y() >= self.get_gravidade_lua():
                tempo = 0


    # calcula novos pontos(intermediario (x,y)) na lista de vertice existente do terreno e os adiciona dinamicamente.
    # A cada dois pontos principais(e ja existentes)  é adicionado x quantidade de pontos entre eles para que a deteccao
    # de colisao seja mais precisa.
    def verifica_colisao_terreno(self, mapa, tela):

        self.set_colidiu_terreno(False)
        # recebe a lista de vertice responsavel por desenhar o terreno
        lista_vertice = mapa.get_terreno()

        i = 0
        j = 1

        for vertice in lista_vertice:

            # Adiciona o primeiro ponto ja existente
            self.__nova_lista_colisores_terreno.append((vertice[0], vertice[1]))

            # obtem os valores dos pontos ja existentes
            ponto_principal_x1 = lista_vertice[i][0]
            ponto_principal_y1 = lista_vertice[i][1]
            ponto_principal_x2 = lista_vertice[j][0]
            ponto_principal_y2 = lista_vertice[j][1]

            #distancia_entre_ponto_principal_x1_y1_x2_y2 = math.sqrt((abs(abs(ponto_principal_x2 - ponto_principal_x1)**2) \
            # + abs(ponto_principal_y1 - ponto_principal_y2)**2))

            # calcula  quantos vertices serao adicionado entre os vertices ja existente e tambem define
            # o qual é o tamanho do incremento nas posicoes x,y dos novos vertices que serao criador
            incremento_x = abs(ponto_principal_x1-ponto_principal_x2)/  (len(lista_vertice)/6)
            incremento_y = abs(ponto_principal_y1-ponto_principal_y2)/ (len(lista_vertice)/6)

            # se der tempo tenho que criar funcao
            # estabiliza o sentido correto do incremento das posicoes dos novos vertices
            #Se o terreno esta aclive faça:
            if ponto_principal_y1>ponto_principal_y2:
                pontos_intermediarios_entre_pontos_principais_p1 = \
                    (int(ponto_principal_x1 + (incremento_x * 1)), int(ponto_principal_y1 - (incremento_y * 1)))
                pontos_intermediarios_entre_pontos_principais_p2 = \
                    (int(ponto_principal_x1 + (incremento_x * 2)), int(ponto_principal_y1 - (incremento_y * 2)))
                pontos_intermediarios_entre_pontos_principais_p3 = \
                    (int(ponto_principal_x1 + (incremento_x * 3)), int(ponto_principal_y1 - (incremento_y * 3)))
                pontos_intermediarios_entre_pontos_principais_p4 = \
                    (int(ponto_principal_x1 + (incremento_x * 4)), int(ponto_principal_y1 - (incremento_y * 4)))
                pontos_intermediarios_entre_pontos_principais_p5 = \
                    (int(ponto_principal_x1 + (incremento_x * 5)), int(ponto_principal_y1 - (incremento_y * 5)))
            #Se for declive faça:
            else:
                pontos_intermediarios_entre_pontos_principais_p1 = \
                    (int(ponto_principal_x1 + (incremento_x * 1)), int(ponto_principal_y1 + (incremento_y * 1)))
                pontos_intermediarios_entre_pontos_principais_p2 = \
                    (int(ponto_principal_x1 + (incremento_x * 2)), int(ponto_principal_y1 + (incremento_y * 2)))
                pontos_intermediarios_entre_pontos_principais_p3 = \
                    (int(ponto_principal_x1 + (incremento_x * 3)), int(ponto_principal_y1 + (incremento_y * 3)))
                pontos_intermediarios_entre_pontos_principais_p4 = \
                    (int(ponto_principal_x1 + (incremento_x * 4)), int(ponto_principal_y1 + (incremento_y * 4)))
                pontos_intermediarios_entre_pontos_principais_p5 = \
                    (int(ponto_principal_x1 + (incremento_x * 5)), int(ponto_principal_y1 + (incremento_y * 5)))

            # apos ser calculado, adiciona os novos pontos na lista entre os vertices ja existentes
            self.__nova_lista_colisores_terreno.append(pontos_intermediarios_entre_pontos_principais_p1)
            self.__nova_lista_colisores_terreno.append(pontos_intermediarios_entre_pontos_principais_p2)
            self.__nova_lista_colisores_terreno.append(pontos_intermediarios_entre_pontos_principais_p3)
            self.__nova_lista_colisores_terreno.append(pontos_intermediarios_entre_pontos_principais_p4)
            self.__nova_lista_colisores_terreno.append(pontos_intermediarios_entre_pontos_principais_p5)

            # pegando o centro de baixo da nave
            p_nave = self.get_posicao_x() + self.get_largura_x() / 2, self.get_posicao_y() + self.get_altura_y()

            # se der tempo tenho que criar funcao
            # calcula a distancia do entre o vertice central inferior da nave e os pontos ja existentes da lista
            distancia_entre_ponto_colisor_nave_ponto_principal = \
                math.sqrt((abs(abs(ponto_principal_x2 - p_nave[0]) ** 2) + abs(p_nave[1] - ponto_principal_y2) ** 2))

            # Calcula a distancia entre o vertice central inferior da nave e os novos pontos adicionados na lista
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

            # verifica se a distancia é menor que 10, se sim, colidiu com o terreno
            if distancia_entre_ponto_colisor_nave_ponto_principal < 10:
                self.set_colidiu_terreno(True)
                #print("COLIDIU PONTO PRINCIPAL")

            # verifica se a distancia é menor que 10, se sim, colidiu com o terreno
            if distancia_entre_ponto_colisor_nave_ponto_intermediario_01 < 5 \
                    or distancia_entre_ponto_colisor_nave_ponto_intermediario_02 < 5 \
                    or distancia_entre_ponto_colisor_nave_ponto_intermediario_03 < 5 \
                    or distancia_entre_ponto_colisor_nave_ponto_intermediario_04 < 5 \
                    or distancia_entre_ponto_colisor_nave_ponto_intermediario_05 < 5 :
                #print("COLIDIU PONTO INTERMEDIARIO")
                self.set_colidiu_terreno(True)

            if j < len(lista_vertice)-1:#6
                i+=1
                j+=1

        #tela.draw_lines((RED), self.get_lista_colisores_terreno(), 2)
