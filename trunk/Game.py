'''
Created on 20/12/2011

@author: gbf
'''
import sys, pygame
pygame.init()

size = width, height = 640, 480
speed = [1, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

vermelho = pygame.image.load("vermelho.png")
verde = pygame.image.load("verde.png")
azul = pygame.image.load("azul.png")
amarelo = pygame.image.load("amarelo.png")

vermelho_rect = vermelho.get_rect() 
vermelho_rect = vermelho_rect.move((10,10))

verde_rect = verde.get_rect()
verde_rect = verde_rect.move((208,10))

azul_rect = azul.get_rect()
azul_rect = azul_rect.move((10,208))

amarelo_rect = amarelo.get_rect()
amarelo_rect = amarelo_rect.move(208,208)

while 1:
        for event in pygame.event.get():
                if event
                if pygame.key.get_pressed()[pygame.K_RETURN] :
                    # Iniciar o jogo
                    lista = []
                        
                if event.type == pygame.QUIT: sys.exit()
                
        screen.fill((255,255,255))
        screen.blit(vermelho, vermelho_rect)
        screen.blit(verde, verde_rect)
        screen.blit(azul, azul_rect)
        screen.blit(amarelo, amarelo_rect)
        pygame.display.flip()

