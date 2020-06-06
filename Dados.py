class Dados:
    def __init__(self, game_loop, botao_play, nave, tela, mapa):
        self.__pontos = 0


        self.__obj_nave = nave
        self.__obj_tela = tela
        self.__obj_mapa = mapa
        self.__obj_botao_play = botao_play
        self.__dados_reset = []
        self.__dados_save = []
        self.__dados_iniciais = True
        self.__game_loop = game_loop


    def get_pontos(self):
        return self.__pontos

    def set_pontos(self, pontos):
        self.__pontos = pontos




    # gera duas listas de dados, uma com dados iniciais e outra com os dados atualizados
    def get_dados(self):

        # tenho que criar outro botao no menu de save para atribuir esse valor quando ele for clicado

        # responsavel por colher os dados  do jogo no momento em que é solicitado para posteriormente efetuar o savegame
        if self.__game_loop == False and self.__obj_botao_play.get_str_botao() == 'IR DENOVO' and self.__obj_botao_play.get_clicou() == True:

            dados_nave = ["nave"], [self.__obj_nave.get_posicao_x(), self.__obj_nave.get_posicao_y()], \
                         [self.__obj_nave.get_altitude()], \
                         [self.__obj_nave.get_angulo_rotacao()], \
                         [self.__obj_nave.get_colidiu_terreno()], \
                         [self.__obj_nave.get_colidiu_area_pouso()], \
                         [self.__obj_nave.get_colidiu_tela()], \
                         [self.__obj_nave.get_rotacionou_dir()], \
                         [self.__obj_nave.get_rotacionou_esq()], \
                         (self.__obj_nave.get_gravidade_lua()), \
                         [self.__obj_nave.get_friccao()], \
                         [self.__obj_nave.get_gravidade_lua() * 2], \
                         #[self.__obj_nave.get_velocidade_x()], \
                         #[self.__obj_nave.get_velocidade_x()]
                         #[self.__obj_nave.get_potencia_propulsor()-00.01]
            self.__dados_save.insert(0, dados_nave)



            dados_pontos_pouso = ["pontos"], [self.get_pontos()]
            self.__dados_save.insert(1, dados_pontos_pouso)

            dados_mapa = ["mapa"], [self.__obj_mapa.get_terreno()]
            self.__dados_save.insert(2, dados_mapa)



            #dados_tela = ["tela"], [self.__obj_tela.get_cronometro()[]]








            print("dados save :", self.__dados_save)
            print("passei no save")

        # responsavel por colher os dados iniciais do jogo para posteriormente efetuar o restart
        if self.__dados_iniciais == True :

            dados_nave = ["nave"], [self.__obj_nave.get_posicao_x(), self.__obj_nave.get_posicao_y()], \
                         [self.__obj_nave.get_altitude()], \
                         [self.__obj_nave.get_angulo_rotacao()], \
                         [self.__obj_nave.get_colidiu_terreno()], \
                         [self.__obj_nave.get_colidiu_area_pouso()], \
                         [self.__obj_nave.get_colidiu_tela()], \
                         [self.__obj_nave.get_rotacionou_dir()], \
                         [self.__obj_nave.get_rotacionou_esq()], \
                         (self.__obj_nave.get_gravidade_lua()), \
                         [self.__obj_nave.get_friccao()], \
                         [self.__obj_nave.get_gravidade_lua() * 2], \


                         #[self.__obj_nave.get_velocidade_x()], \
                         #[self.__obj_nave.get_velocidade_x()]
                         #[self.__obj_nave.get_potencia_propulsor()-00.01]
            self.__dados_reset.insert(0, dados_nave)




            dados_pontos_pouso = ["pontos"], [self.get_pontos()]
            self.__dados_save.insert(1, dados_pontos_pouso)

            dados_mapa = ["mapa"], [self.__obj_mapa.get_terreno()]
            self.__dados_save.insert(2, dados_mapa)

            # dados_tela = ["tela"], [self.__obj_tela.get_cronometro()[]]









            print("dados reset :", self.__dados_reset )
            print("passei no reset")
            self.__dados_iniciais = False


    # retorna a informacao de acordo com o nome do objeto e o indice da informacao
    def get_info(self, in_loop, nome_objeto, posicao_informacao):


        if nome_objeto == 'nave':
            nome_objeto = 0

            if in_loop == True:
                #print("passei no save")
                return  self.__dados_save[nome_objeto][posicao_informacao]
            if in_loop == False:
                #print("passei no reset")
                return self.__dados_reset[nome_objeto][posicao_informacao]


        if nome_objeto == 'pontos':

            nome_objeto = 1

            if in_loop == True:
                return self.__dados_save[nome_objeto][posicao_informacao]
            if in_loop == False:
                return self.__dados_reset[nome_objeto][posicao_informacao]




    def reset_game(self):
        self.__obj_nave.set_posicao((self.get_info(False, 'nave', 1)[0]), (self.get_info(False, 'nave', 1)[1]))
        self.__obj_nave.set_altitude(self.get_info(False, 'nave', 2))
        #self.__obj_nave.set_angulo_rotacao(self.get_info(False, 'nave', 3))
        self.__obj_nave.set_angulo_rotacao(0)

        #atualiza sozinho ao nave ser realocada, nao precisa
        self.__obj_nave.set_colidiu_terreno(self.get_info(False, 'nave', 4))
        #atualiza sozinho ao nave ser realocada, nao precisa
        self.__obj_nave.set_colidiu_area_pouso(self.get_info(False, 'nave', 5))
        #atualiza sozinho ao nave ser realocada, nao precisa
        self.__obj_nave.set_colidiu_tela(self.get_info(False, 'nave', 6))

        self.__obj_nave.set_rotacionou_dir(self.get_info(False, 'nave', 7))
        self.__obj_nave.set_rotacionou_esq(self.get_info(False, 'nave', 8))
        self.__obj_nave.set_gravidade_lua(self.get_info(False, 'nave', 9))
        self.__obj_nave.set_friccao(self.get_info(False, 'nave', 9))
        self.__obj_nave.set_velocidade_rotacao(self.get_info(False, 'nave', 10))



        self.__obj_mapa.reset()
        self.__obj_mapa.desenha_terreno(self.__obj_tela, self.__obj_nave)


        # CONCERTAR ESSES
        #self.__obj_nave.set_velocidade_x(self.get_info(False, 'nave', 11))
        #self.__obj_nave.set_velocidade_y(self.get_info(False, 'nave', 12))
        # self.__obj_nave.set_potencia_propulsor(self.get_info(False, 'nave', 11))
        # self.__obj_nave.update()

