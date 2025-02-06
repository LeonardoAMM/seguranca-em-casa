import pygame
import math
import random

class Minigame:
    def __init__(self, game, dis):
        self.game = game
        self.display = dis
        self.barraV = pygame.image.load('imagens/minigame/1/barra.png')
        self.PontB = pygame.image.load('imagens/minigame/1/pontin.png')
        self.verde = pygame.image.load('imagens/minigame/1/verde.png')
        self.mao1 = pygame.image.load('imagens/minigame/1/mao1.png')
        self.mao2 = pygame.image.load('imagens/minigame/1/mao2.png')
        self.contador = 0
        self.pos = 0
        self.aleat = random.randrange(100, 315)
        self.ativa = False
        self.ponto = 0
        self.machucar=0

        self.tempo = 0

        self.isso  = pygame.Rect(self.aleat,100,self.verde.get_width(),self.verde.get_height())



    def mini1(self,eventAtual,event1,imagen):
        self.display.blit(pygame.image.load(imagen),(0,0))
        if self.ativa == False:
           self.display.blit(self.mao1,(0,0)) 
        else:
            self.display.blit(self.mao2,(0,0)) 
        self.display.blit(self.barraV,(100,100))
        self.display.blit(self.verde,(self.aleat,100))
        self.display.blit(self.PontB,(217+self.pos,100))
        self.isso = pygame.Rect(self.aleat,100,self.verde.get_width(),self.verde.get_height())
        self.pos = math.sin(self.contador*.1)*117

        if self.isso.collidepoint(217+self.pos,100):
            self.contador+=0.15
        else:
            self.contador+=0.7

        if self.ativa == True:
            self.tempo += 0.15

        if self.tempo >= 4:
            self.ativa = False
            self.tempo = 0

        if self.ponto < 3:
            return eventAtual,self.machucar
        else:
            return event1,self.machucar

    def ativarmini1(self):
        
        if self.isso.collidepoint(217+self.pos,100):
        #if 217+self.pos > self.aleat:
            self.ponto+=1
        else:
            self.machucar += 1

        self.ativa = True

        self.aleat = random.randrange(100, 315)

