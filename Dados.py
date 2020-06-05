class Dados:
    def __init__(self, nave):
        self.__pontos = 0


        self.__obj_nave = nave
        self.__dados_reset = []
        self.__dados_save = []
        self.__dados_iniciais = True







    def get_dados(self):


        dados_nave = ["nave"], [self.__obj_nave.get_posicao_x(), (self.__obj_nave.get_posicao_y())]
        self.__dados_save.insert(0, dados_nave)


        dados_pontos_pouso = ["pontos"], [self.get_pontos()]
        self.__dados_save.insert(1, dados_pontos_pouso)


        if self.__dados_iniciais == True :

            dados_nave = ["nave"], [self.__obj_nave.get_posicao_x(), (self.__obj_nave.get_posicao_y())]
            self.__dados_reset.insert(0, dados_nave)

            dados_pontos_pouso = ["pontos"], [self.get_pontos()]
            self.__dados_reset.insert(1, dados_pontos_pouso)
            print("passei")
            self.__dados_iniciais = False



    def get_info(self, in_loop, nome_objeto, posicao_informacao):


        if nome_objeto == 'nave':
            nome_objeto = 0

            if in_loop == True:
                print("passei no save")
                return  self.__dados_save[nome_objeto][posicao_informacao]
            if in_loop == False:
                print("passei no reset")
                return self.__dados_reset[nome_objeto][posicao_informacao]


        if nome_objeto == 'pontos':

            nome_objeto = 1

            if in_loop == True:
                return self.__dados_save[nome_objeto][posicao_informacao]
            if in_loop == False:
                return self.__dados_reset[nome_objeto][posicao_informacao]








    def get_pontos(self):
        return self.__pontos

    def set_pontos(self, pontos):
        self.__pontos = pontos


    def reset_game(self):
        self.__obj_nave.set_posicao((self.get_info(False, 'nave', 1)[0]), (self.get_info(False, 'nave', 1)[1]))
        #self.__obj_nave.set_angulo_rotacao(0)
        #self.__obj_nave.set_colidiu_terreno(False)
        #self.__obj_nave.set_colidiu_area_pouso(False)
