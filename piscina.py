import pygame
from npc import *
from Hud import *
from minigame4 import *
from score import *

_=False
grama = pygame.image.load('imagens/tileset/piscina/grama.png')
piso = pygame.image.load('imagens/tileset/piscina/piso.png')
pisc2 = pygame.image.load('imagens/tileset/piscina/pisc2.png')
pisc3 = pygame.image.load('imagens/tileset/piscina/pisc3.png')
pisc4 = pygame.image.load('imagens/tileset/piscina/pisc4.png')
pisc5 = pygame.image.load('imagens/tileset/piscina/pisc5.png')
pisc6 = pygame.image.load('imagens/tileset/piscina/pisc6.png')
pisc7 = pygame.image.load('imagens/tileset/piscina/pisc7.png')
pisc8 = pygame.image.load('imagens/tileset/piscina/pisc8.png')
pisc9 = pygame.image.load('imagens/tileset/piscina/pisc9.png')
pisc10 = pygame.image.load('imagens/tileset/piscina/pisc10.png')
paredeT = pygame.image.load('imagens/tileset/fora/paredeT.png')
muroT = pygame.image.load('imagens/tileset/piscina/muroT.png')
sujeira = pygame.image.load('imagens/tileset/piscina/sujeira.png')
cerca = pygame.image.load('imagens/tileset/piscina/cerca.png')
balde = pygame.image.load('imagens/tileset/piscina/balde.png')
rede = pygame.image.load('imagens/tileset/piscina/rede.png')
tamanho = piso.get_width()
tamanhoT = piso.get_width()


minimap= [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2],
    [2, 2, 1, 8, 3, 3, 3, 3, 3, 3, 9, 1, 2, 2],
    [2, 2, 1, 5, 7, 7, 7, 7, 7, 7, 4, 1, 2, 2],
    [2, 2, 1, 5, 7, 7, 7, 7, 7, 7, 4, 1, 2, 2],
    [2, 2, 1, 11, 6, 6, 6, 6, 6, 6, 10, 1, 2, 2],
    [2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
]

layer2= [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, 5, 5, 5, 5, 5, 5, _, _, _, 1],
    [1, _, _, _, 5, 5, 5, 5, 5, 5, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 6, _, _, _, _, _, 7, 1],
    [3, _, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
]

mEvents= [
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, 4, 4, 4, 4, 4, 4, _, _, _, _],
    [_, _, _, _, 4, 4, 4, 4, 4, 4, _, _, _, _],
    [_, _, _, _, 4, 4, 4, 4, 4, 4, _, _, _, _],
    [_, _, _, _, 4, 4, 4, 4, 4, 4, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, 2, _, _, _, _, _, 3, _],
    [_, 1, _, _, _, _, _, _, _, _, _, _, _, _],
]


class Piscina:
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
        self.score = [0,Score(dis,game),0]
        self.mao=0
        self.minigame4 = Minigame4(game,dis)
        self.panela = 0
        self.acerto = 0
        self.certado=[1,0,1,0,1]
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
                    if value == 31:
                        self.vetor.append(pygame.Rect(i * tamanho,j * tamanho,tamanho,tamanho))
                    if value >= 3:
                        self.vetor.append(pygame.Rect(i * tamanhoT,j * tamanhoT,piso.get_width(),piso.get_height()*.3))
                    #elif value == 2:
                        #self.vetor.append(pygame.Rect(i * tamanhoT,(j+j*.3) * tamanhoT,wall.get_width(),wall.get_height()))

        for j, row in enumerate(self.layer2):
            for i, value in enumerate(row):
                if value:
                    self.maplayer2[(i, j)] = value
                    if value == 1 or value == 2 or value == 3 or value == 4 or value == 7:
                        self.vetor.append(pygame.Rect(i * tamanho,j * tamanho,tamanho,tamanho))
                    if value == 6:
                        self.vetor.append(pygame.Rect(i * tamanho*1.05,j * tamanho,tamanho*.6,tamanho))
                    
            
        for j, row in enumerate(self.mEvents):
            for i, value in enumerate(row):
                if value:
                    self.mapEvent[(i, j)] = value


    def change_event(self, player, mapa, eventos):
        for pos in mapa:
            if (player.x > (pos[0] * tamanho) -16) and (player.x < (pos[0] * tamanho) +32) and (player.y > (pos[1] * tamanho) - 36) and (player.y < (pos[1] * tamanho) +38):
                if mapa[pos]==2:
                    if eventos[0]==8:
                        eventos[0]=0
                        self.andar = True
                        break
                    if eventos[0]==7:
                        self.maplayer2[pos]=6
                        eventos[0]=0
                        self.game.player.mao = 0
                        self.andar=True
                        break
                    if eventos[0]==6:
                        eventos[0]=7
                    if eventos[0]==5:
                        eventos[0]=6
                        self.maplayer2[pos]=-1
                        self.game.player.mao = 14
                        self.andar=True
                    if eventos[0]==3:
                        eventos[0]=4
                    if eventos[0]==2:
                        eventos[0]=3
                    if eventos[0]==1:
                        eventos[0]=2
                    if eventos[0]==0:
                        if self.game.player.mao != 0 and self.game.player.mao != 14:
                            eventos[0] = 8
                        else:
                            eventos[0]=1
                            #self.score[0]=1
                            
            if (player.x > (pos[0] * tamanho) -16) and (player.x < (pos[0] * tamanho) +32) and (player.y > (pos[1] * tamanho) - 36) and (player.y < (pos[1] * tamanho) +25):
                if mapa[pos]==4:
                    if eventos[2]==15:
                        eventos[2]=0
                        self.certado[2]=0
                        self.andar=True
                        break
                    if eventos[2]==14:
                        eventos[2]=15
                    if eventos[2]==13:
                        eventos[2]=14
                    if eventos[2]==12:
                        eventos[2]=13
                    if eventos[2]==10:
                        eventos[2]=11
                    if eventos[2]==9:
                        eventos[2]=0
                        self.andar=True
                        break
                    if eventos[2]==8:
                        eventos[2]=-1
                        self.score[0]=1
                        self.pontos += 250
                        self.pontos += self.contar(self.certado)
                        self.pontos -= self.game.retry[2]*50
                    if eventos[2]==6:
                        eventos[2]=7
                    if eventos[2]==5:
                        eventos[2]=0
                        self.andar=True
                        self.certado[0]=0
                        break
                    if eventos[2]==3:
                        eventos[2]=4
                    if eventos[2]==2:
                        eventos[2]=3
                    if eventos[2]==1:
                        eventos[2]=2
                    if eventos[2]==0:
                        if self.game.player.mao == 14 and self.certado[0]==1:
                            eventos[2]=1
                        elif self.game.player.mao == 15 and self.certado[2]==1:
                            eventos[2]=10
                            break
                        elif self.game.player.mao != 0:
                            eventos[2]=9
                        else:
                            eventos[2]=6

            if (player.x > (pos[0] * tamanho) -16) and (player.x < (pos[0] * tamanho) +40) and (player.y > (pos[1] * tamanho) - 36) and (player.y < (pos[1] * tamanho) +38):
                if mapa[pos]==3:
                    if eventos[1]==8:
                        eventos[1]=0
                        self.andar = True
                        break
                    if eventos[1]==7:
                        self.maplayer2[pos]=7
                        eventos[1]=0
                        self.game.player.mao = 0
                        self.andar=True
                        break
                    if eventos[1]==6:
                        eventos[1]=7
                    if eventos[1]==5:
                        eventos[1]=6
                        self.maplayer2[pos]=-1
                        self.game.player.mao = 15
                        self.andar=True
                    if eventos[1]==3:
                        eventos[1]=4
                    if eventos[1]==2:
                        eventos[1]=3
                    if eventos[1]==1:
                        eventos[1]=2
                    if eventos[1]==0:
                        if self.game.player.mao != 0 and self.game.player.mao != 15:
                            eventos[1] = 8
                        else:
                            eventos[1]=1
            
                        
            
        return mapa,eventos
    
    def contar(self, vec):
        y = 0
        for x in vec:
            y -= 25*x
        return y
    
    def auto_event(self, player, mapa, eventos):
        for pos in mapa:
            if (player.x > (pos[0] * tamanho) -10) and (player.x < (pos[0] * tamanho) +22) and (player.y > (pos[1] * tamanho) - 7) and (player.y < (pos[1] * tamanho) +32):
                if mapa[pos]==1:
                    self.game.player.setpos(2,5,tamanho,0,15)
                    self.game.mapa=21

            if mapa[pos]==4:
                if eventos[2]==5:
                    self.maplayer2[pos]=-1

        return mapa,eventos


    def acao(self, player):
        self.mapEvent,self.eventos = self.change_event(player, self.mapEvent, self.eventos)
        self.minigame4.ativarmini1()

    def update(self, player):
        self.mapEvent, self.eventos = self.auto_event(player, self.mapEvent, self.eventos)


    def events(self,event):
        if self.eventos[2]==4:
            self.minigame4.update(event)

        if self.score[0]==1:
            self.score[2] = self.score[1].menuE(event,0)

        if self.score[2]==1:
            self.game.player.setpos(7,10,tamanho,0,-15)
            self.score[0]=2
            self.score[2]=0
            self.game.hud.missao = 2
            self.game.pontuacao += self.pontos

        if self.score[0]==2:
            self.score[2] = self.score[1].menuFinal(event,0)

        if self.score[2]==2:
            self.game.muda()
            
            
        
            

    def drawa(self):
        #[dis.blit(terra,(pos[0] * tamanho, pos[1] * tamanho)) for pos in self.worldmap]
        #[pygame.draw.rect(dis, 'darkgray', (pos[0] * tamanho, pos[1] * tamanho, tamanho, tamanho), 1) for pos in self.worldmap]
        if self.game.player.player_rect.x >= 190 and self.game.player.player_rect.x <= 250:
            self.scrow[0] += (self.game.player.player_rect.x -self.scrow[0]-200)/20
        if self.game.player.player_rect.y >= 95 and self.game.player.player_rect.y <= 190:
            self.scrow[1] += (self.game.player.player_rect.y -self.scrow[1]-100)/20
        
        self.dis.fill((117,228,255))

        if self.score[0]==0:
            if self.eventos[2]!=4:
                for pos in self.worldmap:
                        if self.scrow[0]  - (pos[0]*tamanho) < 30 and (pos[0]*tamanho) - self.scrow[0] < 410 and self.scrow[1]  - (pos[1]*tamanho) < 30 and (pos[1]*tamanho) - self.scrow[1] < 210:
                            if self.worldmap[pos] == 1:
                                    self.dis.blit(piso,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                            if self.worldmap[pos] == 2:
                                    self.dis.blit(grama,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                            if self.worldmap[pos] == 3:
                                    self.dis.blit(pisc2,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                            if self.worldmap[pos] == 4:
                                    self.dis.blit(pisc3,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                            if self.worldmap[pos] == 5:
                                    self.dis.blit(pisc4,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                            if self.worldmap[pos] == 6:
                                    self.dis.blit(pisc5,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                            if self.worldmap[pos] == 7:
                                    self.dis.blit(pisc6,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                            if self.worldmap[pos] == 8:
                                    self.dis.blit(pisc7,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                            if self.worldmap[pos] == 9:
                                    self.dis.blit(pisc8,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                            if self.worldmap[pos] == 10:
                                    self.dis.blit(pisc9,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                            if self.worldmap[pos] == 11:
                                    self.dis.blit(pisc10,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                            

                for pos in self.maplayer2:
                    # if self.scrow[0]  - (pos[0]*tamanho) < 235 and (pos[0]*tamanho) - self.game.player.player_rect.x < 230 and self.game.player.player_rect.y  - (pos[1]*tamanho) < 150 and (pos[1]*tamanho) - self.game.player.player_rect.y < 150:
                    if self.scrow[0]  - (pos[0]*tamanho) < 30 and (pos[0]*tamanho) - self.scrow[0] < 410 and self.scrow[1]  - (pos[1]*tamanho) < 30 and (pos[1]*tamanho) - self.scrow[1] < 210:
                        if self.maplayer2[pos] == 2:
                                    self.dis.blit(muroT,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                        if self.maplayer2[pos] == 3:
                                    self.dis.blit(cerca,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                        if self.maplayer2[pos] == 4:
                                    self.dis.blit(paredeT,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                        if self.maplayer2[pos] == 5:
                                    self.dis.blit(sujeira,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                        if self.maplayer2[pos] == 6:
                                    self.dis.blit(rede,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                        if self.maplayer2[pos] == 7:
                                    self.dis.blit(balde,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                #pygame.draw.rect(dis, 'darkgray', (pos[0] * tamanho, pos[1] * tamanho, tamanho, tamanho), 1)

          

    def drawb(self):
        
        if self.score[0]==0:
            if self.eventos[2]==4:
                self.andar=False
                self.eventos[2],self.certado[1] = self.minigame4.mini1(4,5)

            if self.eventos[0]==1:
                    self.andar=False
                    self.hud.draw('Jin','Comprei essa rede para limpar a piscina','há pouco tempo.')
            if self.eventos[0]==2:
                    self.andar=False
                    self.hud.draw('Jin','E ainda não tive a chance de usá-la.','')
            if self.eventos[0]==3:
                    self.andar=False
                    self.hud.draw('Jin','Devo usá-la?','')
            if self.eventos[0]==4:
                    self.andar=False
                    self.hud.draw('Jin','Devo usá-la?','')
                    self.eventos[0] = self.hud.Escolha(4,5,0)
            if self.eventos[0]==5:
                    self.andar=False
                    self.hud.draw('Jin','Hora de limpar a piscina.','')
            if self.eventos[0]==7:
                    self.andar=False
                    self.hud.draw('Jin','Vou guardá-la de volta aqui.','')
            if self.eventos[0]==8:
                    self.andar=False
                    self.hud.draw('Jin','Já estou com a mão ocupada.','')

            if self.eventos[1]==1:
                    self.andar=False
                    self.hud.draw('Jin','Isso aqui é um balde de água com','cloro diluído.')
            if self.eventos[1]==2:
                    self.andar=False
                    self.hud.draw('Jin','Eu o deixei pronto para jogar','na piscina.')
            if self.eventos[1]==3:
                    self.andar=False
                    self.hud.draw('Jin','Devo pegá-lo?','')
            if self.eventos[1]==4:
                    self.andar=False
                    self.hud.draw('Jin','Devo pegá-lo?','')
                    self.eventos[1] = self.hud.Escolha(4,5,0)
            if self.eventos[1]==5:
                    self.andar=False
                    self.hud.draw('Jin','Vamos jogar o cloro na piscina.','')
            if self.eventos[1]==7:
                    self.andar=False
                    self.hud.draw('Jin','Vou guardar o balde de volta.','')
            if self.eventos[1]==8:
                    self.andar=False
                    self.hud.draw('Jin','Já estou com a mão ocupada.','')

            if self.eventos[2]==1:
                    self.andar=False
                    self.hud.draw('Jin','Está na hora de limpar essa piscina.','')
            if self.eventos[2]==2:
                    self.andar=False
                    self.hud.draw('Jin','Vai começar um minigame.','Controle o movimento da rede usando o mouse.')
            if self.eventos[2]==3:
                    self.andar=False
                    self.hud.draw('Jin','O objetivo é coletar o lixo da piscina, clicando','no botão esquerdo do mouse.')
            if self.eventos[2]==5:
                    self.andar=False
                    self.hud.draw('Jin','Pronto! Piscina limpa!','')
            if self.eventos[2]==6:
                    self.andar=False
                    self.hud.draw('Jin','Posso entrar na piscina, agora?','')
            if self.eventos[2]==7:
                    self.andar=False
                    self.hud.draw('Jin','Posso entrar na piscina, agora?','')
                    self.eventos[2] = self.hud.Escolha(7,8,0)
            if self.eventos[2]==8:
                    self.andar=False
                    self.hud.draw('Jin','Bora entrar na piscina!','')
            if self.eventos[2]==9:
                    self.andar=False
                    self.hud.draw('Jin','Não posso entrar na piscina com esse item','na mão.')
            if self.eventos[2]==10:
                    self.andar=False
                    self.hud.draw('Jin','Devo colocar cloro na piscina?','')
            if self.eventos[2]==11:
                    self.andar=False
                    self.hud.draw('Jin','Devo colocar cloro na piscina?','')
                    self.eventos[2] = self.hud.Escolha(11,12,0)
            if self.eventos[2]==12:
                    self.andar=False
                    self.hud.draw('Jin','Pronto!','O cloro vai matar os germes.')
            if self.eventos[2]==13:
                    self.andar=False
                    self.hud.draw('Jin','Agora é só esperar um tempo para o cloro','fazer efeito.')
            if self.eventos[2]==14:
                    self.andar=False
                    self.hud.escurecer(5)
                    self.hud.draw('','Algumas horas depois...','')
            if self.eventos[2]==15:
                    self.andar=False
                    self.hud.clarear(5)
                    self.hud.draw('Jin','O cloro já fez efeito.','')

        if self.score[0]==1:
            self.score[1].ganhar3(self.game.retry[2],self.certado,self.pontos)

        if self.score[0]==2:
            self.score[1].ganharFinal(self.game.pontuacao)     

                #self.minigame.mini1()


                