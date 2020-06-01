from Dados import *
from Nave import *
from Mapa import *
from Interface import *
from Config import *


import pygame

pygame.init()

mapa = Mapa_do_jogo()
mapa.set_cor_terreno(WHITE)
mapa.set_cor_borda_terreno(GREEN)

gamePlay = Nova_tela("Menu", (1200,600))

nave = Nova_nave('arquivos/nave.png', gamePlay.get_resolucao()[0]/2, 100)
nave.set_altitude(abs(nave.get_posicao_y()- gamePlay.get_resolucao()[1]))

terra = Nova_nave('arquivos/terra3.png', 800, 50)
#gamePlay.set_resolucao_tela((pygame.display.list_modes()[0][0],pygame.display.list_modes()[0][1]))

painel_menu = painel()
painel_menu.set_ativo(True)
painel_config = painel()
painel_config.set_ativo(False)
painel_sair = painel()
painel_sair.set_ativo(False)
painel_hud = painel()

botao_play = botao()
botao_exit = botao()
botao_confg = botao()
botao_voltar = botao()
botao_sim = botao()
botao_nao = botao()

botao_aumentar_volume_ambiente = botao()
botao_diminuir_volume_ambiente = botao()

texto_botao_play = 'PLAY'
texto_exit = fonte_texto()


def evento_botoes():
    botao().evento(event, botao_play, painel_menu)
    botao().evento(event, botao_exit, painel_menu)
    botao().evento(event, botao_confg, painel_menu)
    botao().evento(event, botao_voltar, painel_config)
    botao().evento(event, botao_sim, painel_sair)
    botao().evento(event, botao_nao, painel_sair)
    botao().evento(event, botao_aumentar_volume_ambiente, painel_config)

    #botao().verifica_colisao()

texto_velocidade_nave_hud = fonte_texto()
texto_combustivel_hud = fonte_texto()
texto_altitude_hud = fonte_texto()
texto_angulo_nave_hud = fonte_texto()
texto_pontos_hud = fonte_texto()
texto_contagem_regressiva_hud = fonte_texto()
texto_volume_mais = fonte_texto()
texto_volume_menos = fonte_texto()


dados = Dados()

game_loop = False
debug = False
jogoAtivo = True
config = False
tempo = 0
nova_resolucao = False
volume_propulsor = 0.1
nave.set_volume_propulsor(volume_propulsor)



while jogoAtivo:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogoAtivo = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                painel_menu.set_ativo(True)



                game_loop = False
                texto_botao_play = 'PAUSADO'


            elif event.key == pygame.K_LEFT:
                nave.set_rotacionou_esq(True)

            elif event.key == pygame.K_RIGHT:
                nave.set_rotacionou_dir(True)

            elif event.key == pygame.K_UP:
                nave.set_propulsor_ativo(True)


            elif event.key == pygame.K_DOWN:
                pass
            elif event.key == pygame.K_d:
                debug = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                nave.set_rotacionou_dir(False)
                nave.set_rotacionou_esq(False)

            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                nave.set_propulsor_ativo(False)


            # debugar
            elif event.key == pygame.K_UP or event.key == pygame.K_d:
                debug = False

            elif event.key == pygame.K_UP or event.key == pygame.K_ESCAPE:
                pass


    gamePlay.fill(BLACK)


    # PAINEL MENU
    if painel_menu.get_ativo() == True:


        painel_menu .cria(gamePlay, 0, 0, 40, 45)
        painel_menu.draw_painel(gamePlay,AMARELO, 120)

        botao_play.criar(painel_menu, 0, -50, 30, 10)
        botao_play.draw(gamePlay, texto_botao_play)
        #botao_play.draw_borda_botao(gamePlay,RED)

        botao_confg.criar(painel_menu, 0, 0, 30, 10)
        botao_confg.draw(gamePlay, 'CONFIG')
        #botao_confg.draw_borda_botao(gamePlay,RED)

        botao_exit.criar(painel_menu, 0, 50, 30, 10)
        botao_exit.draw(gamePlay, 'EXIT')
        #botao_exit.draw_borda_botao(gamePlay,RED)

        evento_botoes()

    # PAINEL CONFIG
    if painel_config.get_ativo()== True:

        painel_config.cria(gamePlay, 0, 0, 40, 45)
        painel_config.draw_painel(gamePlay, AMARELO, 120)

        botao_voltar.criar(painel_config, 0, gamePlay.get_proporcao()[1] * 150, 30, 10)
        botao_voltar.draw(gamePlay, 'VOLTAR')

        botao_aumentar_volume_ambiente.criar(painel_config, 0, gamePlay.get_proporcao()[1] * 15, 5, 5)
        botao_aumentar_volume_ambiente.draw(gamePlay, '+')

        texto_volume_mais.set_texto('+', 'Times new roman')
        texto_volume_mais.cria(int(gamePlay.get_proporcao()[0] * 30), WHITE, 1)
        gamePlay.blit(texto_volume_mais.get_surface(), (botao_aumentar_volume_ambiente.get_posicao_x()+texto_volume_mais.get_largura_palavra()/2 ,
                                                        botao_aumentar_volume_ambiente.get_posicao_y()))

        evento_botoes()




    # PAINEL CERTEZA DE SAIR
    if painel_sair.get_ativo() == True:

        painel_sair.cria(gamePlay, 0, 0, 50, 20)
        painel_sair.draw_painel(gamePlay,WHITE, 120)

        texto_exit.set_texto("Voce tem certeza que quer fechar o jogo?", 'Times new roman')
        texto_exit.cria(int(gamePlay.get_proporcao()[0] * 30), WHITE, 1)
        gamePlay.blit(texto_exit.get_surface(), (painel_sair.get_posicao_x() , 110))


        botao_sim.criar(painel_sair, -gamePlay.get_proporcao()[0] * 120, 0, 30, 30)
        botao_sim.draw(gamePlay, 'SIM')


        botao_nao.criar(painel_sair, gamePlay.get_proporcao()[0] * 120, 0, 30, 30)
        botao_nao.draw(gamePlay, 'NÃO')

        evento_botoes()

    # HUD
    if painel_hud.get_ativo() == True:

        painel_hud.cria(gamePlay, 0, -gamePlay.get_resolucao()[1] / 2 + 30, 98, int(gamePlay.get_proporcao()[1] * 10))
        painel_hud.draw_painel(gamePlay, WHITE, 120)

        if gamePlay.get_cronometro()[2]<4:
            temp = 3
            temp -=gamePlay.get_cronometro()[2]
            texto_contagem_regressiva_hud.set_texto(" {0:4.4s} ".format(str(temp)), 'Times new roman')
            texto_contagem_regressiva_hud.cria(int(gamePlay.get_proporcao()[1] * 100), WHITE, 1)
            gamePlay.blit(texto_contagem_regressiva_hud.get_surface(),
                          (gamePlay.get_resolucao()[0] / 2 - texto_contagem_regressiva_hud.get_tamanho_letra() / 2,
                           gamePlay.get_resolucao()[1] / 2 - texto_contagem_regressiva_hud.get_tamanho_letra() / 2))

        pos_textos = gamePlay.get_resolucao()[0]/5
        texto_velocidade_nave_hud.set_texto("Velocidade: {0:3.4s} ".format(str(abs(nave.get_velocidade_y()))) , 'Times new roman')
        texto_velocidade_nave_hud.cria(int(gamePlay.get_proporcao()[0] * 20), BLACK, 1)
        gamePlay.blit(texto_velocidade_nave_hud.get_surface(), (painel_hud.get_posicao_x(), painel_hud.get_posicao_y()))

        texto_combustivel_hud.set_texto("Combustivel: {0:4.4s} L. ".format(str(nave.get_combustivel())) , 'Times new roman')
        texto_combustivel_hud.cria(int(gamePlay.get_proporcao()[0] * 20), BLACK, 1)
        gamePlay.blit(texto_combustivel_hud.get_surface(), (painel_hud.get_posicao_x() + gamePlay.get_proporcao()[0]+pos_textos*1, painel_hud.get_posicao_y()))


        texto_altitude_hud.set_texto("Altitude : {0:4.5s} ".format(str(nave.get_altitude())) , 'Times new roman')
        texto_altitude_hud.cria(int(gamePlay.get_proporcao()[0] * 20), BLACK, 1)
        gamePlay.blit(texto_altitude_hud.get_surface(), (painel_hud.get_posicao_x()+gamePlay.get_proporcao()[0]+pos_textos*2, painel_hud.get_posicao_y()))

        texto_angulo_nave_hud.set_texto("Angulo nave : {0:4.4s} ".format(str(abs(nave.get_angulo_rotacao()))) , 'Times new roman')
        texto_angulo_nave_hud.cria(int(gamePlay.get_proporcao()[0] * 20), BLACK, 1)
        gamePlay.blit(texto_angulo_nave_hud.get_surface(), (painel_hud.get_posicao_x()+gamePlay.get_proporcao()[0]+pos_textos*3, painel_hud.get_posicao_y()))

        texto_pontos_hud.set_texto("Pontos : {0:4.4s} ".format(str(dados.get_pontos())) , 'Times new roman')
        texto_pontos_hud.cria(int(gamePlay.get_proporcao()[0] * 20), BLACK, 1)
        gamePlay.blit(texto_pontos_hud.get_surface(), (painel_hud.get_posicao_x()+gamePlay.get_proporcao()[0]+pos_textos*4, painel_hud.get_posicao_y()))

        evento_botoes()





    # GERENTE DO MENU
    if botao_play.get_clicou() == True:
        game_loop = True
        painel_menu.set_ativo(False)
        painel_hud.set_ativo(True)


    if botao_confg.get_clicou() == True:
        painel_menu.set_ativo(False)
        painel_config.set_ativo(True)
        game_loop = False


    if botao_voltar.get_clicou() == True:
        painel_config.set_ativo(False)
        painel_menu.set_ativo(True)


    if botao_exit.get_clicou() == True:
        painel_sair.set_ativo(True)
        painel_config.set_ativo(False)
        painel_menu.set_ativo(False)
        game_loop = False

    if botao_sim.get_clicou() == True:
        jogoAtivo = False
        game_loop = False

    if botao_nao.get_clicou() == True:
        painel_menu.set_ativo(True)
        painel_sair.set_ativo(False)


    if botao_aumentar_volume_ambiente.get_clicou() == True:
        volume_propulsor+=0.1



    print("btn volume propulsor ", botao_aumentar_volume_ambiente.get_clicou())
    print("volume: ", nave.get_volume_propulsor())

    #GAMEPLAY
    if game_loop == True:

        gamePlay.cronometro()
        #nave.set_volume_propulsor(nave.get_volume_propulsor())

        if gamePlay.get_cronometro()[2]>3:

            mapa.desenha_terreno(gamePlay, nave)
            if mapa.get_existe_area_pouso() == False:
                mapa.desenha_terreno(gamePlay, nave)
                print("NAO FOI POSSIVEL SORTEAR UMA AREA DE POUSO, REDESENHANDO TERRENO")

            terra.set_tamanho(int(gamePlay.get_proporcao()[0] * 180), int(gamePlay.get_proporcao()[0] * 180))
            nave.set_tamanho(int(gamePlay.get_proporcao()[0] * 18),
                             int(gamePlay.get_proporcao()[1] * 50))

            nave.set_friccao(1)
            nave.set_velocidade_rotacao(nave.get_gravidade_lua())
            nave.set_volume_propulsor(volume_propulsor)

            velocidade_x = nave.get_velocidade_x()
            velocidade_y = nave.get_velocidade_y()
            posicao_x = nave.get_posicao_x()
            posicao_y = nave.get_posicao_y()
            potencia_propulsor = nave.get_potencia_propulsor()
            angulo = nave.get_angulo_rotacao()
            altitude = nave.get_altitude()

            posicao_x += velocidade_x
            posicao_y += velocidade_y





            # so tem velocidade caso nao colidiu com a tela
            if nave.get_colidiu_tela() == False:
                nave.set_posicao(posicao_x, posicao_y)
                nave.set_altitude(nave.get_altitude() - nave.get_velocidade_y())

            nave.verifica_colisao_tela(gamePlay)
            nave.verifica_colisao_area_pouso(mapa)
            nave.verifica_colisao_terreno(mapa, gamePlay)

            # se a nave pousou verifique as condicoes e atribua a pontuacao correta
            if nave.get_colidiu_area_pouso() == True:
                painel_menu.set_ativo(True)
                angulo = nave.get_angulo_rotacao()
                nave.set_angulo_rotacao(angulo)

                if nave.get_angulo_rotacao() <= 15 and nave.get_angulo_rotacao() >= -15:
                    pouso_perfeito = 150
                    dados.set_pontos(pouso_perfeito)

                elif nave.get_angulo_rotacao() <= 25 and nave.get_angulo_rotacao() >= -25:
                    pouso_toleravel = 100
                    dados.set_pontos(pouso_toleravel)

                elif nave.get_angulo_rotacao() <= 35 and nave.get_angulo_rotacao() >= -35:
                    pouso_forcado = 50
                    dados.set_pontos(pouso_forcado)

                else:
                    print("Voce morreu")

            if nave.get_colidiu_terreno() == True:
                print("colidiu", nave.get_colidiu_terreno())
                # painel_menu.set_ativo(True)
                # mapa.set_cor_terreno(CYAN)
                mapa.set_cor_borda_terreno(CYAN)
            else:
                nave.set_colidiu_terreno(False)
                # mapa.set_cor_terreno(MARRON)
                mapa.set_cor_borda_terreno(AMARELO)

            # print("pontos :", dados.get_pontos())
            # futura condicao de dano/perca pontos/morte etc
            # if nave.get_colidiu_tela() == True:
            #   print('colidiu com a a tela')

            # ACELERACAO do propulsor
            nave.aceleracao_propulsor(tempo, gamePlay)
            # GRAVIDADE
            nave.gravidade(tempo, gamePlay)

            # so adiciona angulo do lado esquerdo da nave se for o grau maximo permitido de 90
            if nave.get_rotacionou_esq() and nave.get_angulo_rotacao() <= 90:
                angulo += nave.get_velocidade_rotacao()
                nave.set_angulo_rotacao(angulo)

            # so adiciona angulo do lado direito da nave se for o grau maximo permitido de 90
            if nave.get_rotacionou_dir() and nave.get_angulo_rotacao() >= -90:
                angulo -= nave.get_velocidade_rotacao()
                nave.set_angulo_rotacao(angulo)

            # cria poligono propulsor e recebe tamanho da calda
            poligono_propulsor_dir = nave.criaPoligono_Propulsor(nave.get_largura_x() / 10, nave.get_largura_x() / 4.5,
                                                                 nave.get_potencia_propulsor() * gamePlay.get_fps())

            poligono_propulsor_esq = nave.criaPoligono_Propulsor(nave.get_largura_x() / 10, -nave.get_largura_x() / 5,
                                                                 nave.get_potencia_propulsor() * gamePlay.get_fps())

            # rotaciona a (imagem) nave
            nave_rot = nave.rotacaoCentralizada()

            gamePlay.blit(terra.get_surface(), terra.get_posicao())
            gamePlay.blit(nave_rot[0], nave_rot[1])
            gamePlay.draw_polygon(CYAN, poligono_propulsor_dir)
            gamePlay.draw_polygon(CYAN, poligono_propulsor_esq)

    tempo+=0.1
    gamePlay.flip()
    gamePlay.set_fps(30)


    if debug:
        #print("config :", botao_confg.get_mouse_cont())
        #print("play   :", botao_play.get_mouse_cont())
        #print("exit   :", botao_exit.get_mouse_cont())
        #print("voltar :", botao_voltar.get_mouse_cont())

        #print("botao play ativo   :", botao_play.get_clicou())
        #print("botao config ativo :", botao_confg.get_clicou())
        #print("botao exit ativo   :", botao_exit.get_clicou())
        #print("botao voltar ativo :", botao_voltar.get_clicou())
        #print("game_loop :", game_loop)

        print("painel menu   :", painel_menu.get_ativo())
        print("painel config :", painel_config.get_ativo())
        print("painel sair   :", painel_sair.get_ativo())







pygame.quit()
