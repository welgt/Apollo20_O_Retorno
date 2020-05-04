import math
from NovaTela import *
from NovoObjeto import *
from Configuracaes import *
import pygame

pygame.init()

gamePlay = Novo_objeto("teste", RESOLUCAO)
nave = Novo_objeto('midias/nave.png', 500, 50)
lua = Novo_objeto('midias/lua.png', 600, 50)
nave.set_tamanho(25, 40)
lua.set_tamanho(200, 200)

# poligono_propulsor = pygame.draw.polygon(gamePlay.tela, WHITE, [(300,600), (295,618), (824,407), (800,400)],0)

# relogio
milisegundos = 0
segundos = 0
delta_time = 0

# gravidade e aceleracao
tempo = 0
nave.set_friccao(FRICCAO_PROPULSOR)
nave.set_velocidade_rotacao(VELOCIDADE_ACELERACAO_LUA * 2)
potencia_propulsor = 0


"""def rotacaoCentralizada(obj, angulo):
    surface = pygame.transform.rotate(obj.imagem, angulo)
    rot_rect = surface.get_rect(center=obj.rect.center)
    rot_rect[0] += obj.posicao_x - obj.tamanho_x
    rot_rect[1] += obj.posicao_y - obj.tamanho_y
    return surface, rot_rect"""


"""def criaPoligonoPropulsor(obj_pai, largura_poligono, posicao_x, ponto_acelerador_poligono):
    ponto_direito = largura_poligono + obj_pai.posicao_x + posicao_x
    ponto_esquerdo = -largura_poligono + obj_pai.posicao_x + posicao_x
    ponto_acelerador_poligono += obj_pai.posicao_y + obj_pai.tamanho_y / 2
    altura_base = obj_pai.tamanho_y / 2

    vertices_propulsor = ((ponto_direito, altura_base + obj_pai.posicao_y),  # (0,3),
                          (obj_pai.posicao_x + posicao_x, ponto_acelerador_poligono),  # (3,-3)
                          (ponto_esquerdo, altura_base + obj_pai.posicao_y))  # (-3,-3)

    origem_nave = obj_pai.posicao_x, obj_pai.posicao_y

    angulo_rotacao = math.radians(-obj_pai.angulo_rotacao)
    poligono_rotacionado = []

    for vertice in vertices_propulsor:
        vertice_aux = vertice[0] - origem_nave[0], vertice[1] - origem_nave[1]
        vertice_aux = (vertice_aux[0] * math.cos(angulo_rotacao) - vertice_aux[1] * math.sin(angulo_rotacao),
                       vertice_aux[0] * math.sin(angulo_rotacao) + vertice_aux[1] * math.cos(angulo_rotacao))
        vertice_aux = vertice_aux[0] + origem_nave[0], vertice_aux[1] + origem_nave[1]
        poligono_rotacionado.append(vertice_aux)

    return poligono_rotacionado"""


debug = False
jogoAtivo = True

while jogoAtivo:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogoAtivo = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jogoAtivo = False

            elif event.key == pygame.K_LEFT:
                #nave.rotacionou_esquerda = True
                nave.set_rotacionou(True)[0]

            elif event.key == pygame.K_RIGHT:
                #nave.rotacionou_direita = True
                nave.set_rotacionou(True)[1]



            elif event.key == pygame.K_UP:
                #nave.propulsor = True
                nave.set_propulsor_ativo(True)

            elif event.key == pygame.K_DOWN:
                pass

            # debugar
            elif event.key == pygame.K_d:
                debug = True


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #nave.rotacionou_esquerda = False
                nave.set_rotacionou(False)[0]
                #nave.rotacionou_direita = False
                nave.set_rotacionou(False)[1]


            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                #nave.velocidade_y += 0
                nave.set_velocidade(0)[1]
                nave.propulsor = False
                nave.set_propulsor_ativo(False)

            # debugar
            elif event.key == pygame.K_UP or event.key == pygame.K_d:
                debug = False

    gamePlay.fill()
    nave.verifica_colisao_tela()

    # futura condicao de dano/perca pontos/morte etc
    if nave.get_colidiu_tela() == True:
        nave.set_velocidade(0)[0]
        nave.set_velocidade(0)[0]

    # RELOGIO
    if milisegundos < FPS:
        milisegundos += 1
        # print("milisegundos  : ", milisegundos)
    else:
        segundos += 1
        # print("segundos :------------", segundos)
        milisegundos = 0

    # ACELERACAO do propulsor
    tempo += 1
    if nave.get_propulsor_ativo() == True:
        nave.get_velocidade()[1] -= (VELOCIDADE_ACELERACAO_LUA / FPS) * tempo * nave.get_friccao()

        # permite aumentar o tamanho do propulsor ate 1
        if potencia_propulsor < 1:
            potencia_propulsor += (VELOCIDADE_ACELERACAO_LUA / FPS) * tempo * nave.friccao

        if nave.velocidade_y <= VELOCIDADE_ACELERACAO_LUA:
            tempo = 0

            # define nova direcao caso a nave esteja inclinada pra direita e propulsor ativo
            if nave.angulo_rotacao <= 1 and nave.propulsor:
                nave.velocidade_x += (nave.angulo_rotacao * -1) / 360

            # define nova direcao caso a nave esteja inclinada pra esquerda e propulsor ativo
            if nave.angulo_rotacao >= 1 and nave.propulsor:
                nave.velocidade_x -= nave.angulo_rotacao / 360

    else:
        # GRAVIDADE
        nave.velocidade_y += (VELOCIDADE_ACELERACAO_LUA / FPS) * tempo * nave.friccao

        # diminiu o tamanho do propulsor
        potencia_propulsor -= (VELOCIDADE_ACELERACAO_LUA / FPS) * tempo * nave.friccao

        # caso ele for menor que zero, fique em zero.
        if potencia_propulsor < 0:
            potencia_propulsor = 0
        if nave.velocidade_y >= VELOCIDADE_ACELERACAO_LUA:
            tempo = 0

    # so adiciona angulo do lado esquerdo da nave se for o grau maximo permitido de 90
    if nave.rotacionou_esquerda and nave.angulo_rotacao <= 90:
        nave.angulo_rotacao += nave.velocidade_rotacao

    # so adiciona angulo do lado direito da nave se for o grau maximo permitido de 90
    if nave.rotacionou_direita and nave.angulo_rotacao >= -90:
        nave.angulo_rotacao -= nave.velocidade_rotacao

    nave.posicao_x += nave.velocidade_x
    nave.posicao_y += nave.velocidade_y

    # rotaciona a (imagem) nave
    nave_rot = rotacaoCentralizada(nave, nave.angulo_rotacao)
    # cria poligono propulsor e recebe tamanho da calda
    poligono_propulsor_dir = criaPoligonoPropulsor(nave, 2, 5, potencia_propulsor * FPS)
    poligono_propulsor_esq = criaPoligonoPropulsor(nave, 2, -5, potencia_propulsor * FPS)

    gamePlay.tela.blit(nave_rot[0], nave_rot[1])
    pygame.draw.polygon(gamePlay.tela, WHITE, poligono_propulsor_dir)
    pygame.draw.polygon(gamePlay.tela, WHITE, poligono_propulsor_esq)
    gamePlay.desenhaSprite(lua)

    gamePlay.clork.tick(FPS)
    pygame.display.flip()

    # debuga se apertar a tecla 'D' printa  os valores
    if debug:
        print("Angulo nave:         ", nave.angulo_rotacao)
        print("Velocidade nave x :  ", nave.velocidade_x)
        print("Velocidade nave y :  ", nave.velocidade_y)
        print("posicao nave x :     ", nave.posicao_x)
        print("posicao nave y :     ", nave.posicao_y)
        print("tamanho nave x :     ", nave.tamanho_x)
        print("tamanho nave y :     ", nave.tamanho_y)
        print("potencia_propulsor   ", potencia_propulsor)
        print("poligono_propulsor : ", poligono_propulsor_dir)
        print("nave.imagem          ", nave.imagem)
        print("nave.rect            ", nave.rect)
        print("nave_rot[1] :        ", nave_rot[1])

pygame.quit()

"""def rotatePolygon(self,angle):
   Rotates the given polygon which consists of corners represented as (x,y),
   around the ORIGIN, clock-wise, theta degrees

    angle = math.radians(angle)
    polygon = self
    rotatedPolygon = []
    for corner in polygon :
        rotatedPolygon.append(( corner[0]*math.cos(angle)-corner[1]*math.sin(angle) , corner[0]*math.sin(angle)+corner[1]*math.cos(angle)) )
    self = rotatedPolygon
    return"""