import pygame
from npc import *
from Hud import *
from minigame import *

_=False
preto = pygame.image.load('imagens/tileset/cabana/preto.png')
parede = pygame.image.load('imagens/tileset/cabana/parede.png')
piso = pygame.image.load('imagens/tileset/cabana/piso.png')
oculos = pygame.image.load('imagens/tileset/cabana/oculos.png')
Soculos = pygame.image.load('imagens/tileset/cabana/Soculos.png')
cortador = pygame.image.load('imagens/tileset/cabana/cortador.png')
caixa = pygame.image.load('imagens/tileset/cabana/caixa.png')
tamanho = preto.get_width()
tamanhoT = preto.get_width()


minimap= [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 1],
    [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
    [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
    [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
    [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
    [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
    [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
    [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
    [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
    [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
    [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
    [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
    [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
    [1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1],
]

layer2= [
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, 2, _, 2, _, 2, 2, _, _, _, _], #2 CAIXA 1 CORTADOR
    [_, _, 2, _, _, _, 2, _, _, 2, _, 2, _, _],
    [_, 2, 2, _, 2, 2, _, _, 2, 2, _, 2, _, _],
    [_, _, _, _, 2, _, _, 2, 2, _, _, 2, _, _],
    [_, _, 2, _, 2, _, _, 2, _, _, 2, 2, _, _],
    [_, _, 2, _, _, _, 2, _, _, 2, _, _, _, _],
    [_, _, 2, 2, 2, 2, 2, _, 2, 2, _, 2, _, _],
    [_, _, _, _, _, _, _, _, 2, _, _, 2, _, _],
    [_, 2, 2, _, 2, 2, 2, 2, 2, _, 2, 2, 2, _],
    [_, 1, 2, _, _, _, 2, _, 2, _, _, _, _, _],
    [_, _, 2, 2, 2, _, 2, _, 2, 2, 2, _, _, _],
    [_, _, _, _, _, _, 2, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
]

mEvents= [
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _], #1CORTADOR 2 OCULOS 3 saida
    [_, _, _, _, _, _, _, 2, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, 1, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, 3, _, _, _, _, _, _],
]


class Cabana:
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
        self.eventos= [0,0,0,0,0,0,0,0,0,0]
        self.getmap()
        self.scrow=[0,0]
        self.asa = {}
        self.ta = 1
        self.hud = Hud(self.dis, game)
        self.andar=True
        self.mao=0
        self.minigame = Minigame(game,dis)
        self.panela = 0
        self.acerto = 0
        self.lavado = [0,0]
        self.errados=[0,1,1,1]


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
                    if value == 2 or value == 4:
                        self.vetor.append(pygame.Rect(i * tamanhoT,j * tamanhoT,parede.get_width(),parede.get_height()*.3))
                    #elif value == 2:
                        #self.vetor.append(pygame.Rect(i * tamanhoT,(j+j*.3) * tamanhoT,wall.get_width(),wall.get_height()))

        for j, row in enumerate(self.layer2):
            for i, value in enumerate(row):
                if value:
                    self.maplayer2[(i, j)] = value
                    if value == 12:
                        self.vetor.append(pygame.Rect(i * tamanho,j * tamanho,tamanho,tamanho))
                    if value == 1 or value == 2:
                        self.vetor.append(pygame.Rect(i * tamanhoT,j * tamanhoT,parede.get_width(),parede.get_height()*.3))
                    
            
        for j, row in enumerate(self.mEvents):
            for i, value in enumerate(row):
                if value:
                    self.mapEvent[(i, j)] = value


    def change_event(self, player, mapa, eventos):
        for pos in mapa:
            if (player.x > (pos[0] * tamanho) -16) and (player.x < (pos[0] * tamanho) +32) and (player.y > (pos[1] * tamanho) - 36) and (player.y < (pos[1] * tamanho) +38):
                if mapa[pos]==2:
                    if eventos[0]==6:
                        eventos[0]=0
                        self.worldmap[pos]=4
                        self.game.player.event[1]=0
                        self.andar=True
                        break
                    if eventos[0]==5:
                        eventos[0]=6
                    if eventos[0]==4:
                        eventos[0]=5
                        self.worldmap[pos]=5
                        self.game.player.event[1]=3
                        self.andar=True
                        break
                    if eventos[0]==2:
                        eventos[0]=3
                    if eventos[0]==1:
                        eventos[0]=2
                    if eventos[0]==0:
                        eventos[0]=1
            if (player.x > (pos[0] * tamanho) -16) and (player.x < (pos[0] * tamanho) +42) and (player.y > (pos[1] * tamanho) - 36) and (player.y < (pos[1] * tamanho) +38):
                if mapa[pos]==1:
                    if eventos[1]==8:
                        eventos[1]=0
                        self.andar = True
                        break
                    if eventos[1]==7:
                        self.maplayer2[pos]=1
                        eventos[1]=0
                        self.game.player.mao = 0
                        self.andar=True
                        break
                    if eventos[1]==6:
                        eventos[1]=7
                    if eventos[1]==5:
                        eventos[1]=6
                        self.maplayer2[pos]=-1
                        self.game.player.mao = 13
                        self.andar=True
                        break
                    if eventos[1]==3:
                        eventos[1]=4
                    if eventos[1]==2:
                        eventos[1]=3
                    if eventos[1]==1:
                        eventos[1]=2
                    if eventos[1]==0:
                        if self.game.player.mao != 0 and self.game.player.mao != 13:
                             eventos[1]=8
                        else:
                            eventos[1]=1


        
        if eventos[2]>0:
            if eventos[2]==4:
                eventos[2]=-1
                self.andar=True
            if eventos[2]==3:
                eventos[2]=4
            if eventos[2]==2:
                eventos[2]=3
            if eventos[2]==1:
                eventos[2]=2        
            
                        
            
        return mapa,eventos
    
    def auto_event(self, player, mapa, eventos):
        for pos in mapa:
            if (player.x > (pos[0] * tamanho) -10) and (player.x < (pos[0] * tamanho) +22) and (player.y > (pos[1] * tamanho) - 7) and (player.y < (pos[1] * tamanho) +32):
                 if mapa[pos]==3:
                    self.game.player.setpos(13,5,tamanho,0,15)
                    self.game.mapa=21

        if eventos[2]==0: 
            eventos[2]=1
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
                if self.scrow[0]  - (pos[0]*tamanho) < 30 and (pos[0]*tamanho) - self.scrow[0] < 410 and self.scrow[1]  - (pos[1]*tamanho) < 30 and (pos[1]*tamanho) - self.scrow[1] < 210:
                    if self.worldmap[pos] == 1:
                            self.dis.blit(preto,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                    if self.worldmap[pos] == 2:
                            self.dis.blit(parede,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                    if self.worldmap[pos] == 3:
                            self.dis.blit(piso,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                    if self.worldmap[pos] == 4:
                            self.dis.blit(oculos,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                    if self.worldmap[pos] == 5:
                            self.dis.blit(Soculos,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                    

        for pos in self.maplayer2:
            # if self.scrow[0]  - (pos[0]*tamanho) < 235 and (pos[0]*tamanho) - self.game.player.player_rect.x < 230 and self.game.player.player_rect.y  - (pos[1]*tamanho) < 150 and (pos[1]*tamanho) - self.game.player.player_rect.y < 150:
            if self.scrow[0]  - (pos[0]*tamanho) < 30 and (pos[0]*tamanho) - self.scrow[0] < 410 and self.scrow[1]  - (pos[1]*tamanho) < 30 and (pos[1]*tamanho) - self.scrow[1] < 210:
                if self.maplayer2[pos] == 1:
                            self.dis.blit(cortador,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                if self.maplayer2[pos] == 2:
                            self.dis.blit(caixa,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
            #pygame.draw.rect(dis, 'darkgray', (pos[0] * tamanho, pos[1] * tamanho, tamanho, tamanho), 1)


        self.hud.pisca(1)
          
        if self.eventos[0]==1:
                self.andar=False
                self.hud.draw('Jin','Isso aqui é um óculos de proteção.','Posso usar para proteger meus olhos')
        if self.eventos[0]==2:
                self.andar=False
                self.hud.draw('Jin','Será que devo colocar?','')
        if self.eventos[0]==3:
                self.andar=False
                self.hud.draw('Jin','Será que devo colocar?','')
                self.eventos[0] = self.hud.Escolha(3,4,0)
        if self.eventos[0]==4:
                self.andar=False
                self.hud.draw('Jin','Pronto, agora estou protegido.','')
        if self.eventos[0]==6:
                self.andar=False
                self.hud.draw('Jin','Vou guardar os óculos de volta aqui','')

        if self.eventos[1]==1:
                self.andar=False
                self.hud.draw('Jin','O cortador de grama é meio antigo.','')
        if self.eventos[1]==2:
                self.andar=False
                self.hud.draw('Jin','Está um pouco enferrujado, mas acho que serve','para o trabalho.')
        if self.eventos[1]==3:
                self.andar=False
                self.hud.draw('Jin','Será que devo usá-lo?','')
        if self.eventos[1]==4:
                self.andar=False
                self.hud.draw('Jin','Será que devo usá-lo?','')
                self.eventos[1] = self.hud.Escolha(4,5,0)
        if self.eventos[1]==5:
                self.andar=False
                self.hud.draw('Jin','Bora cortar essa grama! Não posso esquecer de','trazê-lo de volta depois de usar.')
        if self.eventos[1]==7:
                self.andar=False
                self.hud.draw('Jin','Agora que terminei,','vou deixá-lo aqui.')
        if self.eventos[1]==8:
                self.andar=False
                self.hud.draw('Jin','Não consigo pegar, já estou com a mão ocupada','')

        if self.eventos[2]==1:
                self.andar=False
                self.hud.draw('Jin','Essa dispensa está bem suja, hein!','')
        if self.eventos[2]==2:
                self.andar=False
                self.hud.draw('Jin','E muito desorganizada. Nossa!! Parece um labirinto','com todas essas caixas!')
        if self.eventos[2]==3:
                self.andar=False
                self.hud.draw('Jin','Essa luz está piscando muito.','mal consigo ver o caminho...')
        if self.eventos[2]==4:
                self.andar=False
                self.hud.draw('Jin','Tenho que procurar o cortador de grama','e os óculos de proteção que estão por aqui.')


    def drawb(self):

        
        if self.eventos[2]!=9:
            for pos in self.maplayer2:
             False

                #self.minigame.mini1()


                