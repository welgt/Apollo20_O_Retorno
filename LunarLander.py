import pygame
from NovoObjeto import *
from NovaTela import *

tela = Nova_tela('teste', ((600,600)))
nave = Novo_objeto('arquivos/bola.jpg', (550,550))
nave.set_tamanho((50,50))

print("nave.get_tamanho() :", nave.get_tamanho())
print("nave.get_centro() :", nave.get_centro())
print("nave.get_posicao() :", nave.get_posicao())

i = 0

jogoAtivo = True

while jogoAtivo:
    i+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogoAtivo = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jogoAtivo = False

    tela.fill((0, 0, 0))
    nave.set_angulo_rotacao(i)
    nave_rot = nave.rotacaoCentralizada(i)
    tela.blit(nave_rot[0], nave_rot[1])

    nave.set_posicao((0,0))

    tela.flip()
    tela.fps(60)

    print(nave.get_angulo_rotacao())

pygame.quit()