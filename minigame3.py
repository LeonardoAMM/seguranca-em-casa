import pygame
import math
import random
from npc import *
from Hud import *

class Minigame3:
    def __init__(self, game, dis):
        self.game = game
        self.display = dis
        self.fundo = pygame.image.load('imagens/minigame/3/fundo.png')
        self.atacar = pygame.image.load('imagens/minigame/3/atacar.png')
        self.fujir = pygame.image.load('imagens/minigame/3/fugir.png')
        self.acao = pygame.image.load('imagens/minigame/3/acao.png')
        self.itens = pygame.image.load('imagens/minigame/3/itens.png')
        self.soco = pygame.image.load('imagens/minigame/3/soco.png')
        self.voadora = pygame.image.load('imagens/minigame/3/voadora.png')
        self.vassoura = pygame.image.load('imagens/minigame/3/vassoura.png')
        self.pedra = pygame.image.load('imagens/minigame/3/pedra.png')
        self.ajuda = pygame.image.load('imagens/minigame/3/ajuda.png')
        self.luz = pygame.image.load('imagens/minigame/3/luz.png')
        self.voltar = pygame.image.load('imagens/minigame/3/voltar.png')
        
        self.atacarC = pygame.Rect(20,5,self.atacar.get_width(),self.atacar.get_height())
        self.acaoC = pygame.Rect(20,55,self.acao.get_width(),self.acao.get_height())
        self.itensC = pygame.Rect(300,5,self.itens.get_width(),self.itens.get_height())
        self.fujirC = pygame.Rect(300,5,self.fujir.get_width(),self.fujir.get_height())
        self.socoC = pygame.Rect(20,5,self.soco.get_width(),self.soco.get_height())
        self.voadoraC = pygame.Rect(300,5,self.voadora.get_width(),self.voadora.get_height())
        self.vassouraC = pygame.Rect(20,5,self.vassoura.get_width(),self.vassoura.get_height())
        self.pedraC = pygame.Rect(300,5,self.pedra.get_width(),self.pedra.get_height())
        self.ajudaC = pygame.Rect(20,5,self.ajuda.get_width(),self.ajuda.get_height())
        self.voltarC = pygame.Rect(20,170,self.voltar.get_width(),self.voltar.get_height())

        self.posP = [70,100]
        self.posC = [300,110]
        self.tempo = 0
        self.aleat = random.randrange(30, 170)
        self.ativa = False
        self.velocidade = 0
        self.cena=0
        self.assustado=0
        self.player = Npc('jin',21,2,'luta')
        self.cobra = Npc('cobra',21,2,'parado')
        self.player.criarAnim(82,3,'soco')
        self.player.criarAnim(30,2,'voadora')
        self.player.criarAnim(40,2,'vassoura')
        self.player.criarAnim(30,2,'pedra')
        self.cobra.criarAnim(2,1,'ataque')
        self.tempo = 0
        self.click = False
        self.hud = Hud(self.display, game)
        




    def drawmini2(self,eventAtual,event1):
        self.player.events()
        self.cobra.events()

        m1, m2 = pygame.mouse.get_pos()
        hm1 = int(m1/3.2)
        hm2 = int(m2/3.6)

        self.display.blit(self.fundo,(0,0))
        self.player.draw(self.display,[0,0],1,1,self.posP)
        self.display.blit(pygame.transform.flip(self.cobra.frisk,True,False),self.posC)

        if self.cena == 0:
            self.display.blit(self.atacar,(20,5))
            self.display.blit(self.acao,(20,55))
            self.display.blit(self.itens,(300,5))

            if self.atacarC.collidepoint((hm1, hm2)):
                self.display.blit(self.luz,(20,5))
                if self.click == True:
                    self.cena = 11
                    self.click = False
            if self.acaoC.collidepoint((hm1, hm2)):
                self.display.blit(self.luz,(20,55))
                if self.click == True:
                    self.cena = 13
                    self.click = False
            if self.itensC.collidepoint((hm1, hm2)):
                self.display.blit(self.luz,(300,5))
                if self.click == True:
                    self.cena = 12
                    self.click = False

        if self.cena == 11:
            self.display.blit(self.soco,(20,5))
            self.display.blit(self.voadora,(300,5))
            self.display.blit(self.voltar,(20,170))

            if self.socoC.collidepoint((hm1, hm2)):
                self.display.blit(self.luz,(20,5))
                if self.click == True:
                    self.cena = 1
                    self.click = False
            if self.voadoraC.collidepoint((hm1, hm2)):
                self.display.blit(self.luz,(300,5))
                if self.click == True:
                    self.cena = 5
                    self.click = False
            if self.voltarC.collidepoint((hm1, hm2)):
                if self.click == True:
                    self.cena = 0
                    self.click = False

        if self.cena == 12:
            self.display.blit(self.vassoura,(20,5))
            self.display.blit(self.pedra,(300,5))
            self.display.blit(self.voltar,(20,170))

            if self.vassouraC.collidepoint((hm1, hm2)):
                self.display.blit(self.luz,(20,5))
                if self.click == True:
                    self.cena = 6
                    self.click = False
                    self.assustado +=1
                    self.tempo = 0
            if self.pedraC.collidepoint((hm1, hm2)):
                self.display.blit(self.luz,(300,5))
                if self.click == True:
                    self.cena = 7
                    self.click = False
            if self.voltarC.collidepoint((hm1, hm2)):
                self.display.blit(self.luz,(300,5))
                if self.click == True:
                    self.cena = 0
                    self.click = False

        if self.cena == 13:
            self.display.blit(self.ajuda,(20,5))
            self.display.blit(self.fujir,(300,5))
            self.display.blit(self.voltar,(20,170))

            if self.ajudaC.collidepoint((hm1, hm2)):
                self.display.blit(self.luz,(20,5))
                if self.click == True:
                    self.click = False
                    return event1
            if self.fujirC.collidepoint((hm1, hm2)):
                self.display.blit(self.luz,(300,5))
                if self.click == True:
                    self.click = False
                    self.cena=0
                    return 6
            if self.voltarC.collidepoint((hm1, hm2)):
                self.display.blit(self.luz,(300,5))
                if self.click == True:
                    self.cena = 0
                    self.click = False

        if self.assustado == 2:
            self.cena = 15


        if self.cena == 1:
            self.posP = [270,110]
            self.player.mudar('luta','soco')
            self.hud.draw('','Jin soca a cobra','')
        if self.cena == 2:
            self.posC = [300,120]
            self.posP = [270,100]
            self.player.mudar('soco','luta')
            self.hud.draw('','A cobra desvia','')
        if self.cena == 3:
            self.posC = [300,110]
            self.cobra.mudar('parado','ataque')
            self.hud.draw('','A cobra Ataca','')
        if self.cena == 4:
            self.posC = [300,110]
            self.cobra.mudar('ataque','parado')
            self.hud.draw('','Jin foi envenado','')
            if self.tempo >= 82:
                return 9
        if self.cena == 5:
            self.posP = [270,100]
            self.player.mudar('luta','voadora')
            self.hud.draw('','Jin da uma voadora na cobra','')
        if self.cena == 6:
            self.posP = [275,100]
            self.player.mudar('luta','vassoura')
            self.hud.draw('','Jin tenta espantar a cobra com a vassoura','')
        if self.cena == 7:
            self.posP = [70,100]
            self.player.mudar('luta','pedra')
            self.hud.draw('','Jin ataca uma pedra na cobra','')
        if self.cena == 8:
            self.posC = [300,120]
            self.player.mudar('soco','luta')
            self.hud.draw('','A cobra desvia','')
        if self.cena == 9:
            self.posC = [90,105]
            self.cobra.mudar('parado','ataque')
            self.hud.draw('','A cobra ataca','')
        if self.cena == 10:
            self.posC = [90,105]
            self.cobra.mudar('ataque','parado')
            self.hud.draw('','Jin foi envenado','')
        if self.cena == 14:
            self.posC = [300,120]
            self.player.mudar('soco','luta')
            self.hud.draw('','A cobra se assusta','')
        
        if self.cena == 15:
            self.posC = [500,120]
            self.player.mudar('soco','luta')
            self.hud.draw('','A cobra foge','')
            if self.tempo >= 82:
                return 7
        
        self.tempo+=1

        self.click = False

        return eventAtual
        

        #self.player.draw(self.display,[0,0],self.tamanhoc,self.tamanhoc,[self.jogador.x,self.jogador.y])
        

    def ativarmini3(self):

        if self.cena == 1:
            if self.tempo >= 82:
                self.tempo=0
                self.cena = 2
        if self.cena == 2:
            if self.tempo >= 82:
                self.tempo = 0
                self.cena = 3
        if self.cena == 3:
            if self.tempo >= 82:
                self.tempo = 0
                self.cena = 4
        if self.cena == 5:
            if self.tempo >= 82:
                self.tempo = 0
                self.cena = 2
        if self.cena == 6:
            if self.tempo >= 82:
                self.tempo = 0
                self.cena = 14
        if self.cena == 7:
            if self.tempo >= 82:
                self.tempo = 0
                self.cena = 8
        if self.cena == 8:
            if self.tempo >= 82:
                self.tempo = 0
                self.cena = 9
        if self.cena == 9:
            if self.tempo >= 82:
                self.tempo = 0
                self.cena = 10

        if self.cena == 14:
            if self.tempo >= 82:
                self.tempo = 0
                self.cena = 0
                

    def update(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.click = True


