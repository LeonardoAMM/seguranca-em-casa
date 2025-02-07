import pygame
from npc import *
from Hud import *

_=False
teto = pygame.image.load('imagens/tileset/porao/preto.png')
parede = pygame.image.load('imagens/tileset/porao/Parade.png')
chao = pygame.image.load('imagens/tileset/porao/piso.png')
caixa = pygame.image.load('imagens/tileset/porao/caixa.png')
caixa2 = pygame.image.load('imagens/tileset/porao/caixa2.png')
pisoq = pygame.image.load('imagens/tileset/porao/pisoq.png')
extintor = pygame.image.load('imagens/tileset/porao/extintor.png')
mouseop = pygame.image.load('imagens/Hud/mouseop.png')
tamanho = teto.get_width()
tamanhoT = teto.get_width()


minimap= [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 1],
    [1, 8, 8, 8, 8, 8, 1],
    [1, 8, 8, 8, 8, 8, 1],
    [1, 8, 8, 8, 8, 8, 1],
    [1, 8, 8, 8, 8, 8, 1],
    [1, 1, 1, 8, 1, 1, 1],
]

layer2= [
    [_, _, _, _, _, _, _],
    [_, _, _, _, _, _, _],
    [_, 1, 1, 1, 1, 1, _],
    [_, 3, 1, 1, 1, 2, _],
    [_, _, _, _, _, 2, _],
    [_, 2, _, _, _, 2, _],
    [_, _, _, _, _, _, _],
]

mEvents= [
    [_, _, _, _, _, _, _],
    [_, _, _, _, _, _, _],
    [_, _, _, _, _, _, _],
    [_, 2, _, _, _, _, _],
    [_, _, _, _, _, _, _],
    [_, _, _, _, _, _, _],
    [_, _, _, 1, _, _, _],
]


class Porao:
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
        self.hud = Hud(self.dis, game)
        self.andar=True


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
                    if value == 1:
                        self.vetor.append(pygame.Rect(i * tamanho,j * tamanho,tamanho,tamanho))
                    elif value == 2 or value ==3:
                        self.vetor.append(pygame.Rect(i * tamanhoT,j * tamanhoT,parede.get_width(),parede.get_height()*.3))
                    #elif value == 2:
                        #self.vetor.append(pygame.Rect(i * tamanhoT,(j+j*.3) * tamanhoT,wall.get_width(),wall.get_height()))

        for j, row in enumerate(self.layer2):
            for i, value in enumerate(row):
                if value:
                    self.maplayer2[(i, j)] = value
                    if value == 1 or value == 2 or value ==3:
                        self.vetor.append(pygame.Rect(i * tamanhoT,j * (tamanho*.9),tamanhoT,tamanhoT*.3))
                    if value == 4:
                        self.vetor.append(pygame.Rect(i * tamanhoT,j * (tamanho*.9),tamanhoT,tamanhoT*.3))
            
        for j, row in enumerate(self.mEvents):
            for i, value in enumerate(row):
                if value:
                    self.mapEvent[(i, j)] = value


    def change_event(self, player, mapa, eventos):
        for pos in mapa:
            if (player.x > (pos[0] * tamanho) -10) and (player.x < (pos[0] * tamanho) +22) and (player.y > (pos[1] * tamanho) - 16) and (player.y < (pos[1] * tamanho) +18):
                if mapa[pos]==2:
                    if eventos[0]==8:
                        eventos[0]=0
                        self.maplayer2[pos]=3
                        self.game.player.mao = 0
                        self.game.player.event[0]=0
                        self.andar=True
                        break
                    if eventos[0]==7:
                        self.andar=True
                        eventos[0]=0
                        break
                    if eventos[0]==6:
                        eventos[0]=7
                    if eventos[0]==5:
                        eventos[0]=8
                        self.maplayer2[pos]=-1
                        self.game.player.mao = 3
                        self.game.player.event[0]=3
                        self.andar=True
                    if eventos[0]==3:
                        eventos[0]=4
                    if eventos[0]==2:
                        eventos[0]=3
                    if eventos[0]==1:
                        eventos[0]=2
                    if eventos[0]==0:
                        if self.game.player.mao != 0:
                            eventos[0]=6
                        else:
                            eventos[0]=1
            
        return mapa,eventos
    
    def auto_event(self, player, mapa, eventos):
        for pos in mapa:
            if (player.x > (pos[0] * tamanho) -10) and (player.x < (pos[0] * tamanho) +22) and (player.y > (pos[1] * tamanho) - 7) and (player.y < (pos[1] * tamanho) +18):
                if mapa[pos]==1:
                    self.game.player.setpos(8,2,tamanho,15,0)
                    self.game.mapa=1
            
        return mapa,eventos


    def acao(self, player):
        self.mapEvent,self.eventos = self.change_event(player, self.mapEvent, self.eventos)

    def update(self, player):
        self.mapEvent, self.eventos = self.auto_event(player, self.mapEvent, self.eventos)

    def events(self,event):
         False

                    

    def drawa(self):
        #[dis.blit(terra,(pos[0] * tamanho, pos[1] * tamanho)) for pos in self.worldmap]
        #[pygame.draw.rect(dis, 'darkgray', (pos[0] * tamanho, pos[1] * tamanho, tamanho, tamanho), 1) for pos in self.worldmap]
        self.scrow[0] += (self.game.player.player_rect.x -self.scrow[0]-200)/20
        self.scrow[1] += (self.game.player.player_rect.y -self.scrow[1]-100)/20

        for pos in self.worldmap:
            if self.worldmap[pos] == 8:
                self.dis.blit(chao,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
            elif self.worldmap[pos] == 1:
                self.dis.blit(teto,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
            elif self.worldmap[pos] == 2:
                self.dis.blit(parede,(pos[0] * tamanhoT-int(self.scrow[0]), pos[1] * tamanhoT-int(self.scrow[1])))

        for pos in self.maplayer2:
            if self.maplayer2[pos] == 1:
                self.dis.blit(caixa,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * (tamanho*.85)-int(self.scrow[1])))
            if self.maplayer2[pos] == 2:
                self.dis.blit(caixa2,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * (tamanho*.85)-int(self.scrow[1])))
            if self.maplayer2[pos] == 3:
                self.dis.blit(extintor,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * (tamanho*.85)-int(self.scrow[1])))


        for pos in self.maplayer2:
            if self.eventos[0]==1:
                self.andar=False
                self.game.hud.draw('Leo','Caramba! Nem lembrava de ter um outro extintor','aqui.')
            if self.eventos[0]==2:
                self.andar=False
                self.game.hud.draw('Leo','O rótulo diz que o extintor é de CO2.','')
            if self.eventos[0]==3:
                self.andar=False
                self.game.hud.draw('Leo','Será que devo pegá-lo?','')
            if self.eventos[0]==4:
                self.andar=False
                self.game.hud.draw('Leo','Será que devo pegá-lo?','')
                self.dis.blit(mouseop,(0,0))
                self.eventos[0] = self.game.hud.Escolha(4,5,0)
            if self.eventos[0]==5:
                self.andar=False
                self.game.hud.draw('Leo','Beleza! É melhor voltar para lá, antes que o fogo',' se espalhe pela casa toda.')
            if self.eventos[0]==7:
                self.andar=False
                self.game.hud.draw('Leo','Minhas mãos estão ocupadas,','não posso pegar esse extintor.')
            #pygame.draw.rect(dis, 'darkgray', (pos[0] * tamanho, pos[1] * tamanho, tamanho, tamanho), 1)

    def drawb(self):
        for pos in self.maplayer2:
            pass