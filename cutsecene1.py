import pygame
import math
from npc import *
from Hud import *

_=False

teto = pygame.image.load('imagens/tileset/sala/preto.png')
parede = pygame.image.load('imagens/tileset/sala/Parade.png')
chao = pygame.image.load('imagens/tileset/sala/pisoCasa.png')
televisao = pygame.image.load('imagens/tileset/sala/televisao.png')
Sofa1 = pygame.image.load('imagens/tileset/sala/Sofa1.png')
Sofa2 = pygame.image.load('imagens/tileset/sala/Sofa2.png')
mesa = pygame.image.load('imagens/tileset/sala/Mesa.png')
abajur = pygame.image.load('imagens/tileset/sala/Abajur.png')
tut0 = pygame.image.load('imagens/Hud/tut0.png')
tamanho = teto.get_width()
tamanhoT = teto.get_width()


minimap= [
    [1, 1, 1, 1, 1, 1, 1, 1, _, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 8, 1],
    [1, 8, 8, 8, 8, 8, 8, 8, 8, 1],
    [1, 8, 8, 8, 8, 8, 8, 8, 8, 1],
    [1, 8, 8, 8, 8, 8, 8, 8, 8, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

layer2= [
    [_, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _],
    [_, _, _, 4, 1, 2, 5, _, _, _],
    [_, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, 3, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _],
]

mEvents= [
    [_, _, _, _, _, _, _, _, 3, _],
    [_, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _],
]

class Cutsecene1:
    def __init__(self, game, dis):
        self.game = game
        self.minimap = minimap
        self.dis = dis
        self.layer2 = layer2
        self.mEvents = mEvents
        self.worldmap = {}
        self.maplayer2 = {}
        self.mapEvent = {}
        self.vetor = []
        self.eventos= [0,0]
        self.getmap()
        self.scrow=[0,0]
        self.asa = {}
        self.ta = 1
        self.buginganga=0
        self.hud = Hud(self.dis, game)
        self.andar=True
        self.acao(0)
        self.sofa = Npc('sofa',26,2,'parado')
        self.sofa.criarAnim(26,2,'assustado')
        self.fogo = Npc('televisao',26,2,'parado')
        self.timer=0
        self.tremer = False
        self.explodiu = False
        self.game.player.setpos(4,2,tamanho,0,15)



    def colisos(self,rect,tiles):
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list


    def getmap(self):
        for j, row in enumerate(self.minimap):
            for i, value in enumerate(row):
                if value:
                    self.worldmap[(i, j)] = value
                    if value == 1 or value ==5:
                        self.vetor.append(pygame.Rect(i * tamanho,j * tamanho,tamanho,tamanho))
                    elif value == 3 or value == 4 or value == 6 or value == 2:
                        self.vetor.append(pygame.Rect(i * tamanhoT,j * tamanhoT,parede.get_width(),parede.get_height()*.3))
                    #elif value == 2:
                        #self.vetor.append(pygame.Rect(i * tamanhoT,(j+j*.3) * tamanhoT,wall.get_width(),wall.get_height()))

        for j, row in enumerate(self.layer2):
            for i, value in enumerate(row):
                if value:
                    self.maplayer2[(i, j)] = value
                    if value == 1 or value == 2:
                        self.vetor.append(pygame.Rect(i * tamanhoT,j * tamanhoT,tamanho,tamanho*.3))
                    if value == 3:
                        self.vetor.append(pygame.Rect(i * tamanhoT,j * (tamanhoT*1.2),tamanho,tamanho*.5))
                    if value == 4 or value == 5:
                        self.vetor.append(pygame.Rect(i * tamanhoT,j * (tamanho*.6),tamanho,tamanho))
            
        for j, row in enumerate(self.mEvents):
            for i, value in enumerate(row):
                if value:
                    self.mapEvent[(i, j)] = value


    def auto_event(self, player, mapa, eventos):
        if eventos[0]==3:
            eventos[0] = self.time(30,4,3)
        if eventos[0]==8:
            eventos[0] = self.time(5,9,8)
            self.sofa.mudar('parado','assustado')
            self.explodiu = True
        return mapa,eventos
    
    def change_event(self, mapa, eventos):
        if eventos[0]==10:
            self.andar=True
            self.game.player.invisivel = False
            self.game.player.setpos(4,3,tamanho,0,-15)
            self.game.mapa=5
        if eventos[0]==9:
            self.tremer = False
            eventos[0]=10
        if eventos[0]==7:
            eventos[0]=8
            self.tremer = True
        if eventos[0]==6:
            eventos[0]=7
        if eventos[0]==5:
            eventos[0]=6
        if eventos[0]==4:
            self.timer=0
            eventos[0]=5
        if eventos[0]==2:
            eventos[0]=3
        if eventos[0]==1:
            eventos[0]=2
        if eventos[0]==0:
            eventos[0]=1
            
        return mapa,eventos
    
    def time(self,tempo,event,eventan):
        if self.timer > tempo:
            self.timer=0
            return event
        return eventan



    def acao(self, player):
        self.mapEvent, self.eventos = self.change_event(self.mapEvent, self.eventos)

    def events(self,event):
         False

    def update(self, player):
        self.mapEvent, self.eventos = self.auto_event(player, self.mapEvent, self.eventos)
        self.sofa.events()
        self.fogo.events()
        if self.buginganga == 1:
            self.game.player.invisivel = True
        if self.buginganga == 2:
            self.buginganga = -1
        if self.buginganga >=0:
            self.buginganga+=1
        if self.eventos[0]==3:
            self.timer+=.1
        if self.eventos[0]==8:
            self.timer+=.1

                

    def drawa(self):
        #[dis.blit(terra,(pos[0] * tamanho, pos[1] * tamanho)) for pos in self.worldmap]
        #[pygame.draw.rect(dis, 'darkgray', (pos[0] * tamanho, pos[1] * tamanho, tamanho, tamanho), 1) for pos in self.worldmap]
        if self.tremer == False:
            self.scrow[0] += (self.game.player.player_rect.x -self.scrow[0]-200)/20
            self.scrow[1] += (self.game.player.player_rect.y -self.scrow[1]-100)/20
        else:
            self.scrow[0] += (self.game.player.player_rect.x -self.scrow[0]-200)/20 + (math.sin(self.timer*4))*2

        for pos in self.worldmap:
            if self.worldmap[pos] == 8:
                self.dis.blit(chao,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
            if self.worldmap[pos] == 1:
                self.dis.blit(teto,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
            if self.worldmap[pos] == 2:
                self.dis.blit(parede,(pos[0] * tamanhoT-int(self.scrow[0]), pos[1] * tamanhoT-int(self.scrow[1])))
            if self.worldmap[pos] == 3:
                self.dis.blit(Sofa1,(pos[0] * tamanhoT-int(self.scrow[0]), pos[1] * tamanhoT-int(self.scrow[1])))
            if self.worldmap[pos] == 4:
                self.dis.blit(Sofa2,(pos[0] * tamanhoT-int(self.scrow[0]), pos[1] * tamanhoT-int(self.scrow[1])))


        for pos in self.maplayer2:
            if self.maplayer2[pos] == 1:
                #self.dis.blit(Sofa1,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                self.sofa.draw(self.dis,self.scrow,tamanho,tamanho,pos)

            if self.maplayer2[pos] == 2:
                self.dis.blit(Sofa2,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
            if self.maplayer2[pos] == 4:
                self.dis.blit(abajur,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * (tamanho*.9)-int(self.scrow[1])))
            if self.maplayer2[pos] == 5:
                self.dis.blit(mesa,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * (tamanho*.9)-int(self.scrow[1])))
            #pygame.draw.rect(dis, 'darkgray', (pos[0] * tamanho, pos[1] * tamanho, tamanho, tamanho), 1)

    
    def drawb(self):
        for pos in self.maplayer2:
            if self.maplayer2[pos] == 3:
                if self.explodiu == False:
                    self.dis.blit(televisao,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                else:
                    self.fogo.draw(self.dis,self.scrow,tamanho,tamanho,pos)

        if self.eventos[0]==1:
            self.andar=False
            self.game.hud.draw('Leo','Noooossa... mas que tédio!','')
            self.dis.blit(tut0,(0,0))
        if self.eventos[0]==2:
            self.andar=False
            self.game.hud.draw('Leo','Está na hora da minha série preferida.','')
        if self.eventos[0]==4:
            self.andar=False
            self.game.hud.draw('comercial','Olha só, você sabia que equipamentos','eletrônicos são perigosos?')
        if self.eventos[0]==5:
            self.andar=False
            self.game.hud.draw('comercial','Caso eles peguem fogo, é só....','')
        if self.eventos[0]==6:
            self.andar=False
            self.game.hud.draw('Leo','Esse comercial não acaba não?','')
        if self.eventos[0]==7:
            self.andar=False
            self.game.hud.draw('Leo','Quero ver a série, logo.','')
        if self.eventos[0]==9:
            self.andar=False
            self.game.hud.draw('Leo','Eiiiita! A TV explodiu, doido!','')
        if self.eventos[0]==10:
            self.andar=False
            self.game.hud.draw('Leo','Tenho que apagar isso, antes que a casa inteira','pegue fogo.')
            