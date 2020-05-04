import pygame
from NovoObjeto import *
from NovaTela import *

tela = Nova_tela('teste', ((600,600)))
nave = Novo_objeto('arquivos/nave.png', (0,0))
nave.set_tamanho((50,50))

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)

print("nave.get_tamanho() :", nave.get_tamanho())
print("nave.get_centro() :", nave.get_centro())
print("nave.get_posicao() :", nave.get_posicao())

i = 0

jogoAtivo = True

while jogoAtivo:
    i+=0.5
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
    nave.set_posicao((300,300))

    propulsor = nave.criaPoligonoPropulsor(25, 0, 100)
    tela.draw(WHITE,propulsor)

    tela.flip()
    tela.fps(60)



pygame.quit()