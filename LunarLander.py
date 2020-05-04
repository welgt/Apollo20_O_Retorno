import pygame
from NovoObjeto import *
from NovaTela import *

tela = Nova_tela('teste', ((600,600)))
nave = Novo_objeto('arquivos/nave.png', (300,300))
nave.set_tamanho((50,80))

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)

print("nave.get_tamanho() :", nave.get_tamanho())
print("nave.get_centro() :", nave.get_centro_surface())
print("nave.get_posicao() :", nave.get_posicao())

i = 0

jogoAtivo = True

while jogoAtivo:
    #i+=0.5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogoAtivo = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jogoAtivo = False

    tela.fill(BLACK)
    nave.set_angulo_rotacao(i)
    nave_rot = nave.rotacaoCentralizada(i)
    tela.blit(nave_rot[0], nave_rot[1])


    propulsor = nave.criaPoligono_Propulsor(15, 0, 10)
    tela.draw(WHITE,propulsor)

    print("nave.get_centro() :", nave.get_centro_surface())
    tela.flip()
    tela.fps(60)



pygame.quit()