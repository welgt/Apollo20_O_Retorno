from Dados import *
from Tela import *
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




#gamePlay.set_resolucao_tela((pygame.display.list_modes()[0][0],pygame.display.list_modes()[0][1]))



nave = Nova_nave('arquivos/nave.png', 300, 300)
print("Combustivel inicial: ", nave.get_combustivel())
terra = Nova_nave('arquivos/terra3.png', 800, 50)

painel_menu = painel()
painel_menu.set_ativo(True)
painel_config = painel()
painel_config.set_ativo(False)
painel_sair = painel()
painel_sair.set_ativo(False)

texto_botao_play = 'PLAY'
msg_exit = fonte_texto()

botao_play = botao()
botao_exit = botao()
botao_confg = botao()
botao_voltar = botao()
botao_sim = botao()
botao_nao = botao()

dados = Dados()



def evento_botoes():
    botao().evento(event, botao_play)
    botao().evento(event, botao_exit)
    botao().evento(event, botao_confg)
    botao().evento(event, botao_voltar)
    botao().evento(event, botao_sim)
    botao().evento(event, botao_nao)

game_loop = False


debug = False
jogoAtivo = True
config = False
tempo = 0
nova_resolucao = False




while jogoAtivo:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogoAtivo = False

        #if event.type == pygame.MOUSEBUTTONDOWN:
         #   print("funcionou")

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                painel_menu.set_ativo(True)
                #botao_confg.set_clicou(False)
                # tem que fazer um pouse aqui pra so depois setar o botao play como falso
                botao_play.set_clicou(False)
                game_loop = False
                texto_botao_play = 'DESPAUSAR'



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


        painel_menu .cria_painel(gamePlay, 0, 0, 40, 45)
        painel_menu.draw_painel(gamePlay,WHITE)

        botao_play.criar_botao(painel_menu, 0, -50, 30, 10)
        botao_play.draw_botao(gamePlay, texto_botao_play)
        #botao_play.draw_borda_botao(gamePlay,RED)

        botao_confg.criar_botao(painel_menu, 0, 0, 30, 10)
        botao_confg.draw_botao(gamePlay, 'CONFIG..')
        #botao_confg.draw_borda_botao(gamePlay,RED)

        botao_exit.criar_botao(painel_menu, 0, 50, 30, 10)
        botao_exit.draw_botao(gamePlay, 'EXIT')
        #botao_exit.draw_borda_botao(gamePlay,RED)

        evento_botoes()

    # PAINEL CONFIG
    if painel_config.get_ativo()== True:

        painel_config.cria_painel(gamePlay, -0, 0, 40, 45)
        painel_config.draw_painel(gamePlay, WHITE)

        botao_voltar.criar_botao(painel_config, 0, 100, 30, 10)
        botao_voltar.draw_botao(gamePlay, 'VOLTAR')

        evento_botoes()


    # PAINEL CERTEZA DE SAIR
    if painel_sair.get_ativo() == True:

        painel_sair.cria_painel(gamePlay,0,0, 50, 20)
        painel_sair.draw_painel(gamePlay,AMARELO)

        msg_exit.set_texto("Voce tem certeza que quer fechar o jogo?", 'Times new roman')
        msg_exit.cria_texto(35, WHITE, 1)
        gamePlay.get_surface_tela().blit(msg_exit.get_surface(), (painel_sair.get_posicao_x() , 110))


        botao_sim.criar_botao(painel_sair, -100, 0, 30, 30)
        botao_sim.draw_botao(gamePlay, 'SIM')


        botao_nao.criar_botao(painel_sair, 100, 0, 30, 30)
        botao_nao.draw_botao(gamePlay, 'NÃO')

        evento_botoes()



    # GERENTE DO MENU
    if botao_play.get_clicou() == True:
        game_loop = True
        painel_menu.set_ativo(False)


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


    #GAMEPLAY
    if game_loop == True:

        mapa.desenha_terreno(gamePlay, nave)
        if mapa.get_existe_area_pouso() == False:
            mapa.desenha_terreno(gamePlay, nave)
            print("NAO FOI POSSIVEL SORTEAR UMA AREA DE POUSO, REDESENHANDO TERRENO")

        terra.set_tamanho(250, 250)
        nave.set_tamanho(TAMANHO_DA_NAVE_X, TAMANHO_DA_NAVE_y)
        nave.set_friccao(FRICCAO_PROPULSOR)
        nave.set_velocidade_rotacao(nave.get_gravidade_lua())


        velocidade_x = nave.get_velocidade_x()
        velocidade_y = nave.get_velocidade_y()
        posicao_x = nave.get_posicao_x()
        posicao_y = nave.get_posicao_y()
        potencia_propulsor = nave.get_potencia_propulsor()
        angulo = nave.get_angulo_rotacao()

        posicao_x += velocidade_x
        posicao_y += velocidade_y

        # so tem velocidade caso nao colidiu com a tela
        if nave.get_colidiu_tela() == False:
            nave.set_posicao(posicao_x, posicao_y)

        nave.verifica_colisao_tela(gamePlay)
        nave.verifica_colisao_area_pouso(mapa)
        nave.verifica_colisao_terreno(mapa, gamePlay)

        # se a nave pousou verifique as condicoes e atribua a pontuacao correta
        if nave.get_colidiu_area_pouso() == True:
            painel_menu.set_ativo(True)
            angulo = nave.get_angulo_rotacao()
            nave.set_angulo_rotacao(angulo)
            if nave.get_angulo_rotacao()<=15 and nave.get_angulo_rotacao() >= -15:
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
            #painel_menu.set_ativo(True)
            #mapa.set_cor_terreno(CYAN)
            mapa.set_cor_borda_terreno(CYAN)
        else:
            nave.set_colidiu_terreno(False)
            #mapa.set_cor_terreno(MARRON)
            mapa.set_cor_borda_terreno(AMARELO)



        #print("pontos :", dados.get_pontos())
        # futura condicao de dano/perca pontos/morte etc
        #if nave.get_colidiu_tela() == True:
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
        poligono_propulsor_dir = nave.criaPoligono_Propulsor(2, 4, nave.get_potencia_propulsor() * gamePlay.get_fps())
        poligono_propulsor_esq = nave.criaPoligono_Propulsor(2, -4, nave.get_potencia_propulsor() * gamePlay.get_fps())

        # rotaciona a (imagem) nave
        nave_rot = nave.rotacaoCentralizada()

        gamePlay.blit(terra.get_surface(), terra.get_posicao())
        gamePlay.blit(nave_rot[0], nave_rot[1])
        gamePlay.draw_polygon(CYAN, poligono_propulsor_dir)
        gamePlay.draw_polygon(CYAN, poligono_propulsor_esq)
    tempo+=0.1
    gamePlay.cronometro()
    gamePlay.flip()
    gamePlay.set_fps(30)
    print("Combustivel :", nave.get_combustivel())

    if debug:
        print("config :", botao_confg.get_mouse_cont())
        print("play   :", botao_play.get_mouse_cont())
        print("exit   :", botao_exit.get_mouse_cont())
        print("voltar :", botao_voltar.get_mouse_cont())

        print("botao play ativo   :", botao_play.get_clicou())
        print("botao config ativo :", botao_confg.get_clicou())
        print("botao exit ativo   :", botao_exit.get_clicou())
        print("botao voltar ativo :", botao_voltar.get_clicou())
        print("game_loop :", game_loop)







pygame.quit()
