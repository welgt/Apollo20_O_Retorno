import pygame
from Tela import *

pygame.font.init()
class fonte_texto:
    def __init__(self):
        #self.__inicializa_fonte = pygame.font.init()
        self.__fonte_default = pygame.font.get_default_font()
        ##self.__fonte_default = 'Arial'
        self.__tamanho = 10
        self.__fonte_botao = None
        self.__visivel = 0
        self.__cor = 0
        self.__surface =None

        self.__texto = ""



        #self.__surface = self.get_fonte_botao().render(self.__frase , self.get_visivel(), self.get_cor())
        #teste = texto_play.get_fonte_botao().render('PLAY', texto_play.get_visivel(), WHITE)

    # texto_play = letras()
    # texto_play.set_visivel(1)
    # teste = texto_play.get_fonte_botao().render('PLAY', texto_play.get_visivel(), WHITE)
    # tela.blit(teste, (self.get_posicao_x(),self.get_posicao_y()))


    def cria_texto(self,tamanho, cor, visivel):
        self.set_tamanho(tamanho)
        fonte_botao = pygame.font.SysFont(self.__fonte_default, self.get_tamanho())
        self.__surface = fonte_botao.render(self.get_texto(), visivel, cor)

    def set_tamanho(self, tamanho):
        self.__tamanho = tamanho

    def get_tamanho(self):
        return self.__tamanho

    def set_texto(self, texto, fonte):
        self.__texto = texto
        self.__fonte_default = fonte

    def get_texto(self):
        return self.__texto

    def get_surface(self):
        return self.__surface




class painel:
    def __init__(self):
        self.__painel = None
        self.__cor = 0
        self.__posicao_x = 0
        self.__posicao_y = 0
        self.__largura = 0
        self.__altura = 0

    def cria_painel(self, tela, posicao_x, posicao_y, largura, altura):
        self.__posicao_x = posicao_x + RESOLUCAO[0] / 2 - self.__largura / 2
        self.__posicao_y = posicao_y + RESOLUCAO[1] / 2 - self.__altura / 2
        self.__largura = (RESOLUCAO[0] / 1000) * (largura * 10)
        self.__altura = (RESOLUCAO[1] / 1000) * (altura * 10)

       

    def draw_painel(self, tela, cor):
        self.__painel = pygame.Rect(self.__posicao_x, self.__posicao_y, self.__largura,
                                    self.__altura)
        tela.draw_rect(cor, self.__painel)

        self.draw_borda_painel(tela, AMARELO)

    def draw_borda_painel(self, tela, cor):
        borda = [(self.__posicao_x, self.__posicao_y),
                 (self.__posicao_x + self.__largura, self.__posicao_y),
                 (self.__posicao_x + self.__largura, self.__posicao_y + self.__altura),
                 (self.__posicao_x, self.__posicao_y + self.__altura)]
        tela.draw_lines(cor, borda, 3)


    def get_cor(self):
        return self.__cor

    def set_cor(self, cor):
        self.__cor = cor

    def get_posicao_x(self):
        return self.__posicao_x

    def set_posicao_x(self, posicao_x):
        self.__posicao_x = posicao_x

    def get_posicao_y(self):
        return self.__posicao_y

    def set_posicao_y(self, posicao_y):
        self.__posicao_y = posicao_y

    def get_largura(self):
        return self.__largura

    def set_largura(self, largura):
        self.__largura = largura

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura

    def get_painel(self):
        return self.__painel



class botao:

    def __init__(self):
        self.__botao = None
        self.__cor = 0
        self.__posicao_x = 0
        self.__posicao_y = 0
        self.__largura = 0
        self.__altura = 0
        self.__qtd_botao = 0




    def criar_botao(self, painel, posicao_x, posicao_y, largura, altura):


        self.__posicao_x = posicao_x + painel.get_posicao_x() + painel.get_largura() / 2 - self.__largura / 2
        self.__posicao_y = posicao_y + painel.get_posicao_y() + painel.get_altura() / 2 - self.__altura / 2
        self.__largura = (painel.get_largura() / 1000) * (largura * 10)
        self.__altura = (painel.get_altura()/1000)* (altura*10)




    def draw_botao(self, tela, texto):

        self.__botao = pygame.Rect(self.__posicao_x, self.__posicao_y, self.__largura, self.__altura)
        tela.draw_rect(self.get_cor(), self.__botao)


        txt_play = fonte_texto()
        txt_play.set_texto(texto, 'Times new roman')
        txt_play.cria_texto(30, WHITE, 1)
        tela.blit(txt_play.get_surface(), (self.get_posicao_x() +
                                           txt_play.get_tamanho()+5,self.get_posicao_y()))

        self.draw_borda_botao(RED, tela)


    def draw_borda_botao(self, cor, tela):

        borda = [(self.__posicao_x, self.__posicao_y),
                 (self.__posicao_x+self.__largura, self.__posicao_y),
                 (self.__posicao_x+ self.__largura, self.__posicao_y+self.__altura),
                 (self.__posicao_x ,self.__posicao_y+ self.__altura)]

        tela.draw_lines(cor, borda,3)


    def get_cor(self):
        return self.__cor

    def set_cor(self, cor):
        self.__cor = cor

    def get_posicao_x(self):
        return self.__posicao_x

    def set_posicao_x(self, posicao_x):
        self.__posicao_x = posicao_x

    def get_posicao_y(self):
        return self.__posicao_y

    def set_posicao_y(self, posicao_y):
        self.__posicao_y = posicao_y

    def get_largura(self):
        return self.__largura

    def set_largura(self, largura):
        self.__largura = largura

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura

    def get_botao(self):
        return self.__botao

    # verifica colisao entre a posicao do mouse_x_y e o objeto chamado na funcao
    def __colidiu(self, botao):
        if pygame.mouse.get_pos()[0] >= botao.get_posicao_x() and \
                pygame.mouse.get_pos()[0] <= botao.get_posicao_x() + botao.get_largura() and \
                pygame.mouse.get_pos()[1] >= botao.get_posicao_y() and \
                pygame.mouse.get_pos()[1] <= botao.get_posicao_y() + botao.get_altura():
                return True
        else:
            return False

    def evento(self, evento, botao):

        # se o botao que me chamou colidiu faça:
        if self.__colidiu(botao) == True:

            #captura o click do mouse caso ele for apertado
            if evento.type == pygame.MOUSEBUTTONDOWN:
                print("apertou")
                botao.set_cor(RED)


            # captura se o mouse nao esta apertado
            if evento.type == pygame.MOUSEMOTION:
                print("passei pelo botao")
                # caso tudo for verdadeiro ate aqui mude a cor do botao ao passar o mouse por cima do botao
                botao.set_cor(AMARELO)

        if self.__colidiu(botao) == False:
            botao.set_cor(BLACK)





