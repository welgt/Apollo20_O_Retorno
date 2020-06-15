from Nave import *
from Tela import *
from Mapa import *
from Interface import *
from Item import *

import pygame
pygame.init()

tela = Tela("Menu", (1000, 600))

mapa = Mapa_do_jogo()
mapa.set_cor_terreno(WHITE)
mapa.set_cor_borda_terreno(GREEN)

nave = Nova_nave('arquivos/nave.png', tela.get_resolucao()[0] / 2, 100)
nave.set_altitude(abs(nave.get_posicao_y() - tela.get_resolucao()[1]))
nave.set_posicao_inicial_x(tela.get_resolucao()[0] / 2)
nave.set_posicao_inicial_y(100)

gasolina = Item('arquivos/gasolina.png', tela.get_resolucao()[0] / 2, - 100)
gasolina.set_velocidade_x(0)
gasolina.set_velocidade_y(0)
gasolina.set_posicao_inicial_x(tela.get_resolucao()[0] / 2)
gasolina.set_posicao_inicial_y(- 100)

terra = Nova_nave('arquivos/terra3.png', 800, 50)

painel_menu = painel()
painel_menu.set_ativo(True)
painel_config = painel()
painel_config.set_ativo(False)
painel_sair = painel()
painel_sair.set_ativo(False)
painel_hud = painel()

botao_play = botao()
botao_play.set_str_botao('PLAY')
botao_exit = botao()
botao_confg = botao()
botao_save = botao()
botao_voltar = botao()
botao_sim = botao()
botao_nao = botao()
botao_slider_volume_ambiente = botao()
botao_bola_slider_volume_ambiente = botao()
botao_full_scren = botao()

texto_velocidade_nave_hud = fonte_texto()
texto_combustivel_hud = fonte_texto()
texto_altitude_hud = fonte_texto()
texto_angulo_nave_hud = fonte_texto()
texto_pontos_hud = fonte_texto()
texto_msg_usuario_hud = fonte_texto()
texto_volume_ambiente = fonte_texto()
texto_fullscreen = fonte_texto()
texto_exit = fonte_texto()
texto_feedback_pouso_hud = fonte_texto()
texto_feedback_pouso_hud.set_str('')



debug = False
jogoAtivo = True
config = False
nova_resolucao = False

pos_bola_slider_volume = 0
nave.set_volume_propulsor(0.3)

save = False
carregar_save = False
reiniciar = False
marca_save = 0
cor_texto_botao_save = WHITE
liberar_decolagem = 0
pousou = False

dados = Dados(tela, mapa, nave, gasolina)

#captura o evento do botoes que sao tratados na sua propria classe
def evento_botoes():
    botao().evento(event, botao_play, painel_menu)
    botao().evento(event, botao_exit, painel_menu)
    botao().evento(event, botao_confg, painel_menu)
    botao().evento(event, botao_save, painel_menu)
    botao().evento(event, botao_voltar, painel_config)
    botao().evento(event, botao_bola_slider_volume_ambiente, painel_config)
    botao().evento(event, botao_full_scren, painel_config)
    botao().evento(event, botao_sim, painel_sair)
    botao().evento(event, botao_nao, painel_sair)



# funcina como repercusao, se nao sorteio a area de pouso, volte aqui!
def redesenha_mapa():
    mapa.reiniciar()
    mapa.desenha_terreno(tela, nave)



def libera_decolagem(liberar_decolagem):
    pousou = True
    if liberar_decolagem >= 15:
        texto_feedback_pouso_hud.set_str('DECOLAGEM LIBERADA!')
        nave.set_posicao_y(nave.get_posicao_y() - 2)
        randon = random.randint(0, 255)
        mapa.set_cor_terreno((randon, randon, 0))

        if liberar_decolagem > 20:
            mapa.set_cor_terreno(RED)

        if liberar_decolagem == 30:
            mapa.reiniciar()
            mapa.desenha_terreno(tela, nave)
            mapa.set_cor_terreno(WHITE)
            pousou = False

        return pousou



def reinicia_menu():
    texto_feedback_pouso_hud.set_str('VOCÊ MORREU')
    nave.set_vida(0)
    botao_play.set_str_botao('IR DENOVO')
    painel_menu.set_ativo(True)

    texto_msg_usuario_hud.cria("Game Over", 'Times new roman', int(tela.get_proporcao()[1] * 100), WHITE)
    tela.blit(texto_msg_usuario_hud.get_surface(), (tela.get_resolucao()[0] / 2 - texto_msg_usuario_hud.get_largura()/2,
              int(tela.get_proporcao()[1]*100)))





while jogoAtivo:

    #pos_bola_slider_volume = - botao_slider_volume_ambiente.get_posicao_x()/2 + 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogoAtivo = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                painel_menu.set_ativo(True)

                tela.set_game_loop(False)
                botao_play.set_str_botao('PAUSADO')

            elif event.key == pygame.K_LEFT:
                nave.set_rotacionou_esq(True)

            elif event.key == pygame.K_RIGHT:
                nave.set_rotacionou_dir(True)

            elif event.key == pygame.K_UP:
                nave.set_propulsor_ativo(True)

            elif event.key == pygame.K_DOWN:
                pass
            elif event.key == pygame.K_s:
                # debug = True
                # save = True
                pass

            elif event.key == pygame.K_r:
                # debug = True
                # carregar_save = True
                pass

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                nave.set_rotacionou_dir(False)
                nave.set_rotacionou_esq(False)

            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                nave.set_propulsor_ativo(False)

            elif event.key == pygame.K_UP or event.key == pygame.K_s:
                # debug = False
                # save = False
                pass

            elif event.key == pygame.K_UP or event.key == pygame.K_r:
                # debug = False
                # carregar_save = False
                pass

            elif event.key == pygame.K_UP or event.key == pygame.K_ESCAPE:
                pass

    tela.fill(BLACK)

    # PAINEL MENU
    if painel_menu.get_ativo() == True:
        painel_menu.cria(tela, 0, 0, 40, 45)
        painel_menu.draw_painel(tela, AMARELO, 120)

        botao_play.criar(painel_menu, 0, -70, 30, 10)
        botao_play.draw(tela, botao_play.get_str_botao(), WHITE)

        botao_save.criar(painel_menu, 0, -23, 30, 10)
        botao_save.draw(tela, botao_save.get_str_botao(), cor_texto_botao_save)

        botao_confg.criar(painel_menu, 0, 23, 30, 10)
        botao_confg.draw(tela, 'CONFIG', WHITE)

        botao_exit.criar(painel_menu, 0, 70, 30, 10)
        botao_exit.draw(tela, 'EXIT', WHITE)

        evento_botoes()

    # PAINEL CONFIG
    if painel_config.get_ativo() == True:
        painel_config.cria(tela, 0, 0, 40, 45)
        painel_config.draw_painel(tela, AMARELO, 120)

        botao_voltar.criar(painel_config, 0, tela.get_proporcao()[1] * 180, 30, 10)
        botao_voltar.draw(tela, 'VOLTAR', WHITE)

        botao_slider_volume_ambiente.criar(painel_config, 0, -tela.get_proporcao()[1] * 100, 50, 3)
        botao_slider_volume_ambiente.draw(tela, '-                       +', WHITE)

        #print("texto_volume_ambiente largura: ", texto_volume_ambiente.get_largura())
        texto_volume_ambiente.cria("VOLUME AMBIENTE", 'Times new roman', int(tela.get_proporcao()[0] * 15), WHITE)
        tela.blit(texto_volume_ambiente.get_surface(),
                  (tela.get_resolucao()[0] / 2 - texto_volume_ambiente.get_largura() / 2,
                   botao_slider_volume_ambiente.get_posicao_y() + botao_bola_slider_volume_ambiente.get_altura()))

        # pos_bola_slider_volume = -botao_slider_volume_ambiente.get_posicao_x() / 2 + botao_bola_slider_volume_ambiente.get_largura() * 2 + 20
        botao_bola_slider_volume_ambiente.criar(painel_config, pos_bola_slider_volume,
                                                -tela.get_proporcao()[1] * 100, 6, 5)
        botao_bola_slider_volume_ambiente.draw(tela, '', WHITE)

        botao_full_scren.criar(painel_config, -tela.get_proporcao()[0] * 80, tela.get_proporcao()[1] * 20, 3, 5)
        botao_full_scren.draw(tela, '', AMARELO)

        texto_fullscreen.cria('FULLSCREEN', 'Times new roman', int(tela.get_proporcao()[0] * 15),
                              botao_full_scren.get_cor())
        tela.blit(texto_fullscreen.get_surface(), (
            tela.get_resolucao()[0] / 2 - texto_fullscreen.get_largura() / 2, botao_full_scren.get_posicao_y()))

        evento_botoes()

    # PAINEL CERTEZA DE SAIR
    if painel_sair.get_ativo() == True:
        painel_sair.cria(tela, 0, 0, 50, 20)
        painel_sair.draw_painel(tela, WHITE, 120)

        texto_exit.cria("Você tem certeza que quer sair do jogo?", 'Times new roman',
                        int(tela.get_proporcao()[0] * 30), WHITE)
        tela.blit(texto_exit.get_surface(), (tela.get_resolucao()[0] / 2 - texto_exit.get_largura() / 2, 110))

        botao_sim.criar(painel_sair, -tela.get_proporcao()[0] * 120, 0, 30, 30)
        botao_sim.draw(tela, 'SIM', WHITE)

        botao_nao.criar(painel_sair, tela.get_proporcao()[0] * 120, 0, 30, 30)
        botao_nao.draw(tela, 'NÃO', WHITE)

        evento_botoes()

    # HUD
    if painel_hud.get_ativo() == True:

        painel_hud.cria(tela, 0, -tela.get_resolucao()[1] / 2 + 30, 98, int(tela.get_proporcao()[1] * 10))
        painel_hud.draw_painel(tela, WHITE, 120)

        if tela.get_cronometro()[4] < 4:
            temp = 3
            temp -= tela.get_cronometro()[4]

            texto_msg_usuario_hud.cria(" {0:4.4s} ".format(str(temp)), 'Times new roman', int(tela.get_proporcao()[1] * 100), WHITE)
            tela.blit(texto_msg_usuario_hud.get_surface(), (tela.get_resolucao()[0] / 2
                                                                    - texto_msg_usuario_hud.get_tamanho_letra() / 2,
                                                                    tela.get_resolucao()[1] / 2 - texto_msg_usuario_hud.get_tamanho_letra() / 2))

        pos_textos = tela.get_resolucao()[0] / 5

        texto_velocidade_nave_hud.cria("Velocidade: {0:3.4s} ".format(str(abs(nave.get_velocidade_media()))),
            'Times new roman', int(tela.get_proporcao()[0] * 20), BLACK)

        tela.blit(texto_velocidade_nave_hud.get_surface(), (painel_hud.get_posicao_x(), painel_hud.get_posicao_y()))

        texto_combustivel_hud.cria("Combustivel: {0:4.4s} L. ".format(str(nave.get_combustivel())), 'Times new roman',
                                   int(tela.get_proporcao()[0] * 20), BLACK)

        tela.blit(texto_combustivel_hud.get_surface(), (
            painel_hud.get_posicao_x() + tela.get_proporcao()[0] + pos_textos * 1, painel_hud.get_posicao_y()))

        texto_altitude_hud.cria("Altitude : {0:4.5s} ".format(str(nave.get_altitude())), 'Times new roman',
                                int(tela.get_proporcao()[0] * 20), BLACK)

        tela.blit(texto_altitude_hud.get_surface(), (
            painel_hud.get_posicao_x() + tela.get_proporcao()[0] + pos_textos * 2, painel_hud.get_posicao_y()))

        texto_angulo_nave_hud.cria("Angulo nave : {0:4.4s} ".format(str(abs(nave.get_angulo_rotacao()))),
            'Times new roman', int(tela.get_proporcao()[0] * 20), BLACK)

        tela.blit(texto_angulo_nave_hud.get_surface(), (
            painel_hud.get_posicao_x() + tela.get_proporcao()[0] + pos_textos * 3, painel_hud.get_posicao_y()))

        texto_pontos_hud.cria("Pontos : {0:4.4s} ".format(str(dados.get_pontos())), 'Times new roman',
                              int(tela.get_proporcao()[0] * 20), BLACK)

        tela.blit(texto_pontos_hud.get_surface(), (
            painel_hud.get_posicao_x() + tela.get_proporcao()[0] + pos_textos * 4, painel_hud.get_posicao_y()))

        texto_feedback_pouso_hud.cria(texto_feedback_pouso_hud.get_str(), 'Times new roman',
                                      int(tela.get_proporcao()[0] * 10), WHITE)

        if tela.get_game_loop() == True:
            tela.blit(texto_feedback_pouso_hud.get_surface(), (nave.get_posicao_x() + nave.get_largura_x() / 2
                                                               - texto_feedback_pouso_hud.get_largura() / 2, nave.get_posicao_y() - tela.get_proporcao()[1] * 20))

        evento_botoes()


    # GERENTE DO MENU
    if botao_full_scren.get_clicou() == True:
        tela.set_resolucao((pygame.display.list_modes()[0][0], pygame.display.list_modes()[0][1] - 38))
        painel_menu.set_ativo(False)
        tela.fill(0)
        tela.flip()
        evento_botoes()

    if tela.get_resolucao()[0] == pygame.display.list_modes()[0][0]:
        botao_full_scren.set_cor(AMARELO)

    #if botao_full_scren.get_clicou() == True and tela.get_resolucao()[1] <= pygame.display.list_modes()[0][1]:
     #   tela.set_resolucao((1000, 600))

    if botao_play.get_clicou() == True and botao_play.get_str_botao() == 'PLAY':
        tela.set_game_loop(True)
        painel_menu.set_ativo(False)
        painel_hud.set_ativo(True)
    elif botao_play.get_clicou() == True and botao_play.get_str_botao() == 'PAUSADO':
        tela.set_game_loop(True)
        painel_menu.set_ativo(False)

    if botao_save.get_clicou() == True and botao_save.get_str_botao() == 'SAVE VAZIO':
        botao_save.set_str_botao('VOCE DEVE PRIMEIRO JOGAR UMA VEZ!')
        botao_save.set_cor(GREEN)
        cor_texto_botao_save = RED
    else:
        cor_texto_botao_save = WHITE

    if botao_save.get_clicou() == True and botao_play.get_str_botao() == 'PAUSADO':
        marca_save = 1
        mapa.salvar()
        nave.salvar()
        gasolina.salvar()
        save = True

    if botao_save.get_clicou() == True and botao_save.get_str_botao() == 'JOGAR SAVE' and \
            botao_play.get_str_botao() == 'IR DENOVO' and marca_save == 1:
            painel_menu.set_ativo(False)
            texto_feedback_pouso_hud.set_str('')
            mapa.carregar_save()
            nave.carregar_save()
            gasolina.carregar_save()
            carregar_save = True

    if botao_play.get_clicou() == True and botao_play.get_str_botao() == 'IR DENOVO':
        tela.set_game_loop(True)
        mapa.reiniciar()
        nave.reiniciar()
        gasolina.reiniciar()
        texto_feedback_pouso_hud.set_str('')
        botao_play.set_str_botao('PLAY')

    if painel_menu.get_ativo() == True:
        if marca_save == 0:
            botao_save.set_str_botao('SAVE VAZIO')

        if marca_save == 1:
            botao_save.set_str_botao('JOGAR SAVE')

        if marca_save == 1 and botao_play.get_str_botao() == 'PLAY':
            botao_save.set_str_botao('JOGAR SAVE')

        if marca_save == 0 and botao_play.get_str_botao() == 'PAUSADO':
            botao_save.set_str_botao('SALVAR')

        elif marca_save == 1:
            botao_save.set_str_botao('JOGAR SAVE')

        if marca_save == 1 and botao_play.get_str_botao() == 'PAUSADO':
            botao_save.set_str_botao('SALVO')
            save = False

        if marca_save == 1 and botao_save.get_str_botao() == 'SALVO':
            botao_save.set_str_botao('RESALVAR')

    if botao_confg.get_clicou() == True:
        painel_menu.set_ativo(False)
        painel_config.set_ativo(True)
        tela.set_game_loop(False)

    if botao_bola_slider_volume_ambiente.get_clicou() == True:

        if botao_bola_slider_volume_ambiente.get_posicao_x() >= botao_slider_volume_ambiente.get_posicao_x() and \
            botao_bola_slider_volume_ambiente.get_posicao_x() <= botao_slider_volume_ambiente.get_posicao_x() + \
            botao_slider_volume_ambiente.get_largura() - botao_bola_slider_volume_ambiente.get_largura():
                pos_bola_slider_volume = pygame.mouse.get_pos()[0] - tela.get_resolucao()[0] / 2

    if botao_voltar.get_clicou() == True:
        painel_config.set_ativo(False)
        painel_menu.set_ativo(True)

    if botao_exit.get_clicou() == True:
        painel_sair.set_ativo(True)
        painel_config.set_ativo(False)
        painel_menu.set_ativo(False)
        tela.set_game_loop(False)

    if botao_sim.get_clicou() == True:
        jogoAtivo = False
        tela.set_game_loop(False)

    if botao_nao.get_clicou() == True:
        painel_menu.set_ativo(True)
        painel_sair.set_ativo(False)
        painel_config.set_ativo(False)


    # GAMEPLAY
    if tela.get_game_loop() == True:


        #box_surface_polygon = pygame.Surface((500, 300), pygame.SRCALPHA)
        #pygame.draw.polygon(box_surface_polygon, (255, 255, 255, 200), ((25, 0), (0, 25), (25, 50), (50, 25)))

        #tela.draw_polygon(self.get_cor_terreno(), self.__terreno)

        tela.cronometro()

        # só inicia apos 3 segundos
        if tela.get_cronometro()[4] > 3:

            if save == False:
                mapa.desenha_terreno(tela, nave)
                if mapa.get_existe_area_pouso() == False:
                    redesenha_mapa()
                    print("NAO FOI POSSIVEL SORTEAR UMA AREA DE POUSO, REDESENHANDO TERRENO [RANDON]")


            gasolina.set_tamanho(int(tela.get_proporcao()[0] * 15), int(tela.get_proporcao()[1] * 30))
            gasolina.set_volume_item(pos_bola_slider_volume)
            terra.set_tamanho(int(tela.get_proporcao()[0] * 180), int(tela.get_proporcao()[0] * 180))
            nave.set_tamanho(int(tela.get_proporcao()[0] * 18),
                             int(tela.get_proporcao()[1] * 50))

            print("pos_bola_slider_volume :",pos_bola_slider_volume)
            nave.set_friccao(5)
            nave.set_velocidade_rotacao(nave.get_gravidade_lua() * 2)
            nave.set_volume_propulsor(pos_bola_slider_volume)
            nave.set_volume_explosao(pos_bola_slider_volume- 0.5)
            nave.set_altitude(abs(nave.get_posicao_y() - tela.get_resolucao()[1]))
            nave.update()
            nave.verifica_colisao_tela(tela)
            nave.verifica_colisao_area_pouso(mapa)
            nave.verifica_colisao_terreno(mapa)
            gasolina.verifica_colisao_nave(nave)
            gasolina.verifica_colisao_terreno(mapa)

            # GRAVIDADE
            nave.gravidade(tela)
            gasolina.gravidade(tela)

            # ACELERACAO do propulsor
            nave.aceleracao_propulsor(tela)

            if nave.get_combustivel() == 500:
                gasolina.posicao_randomica(tela)
                gasolina.set_velocidade_y(1)

            # so sorteia se caso  a gasolina  esta aguardando em cima da tela
            sort = random.randint(0, 200)
            if nave.get_combustivel() < 500 and sort == 100 and gasolina.get_posicao_y() < -gasolina.get_altura_y()-10:
                gasolina.posicao_randomica(tela)
                gasolina.set_velocidade_y(1)


            if gasolina.get_colidiu_nave() == True:
                if nave.get_combustivel() + 300 <= 1000:
                    nave.set_combustivel(nave.get_combustivel() + 300)
                    gasolina.set_posicao_y(-gasolina.get_altura_y() - 10)
                    gasolina.set_velocidade_y(0)


            if gasolina.get_colidiu_terreno() == True:
                gasolina.set_velocidade_y(0)


            # se a nave pousou verifique as condicoes e atribua a pontuacao correta
            # verificacao antecipada distingue se pousou na area de pouso, pois de fato ela tbm colide com o terreno
            if nave.get_colidiu_area_pouso() == False and nave.get_potencia_propulsor() > 0.4 and nave.get_posicao_y() < mapa.get_maior_altura_terreno()-80:
                texto_feedback_pouso_hud.set_str('')
                liberar_decolagem = 0


            # o jogador é obrigado a decolar a partir do momento em que ele pousou, ele estara seguro só apos subir acima do topo do terreno
            if texto_feedback_pouso_hud.get_str() == '' and pousou == True and nave.get_posicao_y() < mapa.get_maior_altura_terreno()-80:
                mapa.reiniciar()
                mapa.desenha_terreno(tela, nave)
                mapa.set_cor_terreno(WHITE)
                pousou = False


            dados.set_pontos(texto_feedback_pouso_hud.get_str())
            if nave.get_colidiu_area_pouso() == False:
                dados.set_cont(0)


            if nave.get_colidiu_tela() == True:

                reinicia_menu()
                # seta intensidade da explosa, circunferencia e tempo
                nave.explodir(tela, 10, 25, 20)


            if nave.get_colidiu_area_pouso() == True and nave.get_verifica_colisao_antecipada() == True:
                nave.set_angulo_rotacao(nave.get_angulo_rotacao())

                # verifica o pouso e gera a pontuacao
                if nave.get_angulo_rotacao() <= 10 and nave.get_angulo_rotacao() >= -10:
                    texto_feedback_pouso_hud.set_str('POUSO PERFEITO')
                    liberar_decolagem += 1
                    pousou = libera_decolagem(liberar_decolagem)

                elif nave.get_angulo_rotacao() <= 20 and nave.get_angulo_rotacao() >= -20:
                    texto_feedback_pouso_hud.set_str('POUSO TOLERÁVEL')
                    liberar_decolagem += 1
                    pousou = libera_decolagem(liberar_decolagem)

                elif nave.get_angulo_rotacao() <= 35 and nave.get_angulo_rotacao() >= -35:
                    texto_feedback_pouso_hud.set_str('POUSO FORÇADO')
                    liberar_decolagem += 1
                    pousou = libera_decolagem(liberar_decolagem)

                else:

                    reinicia_menu()
                    nave.explodir(tela, 10, 25, 20)
                    #tela.set_game_loop(False)
                    pousou = False



            if nave.get_colidiu_terreno() == True:
                reinicia_menu()
                # seta intensidade da explosa, circunferencia e tempo
                nave.explodir(tela,10, 25, 20)
                mapa.set_cor_borda_terreno(CYAN)

            else:
                mapa.set_cor_borda_terreno(AMARELO)



            # so adiciona angulo do lado esquerdo da nave se for o grau maximo permitido de 90
            if nave.get_rotacionou_esq() and nave.get_angulo_rotacao() <= 90:
                nave.set_angulo_rotacao(nave.get_angulo_rotacao() + nave.get_velocidade_rotacao())

            # so adiciona angulo do lado direito da nave se for o grau maximo permitido de 90
            if nave.get_rotacionou_dir() and nave.get_angulo_rotacao() >= -90:
                nave.set_angulo_rotacao(nave.get_angulo_rotacao() - nave.get_velocidade_rotacao())


            # cria poligono propulsor e recebe tamanho da calda
            poligono_propulsor_dir = nave.criaPoligono_Propulsor(nave.get_largura_x() / 10, nave.get_largura_x() / 4.5,
                                                                 nave.get_potencia_propulsor() * tela.get_fps())

            poligono_propulsor_esq = nave.criaPoligono_Propulsor(nave.get_largura_x() / 10, -nave.get_largura_x() / 5,
                                                                 nave.get_potencia_propulsor() * tela.get_fps())

            # rotaciona a (imagem) nave
            nave_rot = nave.rotacaoCentralizada()

            tela.blit(terra.get_surface(), terra.get_posicao())
            tela.blit(nave_rot[0], nave_rot[1])
            tela.draw_polygon(CYAN, poligono_propulsor_dir)
            tela.draw_polygon(CYAN, poligono_propulsor_esq)
            tela.blit(gasolina.get_surface(), (gasolina.get_posicao_x(), gasolina.get_posicao_y()))


    tela.flip()
    tela.set_fps(30)

    if debug:
        # print("config :", botao_confg.get_mouse_cont())
        # print("play   :", botao_play.get_mouse_cont())
        # print("exit   :", botao_exit.get_mouse_cont())
        # print("voltar :", botao_voltar.get_mouse_cont())

        # print("botao play ativo   :", botao_play.get_clicou())
        # print("botao config ativo :", botao_confg.get_clicou())
        # print("botao exit ativo   :", botao_exit.get_clicou())
        # print("botao voltar ativo :", botao_voltar.get_clicou())
        # print("str play,:", str_botao_play)
        # print("game_loop :", game_loop)

        # print("painel menu   :", painel_menu.get_ativo())
        # print("painel config :", painel_config.get_ativo())
        # print("painel sair   :", painel_sair.get_ativo())

        # print("pos_bola_slider_volume:", pos_bola_slider_volume / 1000)
        # print("pos mouse oficial  :", pygame.mouse.get_pos()[0])
        # print("pos bola slider    :", botao_bola_slider_volume_ambiente.get_posicao_x())
        # print("posicao slider x :", botao_slider_volume_ambiente.get_posicao_x())
        # print("volume propulsor :", nave.get_volume_propulsor())

        # print("colisao terreno:", nave.get_colidiu_terreno())
        # print("colisao pouso  :", nave.get_colidiu_area_pouso())
        # print("colisao antecip:", nave.get_verifica_colisao_antecipada())

        # print("vida", nave.get_vida())
        # print("game loop", tela.get_game_loop())
        # print("botao play:", botao_play.get_str_botao())

        # print("altitude reiniciar :", dados.get_info(False, 'nave', 2))
        # print("angulo rotacao :", dados.get_info(False, 'nave', 3))

        # print("angulo rotacao :", nave.get_angulo_rotacao())
        # print("colidiu terreno :", dados.get_info(False, 'nave', 4))

        # print(texto_feedback_pouso_hud.get_str())
        # print("game_loop :", tela.get_game_loop())
        pass

pygame.quit()
