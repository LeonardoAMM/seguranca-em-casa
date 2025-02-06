import pygame
import math
import random
from npc import *

class Minigame2:
    def __init__(self, game, dis):
        self.game = game
        self.display = dis
        self.vermelho = pygame.image.load('imagens/minigame/2/pedra.png')
        self.fundo = pygame.image.load('imagens/minigame/2/fundo.png')
        self.fundo2 = pygame.image.load('imagens/minigame/2/fundo.png')
        self.tamanhol = self.vermelho.get_width()
        self.tamanhoc = self.vermelho.get_height()
        self.jogador = pygame.Rect(110,100,self.tamanhol,self.tamanhoc)
        self.ntocar = {}
        self.coli=[]
        self.contador = 0
        self.vec=[False,False,False,False]
        self.pos = 0
        self.parado = 0
        self.aleat = random.randrange(30, 170)
        self.ativa = False
        self.velocidade = 0
        self.machucar=0
        self.apagar=-1
        self.player = Npc('cortar',21,2,'andando')
        self.tempo = 0
        self.id = 0
        self.criarini(self.aleat)
        self.fun1 = 0
        self.fun2 = 400
        self.erros = 0


    def criarini(self,posy):
        self.ntocar[self.id]  = [400,posy,True]
        self.coli.append(pygame.Rect(400,posy,self.tamanhol,self.tamanhol))
        self.id += 1
        self.aleat = random.randrange(30, 170)



    def mini1(self,eventAtual,event1):
        self.player.events()

        self.display.blit(self.fundo,(self.fun1,0))
        self.display.blit(self.fundo2,(self.fun2,0))
        self.fun1 -= (1.5+self.contador*.001)
        self.fun2 -= (1.5+self.contador*.001)
        if self.fun1 <= -400:
            self.fun1 = 0
        if self.fun2 <= 0:
            self.fun2 = 400

        self.contador += 1

        #self.player.draw(self.display,[0,0],self.tamanhoc,self.tamanhoc,[self.jogador.x,self.jogador.y])
        self.display.blit(self.player.frisk,(self.jogador.x,self.jogador.y))

        if self.vec[0]== True:
            if self.jogador.y >= 0:
                self.jogador.y -= 1.4
        if self.vec[1]== True:
            if self.jogador.y <= 170:
                self.jogador.y += 1.4
        if self.vec[2]== True:
            if self.jogador.x >= 0:
                self.jogador.x -= 1.2
        if self.vec[3]== True:
            if self.jogador.x <= 370:
                self.jogador.x += 1.2

        self.tempo += 1
        if self.tempo >= 50:
            self.criarini(self.aleat)
            self.tempo=0


        for ini in self.ntocar:
            if self.ntocar[ini][2] == True:
                self.display.blit(self.vermelho,(self.ntocar[ini][0], self.ntocar[ini][1]))

                batata = self.ntocar[ini][0] - (2+self.contador*.001)
                self.coli[ini].x -= (2+self.contador*.001)
                
                self.ntocar.update({ini : [batata, self.ntocar[ini][1], self.ntocar[ini][2]]})
                if self.coli[ini].colliderect(self.jogador):
                    if self.ntocar[ini][2] == True:
                        self.erros += 1
                        self.ntocar.update({ini : [self.ntocar[ini][0], self.ntocar[ini][1], False]})
                if self.ntocar[ini][0] <= -30:
                    self.ntocar.update({ini : [self.ntocar[ini][0], self.ntocar[ini][1], False]})
                    self.apagar +=1


        if self.apagar in self.ntocar:
            self.ntocar.pop(self.apagar)



        #if self.parado == 1:
         #   self.jogador.y -= self.velocidade
          #  self.velocidade -= .1
           # self.tempo -= .1
            #if self.tempo <= 0:
             #   self.parado = 0
        #if self.jogador.y >= 100:
         #   self.velocidade=0
          #  self.parado = 0
           # self.tempo = 0


        if self.contador < 1700:
            return eventAtual,self.erros
        else:
            return event1,self.erros

    def update(self,event):
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.vec[0]=True
                if event.key == pygame.K_DOWN:
                    self.vec[1]=True
                if event.key == pygame.K_LEFT:
                    self.vec[2]=True
                if event.key == pygame.K_RIGHT:
                    self.vec[3]=True
        if event.type == pygame.QUIT:
                    pygame.quit()
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.vec[0]=False
                if event.key == pygame.K_DOWN:
                    self.vec[1]=False
                if event.key == pygame.K_LEFT:
                    self.vec[2]=False
                if event.key == pygame.K_RIGHT:
                    self.vec[3]=False

    def ativarmini1(self):
        
        self.parado = 1
        self.velocidade = 3
        self.tempo = 10

