
from Tela import *
from Nave import *
from Mapa import *
from Interface import *


import pygame

pygame.init()
mapa = Mapa_do_jogo()
gamePlay = Nova_tela("teste", RESOLUCAO)

nave = Nova_nave('arquivos/nave.png', 300, 300)
lua = Nova_nave('arquivos/lua.png', 800, 50)

painel_menu = painel()
painel_menu.set_ativo(True)
painel_config = painel()
painel_config.set_ativo(False)
painel_sair = painel()
painel_sair.set_ativo(False)

msg_exit = fonte_texto()

botao_play = botao()
botao_exit = botao()
botao_confg = botao()
botao_voltar = botao()
botao_sim = botao()
botao_nao = botao()

def evento_botoes():
    botao().evento(event, botao_play)
    botao().evento(event, botao_exit)
    botao().evento(event, botao_confg)
    botao().evento(event, botao_voltar)
    botao().evento(event, botao_sim)
    botao().evento(event, botao_nao)

game_loop = False

tempo = 0
debug = False
jogoAtivo = True
config = False



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
        botao_play.draw_botao(gamePlay, 'PLAY')
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

        mapa.desenha_terreno(gamePlay)
        lua.set_tamanho(200, 200)
        nave.set_tamanho(TAMANHO_DA_NAVE_X, TAMANHO_DA_NAVE_y)
        nave.set_friccao(FRICCAO_PROPULSOR)
        nave.set_velocidade_rotacao(VELOCIDADE_ROTACAO)

        velocidade_x = nave.get_velocidade_x()
        velocidade_y = nave.get_velocidade_y()
        posicao_x = nave.get_posicao_x()
        posicao_y = nave.get_posicao_y()
        potencia_propulsor = nave.get_potencia_propulsor()
        angulo = nave.get_angulo_rotacao()

        nave.verifica_colisao_tela()
        # ACELERACAO do propulsor
        nave.aceleracao_propulsor(tempo)
        # GRAVIDADE
        nave.gravidade(tempo)

        # so adiciona angulo do lado esquerdo da nave se for o grau maximo permitido de 90
        if nave.get_rotacionou_esq() and nave.get_angulo_rotacao() <= 90:
            angulo += nave.get_velocidade_rotacao()
            nave.set_angulo_rotacao(angulo)

        # so adiciona angulo do lado direito da nave se for o grau maximo permitido de 90
        if nave.get_rotacionou_dir() and nave.get_angulo_rotacao() >= -90:
            angulo -= nave.get_velocidade_rotacao()
            nave.set_angulo_rotacao(angulo)

        posicao_x += velocidade_x
        posicao_y += velocidade_y
        nave.set_posicao(posicao_x, posicao_y)

        # cria poligono propulsor e recebe tamanho da calda
        poligono_propulsor_dir = nave.criaPoligono_Propulsor(2, 4, nave.get_potencia_propulsor() * FPS)
        poligono_propulsor_esq = nave.criaPoligono_Propulsor(2, -4, nave.get_potencia_propulsor() * FPS)

        # rotaciona a (imagem) nave
        nave_rot = nave.rotacaoCentralizada(nave.get_angulo_rotacao())

        gamePlay.blit(lua.get_surface(), lua.get_posicao())
        gamePlay.blit(nave_rot[0], nave_rot[1])
        gamePlay.draw_polygon(WHITE, poligono_propulsor_dir)
        gamePlay.draw_polygon(WHITE, poligono_propulsor_esq)

        # futura condicao de dano/perca pontos/morte etc
        if nave.get_colidiu_tela() == True:
            nave.set_velocidade_x(0)
            nave.set_velocidade_y(0)




    gamePlay.cronometro()
    tempo+=0.1
    gamePlay.flip()
    gamePlay.set_fps(FPS)

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
