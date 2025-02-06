import pygame
from npc import *
from Hud import *

_=False

wallc1 = pygame.image.load('imagens/tileset/preto.png')
white = pygame.image.load('imagens/tileset/pisoCasa.png')
wall = pygame.image.load('imagens/tileset/GRAYWALL2.png')
mes3 = pygame.image.load('imagens/tileset/mes1.png')
mes4 = pygame.image.load('imagens/tileset/mes2.png')
mes5 = pygame.image.load('imagens/tileset/mes3.png')
mes6 = pygame.image.load('imagens/tileset/mes4.png')
itens = pygame.image.load('imagens/tileset/itens/vaso.png')
tamanho = wallc1.get_width()
tamanhoT = wall.get_width()


minimap= [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 8, 1, 2, 2, 2, 1],
    [1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 8, 8, 2, 3, 6, 4, 1],
    [1, 8, 8, 3, 6, 6, 4, 8, 8, 8, 8, 8, 1, 8, 8, 8, 8, 8, 8, 1],
    [1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 2, 8, 8, 1, 8, 8, 8, 1],
    [1, 8, 8, 3, 6, 6, 4, 8, 8, 8, 8, 8, 8, 8, 8, 1, 1, 1, 1, 1],
    [1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 8, 8, 2, 2, 2, 2, 1],
    [1, 8, 8, 3, 6, 6, 4, 8, 8, 8, 8, 8, 1, 8, 8, 8, 8, 8, 8, 1],
    [1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 8, 8, 1, 3, 6, 4, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [_, _, _, _, _, 1, 1, 1, 1, 1, 1, 1, _, _, _, _],
]

layer2= [
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, 3, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, 2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
]

mEvents= [
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, 4, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, 3, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, 2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
]


class Map:
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
        self.carlos = Npc('cara')
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
                    if value == 1 or value ==5:
                        self.vetor.append(pygame.Rect(i * tamanho,j * tamanho,tamanho,tamanho))
                    elif value == 3 or value == 4 or value == 6 or value == 2:
                        self.vetor.append(pygame.Rect(i * tamanhoT,j * tamanhoT,wall.get_width(),wall.get_height()*.3))
                    #elif value == 2:
                        #self.vetor.append(pygame.Rect(i * tamanhoT,(j+j*.3) * tamanhoT,wall.get_width(),wall.get_height()))

        for j, row in enumerate(self.layer2):
            for i, value in enumerate(row):
                if value:
                    self.maplayer2[(i, j)] = value
                    if value == 3:
                        self.vetor.append(pygame.Rect(i * (tamanhoT*1.3),j * tamanhoT,tamanho*.3,tamanho*.5))
            
        for j, row in enumerate(self.mEvents):
            for i, value in enumerate(row):
                if value:
                    self.mapEvent[(i, j)] = value


    def change_event(self, player, mapa, eventos):
        for pos in mapa:
            if (player.x > (pos[0] * tamanho) -5) and (player.x < (pos[0] * tamanho) +22) and (player.y > (pos[1] * tamanho) +7) and (player.y < (pos[1] * tamanho) +22):
                if mapa[pos]==2:
                    if eventos[0]==2:
                        mapa[pos] = 1
                        self.maplayer2[pos]=1
                        eventos[0]=3
                        return mapa,eventos
                if mapa[pos]==1:
                    if eventos[0]==0:
                        mapa[pos] = -1
                        self.maplayer2[pos]=-1
                        eventos[0]=2
                        return mapa,eventos
                if mapa[pos]==3:
                    if eventos[1]==-1:
                        eventos[1]=2
                        break
                    if eventos[1]==2:
                        eventos[1]=-1
                        self.andar=True
                    if eventos[1]==1:
                        eventos[1]=2
                    if eventos[1]==0:
                        eventos[1]=1
                if mapa[pos]==4:
                    self.game.mapa=1
                    print(self.game.mapa)

        return mapa,eventos


    def acao(self, player):
        self.mapEvent,self.eventos = self.change_event(player, self.mapEvent, self.eventos)

    def update(self, player):
        self.carlos.events()

                    

    def drawa(self):
        #[dis.blit(terra,(pos[0] * tamanho, pos[1] * tamanho)) for pos in self.worldmap]
        #[pygame.draw.rect(dis, 'darkgray', (pos[0] * tamanho, pos[1] * tamanho, tamanho, tamanho), 1) for pos in self.worldmap]
        self.scrow[0] += (self.game.player.player_rect.x -self.scrow[0]-200)/20
        self.scrow[1] += (self.game.player.player_rect.y -self.scrow[1]-100)/20

        for pos in self.worldmap:
            if self.worldmap[pos] == 8:
                self.dis.blit(white,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
            elif self.worldmap[pos] == 1:
                self.dis.blit(wallc1,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
            elif self.worldmap[pos] == 2:
                self.dis.blit(wall,(pos[0] * tamanhoT-int(self.scrow[0]), pos[1] * tamanhoT-int(self.scrow[1])))
            elif self.worldmap[pos] == 3:
                self.dis.blit(mes3,(pos[0] * tamanhoT-int(self.scrow[0]), pos[1] * tamanhoT-int(self.scrow[1])))
            elif self.worldmap[pos] == 4:
                self.dis.blit(mes4,(pos[0] * tamanhoT-int(self.scrow[0]), pos[1] * tamanhoT-int(self.scrow[1])))
            elif self.worldmap[pos] == 5:
                self.dis.blit(mes5,(pos[0] * tamanhoT-int(self.scrow[0]), pos[1] * tamanhoT-int(self.scrow[1])))
            elif self.worldmap[pos] == 6:
                self.dis.blit(mes6,(pos[0] * tamanhoT-int(self.scrow[0]), pos[1] * tamanhoT-int(self.scrow[1])))

        for pos in self.maplayer2:
            if self.maplayer2[pos] == 1:
                self.dis.blit(itens,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
            if self.maplayer2[pos] == 3:
                self.carlos.draw(self.dis,self.scrow,tamanhoT*1.3,tamanhoT,pos)
            
        if self.eventos[1]==1:
            self.andar=False
            self.game.hud.draw('eaeeeeeeee')
        if self.eventos[1]==2:
            self.andar=False
            self.game.hud.draw('beleza? eu só estou vendo essa planta daqui')
            
            #pygame.draw.rect(dis, 'darkgray', (pos[0] * tamanho, pos[1] * tamanho, tamanho, tamanho), 1)