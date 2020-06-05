from Dados import *
from Nave import *
from Mapa import *
from Interface import *
from Config import *
from Item import *


import pygame

pygame.init()

mapa = Mapa_do_jogo()
mapa.set_cor_terreno(WHITE)
mapa.set_cor_borda_terreno(GREEN)


gamePlay = Nova_tela("Menu", (1000,600))
#gamePlay.set_resolucao((pygame.display.list_modes()[0][0],pygame.display.list_modes()[0][1]))

nave = Nova_nave('arquivos/nave.png', gamePlay.get_resolucao()[0]/2, 100)
nave.set_altitude(abs(nave.get_posicao_y()- gamePlay.get_resolucao()[1]))

gasolina = Item('arquivos/gasolina.png', gamePlay.get_resolucao()[0]/2, - 100)
gasolina.set_velocidade_x(0)
gasolina.set_velocidade_y(0)

terra = Nova_nave('arquivos/terra3.png', 800, 50)
#gamePlay.set_resolucao_tela((pygame.display.list_modes()[0][0],pygame.display.list_modes()[0][1]))

dados = Dados()

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
botao_slider_volume_ambiente = botao()
botao_bola_slider_volume_ambiente = botao()
botao_full_scren = botao()

def evento_botoes():
    botao().evento(event, botao_play, painel_menu)
    botao().evento(event, botao_exit, painel_menu)
    botao().evento(event, botao_confg, painel_menu)
    botao().evento(event, botao_voltar, painel_config)
    botao().evento(event, botao_bola_slider_volume_ambiente, painel_config)
    botao().evento(event, botao_full_scren, painel_config)
    botao().evento(event, botao_sim, painel_sair)
    botao().evento(event, botao_nao, painel_sair)



texto_velocidade_nave_hud = fonte_texto()
texto_combustivel_hud = fonte_texto()
texto_altitude_hud = fonte_texto()
texto_angulo_nave_hud = fonte_texto()
texto_pontos_hud = fonte_texto()
texto_contagem_regressiva_hud = fonte_texto()
texto_volume_ambiente = fonte_texto()
texto_fullscreen = fonte_texto()
texto_exit = fonte_texto()
texto_feedback_pouso_hud = fonte_texto()

str_botao_play = 'PLAY'
str_feedback_pouso = ''
cor_botao_fullscreen = BLACK

game_loop = False
debug = False
jogoAtivo = True
config = False
nova_resolucao = False

pos_bola_slider_volume = 0
nave.set_volume_propulsor(0.1)



while jogoAtivo:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogoAtivo = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                painel_menu.set_ativo(True)

                game_loop = False
                str_botao_play = 'PAUSADO'


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
        botao_play.draw(gamePlay, str_botao_play)

        botao_confg.criar(painel_menu, 0, 0, 30, 10)
        botao_confg.draw(gamePlay, 'CONFIG')

        botao_exit.criar(painel_menu, 0, 50, 30, 10)
        botao_exit.draw(gamePlay, 'EXIT')

        evento_botoes()

    # PAINEL CONFIG
    if painel_config.get_ativo()== True:

        painel_config.cria(gamePlay, 0, 0, 40, 45)
        painel_config.draw_painel(gamePlay, AMARELO, 120)

        botao_voltar.criar(painel_config, 0, gamePlay.get_proporcao()[1] * 150, 30, 10)
        botao_voltar.draw(gamePlay, 'VOLTAR')

        botao_slider_volume_ambiente.criar(painel_config, 0, -gamePlay.get_proporcao()[1] * 100, 50, 3)
        botao_slider_volume_ambiente.draw(gamePlay, '-                       +')

        print("texto_volume_ambiente largura: ", texto_volume_ambiente.get_largura())
        texto_volume_ambiente.cria("VOLUME AMBIENTE", 'Times new roman', int(gamePlay.get_proporcao()[0] * 15), WHITE)
        gamePlay.blit(texto_volume_ambiente.get_surface(), (gamePlay.get_resolucao()[0]/2 - texto_volume_ambiente.get_largura()/2,
            botao_slider_volume_ambiente.get_posicao_y()+botao_bola_slider_volume_ambiente.get_altura()))

        #pos_bola_slider_volume = -botao_slider_volume_ambiente.get_posicao_x() / 2 + botao_bola_slider_volume_ambiente.get_largura() * 2 + 20
        botao_bola_slider_volume_ambiente.criar(painel_config, pos_bola_slider_volume, -gamePlay.get_proporcao()[1] * 100, 6, 5)
        botao_bola_slider_volume_ambiente.draw(gamePlay, '')

        botao_full_scren.criar(painel_config, -gamePlay.get_proporcao()[0] * 80, gamePlay.get_proporcao()[1] * 20, 3, 5)
        botao_full_scren.draw(gamePlay, '')

        texto_fullscreen.cria('FULLSCREEN', 'Times new roman', int(gamePlay.get_proporcao()[0] * 15), WHITE)
        gamePlay.blit(texto_fullscreen.get_surface(), (gamePlay.get_resolucao()[0]/2 - texto_fullscreen.get_largura()/2 ,botao_full_scren.get_posicao_y()))


        evento_botoes()


    # PAINEL CERTEZA DE SAIR
    if painel_sair.get_ativo() == True:

        painel_sair.cria(gamePlay, 0, 0, 50, 20)
        painel_sair.draw_painel(gamePlay,WHITE, 120)

        texto_exit.cria("Você tem certeza que quer sair do jogo?", 'Times new roman', int(gamePlay.get_proporcao()[0] * 30), WHITE)
        gamePlay.blit(texto_exit.get_surface(), (gamePlay.get_resolucao()[0]/2 - texto_exit.get_largura()/2 , 110))

        botao_sim.criar(painel_sair, -gamePlay.get_proporcao()[0] * 120, 0, 30, 30)
        botao_sim.draw(gamePlay, 'SIM')

        botao_nao.criar(painel_sair, gamePlay.get_proporcao()[0] * 120, 0, 30, 30)
        botao_nao.draw(gamePlay, 'NÃO')

        evento_botoes()


    # HUD
    if painel_hud.get_ativo() == True:

        painel_hud.cria(gamePlay, 0, -gamePlay.get_resolucao()[1] / 2 + 30, 98, int(gamePlay.get_proporcao()[1] * 10))
        painel_hud.draw_painel(gamePlay, WHITE, 120)

        if gamePlay.get_cronometro()[4]<4:
            temp = 3
            temp -=gamePlay.get_cronometro()[4]

            texto_contagem_regressiva_hud.cria(" {0:4.4s} ".format(str(temp)), 'Times new roman', int(gamePlay.get_proporcao()[1] * 100), WHITE)
            gamePlay.blit(texto_contagem_regressiva_hud.get_surface(),
                          (gamePlay.get_resolucao()[0] / 2 - texto_contagem_regressiva_hud.get_tamanho_letra() / 2,
                           gamePlay.get_resolucao()[1] / 2 - texto_contagem_regressiva_hud.get_tamanho_letra() / 2))

        pos_textos = gamePlay.get_resolucao()[0]/5

        texto_velocidade_nave_hud.cria("Velocidade: {0:3.4s} ".format(str(abs(nave.get_velocidade_y()))), 'Times new roman',
                                       int(gamePlay.get_proporcao()[0] * 20), BLACK)
        gamePlay.blit(texto_velocidade_nave_hud.get_surface(), (painel_hud.get_posicao_x(), painel_hud.get_posicao_y()))

        texto_combustivel_hud.cria("Combustivel: {0:4.4s} L. ".format(str(nave.get_combustivel())) , 'Times new roman',
                                   int(gamePlay.get_proporcao()[0] * 20), BLACK)

        gamePlay.blit(texto_combustivel_hud.get_surface(), (painel_hud.get_posicao_x() + gamePlay.get_proporcao()[0]+pos_textos*1, painel_hud.get_posicao_y()))

        texto_altitude_hud.cria("Altitude : {0:4.5s} ".format(str(nave.get_altitude())) , 'Times new roman', int(gamePlay.get_proporcao()[0] * 20), BLACK)
        gamePlay.blit(texto_altitude_hud.get_surface(), (painel_hud.get_posicao_x() + gamePlay.get_proporcao()[0] + pos_textos * 2, painel_hud.get_posicao_y()))

        texto_angulo_nave_hud.cria("Angulo nave : {0:4.4s} ".format(str(abs(nave.get_angulo_rotacao()))) , 'Times new roman', int(gamePlay.get_proporcao()[0] * 20), BLACK)
        gamePlay.blit(texto_angulo_nave_hud.get_surface(), (painel_hud.get_posicao_x() + gamePlay.get_proporcao()[0] + pos_textos * 3, painel_hud.get_posicao_y()))

        texto_pontos_hud.cria("Pontos : {0:4.4s} ".format(str(dados.get_pontos())) , 'Times new roman', int(gamePlay.get_proporcao()[0] * 20), BLACK)
        gamePlay.blit(texto_pontos_hud.get_surface(), (painel_hud.get_posicao_x() + gamePlay.get_proporcao()[0] + pos_textos * 4, painel_hud.get_posicao_y()))

        texto_feedback_pouso_hud.cria(str_feedback_pouso, 'Times new roman', int(gamePlay.get_proporcao()[0] * 10), WHITE)
        gamePlay.blit(texto_feedback_pouso_hud.get_surface(), (nave.get_posicao_x() - texto_feedback_pouso_hud.get_largura() / 6 , nave.get_posicao_y() - gamePlay.get_proporcao()[1] * 20))


        evento_botoes()



    # GERENTE DO MENU

    if botao_full_scren.get_clicou() == True:
        cor_botao_fullscreen = WHITE


        gamePlay.set_resolucao((pygame.display.list_modes()[0][0], pygame.display.list_modes()[0][1] - 38))
        #gamePlay.fill(BLACK)
        gamePlay.flip()
    botao_full_scren.set_cor(cor_botao_fullscreen)

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
        painel_config.set_ativo(False)

    if botao_bola_slider_volume_ambiente.get_clicou() == True:

        if botao_bola_slider_volume_ambiente.get_posicao_x()>= botao_slider_volume_ambiente.get_posicao_x() and \
                botao_bola_slider_volume_ambiente.get_posicao_x()<= botao_slider_volume_ambiente.get_posicao_x()+ \
                botao_slider_volume_ambiente.get_largura() - botao_bola_slider_volume_ambiente.get_largura():

            pos_bola_slider_volume = pygame.mouse.get_pos()[0] - gamePlay.get_resolucao()[0] / 2




    #GAMEPLAY
    if game_loop == True:

        gamePlay.cronometro()

        if gamePlay.get_cronometro()[4]>3:

            mapa.desenha_terreno(gamePlay, nave)
            if mapa.get_existe_area_pouso() == False:
                mapa.desenha_terreno(gamePlay, nave)
                print("NAO FOI POSSIVEL SORTEAR UMA AREA DE POUSO, REDESENHANDO TERRENO")

            gasolina.set_tamanho(int(gamePlay.get_proporcao()[0] * 15), int(gamePlay.get_proporcao()[1] * 30))
            terra.set_tamanho(int(gamePlay.get_proporcao()[0] * 180), int(gamePlay.get_proporcao()[0] * 180))
            nave.set_tamanho(int(gamePlay.get_proporcao()[0] * 18),
                             int(gamePlay.get_proporcao()[1] * 50))

            nave.set_friccao(6)
            nave.set_velocidade_rotacao(nave.get_gravidade_lua()*2)
            nave.set_volume_propulsor(pos_bola_slider_volume)
            nave.set_altitude(nave.get_altitude() - nave.get_velocidade_y())
            nave.update()
            nave.verifica_colisao_tela(gamePlay)
            nave.verifica_colisao_area_pouso(mapa)
            nave.verifica_colisao_terreno(mapa)
            gasolina.verifica_colisao_nave(nave)
            gasolina.verifica_colisao_terreno(mapa)


            # GRAVIDADE
            nave.gravidade(gamePlay)

            # ACELERACAO do propulsor
            nave.aceleracao_propulsor(gamePlay)

            gasolina.gravidade(gamePlay)


            if nave.get_combustivel() == 500:
                gasolina.posicao_randomica(gamePlay)
                gasolina.set_velocidade_y(1)

            # so sorteia se caso  a gasolina  esta aguardando em cima da tela
            sort = random.randint(0, 200)
            if nave.get_combustivel() < 600 and sort == 100 and gasolina.get_posicao_y()<0 :
                gasolina.posicao_randomica(gamePlay)
                gasolina.set_velocidade_y(1)


            if gasolina.get_colidiu_nave() == True:

                if nave.get_combustivel()+300<=1000:
                    nave.set_combustivel(nave.get_combustivel() + 300)
                    #abasteceu = 1
                    gasolina.set_posicao_y(-gasolina.get_altura_y() - 10)
                    gasolina.set_velocidade_y(0)

            if gasolina.get_colidiu_terreno() == True:
                gasolina.set_velocidade_y(0)


            # se a nave pousou verifique as condicoes e atribua a pontuacao correta
            if nave.get_colidiu_area_pouso() == True:
                painel_menu.set_ativo(True)
                velocidade_rotacao = nave.get_angulo_rotacao()
                nave.set_angulo_rotacao(nave.get_angulo_rotacao())


                if nave.get_angulo_rotacao() <= 15 and nave.get_angulo_rotacao() >= -15:
                    pouso_perfeito = 150
                    dados.set_pontos(pouso_perfeito)
                    str_feedback_pouso = 'POUSO PERFEITO'


                elif nave.get_angulo_rotacao() <= 25 and nave.get_angulo_rotacao() >= -25:
                    pouso_toleravel = 100
                    dados.set_pontos(pouso_toleravel)
                    str_feedback_pouso = 'POUSO TOLERÁVEL'

                elif nave.get_angulo_rotacao() <= 35 and nave.get_angulo_rotacao() >= -35:
                    pouso_forcado = 50
                    dados.set_pontos(pouso_forcado)
                    str_feedback_pouso = 'POUSO FORÇADO'

            if nave.get_colidiu_terreno() == True and nave.get_colidiu_area_pouso() == False:
                str_feedback_pouso = 'VOCÊ MORREU'
                str_botao_play = 'IR DENOVO'
                print("colidiu", nave.get_colidiu_terreno())
                #game_loop = False
                painel_menu.set_ativo(True)
                # mapa.set_cor_terreno(CYAN)
                mapa.set_cor_borda_terreno(CYAN)


            else:
                nave.set_colidiu_terreno(False)
                # mapa.set_cor_terreno(MARRON)
                mapa.set_cor_borda_terreno(AMARELO)


            # so adiciona angulo do lado esquerdo da nave se for o grau maximo permitido de 90
            if nave.get_rotacionou_esq() and nave.get_angulo_rotacao() <= 90:
                nave.set_angulo_rotacao(nave.get_angulo_rotacao()+nave.get_velocidade_rotacao())

            # so adiciona angulo do lado direito da nave se for o grau maximo permitido de 90
            if nave.get_rotacionou_dir() and nave.get_angulo_rotacao() >= -90:
                nave.set_angulo_rotacao(nave.get_angulo_rotacao()- nave.get_velocidade_rotacao())

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
            #print('Abasteceu :', abasteceu)
            #if abasteceu <1:
            gamePlay.blit(gasolina.get_surface(), (gasolina.get_posicao_x(), gasolina.get_posicao_y()))
            #print(gasolina.get_posicao_y())


    #tempo+=0.1
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

        #print("painel menu   :", painel_menu.get_ativo())
        #print("painel config :", painel_config.get_ativo())
        #print("painel sair   :", painel_sair.get_ativo())

        print("pos_bola_slider_volume:", pos_bola_slider_volume / 1000)
        print("pos mouse oficial  :", pygame.mouse.get_pos()[0])
        print("pos bola slider    :", botao_bola_slider_volume_ambiente.get_posicao_x())
        print("posicao slider x :", botao_slider_volume_ambiente.get_posicao_x())
        print("volume propulsor :", nave.get_volume_propulsor())

pygame.quit()
