from pygame import font
from Tela import *

class fonte_texto:
    def __init__(self):
        pygame.font.init()
        self.__largura = 0
        self.__altura  = 0
        self.__font = None
        self.__texto = None
        self.__tamanho_fonte = 0
        self.__altura = 0
        self.__largura = 0





    def cria(self, texto, fonte, tamanho_fonte, cor ):
        font = pygame.font.SysFont(fonte, tamanho_fonte, True, False)
        text = font.render(texto, True, cor)
        self.__font = font
        self.__texto = text
        self.__largura = self.__texto .get_rect()[2]
        self.__altura  = self.__texto .get_rect()[3]
        self.set_surface(text)
        self.set_tamanho_fonte(tamanho_fonte)


    def set_tamanho(self, novo_largura, novo_altura):
        self.set_surface(pygame.transform.scale(self.get_surface(), novo_largura, novo_altura))

    def get_largura(self):
        return self.__largura

    def get_altura(self):
        return self.__altura

    def set_tamanho_fonte(self, tamanho):
        self.__tamanho_fonte = tamanho

    def get_tamanho_letra(self):
        return self.__tamanho_fonte

    def get_texto(self):
        return self.__texto

    def get_fonte(self):
        return self.__tipo_fonte

    def set_fonte(self, fonte):
        self.__tipo_fonte = fonte

    def set_surface(self, surface):
        self.__surface = surface

    def get_surface(self):
        return self.__surface

    def get_largura(self):
        return self.__largura

    def set_largura(self, largura):
        self.__largura = largura

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura

    def set_cor(self, cor):
        self.__cor = cor

    def get_cor(self):
        return self.__cor

    def get_posicao_x(self):
        return self.__posicao_x

    def set_posicao_x(self, posicao):
        self.__posicao_x = posicao

    def get_posicao_y(self):
        return self.__posicao_y

    def set_posicao_y(self, posicao):
        self.__posicao_y = posicao

    def get_centro(self):
        return self.__texto.get_rect().center





class painel:
    def __init__(self):
        self.__painel = None
        self.__cor = 0
        self.__posicao_x = 0
        self.__posicao_y = 0
        self.__largura = 0
        self.__altura = 0
        self.__ativo = False
        self.__opacidade = 100
        self.__borda_botao = None


    def get_ativo(self):
        return self.__ativo

    def set_ativo(self, ativo):
        self.__ativo = ativo

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

    def get_opacidade(self):
        return self.__opacidade

    def set_opacidade(self, opacidade):
        self.__opacidade = opacidade



    def cria(self, tela, posicao_x, posicao_y, largura, altura):
        self.__posicao_x = posicao_x + tela.get_resolucao()[0] / 2 - self.__largura / 2
        self.__posicao_y = posicao_y + tela.get_resolucao()[1] / 2 - self.__altura / 2
        self.__largura = (tela.get_resolucao()[0] / 1000) * (largura * 10)
        self.__altura = (tela.get_resolucao()[1] / 1000) * (altura * 10)

       

    def draw_painel(self, tela, cor, opacidade):

        self.__painel = pygame.Surface((self.__largura, self.__altura))
        self.set_opacidade(opacidade)
        self.__painel.set_alpha(self.get_opacidade())
        self.set_cor(cor)
        self.__painel.fill(self.get_cor())

        if self.get_ativo()== True:
            #tela.draw_rect(cor, self.__painel)
            tela.blit(self.__painel,(self.__posicao_x, self.__posicao_y))
            self.__draw_borda(tela, AMARELO)

    def __draw_borda(self, tela, cor):
        self.__borda_botao = [(self.__posicao_x, self.__posicao_y),
                 (self.__posicao_x + self.__largura, self.__posicao_y),
                 (self.__posicao_x + self.__largura, self.__posicao_y + self.__altura),
                 (self.__posicao_x, self.__posicao_y + self.__altura)]
        tela.draw_lines(cor, self.__borda_botao, 3)



class botao:

    def __init__(self):
        self.__botao = None
        self.__cor = 0
        self.__posicao_x = 0
        self.__posicao_y = 0
        self.__largura = 0
        self.__altura = 0
        self.__qtd_botao = 0
        self.__clicou = False
        self.__mouse_cont = 0
        self.__som_botao = pygame.mixer.music
        self.__area_colisao = False


    def get_volume(self):
        return self.__som_botao.get_volume()

    def set_volume(self, volume):
        self.__som_botao.set_volume(volume)

    def get_mouse_cont(self):
        return self.__mouse_cont

    def set_mouse_cont(self, int):
        self.__mouse_cont = int

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

    def get_clicou(self):
        return self.__clicou

    def set_clicou(self, clicou):
        self.__clicou = clicou





    def criar(self, painel, posicao_x, posicao_y, largura, altura):

        self.__posicao_x = posicao_x + painel.get_posicao_x() + painel.get_largura() / 2 - self.__largura / 2
        self.__posicao_y = posicao_y + painel.get_posicao_y() + painel.get_altura() / 2 - self.__altura / 2
        self.__largura = (painel.get_largura() / 1000) * (largura * 10)
        self.__altura = (painel.get_altura()/1000)* (altura*10)

        self.__colidiu(painel)

    def draw(self, tela, texto):

        self.__botao = pygame.Rect(self.__posicao_x, self.__posicao_y, self.__largura, self.__altura)
        tela.draw_rect(self.get_cor(), self.__botao)

        txt_botao = fonte_texto()
        txt_botao.cria(texto,'Times new roman', int(self.get_largura()/1000*150), WHITE)
        tela.blit(txt_botao.get_surface(), (self.get_posicao_x() + txt_botao.get_tamanho_letra() * 7 / 2 - txt_botao.get_centro()[0],
                                            self.get_posicao_y() ))

        self.__draw_borda(WHITE, tela)


    def __draw_borda(self, cor, tela):

        borda = [(self.__posicao_x, self.__posicao_y),
                 (self.__posicao_x+self.__largura, self.__posicao_y),
                 (self.__posicao_x+ self.__largura, self.__posicao_y+self.__altura),
                 (self.__posicao_x ,self.__posicao_y+ self.__altura)]

        tela.draw_lines(cor, borda,3)



    # verifica colisao entre a posicao do mouse_x_y e o objeto chamado na funcao
    def __colidiu(self, painel):

        if painel.get_ativo() == True:
            if pygame.mouse.get_pos()[0] >= self.get_posicao_x() \
                    and pygame.mouse.get_pos()[0] <= self.get_posicao_x() + self.get_largura() \
                    and pygame.mouse.get_pos()[1] >= self.get_posicao_y() \
                    and pygame.mouse.get_pos()[1] <= self.get_posicao_y() + self.get_altura():

                self.__area_colisao = True
                return True
            else:
                self.__area_colisao = False
                self.set_mouse_cont(0)
                return False




    def evento(self, evento, botao, painel):

        # se o botao que me chamou colidiu faça:
        if botao.__colidiu(painel) == True:
            #self.set_mouse_cont(0)
            #captura o click do mouse caso ele for apertado
            if evento.type == pygame.MOUSEBUTTONDOWN:
                self.__som_botao.load('arquivos/botao.mp3')
                self.__som_botao.set_volume(0.3)
                self.__som_botao.play()
                botao.set_mouse_cont(1)
                botao.set_clicou(True)

            # captura se o mouse nao esta apertado e nesse caso so se for em cima do botao
            if evento.type == pygame.MOUSEMOTION:
                # caso tudo for verdadeiro ate aqui mude a cor do botao ao passar o mouse por cima do botao
                botao.set_cor(AMARELO)
        else:
            botao.set_cor(BLACK)

        if botao.get_clicou() == False:
            botao.set_mouse_cont(0)

        if evento.type == pygame.MOUSEBUTTONUP:
            botao.set_clicou(False)