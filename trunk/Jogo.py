# -*- coding: utf-8 -*-
'''

Created on 20/12/2011

@author: gbf
'''

import random

class Simon():
    def __init__(self):
        self.sequencia = []        
    
    def comecar(self):
        i = 0
        self.acertos = 0
        while True:
            
            self.vez_do_pc()
            jogada = self.vez_do_jogador()
            
            # Se o jogar acertar a sequencia continua
            if jogada == self.sequencia :
                self.acertos += 1
                print "Acerto"
                
            # Senão errou, para o jogo
            else :
                print "Perdeu"
                print "Você conseguio  %i acertos " % self.acertos 
                break
      
    
    def vez_do_pc(self):
        escolha = self.escolher_cor()
        self.sequencia.append(escolha)
        print "Vez do pc → ", self.sequencia
	print "PISCAR TODA A SEQUENCIA"
        return self.sequencia
	
    
    def vez_do_jogador(self):
        jogadas = []
        for i, cor in enumerate(self.sequencia):
            jogada = raw_input("Digite a cor : ")
            jogadas.append(jogada)
            print "Piscar jogada"
            if jogada != self.sequencia[i] :
                break
        return jogadas
             

    def escolher_cor(self):
        return random.choice(("azul", "vermelho", "verde", "amarelo"))  


        
