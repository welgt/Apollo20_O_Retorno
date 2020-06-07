class Dados:
    def __init__(self,tela, mapa, nave, item_gasolina):
        self.__pontos = 0


        self.__obj_nave = nave
        self.__obj_tela = tela
        self.__obj_mapa = mapa
        self.__obj_item_gasolina = item_gasolina






 #[self.__obj_nave.get_posicao_x(), self.__obj_nave.get_posicao_y()], \
 #[self.__obj_nave.get_altitude()], \
 #[self.__obj_nave.get_angulo_rotacao()], \
 #[self.__obj_nave.get_colidiu_terreno()], \
 #[self.__obj_nave.get_colidiu_area_pouso()], \
 #[self.__obj_nave.get_colidiu_tela()], \
 #[self.__obj_nave.get_rotacionou_dir()], \
 #[self.__obj_nave.get_rotacionou_esq()], \
 #(self.__obj_nave.get_gravidade_lua()), \
 #[self.__obj_nave.get_friccao()], \
 #[self.__obj_nave.get_gravidade_lua() * 2], \
 #(self.__obj_nave.get_combustivel())
 #[self.get_pontos()]
 #[self.__obj_mapa.get_terreno()]
 #[self.__obj_item_gasolina.get_posicao_x(), self.__obj_item_gasolina.get_posicao_x()]



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








    #def reset_game(self):





    #def save_game(self):

        #self.__obj_mapa.copia(self.__obj_tela)
        #self.__obj_mapa.set_terreno(self.__obj_mapa.get_copia_vertices_terreno())






    #def reload_game(self):

        #self.__obj_mapa.copia(self.__obj_tela)
        #self.__obj_mapa.set_terreno(self.__obj_mapa.get_copia_vertices_terreno())





    def get_pontos(self):
        return self.__pontos

    def set_pontos(self, pontos):
        self.__pontos = pontos