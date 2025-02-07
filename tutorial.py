import pygame
from npc import *
from Hud import *
from gameover import *
from score import *

_=False

teto = pygame.image.load('imagens/tileset/sala/preto.png')
parede = pygame.image.load('imagens/tileset/sala/Parade.png')
chao = pygame.image.load('imagens/tileset/sala/pisoCasa.png')
televisao = pygame.image.load('imagens/tileset/sala/televisao.png')
Sofa1 = pygame.image.load('imagens/tileset/sala/Sofa1.png')
Sofa2 = pygame.image.load('imagens/tileset/sala/Sofa2.png')
mesa = pygame.image.load('imagens/tileset/sala/Mesa.png')
abajur = pygame.image.load('imagens/tileset/sala/Abajur.png')
tut1 = pygame.image.load('imagens/Hud/Tut1.png')
tut2 = pygame.image.load('imagens/Hud/Tut2.png')
tut4 = pygame.image.load('imagens/Hud/Tut3.png')
tut3 = pygame.image.load('imagens/Hud/Tut4.png')
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
    [_, _, _, _, 1, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _],
]

class Tutorial:
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
        self.acao(self.game.player.player_rect)
        self.scrow=[0,0]
        self.asa = {}
        self.game.player.mao=0
        self.game.player.event[0]=0
        self.ta = 1
        self.hud = Hud(self.dis, game)
        self.andar=True
        self.gameover = [0,Gameover(dis,game),0,"","",""]
        self.score = [0,Score(dis,game),0]
        self.timer=0
        self.fogo = Npc('televisao',26,2,'parado')
        self.game.player.invisivel = False
        self.pontos = 0


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
        for pos in mapa:
            if (player.x > (pos[0] * tamanho) -10) and (player.x < (pos[0] * tamanho) +22) and (player.y > (pos[1] * tamanho) - 7) and (player.y < (pos[1] * tamanho) +32):
                if mapa[pos]==3:
                    self.game.player.setpos(0,1,tamanho,25,15)
                    self.game.mapa=1
                    #self.score[0]=1
            if eventos[0]==15:
                eventos[0] = self.time(20,16,15)
            
        return mapa,eventos
    

    def time(self,tempo,event,eventan):
        if self.timer > tempo:
            self.timer=0
            return event
        return eventan


    def change_event(self, player, mapa, eventos):
        for pos in mapa:
            if (player.x > (pos[0] * tamanho) -25) and (player.x < (pos[0] * tamanho) +35) and (player.y > (pos[1] * tamanho) - 17) and (player.y < (pos[1] * tamanho) +22):
                if mapa[pos]==1:
                    if self.game.player.event[0]==0:
                        if eventos[0]==-1:
                            eventos[0]=1
                            break
                        if eventos[0]==1:
                            eventos[0]=-1
                            self.andar=True
                        if eventos[0]==0:
                            eventos[0]=1
                    if self.game.player.event[0]==1:
                        if eventos[0]==4:
                            #self.game.muda()
                            self.gameover[0]=1
                            self.gameover[3]="Em um incedio em um equipamento eletrico água"
                            self.gameover[4]="conduz eletricidade, ou seja você tem um alto"
                            self.gameover[5]="risco de levar um choque."
                        if eventos[0]==3:
                            eventos[0]=4
                        if eventos[0]==2:
                            eventos[0]=3
                        if eventos[0]==0 or eventos[0]==1 or eventos[0]== -1:
                            eventos[0]=2
                    if self.game.player.event[0]==2:
                        if eventos[0]==10:
                            #self.game.muda()
                            self.gameover[0]=1
                            self.gameover[3]="Existe diversos tipos de extintor de incêndio,"
                            self.gameover[4]="o tipo Espuma mecânica não é recomendado pois"
                            self.gameover[5]="é feito de água e ela é condutor de eletricidade."
                        if eventos[0]==9:
                            eventos[0]=10
                        if eventos[0]==8:
                            eventos[0]=9
                        if eventos[0]==7:
                            eventos[0]=8
                        if eventos[0]==6:
                            eventos[0]=7
                        if eventos[0]==0 or eventos[0]==1 or eventos[0]== -1:
                            eventos[0]=6
                    if self.game.player.event[0]==3:
                        if eventos[0]==14:
                            self.maplayer2[pos]=6
                            self.score[0]=1
                            self.pontos += 200
                            self.pontos -= self.game.retry[0]*50
                            eventos[0]=15
                        if eventos[0]==13:
                            eventos[0]=14
                        if eventos[0]==12:
                            eventos[0]=13
                        if eventos[0]==11:
                            eventos[0]=12
                            self.game.player.mao = 0
                        if eventos[0]==0 or eventos[0]==1 or eventos[0]== -1:
                            eventos[0]=11
            if eventos[1]==4:
                eventos[1]=5
                self.andar=True
                break
            if eventos[1]==3:
                eventos[1]=4
                break
            if eventos[1]==2:
                eventos[1]=3
                break
            if eventos[1]==1:
                eventos[1]=2
                break
            if eventos[1]==0:
                eventos[1]=1
                break

        return mapa,eventos


    def acao(self, player):
        self.mapEvent, self.eventos = self.change_event(player, self.mapEvent, self.eventos)

    def update(self, player):
        self.mapEvent, self.eventos = self.auto_event(player, self.mapEvent, self.eventos)

    def events(self,event):
        if self.gameover[0]==1:
            self.gameover[2] = self.gameover[1].menuE(event,0)
        if self.gameover[2]==1:
            self.game.reiniciar(5)
            self.game.player.setpos(4,3,tamanho,0,-15)
            self.game.retry[0]+=1
        if self.gameover[2]==2:
            self.game.muda()

        if self.score[0]==1:
            self.score[2] = self.score[1].menuE(event,0)
        if self.score[2]==1:
            self.game.player.setpos(1,2,tamanho,15,0)
            self.game.hud.missao = 1
            self.game.mapa=11
            self.game.pontuacao += self.pontos
        if self.score[2]==2:
            self.game.muda()

                
    def drawa(self):
        #[dis.blit(terra,(pos[0] * tamanho, pos[1] * tamanho)) for pos in self.worldmap]
        #[pygame.draw.rect(dis, 'darkgray', (pos[0] * tamanho, pos[1] * tamanho, tamanho, tamanho), 1) for pos in self.worldmap]
        self.scrow[0] += (self.game.player.player_rect.x -self.scrow[0]-200)/20
        self.scrow[1] += (self.game.player.player_rect.y -self.scrow[1]-100)/20


        if self.gameover[0]==0 and self.score[0]==0:
            for pos in self.worldmap:
                if self.worldmap[pos] == 8:
                    self.dis.blit(chao,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                elif self.worldmap[pos] == 1:
                    self.dis.blit(teto,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                elif self.worldmap[pos] == 2:
                    self.dis.blit(parede,(pos[0] * tamanhoT-int(self.scrow[0]), pos[1] * tamanhoT-int(self.scrow[1])))
                elif self.worldmap[pos] == 3:
                    self.dis.blit(Sofa1,(pos[0] * tamanhoT-int(self.scrow[0]), pos[1] * tamanhoT-int(self.scrow[1])))
                elif self.worldmap[pos] == 4:
                    self.dis.blit(Sofa2,(pos[0] * tamanhoT-int(self.scrow[0]), pos[1] * tamanhoT-int(self.scrow[1])))
                elif self.worldmap[pos] == 5:
                    self.dis.blit(televisao,(pos[0] * tamanhoT-int(self.scrow[0]), pos[1] * tamanhoT-int(self.scrow[1])))

            for pos in self.maplayer2:
                if self.maplayer2[pos] == 1:
                    self.dis.blit(Sofa1,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                if self.maplayer2[pos] == 2:
                    self.dis.blit(Sofa2,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                if self.maplayer2[pos] == 4:
                    self.dis.blit(abajur,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * (tamanho*.9)-int(self.scrow[1])))
                if self.maplayer2[pos] == 5:
                    self.dis.blit(mesa,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * (tamanho*.9)-int(self.scrow[1])))
            #pygame.draw.rect(dis, 'darkgray', (pos[0] * tamanho, pos[1] * tamanho, tamanho, tamanho), 1)
            
    
    def drawb(self):
        if self.gameover[0]==0 and self.score[0]==0:
            for pos in self.maplayer2:
                if self.maplayer2[pos] == 3:
                    self.fogo.events()
                    self.fogo.draw(self.dis,self.scrow,tamanho,tamanho,pos)
                if self.maplayer2[pos] == 6:
                    self.dis.blit(televisao,(pos[0] * tamanhoT-int(self.scrow[0]), pos[1] * tamanhoT-int(self.scrow[1])))

            if self.eventos[0]==1:
                self.andar=False
                self.hud.draw('Leo','Tenho que apagar isso logo.','')
            if self.eventos[0]==2:
                self.andar=False
                self.hud.draw('Leo','Vamos ver se a água funciona.','')
            if self.eventos[0]==3:
                self.andar=False
                self.game.hud.escurecer(6)
                self.hud.draw('Leo','Afinal água apaga o fogo né.','')
            if self.eventos[0]==4:
                self.andar=False
                self.game.hud.escurecer(4)
                self.hud.draw('Leo','AAAAAAAAA.','')
            if self.eventos[0]==6:
                self.andar=False
                self.hud.draw('Leo','Eu não esperava que este extintor fosse realmente','ser usado.')
            if self.eventos[0]==7:
                self.andar=False
                self.hud.draw('Leo','ainda bem que peguei ele.','')
            if self.eventos[0]==8:
                self.andar=False
                self.hud.escurecer(4)
                self.hud.draw('Leo','agora vamos apagar logo esse fogo chato.','')
            if self.eventos[0]==9:
                self.andar=False
                self.hud.escurecer(4)
                self.hud.draw('Leo','ué?? não esta apagando nâo.','')
            if self.eventos[0]==10:
                self.andar=False
                self.hud.escurecer(4)
                self.hud.draw('Leo','Socooooorro.','')

            if self.eventos[0]==11:
                self.andar=False
                self.hud.draw('Leo','Confio que este extintor vai funcionar.','')
            if self.eventos[0]==12:
                self.andar=False
                self.hud.draw('Leo','Por isso vamos logo apagar esse fogo.','')
            if self.eventos[0]==13:
                self.andar=False
                self.hud.escurecer(4)
                self.hud.draw('Leo','agora só apagar logo esse fogo chato.','')
            if self.eventos[0]==14:
                self.andar=False
                self.hud.escurecer(4)
                self.hud.draw('Leo','Booa, consegui apagar.','')
                

            if self.eventos[1]==1:
                self.andar=False
                self.dis.blit(tut1,(0, 0))
            if self.eventos[1]==2:
                self.andar=False
                self.dis.blit(tut2,(0, 0))
            if self.eventos[1]==3:
                self.andar=False
                self.dis.blit(tut3,(0, 0))
            if self.eventos[1]==4:
                self.andar=False
                self.dis.blit(tut4,(0, 0))
                    #self.dis.blit(televisao,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))

        if self.gameover[0]==1:
            self.gameover[1].menuD(self.gameover[3],self.gameover[4],self.gameover[5])   

        if self.score[0]==1:
            self.score[1].ganhar1(self.game.retry[0],self.pontos)   