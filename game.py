import pygame
import sys
from corredor import *
from cutsecene1 import *
from cozinha import *
from cozinhaF1 import *
from quarto import *
from player import *
from porao import *
from tutorial import *
from fora import *
from cabana import *
from piscina import *

RES = WIDTH, HEIGHT = 1280,720 #Resolução da janela

display = pygame.Surface((400,200)) #Resolção do jogo

class Menu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.novojogo = pygame.image.load('imagens/Hud/novojogo.png')
        self.novojogoBut = pygame.Rect(134,60,self.novojogo.get_width(),self.novojogo.get_height())
        self.carregar = pygame.image.load('imagens/Hud/carregar.png')
        self.carregarBut = pygame.Rect(134,165,self.carregar.get_width(),self.carregar.get_height())
        self.pontuacoes = pygame.image.load('imagens/Hud/pontuacoes.png')
        self.direitos = pygame.image.load('imagens/Hud/menu.png')
        self.pontuacoesBut = pygame.Rect(134,120,self.pontuacoes.get_width(),self.pontuacoes.get_height())
        self.click = False
        self.fases = 0

    def update(self):
        pygame.display.update()
        surf = pygame.transform.scale(display,RES)
        self.screen.blit(surf,(0, 0))

    def events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.m1, self.m2 = pygame.mouse.get_pos()
                self.hm1 = int(self.m1/3.2)
                self.hm2 = int(self.m2/3.6)
                if self.novojogoBut.collidepoint((self.hm1, self.hm2)):
                    if self.click:
                        self.click = False
                        game = Game(0,4*32,3*32)
                        game.run()

                if self.pontuacoesBut.collidepoint((self.hm1, self.hm2)):
                    if self.click:
                        self.click = False
                        pontuacao = Pontuacao()
                        pontuacao.run()

                if self.carregarBut.collidepoint((self.hm1, self.hm2)):
                    if self.click:
                        self.click = False 
                        try:
                            with open("salvar.txt") as file:
                                x=0
                                for item in file:
                                    if x == 0:
                                        mapa=int(item)
                                    if x == 1:
                                        posx=int(item)
                                    if x == 2:
                                        posy=int(item)
                                    x+=1
                            file.close()
                            game = Game(mapa,posx,posy)
                            game.run()
                        except:
                            pass

                self.click = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

    def draw(self):
        display.fill('black')
        display.blit(self.direitos,(0, 0))
        display.blit(self.novojogo,(134,60))
        display.blit(self.pontuacoes,(134, 120))

    def run(self):
        while True:
            self.events()
            self.update()
            self.draw()


class Pontuacao:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.pontuacao = pygame.image.load('imagens/Hud/pontuacao.png')
        self.my_font = pygame.font.SysFont('Comic Sans MS', 15)
        self.voltar = pygame.image.load('imagens/Hud/voltar.png')
        self.fundo = pygame.image.load('imagens/Hud/fundo.png')
        self.voltarBut = pygame.Rect(5,5,self.voltar.get_width(),self.voltar.get_height())
        self.nome = []
        self.ponto = []
        self.maiorP = []
        self.maiorN = []

        self.text_surface = []
        self.rodando = True
        self.click = False
        self.nomes()
        self.pontos()
        self.contar()
        self.rendere()

    
    def nomes(self):
        try:
            with open("score/salvar.txt") as file:
                for item in file:
                    mapa = item.split(",")
                    self.nome.append(mapa[0])
            file.close()
        except:
            pass

    
    def pontos(self):
        try:
            with open("score/salvar.txt") as file:
                for item in file:
                    mapa = item.split(",")
                    self.ponto.append(mapa[1])
            file.close()
        except:
            pass

    def contar(self):
        maior = 0
        vMaior = 0
        numero = len(self.ponto)

        if len(self.ponto) >= 5:
            numero = 5
            
        for y in range(numero):
            for x in range(len(self.ponto)):
                if int(self.ponto[x]) > maior:
                    maior = int(self.ponto[x])
                    vMaior = x
            self.maiorP.append(self.ponto[vMaior])
            self.maiorN.append(self.nome[vMaior])
            del self.ponto[vMaior]
            del self.nome[vMaior]
            maior=0


    def rendere(self):
        for x in range(len(self.maiorN)):
            self.text_surface.append(self.my_font.render(self.maiorN[x]+" = "+self.maiorP[x], False, (0, 0, 0)))


    

    def update(self):
        pygame.display.update()
        surf = pygame.transform.scale(display,RES)
        self.screen.blit(surf,(0, 0))
        pygame.display.set_caption("Bioproteção cotidiana")
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            self.m1, self.m2 = pygame.mouse.get_pos()
            self.hm1 = int(self.m1/3.2)
            self.hm2 = int(self.m2/3.6)

            if self.voltarBut.collidepoint((self.hm1, self.hm2)):
                    if self.click:
                        self.click = False
                        self.rodando = False

            self.click = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True



    def draw(self):
        display.blit(self.fundo,(0, 0))
        display.blit(self.pontuacao, (0,0))
        for x in range(len(self.text_surface)):
            display.blit(self.text_surface[x], (74,40+(x*20)))
        display.blit(self.voltar, (5,5))
        
    def run(self):
        while self.rodando:
            self.events()
            self.update()
            self.draw()


class Game:
    def __init__(self, mapa, posx, posy):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.posx = posx
        self.posy = posy
        self.novo()
        self.screen = pygame.display.set_mode(RES)
        self.mapa = mapa
        self.player.setpos(posx/32,posy/32,32,0,0)
        self.rodando = True
        self.pontuacao = 0
        self.retry = [0,0,0]

    def novo(self):
        self.player = Player(self, self.posx, self.posy)
        self.map6 = Cutsecene1(self,display)
        self.map1 = Tutorial(self,display)
        self.map2 = Corredor(self,display)
        self.map3 = Cozinha(self,display)
        self.map4 = Quarto(self,display)
        self.map5 = Porao(self,display)
        self.map11 = CozinhaF1(self,display)
        self.map21 = Fora(self,display)
        self.map22 = Cabana(self,display)
        self.map23 = Piscina(self,display)
        self.map = self.map6
        self.hud = Hud(display, self)
        self.player.player_rect.x

    def muda(self):
        self.rodando = False

    def reiniciar(self,value):
        if value == 11:
            self.map11 = CozinhaF1(self,display)
        if value == 5:
            self.map1 = Tutorial(self,display)
            self.map2 = Corredor(self,display)
            self.map3 = Cozinha(self,display)
        if value == 21:
            self.map21 = Fora(self,display)
            self.map22 = Cabana(self,display)

            
    def mudar(self,atual,novo):
        if atual != novo:
            atual = novo
        return atual
    
    def mudar2(self,atual,novo):
        if atual != novo:
            atual = novo
            self.map21 = atual
        return atual

    def update(self):
        self.player.update()
        pygame.display.update()
        self.delta_time = self.clock.tick(100)
        pygame.display.set_caption("Bioproteção cotidiana")
        surf = pygame.transform.scale(display,RES)
        self.screen.blit(surf,(0, 0))

        if self.mapa==0:
            self.map = self.mudar(self.map, self.map6)
        if self.mapa==1:
            self.map = self.mudar(self.map, self.map2)
        if self.mapa==2:
            self.map = self.mudar(self.map, self.map3)
        if self.mapa==3:
            self.map = self.mudar(self.map, self.map4)
        if self.mapa==4:
            self.map = self.mudar(self.map, self.map5)
        if self.mapa==5:
            self.map = self.mudar(self.map, self.map1)
        if self.mapa==11:
            self.map = self.mudar(self.map, self.map11)
        if self.mapa==21:
            self.map = self.mudar(self.map, self.map21)
        if self.mapa==22:
            self.map = self.mudar(self.map, self.map22)
        if self.mapa==23:
            self.map = self.mudar(self.map, self.map23)


    def draw(self):
        display.fill('black')
        self.map.drawa()
        self.player.draw(display)
        self.map.drawb()
        self.player.drawb(display)

    def events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.player.andar(event)
                self.player.eventos(event)
        

    def run(self):
        while self.rodando:
            self.events()
            self.update()
            self.draw()

    
menu = Menu()
menu.run()

#pygame.display.update()