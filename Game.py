'''
Created on 20/12/2011

@author: gbf
'''


import sys, pygame, random, time

from Jogo import Simon


pygame.init()

def pisca(lista):
    for cor in lista :
        original = cor
        if cor == "amarelo" :
            amarelo = pygame.image.load("amarelo.png") 
            amarelo_rect = amarelo.get_rect()
            amarelo_rect = amarelo_rect.move((208,208))
            screen.blit(amarelo, amarelo_rect)
            pygame.display.flip()

        elif cor == "verde" :
            verde = pygame.image.load("verde.png")
            verde = pygame.image.load("verde.png") 
            verde_rect = verde.get_rect()
            verde_rect = verde_rect.move((208,10))
            screen.blit(verde, verde_rect)
            pygame.display.flip()

        elif cor == "vermelho":
            vermelho = pygame.image.load("vermelho.png")
            vermelho = pygame.image.load("vermelho.png") 
            vermelho_rect = vermelho.get_rect()
            vermelho_rect = vermelho_rect.move((10,10))
            screen.blit(vermelho, vermelho_rect)
            pygame.display.flip()

        else :
            azul = pygame.image.load("azul.png")
            azul = pygame.image.load("azul.png") 
            azul_rect = azul.get_rect()
            azul_rect = azul_rect.move((10,208))
            screen.blit(azul, azul_rect)
            pygame.display.flip()

        time.sleep(1)
        cor = original
        pygame.display.flip()

size = width, height = 396, 396
speed = [1, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

vermelho = pygame.image.load("vermelho_.png")
verde = pygame.image.load("verde_.png")
azul = pygame.image.load("azul_.png")
amarelo = pygame.image.load("amarelo_.png")

vermelho_rect = vermelho.get_rect() 
vermelho_rect = vermelho_rect.move((10,10))

verde_rect = verde.get_rect()
verde_rect = verde_rect.move((208,10))

azul_rect = azul.get_rect()
azul_rect = azul_rect.move((10,208))

amarelo_rect = amarelo.get_rect()
amarelo_rect = amarelo_rect.move(208,208)

jogo = Simon()

while 1:
        for event in pygame.event.get():
            if pygame.key.get_pressed()[pygame.K_RETURN] :
                if event.type == pygame.MOUSEBUTTONDOWN :
                    pisca(jogo.vez_do_pc())         
                    if vermelho_rect.collidepoint(event.pos):
                        clicado = "vermelho"
                    elif azul_rect.collidepoint(event.pos):
                        clicado = "azul"
                    elif verde_rect.collidepoint(event.pos):
                        clicado = "verde"
                    elif amarelo_rect.collidepoint(event.pos):
                        clicado = "amarelo"
                        
                    print clicado
                    
            if event.type == pygame.QUIT: sys.exit()
                
        screen.fill((255,255,255))
        screen.blit(vermelho, vermelho_rect)
        screen.blit(verde, verde_rect)
        screen.blit(azul, azul_rect)
        screen.blit(amarelo, amarelo_rect)
        pygame.display.flip()
