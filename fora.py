import pygame
from npc import *
from Hud import *
from minigame2 import *
from minigame3 import *
from gameover import *

_=False
grama = pygame.image.load('imagens/tileset/fora/grama.png')
grama2 = pygame.image.load('imagens/tileset/fora/grama2.png')
garama= pygame.image.load('imagens/tileset/fora/garama.png')
garama3 = pygame.image.load('imagens/tileset/fora/garama3.png')
garama2 = pygame.image.load('imagens/tileset/fora/garama2.png')
parede = pygame.image.load('imagens/tileset/fora/parede.png')
paredeD = pygame.image.load('imagens/tileset/fora/paredeD.png')
paredeE = pygame.image.load('imagens/tileset/fora/paredeE.png')
paredeT = pygame.image.load('imagens/tileset/fora/paredeT.png')
caminho = pygame.image.load('imagens/tileset/fora/caminho.png')
porta = pygame.image.load('imagens/tileset/fora/porta.png')
preto = pygame.image.load('imagens/tileset/fora/preto.png')
nada = pygame.image.load('imagens/tileset/fora/nada.png')
parede2 = pygame.image.load('imagens/tileset/fora/parede2.png')
porta2 = pygame.image.load('imagens/tileset/fora/porta2.png')
piso2 = pygame.image.load('imagens/tileset/piscina/piso.png')
cerca = pygame.image.load('imagens/tileset/fora/cerca.png')
cercae = pygame.image.load('imagens/tileset/fora/cercaE.png')
janela = pygame.image.load('imagens/tileset/fora/janela.png')
tamanho = grama.get_width()
tamanhoT = grama.get_width()


minimap= [
    [12, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 2, 2, 2],
    [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 2, 2, 2],
    [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 10, 10, 10, 10],
    [2, 2, 9, 2, 7, 6, 6, 6, 6, 6, 6, 5, 10, 11, 10, 10],
    [2, 2, 9, 2, 7, 8, 8, 8, 8, 8, 8, 5, 2, 2, 2, 2],
    [2, 2, 9, 2, 7, 8, 8, 8, 8, 8, 8, 5, 2, 2, 2, 2],
    [2, 2, 9, 2, 7, 8, 8, 8, 8, 8, 8, 5, 2, 2, 2, 2],
    [2, 2, 9, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2],
    [2, 2, 9, 2, 3, 3, 3, 4, 3, 3, 3, 3, 2, 2, 2, 2],
    [2, 2, 9, 2, 2, 2, 2, 9, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 9, 9, 9, 9, 9, 9, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 9, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 9, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 9, 2, 2, 2, 2, 2, 2, 2, 2],
]

layer2= [
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [4, 4, 5, 4, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, 7, _, _, _, 7, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, 1, 1, 1, 1, 1, _, 3],
    [3, _, _, _, _, _, _, _, _, 6, 6, 6, 6, 6, _, 3],
    [3, _, 8, _, _, _, _, _, _, 2, 2, 2, 2, 2, _, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
]

mEvents= [
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, 4, _, _, _, _, _, _, _, _, _, _, 1, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, 2, 2, 2, 2, 2, _, _],
    [_, _, _, _, _, _, _, _, _, 2, 2, 2, 2, 2, _, _],
    [_, _, 3, _, _, _, _, _, _, 2, 2, 2, 2, 2, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
]


class Fora:
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
        self.gameover = [0,Gameover(dis,game),0,"","",""]
        self.game.player.mao=0
        self.mao=0
        self.minigame = Minigame2(game,dis)
        self.minigame3 = Minigame3(game,dis)
        self.erros = [0,1]
        self.cobra = Npc('cobra',30,2,'parado')


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
                    if value == 3 or value == 4 or value == 10 or value == 11:
                        self.vetor.append(pygame.Rect(i * tamanhoT,j * tamanhoT,parede.get_width(),parede.get_height()*.3))
                    if  value == 5 or value == 6 or value == 7 or value == 8:
                        self.vetor.append(pygame.Rect(i * tamanho,j * tamanho,tamanho,tamanho))
                    #elif value == 2:
                        #self.vetor.append(pygame.Rect(i * tamanhoT,(j+j*.3) * tamanhoT,wall.get_width(),wall.get_height()))

        for j, row in enumerate(self.layer2):
            for i, value in enumerate(row):
                if value:
                    self.maplayer2[(i, j)] = value
                    if value == 3:
                        self.vetor.append(pygame.Rect(i * tamanho,j * tamanho,tamanho,tamanho))
                    if value == 4 or value == 5:
                        self.vetor.append(pygame.Rect(i * tamanhoT,j * tamanhoT,parede.get_width(),parede.get_height()*.3))
                    
            
        for j, row in enumerate(self.mEvents):
            for i, value in enumerate(row):
                if value:
                    self.mapEvent[(i, j)] = value

    
    def retirarGrama(self,mapa):
         for pos in mapa:
              if mapa[pos]==2 or mapa[pos]==6 or mapa[pos]==1:
                   mapa[pos]=-1


    def change_event(self, player, mapa, eventos):
        for pos in mapa:
            if (player.x > (pos[0] * tamanho) -10) and (player.x < (pos[0] * tamanho) +22) and (player.y > (pos[1] * tamanho) - 7) and (player.y < (pos[1] * tamanho) +18):
                if mapa[pos]==1:
                    self.game.player.setpos(7,13,tamanho,14,-15)
                    self.game.mapa=22
                if mapa[pos]==4:
                    if eventos[3]==3:
                        self.game.player.setpos(2,5,tamanho,-15,15)
                        self.game.mapa=23
                        self.game.map23.certado[3]=self.erros[0]
                        self.game.map23.certado[4]=self.erros[1]
                    if eventos[3]==2:
                        eventos[3]=3
                    if eventos[3]==1:
                        eventos[3]=0
                        self.andar=True
                        break
                    if eventos[3]==0:
                        eventos[3]=1
            if (player.x > (pos[0] * tamanho) -10) and (player.x < (pos[0] * tamanho) +22) and (player.y > (pos[1] * tamanho) - 7) and (player.y < (pos[1] * tamanho) +32):
                  if mapa[pos]==2:
                        if eventos[0]==8:
                            self.andar=False
                            #self.game.muda()
                            self.gameover[0]=1
                            self.gameover[3]="Até mesmo em tarefas simples é importante usar os"
                            self.gameover[4]="equipamentos de proteção individual. Neste"
                            self.gameover[5]="caso devo usar os óculos de proteção."
                            
                        if eventos[0]==7:
                            eventos[0]=-1
                            eventos[3]=2
                            self.andar=True
                        if eventos[0]==5:
                            eventos[0]=6
                        if eventos[0]==4:
                            eventos[0]=5
                        if eventos[0]==3:
                            if self.game.player.event[1]==3:
                                eventos[0]=4
                            else:
                                eventos[0]=8
                        if eventos[0]==2:
                            eventos[0]=0
                            self.andar=True
                            break
                        if eventos[0]==1:
                            eventos[0]=2
                            break
                        if eventos[0]==0:
                            if self.game.player.mao == 13:
                                eventos[0]=3
                            else:
                                eventos[0]=1
                                break
            if (player.x > (pos[0] * tamanho) -10) and (player.x < (pos[0] * tamanho) +22) and (player.y > (pos[1] * tamanho) - 17) and (player.y < (pos[1] * tamanho) +32):
                  if mapa[pos]==3:
                        if eventos[1]==9:
                            self.gameover[0]=1
                            self.gameover[3]="Atacar uma cobra é algo muito arriscado de se"
                            self.gameover[4]="fazer, pois elas podem ser peçonhentas."
                            self.gameover[5]=""
                        if eventos[1]==5 or eventos[1]==7:
                            eventos[1]=-1
                            self.andar=True
                            self.erros[1]=0
                        if eventos[1]==4:
                            eventos[1]=5
                        if eventos[1]==3:
                            eventos[1]=4
                        if eventos[1]==1:
                            eventos[1]=2

        
        if eventos[2]>0:
            if eventos[2]==5:
                eventos[2]=-1
                self.andar=True
            if eventos[2]==4:
                eventos[2]=5
            if eventos[2]==3:
                eventos[2]=4
            if eventos[2]==2:
                eventos[2]=3
            if eventos[2]==1:
                eventos[2]=2
                            
                  
                        
            
        return mapa,eventos
    
    def auto_event(self, player, mapa, eventos):
        for pos in mapa:
            if (player.x > (pos[0] * tamanho) -10) and (player.x < (pos[0] * tamanho) +22) and (player.y > (pos[1] * tamanho) - 17) and (player.y < (pos[1] * tamanho) +32):
                  if mapa[pos]==3:
                        if eventos[1]==0:
                            eventos[1]=1
                        if eventos[1]==6:
                            self.game.player.setpos(2,12,tamanho,0,-15)
                            eventos[1]=0
                            self.andar = True
                            break

            if eventos[2]==0: 
                eventos[2]=1

        if self.eventos[1]==1:
            self.game.player.moving_right = False
            self.game.player.moving_left = False
            self.game.player.moving_up = False
            self.game.player.moving_down = False
        return mapa,eventos


    def acao(self, player):
        self.mapEvent,self.eventos = self.change_event(player, self.mapEvent, self.eventos)
        self.minigame.ativarmini1()
        self.minigame3.ativarmini3()

    def update(self, player):
        self.cobra.events()
        self.mapEvent, self.eventos = self.auto_event(player, self.mapEvent, self.eventos)
        if self.eventos[0]==6:
            self.retirarGrama(self.maplayer2)
        if self.eventos[1]==3 or self.eventos[1]==7:
            for pos in self.maplayer2:
                  if self.maplayer2[pos]==8:
                        self.maplayer2[pos]=-1

    def events(self,event):
        if self.eventos[1]==2:
            self.minigame3.update(event)
        if self.eventos[0]==6:
            self.minigame.update(event)
        if self.gameover[0]==1:
            self.gameover[2] = self.gameover[1].menuE(event,0)
        if self.gameover[2]==1:
            self.game.reiniciar(21)
            self.game.retry[2]+=1
            self.game.player.setpos(7,10,tamanho,0,-15)
        if self.gameover[2]==2:
            self.game.muda()
        
            

    def drawa(self):
        #[dis.blit(terra,(pos[0] * tamanho, pos[1] * tamanho)) for pos in self.worldmap]
        #[pygame.draw.rect(dis, 'darkgray', (pos[0] * tamanho, pos[1] * tamanho, tamanho, tamanho), 1) for pos in self.worldmap]



        if self.game.player.player_rect.x >= 190 and self.game.player.player_rect.x <= 320:
            self.scrow[0] += (self.game.player.player_rect.x -self.scrow[0]-200)/20
        if self.game.player.player_rect.y >= 190 and self.game.player.player_rect.y <= 390:
            self.scrow[1] += (self.game.player.player_rect.y -self.scrow[1]-100)/20
        
        if self.gameover[0]==0:
            if self.eventos[0]!=6 and self.eventos[1]!=2:
                self.dis.fill((117,228,255))
                for pos in self.worldmap:
                        if self.scrow[0]  - (pos[0]*tamanho) < 30 and (pos[0]*tamanho) - self.scrow[0] < 410 and self.scrow[1]  - (pos[1]*tamanho) < 30 and (pos[1]*tamanho) - self.scrow[1] < 210:
                            if self.worldmap[pos] == 2:
                                    self.dis.blit(grama,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                            if self.worldmap[pos] == 3:
                                    self.dis.blit(parede,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                            if self.worldmap[pos] == 4:
                                    self.dis.blit(porta,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                            if self.worldmap[pos] == 5:
                                    self.dis.blit(paredeE,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                            if self.worldmap[pos] == 6:
                                    self.dis.blit(paredeT,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                            if self.worldmap[pos] == 7:
                                    self.dis.blit(paredeD,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                            if self.worldmap[pos] == 8:
                                    self.dis.blit(preto,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                            if self.worldmap[pos] == 9:
                                    self.dis.blit(caminho,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                            if self.worldmap[pos] == 10:
                                    self.dis.blit(parede2,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                            if self.worldmap[pos] == 11:
                                    self.dis.blit(porta2,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                            if self.worldmap[pos] == 12:
                                    self.dis.blit(piso2,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                            

                for pos in self.maplayer2:
                    # if self.scrow[0]  - (pos[0]*tamanho) < 235 and (pos[0]*tamanho) - self.game.player.player_rect.x < 230 and self.game.player.player_rect.y  - (pos[1]*tamanho) < 150 and (pos[1]*tamanho) - self.game.player.player_rect.y < 150:
                    if self.scrow[0]  - (pos[0]*tamanho) < 30 and (pos[0]*tamanho) - self.scrow[0] < 410 and self.scrow[1]  - (pos[1]*tamanho) < 30 and (pos[1]*tamanho) - self.scrow[1] < 210:
                        if self.maplayer2[pos] == 1:
                                self.dis.blit(garama,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                        if self.maplayer2[pos] == 2:
                                self.dis.blit(garama3,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                        if self.maplayer2[pos] == 6:
                                self.dis.blit(garama2,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                        if self.maplayer2[pos] == 3:
                                        self.dis.blit(nada,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                        if self.maplayer2[pos] == 4:
                                    self.dis.blit(cerca,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                        if self.maplayer2[pos] == 5:
                                    self.dis.blit(cercae,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                        if self.maplayer2[pos] == 7:
                                    self.dis.blit(janela,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                        if self.maplayer2[pos] == 8:
                                    self.cobra.draw(self.dis,self.scrow,tamanho,tamanho,pos)
                #pygame.draw.rect(dis, 'darkgray', (pos[0] * tamanho, pos[1] * tamanho, tamanho, tamanho), 1)
            

          



    def drawb(self):
        
        if self.gameover[0]==0:
            if self.eventos[0]==6:
                    self.andar=False
                    self.eventos[0],self.erros[0] = self.minigame.mini1(6,7)
            #self.minigame.mini1()
            
            if self.eventos[0]!=6 and self.eventos[1]!=2:
                for pos in self.maplayer2:
                    if self.scrow[0]  - (pos[0]*tamanho) < 30 and (pos[0]*tamanho) - self.scrow[0] < 410 and self.scrow[1]  - (pos[1]*tamanho) < 30 and (pos[1]*tamanho) - self.scrow[1] < 210:
                        False

            if self.eventos[1]==2:
                self.andar=False
                self.eventos[1] = self.minigame3.drawmini2(2,3)

            if self.eventos[0]==1:
                    self.andar=False
                    self.hud.draw('Leo','A grama está alta, né?','')
            if self.eventos[0]==2:
                    self.andar=False
                    self.hud.draw('Leo','Mas, para isso, preciso encontrar o cortador de grama.','')
            if self.eventos[0]==3:
                    self.andar=False
                    self.hud.draw('Leo','Já estou com o cortador na mão, bora cortar',' essa grama!')
            if self.eventos[0]==4:
                    self.andar=False
                    self.hud.draw('','Vamos jogar um minigame.','Nele, você terá que desviar')
            if self.eventos[0]==5:
                    self.andar=False
                    self.hud.draw('','das pedras que estão no chão, para não quebrar',' o cortador de grama.')
            if self.eventos[0]==7:
                    self.andar=False
                    self.hud.draw('Leo','Grama cortada com sucesso!','')
            if self.eventos[0]==8:
                    self.andar=False
                    self.hud.escurecer(6)
                    self.hud.draw('Leo','AAAAAAHHH!! Meu olho.','Deveria ter usado o óculos de proteção')
            
            if self.eventos[1]==1:
                    self.andar=False
                    self.hud.draw('Leo','Que susto! Uma cobra.','')
            if self.eventos[1]==3:
                    self.andar=False
                    self.hud.draw('Leo','Vou ligar para os bombeiros.','')
            if self.eventos[1]==4:
                    self.andar=False
                    self.hud.escurecer(6)
                    self.hud.draw('','Um tempo depois...','')
            if self.eventos[1]==5:
                    self.andar=False
                    self.hud.clarear(6)
                    self.hud.draw('Leo','Ainda bem que chamei os bombeiros.','')
            if self.eventos[1]==5:
                    self.andar=False
                    self.hud.draw('Leo','E pensar que poderia aparecer uma','cobra no meu quintal...')

            if self.eventos[1]==7:
                    self.andar=False
                    self.hud.draw('Leo','Pronto! Consegui espantar a cobra.','')

            if self.eventos[1]==9:
                    self.andar=False
                    self.hud.draw('Leo','Não estou me sintindo muito bem...','')

            if self.eventos[2]==1:
                    self.andar=False
                    self.hud.draw('Leo','Aquele frango que preparei estava uma delícia.','')
                    self.game.player.mao=0
            if self.eventos[2]==2:
                    self.andar=False
                    self.hud.draw('Leo','E isso até me motivou a cortar a grama.', '')
            if self.eventos[2]==3:
                    self.andar=False
                    self.hud.draw('Leo','Antes disso,devo pegar o cortador e os óculos de','proteção na dispensa.')
            if self.eventos[2]==4:
                    self.andar=False
                    self.hud.draw('Leo','E quando terminar tomarei um banho relaxante','de piscina.')
            if self.eventos[2]==5:
                    self.andar=False
                    self.hud.draw('Leo','Bora trabalhar!','')

            if self.eventos[3]==1:
                    self.andar=False
                    self.hud.draw('Leo','Ainda tenho que cortar a grama.','')

                #self.minigame.mini1()

        if self.gameover[0]==1:
            self.gameover[1].menuD(self.gameover[3],self.gameover[4],self.gameover[5])   


                