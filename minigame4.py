import pygame
import math
import random
from npc import *

class Minigame4:
    def __init__(self, game, dis):
        self.game = game
        self.display = dis
        self.rede = pygame.image.load('imagens/minigame/4/rede.png')
        self.fundo = pygame.image.load('imagens/minigame/4/fundo.png')
        self.rede2 = pygame.image.load('imagens/minigame/4/rede2.png')
        self.sujeira = pygame.image.load('imagens/minigame/4/sujeira.png')
        self.tamanhol = self.sujeira.get_width()
        self.tamanhoc = self.sujeira.get_height()
        self.redeco = pygame.Rect(110,100,self.tamanhol,self.tamanhoc)
        self.ntocar = {}
        self.coli=[]
        self.contador = 0
        self.vec=[False,False,False,False]
        self.pos = 0
        self.parado = 0
        self.aleat = random.randrange(30, 150)
        self.ativa = False
        self.velocidade = 0
        self.machucar=0
        self.subir = False
        self.apagar=-1
        self.tempo = 0
        self.id = 0
        self.criarini(self.aleat)
        self.fun1 = 0
        self.fun2 = 400
        self.click = False
        self.error = 0


    def criarini(self,posy):
        asd = random.randrange(0, 2)
        self.ntocar[self.id]  = [400*(asd),posy,True,asd, pygame.Rect(400*(asd),posy,self.tamanhol,self.tamanhol)]
        #self.coli.append(pygame.Rect(400*(asd),posy,self.tamanhol,self.tamanhol))
        self.id += 1
        self.aleat = random.randrange(30, 150)



    def mini1(self,eventAtual,event1):

        m1, m2 = pygame.mouse.get_pos()
        hm1 = int(m1/3.2)
        hm2 = int(m2/3.6)

        self.display.blit(self.fundo,(0,0))
        self.redeco = pygame.Rect(hm1-13,hm2-12,self.tamanhol,self.tamanhoc)
  


        self.contador += 1

        #self.player.draw(self.display,[0,0],self.tamanhoc,self.tamanhoc,[self.jogador.x,self.jogador.y])
        if self.click == False:
            self.display.blit(self.rede,(hm1-10,hm2-10))
        else:
            self.display.blit(self.rede2,(hm1-10,hm2))

        self.tempo += 1
        if self.tempo >= 50:
            self.criarini(self.aleat)
            self.tempo=0


        for ini in self.ntocar:
            if self.ntocar[ini][2] == True:
                self.display.blit(self.sujeira,(self.ntocar[ini][0], self.ntocar[ini][1]))
                if self.ntocar[ini][3] == 1:
                    batata = self.ntocar[ini][0] - 2
                    frita = self.ntocar[ini][4]
                    frita.x -= 2
                    #self.coli[ini].x -= (2)
                else:
                    batata = self.ntocar[ini][0] + 2
                    frita = self.ntocar[ini][4]
                    frita.x += 2
                    #self.coli[ini].x += (2)
                self.ntocar.update({ini : [batata, self.ntocar[ini][1], self.ntocar[ini][2], self.ntocar[ini][3], frita]})

                #if self.coli[ini].colliderect(self.redeco):
                if self.ntocar[ini][4].colliderect(self.redeco):
                    if self.subir == True:
                        self.ntocar.update({ini : [self.ntocar[ini][0], self.ntocar[ini][1], False, self.ntocar[ini][3], self.ntocar[ini][4]]})
                        self.apagar +=1

                if self.ntocar[ini][0] <= -30 or self.ntocar[ini][0] >= 430:
                    self.ntocar.update({ini : [self.ntocar[ini][0], self.ntocar[ini][1], False, self.ntocar[ini][3], self.ntocar[ini][4]]})
                    self.apagar +=1
                    self.error+=1

        self.subir = False

        if self.apagar in self.ntocar:
            self.ntocar.pop(self.apagar)

        if self.contador < 1700:
            return eventAtual,self.error
        else:
            return event1,self.error




    def update(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.click = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.subir = True
                self.click = False


    def ativarmini1(self):
        
        self.parado = 1
        self.velocidade = 3
        self.tempo = 10

