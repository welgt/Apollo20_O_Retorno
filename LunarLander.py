
from Tela import *
from Objeto import *
from Mapa import *
import pygame

pygame.init()
mapa = Mapa_do_jogo()
clock = pygame.time.Clock()
gamePlay = Nova_tela("teste", RESOLUCAO)

nave = Novo_objeto('arquivos/nave.png', 300, 300)
nave.set_tamanho(TAMANHO_DA_NAVE_X, TAMANHO_DA_NAVE_y)
nave.set_friccao(FRICCAO_PROPULSOR)
nave.set_velocidade_rotacao(VELOCIDADE_ROTACAO)

lua = Novo_objeto('arquivos/lua.png', 800, 50)
lua.set_tamanho(200, 200)

tempo = 0

# poligono_propulsor = pygame.draw.polygon(gamePlay.tela, WHITE, [(300,600), (295,618), (824,407), (800,400)],0)

# relogio
milisegundos = 0
segundos = 0
delta_time = 0

debug = False
jogoAtivo = True
menu = False
game = False
config = False


while jogoAtivo:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogoAtivo = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jogoAtivo = False

            elif event.key == pygame.K_LEFT:
                nave.set_rotacionou_esq(True)

            elif event.key == pygame.K_RIGHT:
                nave.set_rotacionou_dir(True)

            elif event.key == pygame.K_UP:
                nave.set_propulsor_ativo(True)

            elif event.key == pygame.K_DOWN:
                pass

            # debugar
            elif event.key == pygame.K_g:
                game = True
                debug = True

            elif event.key == pygame.K_m:
                menu = True
                debug = True

            elif event.key == pygame.K_c:
                config = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                nave.set_rotacionou_dir(False)
                nave.set_rotacionou_esq(False)

            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                nave.set_propulsor_ativo(False)

            # debugar
            elif event.key == pygame.K_UP or event.key == pygame.K_d:
                debug = False

    gamePlay.fill(BLACK)

    if menu == True:
        print("Entrei no menu")

    game = True
    if game == True:

        mapa.desenha_solo(gamePlay)

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
        if nave.get_rotacionou_esq() and nave.get_angulo_rotacao() <=90:
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
        poligono_propulsor_dir = nave.criaPoligono_Propulsor(1, 4, nave.get_potencia_propulsor() * FPS)
        poligono_propulsor_esq = nave.criaPoligono_Propulsor(1, -4, nave.get_potencia_propulsor() * FPS)

        # rotaciona a (imagem) nave
        nave_rot = nave.rotacaoCentralizada(nave.get_angulo_rotacao())

        gamePlay.blit(lua.get_surface(), lua.get_posicao())
        gamePlay.blit(nave_rot[0],nave_rot[1])
        gamePlay.draw_polygon(WHITE, poligono_propulsor_dir)
        gamePlay.draw_polygon(WHITE, poligono_propulsor_esq)

        # futura condicao de dano/perca pontos/morte etc
        if nave.get_colidiu_tela() == True:
            nave.set_velocidade_x(0)
            nave.set_velocidade_y(0)

    if config == True:
        print("Entrei nas configuracoes")

    # RELOGIO
    if milisegundos < FPS:
        milisegundos += 1
        # print("milisegundos  : ", milisegundos)
    else:
        segundos += 1
        # print("segundos :------------", segundos)
        milisegundos = 0

    tempo+=0.1
    gamePlay.flip()
    clock.tick(FPS)

pygame.quit()