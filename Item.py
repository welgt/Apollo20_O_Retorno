import math
import random
import pygame
from Dados import GREEN
from Dados import LARANJA

class Item:
    def __init__(self, posicao_x, posicao_y):

        # tive que fazer essa gambiarra de ultima hora pra dar tempo porque troquei de imagem para Surface
        #r = random.randint(0,1)
        #if r == 0:
         #   color = GREEN

        #if r == 1:
         #   color = LARANJA
        retangulo = pygame.Surface((100,100))
        retangulo.set_alpha(255)
        retangulo.fill((GREEN))

        self.__surface = retangulo

        #self.__surface = pygame.image.load(surface)
        self.__posicao_x = posicao_x
        self.__posicao_y = posicao_y
        self.__velocidade_x = 0
        self.__velocidade_y = 0
        self.__largura_x = self.__surface.get_rect()[2]
        self.__altura_y = self.__surface.get_rect()[3]
        self.__colidiu_pouso = False
        self.__colidiu_terreno = False
        self.__gravidade_lua = 1.6
        self.__friccao = 0
        self.__centro_surface = 0
        self.__som_item = pygame.mixer.music
        self.__nova_lista_colisores_terreno = []
        self.__colidiu_nave = False

        self.__posicao_inicial_x = 0
        self.__posicao_inicial_y = 0

        self.__eh_save = False




    def reiniciar(self):

        self.set_posicao_x(self.get_posicao_inicial_x())
        self.set_posicao_y(self.get_posicao_inicial_y())
        self.set_velocidade_x(0)
        self.set_velocidade_y(0)
        self.set_gravidade_lua(1.6)
        self.set_friccao(0)


        #self.__largura_x = self.__surface.get_rect()[2]
        #self.__altura_y = self.__surface.get_rect()[3]
        #self.__colidiu_pouso = False
        #self.__colidiu_terreno = False
        #self.set_centro(0)
        #self.__som_item = pygame.mixer.music
        #self.__nova_lista_colisores_terreno = []
        #self.__colidiu_nave = False

    def salvar(self):

        self.__s_posicao_x = self.get_posicao_x()
        self.__s_posicao_y = self.get_posicao_y()
        self.__s_velocidade_x = self.get_velocidade_x()
        self.__s_velocidade_y = self.get_velocidade_y()
        self.__s_gravidade_lua = self.get_gravidade_lua()
        self.__s_friccao = self.get_friccao()
        self.__s_eh_save = self.set_eh_save(True)

    def carregar_save(self):

        self.set_posicao_x(self.__s_posicao_x)
        self.set_posicao_y(self.__s_posicao_y)
        self.set_velocidade_x(self.__s_velocidade_x)
        self.set_velocidade_y(self.__s_velocidade_y)
        self.set_gravidade_lua(self.__s_gravidade_lua)
        self.set_friccao(self.__s_friccao)
        self.set_eh_save(self.__s_eh_save)





    def play_som_item(self):
        self.__som_item.play()

    def set_volume_item(self, volume):
        self.__som_item.set_volume(volume)

    def get_volume_propulsor(self):
        return self.__som_item.get_volume()



    def get_posicao_inicial_x(self):
        return self.__posicao_inicial_x

    def set_posicao_inicial_x(self, posicao):
        self.__posicao_inicial_x = posicao

    def get_posicao_inicial_y(self):
        return self.__posicao_inicial_y

    def set_posicao_inicial_y(self, posicao):
        self.__posicao_inicial_y = posicao


    def gravidade(self, tela):
        # GRAVIDADE

        self.set_posicao_y(self.get_posicao_y() + (self.get_gravidade_lua() / tela.get_cronometro()[4]) * self.get_friccao() + self.get_velocidade_y())


    def get_gravidade_lua(self):
        return self.__gravidade_lua

    def set_gravidade_lua(self, gravidade):
        self.__gravidade_lua = gravidade


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

    def set_velocidade_x(self, velocidade):
        self.__velocidade_x = velocidade

    def get_velocidade_x(self):
        return self.__velocidade_x

    def set_velocidade_y(self, velocidade):
        self.__velocidade_y = velocidade

    def get_velocidade_y(self):
        return self.__velocidade_y

    def set_largura(self, largura):
        self.__largura_x = largura

    def get_largura_x(self):
        return self.__largura_x

    def set_altura(self, altura):
        self.__altura_y = altura

    def get_altura_y(self):
        return self.__altura_y

    def set_tamanho(self, novo_tamanho_x, novo_tamanho_y):
        self.__surface = pygame.transform.scale(self.__surface, (novo_tamanho_x, novo_tamanho_y))
        novo_centro = novo_tamanho_x/2, novo_tamanho_y/2
        self.set_centro(novo_centro)
        self.set_largura(novo_tamanho_x)
        self.set_altura(novo_tamanho_y)

    def get_centro_surface(self):
        return self.__centro_surface

    def set_centro(self, novo_centro):
        self.__centro_surface = novo_centro


    def get_friccao(self):
        return self.__friccao

    def set_friccao(self, nova_friccao):
        self.__friccao = nova_friccao


    def get_colidiu_area_pouso(self):
        return self.__colidiu_pouso

    def set_colidiu_area_pouso(self, booleana):
        self.__colidiu_pouso = booleana

    def get_colidiu_terreno(self):
        return self.__colidiu_terreno

    def set_colidiu_terreno(self, booleana):
        self.__colidiu_terreno = booleana

    def posicao_randomica(self, tela):
        sort1 = random.randint(100, tela.get_resolucao()[0])
        self.set_posicao_x(sort1)
        self.set_posicao_y(-self.get_altura_y()-10)

    def get_colidiu_nave(self):
        return self.__colidiu_nave

    def set_colidiu_nave(self, colidiu):
        self.__colidiu_nave = colidiu

    def get_eh_save(self):
        return self.__eh_save

    def set_eh_save(self, eh_save):
        self.__eh_save = eh_save

    def verifica_colisao_nave(self, nave):


        if nave.get_posicao_x()+nave.get_largura_x()>= self.get_posicao_x() and nave.get_posicao_x() <= self.get_posicao_x()+ self.get_largura_x()\
                and nave.get_posicao_y()+nave.get_altura_y()>= self.get_posicao_y() and nave.get_posicao_y()<= self.get_posicao_y()+self.get_altura_y() :

            print('Colidiu')
            self.set_colidiu_nave(True)

            self.set_volume_item(1)
            self.__som_item.load('arquivos/item.mp3')
            self.__som_item.play()
        else:
            self.set_colidiu_nave(False)








    # calcula novos pontos(intermediario (x,y)) na lista de vertice existente do terreno e os adiciona dinamicamente.
    # A cada dois pontos principais(e ja existentes)  é adicionado x quantidade de pontos entre eles para que a deteccao
    # de colisao seja mais precisa.
    def verifica_colisao_terreno(self, mapa):

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
            p_item = self.get_posicao_x() + self.get_largura_x() / 2, self.get_posicao_y() + self.get_altura_y()

            # se der tempo tenho que criar funcao
            # calcula a distancia do entre o vertice central inferior da nave e os pontos ja existentes da lista
            distancia_entre_ponto_colisor_item_ponto_principal = \
                math.sqrt((abs(abs(ponto_principal_x2 - p_item[0]) ** 2) + abs(p_item[1] - ponto_principal_y2) ** 2))

            # Calcula a distancia entre o vertice central inferior da nave e os novos pontos adicionados na lista
            distancia_entre_ponto_colisor_item_ponto_intermediario_01 = \
                math.sqrt((abs(abs(pontos_intermediarios_entre_pontos_principais_p1[0] - p_item[0]) ** 2)
                             + abs(p_item[1] - pontos_intermediarios_entre_pontos_principais_p1[1]) ** 2))

            distancia_entre_ponto_colisor_item_ponto_intermediario_02 = \
                math.sqrt((abs(abs(pontos_intermediarios_entre_pontos_principais_p2[0] - p_item[0]) ** 2)
                           + abs(p_item[1] - pontos_intermediarios_entre_pontos_principais_p2[1]) ** 2))

            distancia_entre_ponto_colisor_item_ponto_intermediario_03 = \
                math.sqrt((abs(abs(pontos_intermediarios_entre_pontos_principais_p3[0] - p_item[0]) ** 2)
                           + abs(p_item[1] - pontos_intermediarios_entre_pontos_principais_p3[1]) ** 2))

            distancia_entre_ponto_colisor_item_ponto_intermediario_04 = \
                math.sqrt((abs(abs(pontos_intermediarios_entre_pontos_principais_p4[0] - p_item[0]) ** 2)
                           + abs(p_item[1] - pontos_intermediarios_entre_pontos_principais_p4[1]) ** 2))

            distancia_entre_ponto_colisor_item_ponto_intermediario_05 = \
                math.sqrt((abs(abs(pontos_intermediarios_entre_pontos_principais_p5[0] - p_item[0]) ** 2)
                           + abs(p_item[1] - pontos_intermediarios_entre_pontos_principais_p5[1]) ** 2))

            # verifica se a distancia é menor que 1, se sim, colidiu com o terreno
            if distancia_entre_ponto_colisor_item_ponto_principal < 5:
                self.set_colidiu_terreno(True)
                #print("COLIDIU PONTO PRINCIPAL")

            # verifica se a distancia é menor que 1, se sim, colidiu com o terreno
            if distancia_entre_ponto_colisor_item_ponto_intermediario_01 < 5 \
                    or distancia_entre_ponto_colisor_item_ponto_intermediario_02 < 5 \
                    or distancia_entre_ponto_colisor_item_ponto_intermediario_03 < 5 \
                    or distancia_entre_ponto_colisor_item_ponto_intermediario_04 < 5 \
                    or distancia_entre_ponto_colisor_item_ponto_intermediario_05 < 5 :
                #print("COLIDIU PONTO INTERMEDIARIO")
                self.set_colidiu_terreno(True)

            if j < len(lista_vertice)-1:#6
                i+=1
                j+=1