import math
import random
from Dados import RED
from Dados import AMARELO
from Dados import CYAN
from Dados import BLACK

import pygame


class Nova_nave:
    def __init__(self, surface, posicao_x, posicao_y):
        self.__surface = pygame.image.load(surface)
        self.__largura_x = self.__surface.get_rect()[2]
        self.__altura_y = self.__surface.get_rect()[3]
        self.__posicao_x = posicao_x
        self.__posicao_y = posicao_y
        self.__velocidade_x = 0
        self.__velocidade_y = 0
        self.__velocidade_media = 0
        self.__potencia_propulsor = 0
        self.__friccao = 0
        self.__angulo_rotacao = 0
        self.__velocidade_rotacao = 0
        self.__rect =self.__surface.get_rect()
        self.__propulsor = False
        self.__colidiu_tela = False
        self.__colidiu_pouso = False
        self.__colisao_antecipada = False
        self.__colidiu_terreno = False
        self.__rotacionou_dir = False
        self.__rotacionou_esq = False
        self.__nova_lista_colisores_terreno = []
        self.__combustivel = 1000
        self.__gravidade_lua = 1.6
        self.__altitude = 0
        self.__cont = 0
        self.__som_propulsor = pygame.mixer.music
        self.__vida = 1
        self.__posicao_inicial_x = 0
        self.__pocicao_inicial_y = 0
        self.__pare_de_explodir = True
        self.__contador_explosao = 0


    def reiniciar(self):
        self.set_posicao_x(self.get_posicao_inicial_x())
        self.set_posicao_y(self.get_posicao_inicial_y())
        self.set_velocidade_x(0)
        self.set_velocidade_x(0)
        self.set_velocidade_media(0)
        self.set_potencia_propulsor(0)
        self.set_friccao(0)
        self.set_angulo_rotacao(0)
        self.set_velocidade_rotacao(0)
        self.set_combustivel(1000)
        self.set_gravidade_lua(1.6)
        self.set_vida(1)
        self.__set_pode_explodir(True)
        self.set_contador_explosao(0)


    def salvar(self):

        self.__s_posicao_x = self.get_posicao_x()
        self.__s_posicao_y = self.get_posicao_y()
        self.__s_velocidade_x = self.get_velocidade_x()
        self.__s_velocidade_y = self.get_velocidade_y()
        self.__s_velocidade_media = self.get_velocidade_media()
        self.__s_potencia_propulsor = self.get_potencia_propulsor()
        self.__s_friccao = self.get_friccao()
        self.__s_angulo_rotacao = self.get_angulo_rotacao()
        self.__s_velocidade_rotacao = self.get_velocidade_rotacao()
        self.__s_combustivel = self.get_combustivel()
        self.__s_gravidade_lua = self.get_gravidade_lua()
        self.__s_vida = self.get_vida()
        self.__s_pode_explodir = self.__get_pode_explodir()
        self.__s_contador_explosao = self.get_contador_explosao()


    def carregar_save(self):

        self.set_posicao_x(self.__s_posicao_x)
        self.set_posicao_y(self.__s_posicao_y)
        self.set_velocidade_x(self.__s_velocidade_x)
        self.set_velocidade_y(self.__s_velocidade_y)
        self.set_velocidade_media(self.__s_velocidade_media)
        self.set_potencia_propulsor(self.__s_potencia_propulsor)
        self.set_friccao(self.__s_friccao)
        self.set_angulo_rotacao(self.__s_angulo_rotacao)
        self.set_velocidade_rotacao(self.__s_velocidade_rotacao)
        self.set_combustivel(self.__s_combustivel)
        self.set_gravidade_lua(self.__s_gravidade_lua)
        self.set_vida(self.__s_vida)
        self.__set_pode_explodir(self.__s_pode_explodir)
        self.set_contador_explosao(self.__s_contador_explosao)

    def get_contador_explosao(self):
        return self.__contador_explosao

    def set_contador_explosao(self, contador):
        self.__contador_explosao = contador

    def __get_pode_explodir(self):
        return self.__pare_de_explodir

    def __set_pode_explodir(self, pode):
        self.__pare_de_explodir = pode

    def get_posicao_inicial_x(self):
        return self.__posicao_inicial_x

    def set_posicao_inicial_x(self, posicao_x):
        self.__posicao_inicial_x = posicao_x

    def get_posicao_inicial_y(self):
        return self.__posicao_inicial_y

    def set_posicao_inicial_y(self, posicao_y):
        self.__posicao_inicial_y = posicao_y


    def set_vida(self, vida):
        self.__vida = vida

    def get_vida(self):
        return self.__vida


    def update(self):
        self.set_posicao_x(self.get_posicao_x() + self.get_velocidade_x())
        self.set_posicao_y(self.get_posicao_y() + self.get_velocidade_y())

        if self.get_velocidade_x() !=0:
            self.set_velocidade_media((self.get_velocidade_x() + self.get_velocidade_y() * 2))
        else:
            self.set_velocidade_media(self.get_velocidade_y())

    def play_som_propulsor(self):
        self.__som_propulsor.play()

    def set_volume_propulsor(self, volume):
        self.__som_propulsor.set_volume(volume)

    def get_volume_propulsor(self):
        return self.__som_propulsor.get_volume()

    def set_altitude(self, altitude):
        self.__altitude = altitude

    def get_altitude(self):
        return  self.__altitude

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

    def get_velocidade_media(self):
        return self.__velocidade_media

    def set_velocidade_media(self, velocidade_media):
        self.__velocidade_media = velocidade_media

    def get_potencia_propulsor(self):
         return self.__potencia_propulsor

    def set_potencia_propulsor(self, potencia_propulsor):
        self.__potencia_propulsor = potencia_propulsor

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

    def get_verifica_colisao_antecipada(self):
        return self.__colisao_antecipada

    def set_colisao_antecipada(self, booleana):
        self.__colisao_antecipada =  booleana

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





    def gravidade(self,tela):

        # GRAVIDADE
        # se nao tiver acelerando e nao tiver colidido com a tela ou com a area de pouso executa a gravidade
        if self.get_propulsor_ativo() == False and self.get_colidiu_tela() == False \
            and self.get_colidiu_area_pouso() == False:

            self.__som_propulsor.fadeout(700)
            self.__som_propulsor.stop()

            # diminiu o tamanho do propulsor
            self.set_potencia_propulsor(self.get_potencia_propulsor()-00.01)

            # caso ele for menor que zero, fique em zero.
            if self.get_potencia_propulsor() < 0:
                self.set_potencia_propulsor(0)

            # a gravidade só puxa a nave com uma força de até 1.6(gravidade da lua)
            if self.get_velocidade_y() < self.get_gravidade_lua():
                self.set_velocidade_y(self.get_velocidade_y()+(00.01 * self.get_friccao()))




    # ACELERACAO do propulsor
    def aceleracao_propulsor(self,tela):

        if self.get_propulsor_ativo() == True and self.get_colidiu_tela() == False and self.get_colidiu_area_pouso() == False:
            self.__cont += 1

            self.__som_propulsor.load('arquivos/propulsor.mp3')
            self.__som_propulsor.play()

            # gasta combustivel ao acelerar e so acelera se caso tiver
            if self.get_combustivel()>0:
                #self.__velocidade_y -= (self.get_gravidade_lua() / tempo) * self.get_friccao()
                self.set_combustivel(self.get_combustivel() - 1)

                # só é possivel acelerar ate a velocidade maxima de 1.6
                if self.get_velocidade_y() > -self.get_gravidade_lua():
                    self.set_velocidade_y(self.get_velocidade_y() - (00.01 * self.get_friccao()))
            else:
                self.set_combustivel(0)
                self.set_potencia_propulsor(0)

            angulo = self.get_angulo_rotacao() / 1000 * 10
            # permite aumentar o tamanho do propulsor baseado no tamanho dela "%"
            if self.get_potencia_propulsor() < self.get_altura_y()/1000*15:
                self.set_potencia_propulsor(self.get_potencia_propulsor()+00.01)

            # define nova direcao caso a nave esteja inclinada pra direita  ou esquerda
            self.set_velocidade_x((self.get_velocidade_x() + (00.01 * -angulo * self.get_friccao())))
            #print("v:", self.get_velocidade_x())

            # significa que ela esta executando nova direcao, entao aplica mais força de gravidade de acordo com o angulo
            if self.get_velocidade_y() < self.get_gravidade_lua():
                self.set_velocidade_y(self.get_velocidade_y() + (00.01 * abs(angulo) * self.get_friccao()))





    def verifica_colisao_tela(self, tela):

        # se for diferente disso é porque esta fora da tela
        if self.get_posicao_x() >= 0 and self.__posicao_x <= tela.get_resolucao()[0] - self.get_largura_x()\
            and self.get_posicao_y() >= 0 and self.__posicao_y <= tela.get_resolucao()[1] - self.get_altura_y():
            #print("nao colidiu com a tela")
            self.set_colidiu_tela(False)

        else:
            #print("colidiu com a tela")
            # pega a posicao do momento da colisao e deixa a nave travada nela
            self.set_colidiu_tela(True)
            self.set_velocidade_x(0)
            self.set_velocidade_y(0)
            self.set_gravidade_lua(0)
            self.set_potencia_propulsor(0)
            self.set_rotacionou_dir(False)
            self.set_rotacionou_esq(False)
            self.set_gravidade_lua(0)
            self.set_angulo_rotacao(self.get_angulo_rotacao())
            self.set_posicao(self.get_posicao_x(), self.get_posicao_y())






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
                #print("COLIDIU COM A AREA DE POUSO")
                #se colidiu trave a nave
                #self.set_potencia_propulsor(0)
                self.set_rotacionou_dir(False)
                self.set_rotacionou_esq(False)
                self.set_velocidade_x(0)
                self.set_velocidade_y(0)
                #self.set_angulo_rotacao(self.get_angulo_rotacao())
                #self.set_posicao(self.get_posicao_x(), (self.get_posicao_y()))
            else:
                self.set_colidiu_area_pouso(False)

            # tenho que fazer essa verificacao pois quando a nave pousa tbm colide com o terreno, isso é pra destinguir
            # que a nave pousou e nao colidiucom o terreno e morreu

            if self.get_posicao_x()+ self.get_largura_x()/2 >= inicio_area_pouso_horizontal and \
                    self.get_posicao_x() + self.get_largura_x()/2 <= fim_area_pouso_horizontal:
                self.set_colisao_antecipada(True)
                #print("Colisao antecipada :", self.get_verifica_colisao_antecipada())
            else:
                self.set_colisao_antecipada(False)


    def explodir(self, tela, intensidade, diametro, duracao):



        if self.get_colidiu_terreno() == True:
            self.__contador_explosao+=1

        if self.__contador_explosao > duracao:
            self.__set_pode_explodir(False)


        if self.__get_pode_explodir() == True:
            for x in range(intensidade):
                self.__gerador_explosao(tela, diametro)



    def __gerador_explosao(self, tela, diametro_explosao):

        # sorteia as cores da explosao dentre essas pre definidas
        c1 = random.randint(1,4)
        color = (0,0,0)
        if c1 == 1:
            color = RED
        if c1 == 2:
            color = CYAN

        if c1 == 3:
            color = AMARELO

        if c1 == 4:
            color = BLACK

        # define o ponto central de origem da explosao e o diametro
        x_dir = abs(int((self.get_posicao_x()+ (self.get_largura_x()/2)) + diametro_explosao))
        x_esq = abs(int((self.get_posicao_x() + (self.get_largura_x()/2)) - diametro_explosao))
        y_cima = abs(int((self.get_posicao_y()+ (self.get_altura_y()/2)) - diametro_explosao))
        y_baixo = abs(int((self.get_posicao_y() + (self.get_altura_y()/2)) + diametro_explosao))

        # sortei um ponto(posicao) que esteja dentro da area limite para desenhar
        posicao_x = random.randint(x_esq,x_dir)
        posicao_y = random.randint(y_cima, y_baixo)

        # define os tamanhos posiveis dos retangulos(particulas)
        random_tamanho = random.randint(1,10)
        # define  a area limite que a explosao atinge

        # cria a "particula"
        retangulo = pygame.Surface((random_tamanho,random_tamanho))
        retangulo.set_alpha(200)
        retangulo.fill((color))

        # desenha na tela
        tela.blit(retangulo, (posicao_x, posicao_y))




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
            if distancia_entre_ponto_colisor_nave_ponto_principal < 8:

                if self.get_colidiu_area_pouso() == False and self.get_verifica_colisao_antecipada() == False:
                    self.set_colidiu_terreno(True)
                    self.set_velocidade_x(0)
                    self.set_velocidade_y(0)
                    self.set_gravidade_lua(0)
                    self.set_potencia_propulsor(0)
                    self.set_rotacionou_dir(False)
                    self.set_rotacionou_esq(False)
                    self.set_gravidade_lua(0)
                    self.set_angulo_rotacao(self.get_angulo_rotacao())
                    self.set_posicao(self.get_posicao_x(), self.get_posicao_y())
                    #print("COLIDIU PONTO PRINCIPAL")
                else:
                    self.set_colidiu_terreno(False)

            # verifica se a distancia é menor que 10, se sim, colidiu com o terreno
            if distancia_entre_ponto_colisor_nave_ponto_intermediario_01 < 8 \
                    or distancia_entre_ponto_colisor_nave_ponto_intermediario_02 < 8 \
                    or distancia_entre_ponto_colisor_nave_ponto_intermediario_03 < 8 \
                    or distancia_entre_ponto_colisor_nave_ponto_intermediario_04 < 8 \
                    or distancia_entre_ponto_colisor_nave_ponto_intermediario_05 < 8 :
                #self.set_colidiu_terreno(True)

                if self.get_colidiu_area_pouso() == False and self.get_verifica_colisao_antecipada() == False:
                    self.set_colidiu_terreno(True)
                    self.set_velocidade_x(0)
                    self.set_velocidade_y(0)
                    self.set_gravidade_lua(0)
                    self.set_potencia_propulsor(0)
                    self.set_rotacionou_dir(False)
                    self.set_rotacionou_esq(False)
                    self.set_gravidade_lua(0)
                    self.set_angulo_rotacao(self.get_angulo_rotacao())
                    self.set_posicao(self.get_posicao_x(), self.get_posicao_y())
                    #print("COLIDIU PONTO INTERMEDIARIO")

                else:
                    self.set_colidiu_terreno(False)


            if j < len(lista_vertice)-1:#6
                i+=1
                j+=1