
CYAN = (0,255,255)
BLACK = (0, 0, 0)
GREY = (128,128,128)
LARANJA = (255,165,0)
AMARELO = (255,255,0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
MARRON = (184,134,11)


class Dados:
    def __init__(self,tela, mapa, nave, item_gasolina):
        self.__pontos = 0
        self.__obj_nave = nave
        self.__obj_tela = tela
        self.__obj_mapa = mapa
        self.__obj_item_gasolina = item_gasolina

        self.__cont = 0



    def get_pontos(self):
        return self.__pontos

    def set_cont(self, cont):
        self.__cont = cont

    def get_cont(self):
        return self.__cont

    def set_pontos(self, feedback_pouso, nave, mapa):


        if feedback_pouso == 'POUSO PERFEITO' and self.get_cont() == 0:
            self.__pontos  += 150
            self.set_cont(1)

        if feedback_pouso == 'POUSO TOLERÁVEL' and self.get_cont() == 0:
            self.__pontos  += 100
            self.set_cont(1)

        if feedback_pouso == 'POUSO FORÇADO' and self.get_cont() == 0:
            self.__pontos  += 50
            self.set_cont(1)


    def restart_nave(self):

        self.__nave_posicao_x = self.get_posicao_x()
        self.__nave_posicao_y = self.get_posicao_y()
        self.__nave_velocidade_x = 0
        self.__nave_velocidade_y = 0
        self.__nave_velocidade_media = 0
        self.__nave_potencia_propulsor = 0
        self.__nave_friccao = 0
        self.__nave_angulo_rotacao = 0
        self.__nave_velocidade_rotacao = 0
        self.__nave_combustivel = 1000
        self.__nave_gravidade_lua = 5#1.6
        self.__nave_vida = 1


