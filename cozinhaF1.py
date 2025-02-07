import pygame
from npc import *
from Hud import *
from minigame import *
from gameover import *
from score import *

_=False
teto = pygame.image.load('imagens/tileset/cozinha/preto.png')
parede = pygame.image.load('imagens/tileset/cozinha/Parade.png')
chao = pygame.image.load('imagens/tileset/cozinha/Piso.png')
armario = pygame.image.load('imagens/tileset/cozinha/armario.png')
pia = pygame.image.load('imagens/tileset/cozinha/pia.png')
cont = pygame.image.load('imagens/tileset/cozinha/contSF.png')
contCF = pygame.image.load('imagens/tileset/cozinha/contCF.png')
fogao = pygame.image.load('imagens/tileset/cozinha/fogaoP.png')
geladeira = pygame.image.load('imagens/tileset/cozinha/geladeira.png')
lixo = pygame.image.load('imagens/tileset/cozinha/lixo.png')
molhado = pygame.image.load('imagens/tileset/cozinha/PisoMolhado.png')
calendario = pygame.image.load('imagens/tileset/cozinha/calendario.png')
tamanho = teto.get_width()
tamanhoT = teto.get_width()

minimap= [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 8, 2, 2, 2, 2, 2, 4, 2, 1],
    [1, 8, 8, 8, 8, 8, 8, 8, 8, 1],
    [1, 8, 8, 8, 8, 8, 8, 8, 8, 1],
    [1, 8, 8, 8, 8, 8, 3, 8, 8, 1],
    [1, 8, 8, 8, 8, 8, 8, 8, 8, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

layer2= [
    [_, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _],
    [_, _, _, 1, 2, 2, 2, _, 5, _],
    [_, _, _, _, _, _, _, _, 3, _],
    [_, _, _, _, _, _, _, _, 4, _],
    [_, _, _, _, _, _, _, _, 7, _],
    [_, _, _, _, _, _, _, _, _, _],
]

mEvents= [
    [_, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, 10, _, _],
    [_, _, _, 2, _, 5, 6, _, 8, _],
    [_, _, _, _, _, _, _, _, 9, _],
    [_, _, _, _, _, _, 7, _, 4, _],
    [_, _, _, _, _, _, _, _, 3, _],
    [_, _, _, _, _, _, _, _, _, _],
]


class CozinhaF1:
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
        self.eventos= [0,0,0,0,0,0,0,0,0,0,0]
        self.geladeira=[0,0,0,1,1,0]
        self.getmap()
        self.scrow=[0,0]
        self.asa = {}
        self.ta = 1
        self.hud = Hud(self.dis, game)
        self.andar=True
        self.mao=0
        self.minigame = Minigame(game,dis)
        self.panela = 0
        self.gameover = [0,Gameover(dis,game),0,"","",""]
        self.score = [0,Score(dis,game),0]
        self.acerto = 0
        self.lavado = [0,0]
        self.errados=[0,1,1,1,0] #lavar F,estragado,molhado,fogao sujo, mini
        self.pontos = 0
        self.fogao = 1


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
                    elif value == 2 or value == 4:
                        self.vetor.append(pygame.Rect(i * tamanhoT,j * tamanhoT,parede.get_width(),parede.get_height()*.3))
                    #elif value == 2:
                        #self.vetor.append(pygame.Rect(i * tamanhoT,(j+j*.3) * tamanhoT,wall.get_width(),wall.get_height()))

        for j, row in enumerate(self.layer2):
            for i, value in enumerate(row):
                if value:
                    self.maplayer2[(i, j)] = value
                    if value == 1 or value == 2:
                        self.vetor.append(pygame.Rect(i * tamanhoT,j * (tamanho*.85),tamanho,tamanho*.3))
                    if value == 5 or value == 3:
                        self.vetor.append(pygame.Rect(i * (tamanho*1.05),j * tamanhoT,(tamanho*.85),tamanho))
                    if value == 4:
                        self.vetor.append(pygame.Rect(i * (tamanho*1.05),j * tamanhoT,(tamanho*.85),tamanho*.5))
                    if value == 6:
                        self.vetor.append(pygame.Rect(i * (tamanho*1.09),j * (tamanho*1.07),(tamanho*.5),tamanho*.4))
                    if value == 7:
                        self.vetor.append(pygame.Rect(i * (tamanho*1.05),j * tamanho,(tamanho*.85),tamanho))
            
        for j, row in enumerate(self.mEvents):
            for i, value in enumerate(row):
                if value:
                    self.mapEvent[(i, j)] = value


    def change_event(self, player, mapa, eventos):
        for pos in mapa:
            if (player.x > (pos[0] * tamanho) -16) and (player.x < (pos[0] * tamanho) +32) and (player.y > (pos[1] * tamanho) - 36) and (player.y < (pos[1] * tamanho) +17):
                if mapa[pos]==2:      #GELADEIRA
                    if eventos[0]==10:
                        eventos[0]=0
                        self.andar=True
                        break
                    if eventos[0]==6:
                        eventos[0]=3
                    if eventos[0]==5:
                        eventos[0]=0
                        self.andar=True
                        break
                    if eventos[0]==4:
                        eventos[0]=0
                        self.andar=True
                        break
                    if eventos[0]==2:
                        eventos[0]=3
                    if eventos[0]==1:
                        if self.errados[1] == 1:
                            eventos[0]=2
                        else:
                            eventos[0]=6
                    if eventos[0]==0:
                        if self.mao < 7:
                            eventos[0]=1
                        else:
                            eventos[0]=10

                if mapa[pos]==10:      #calendario
                    if eventos[10]==3:
                        eventos[10]=0
                        self.andar=True
                        break
                    if eventos[10]==2:
                        eventos[10]=3
                    if eventos[10]==1:
                        eventos[10]=2
                    if eventos[10]==0:
                        eventos[10]=1
                    

            if (player.x > (pos[0] * tamanho) -16) and (player.x < (pos[0] * tamanho) +16) and (player.y > (pos[1] * tamanho) - 16) and (player.y < (pos[1] * tamanho) +18):
                if mapa[pos]==3:      #LIXO
                    if eventos[1]==5:
                        eventos[1]=0
                        self.andar = True
                        break
                    if eventos[1]==4:
                        eventos[1]=0
                        break
                    if eventos[1]==3:
                        eventos[1]=4
                        if self.mao == 6:
                            self.errados[1]=0
                        self.mao=0
                        self.andar=True
                    if eventos[1]==1:
                        eventos[1]=2
                    if eventos[1]==0:
                        if self.mao == 6 or self.mao == 3:
                            eventos[1]=1
                        else:
                            eventos[1]=5
                        
                if mapa[pos]==4:      #TAUBA
                    if eventos[2]==10:
                        if self.mao == 1:
                            self.mao = 11
                        if self.mao == 2:
                            self.mao = 12
                        if self.mao == 3:
                            self.mao = 13
                        if self.mao == 4:
                            self.mao = 10
                        if self.mao == 5:
                            self.mao = 9
                        eventos[2]=7
                        self.andar=True
                        break
                    if eventos[2]==8:
                        self.minigame.ponto=0
                        eventos[2]=9
                    if eventos[2]==7:
                        if self.mao < 6 and self.mao != 0:
                            eventos[2]=8
                        else:
                            eventos[2]=6
                        break
                    if eventos[2]==6:
                        eventos[2]=7
                        self.andar=True
                        break
                    if eventos[2]==4:
                        eventos[2]=6
                        self.maplayer2[pos]=44
                        self.mao=0
                        self.andar=True
                    if eventos[2]==2:
                        eventos[2]=0
                        self.andar=True
                        break
                    if eventos[2]==1:
                        if self.mao == 7:
                            eventos[2]=4
                        else:
                            eventos[2]=2
                    if eventos[2]==0:
                        #self.score[0]=1
                        eventos[2]=1

                if mapa[pos]==5:      #FACA
                    if eventos[3]==10:
                        eventos[3]=0
                        self.andar=True
                        break
                    if eventos[3]==7:
                        if self.mao == 7:
                            eventos[3]=9
                        else:
                            eventos[3]=8
                        break
                    if eventos[3]==8: #peguei oq preciso
                        eventos[3]=7
                        self.andar=True
                    if eventos[3]==4:
                        self.mao=7
                        self.andar=True
                        eventos[3]=7
                    if eventos[3]==2:
                        eventos[3]=3
                    if eventos[3]==1:
                        eventos[3]=2
                    if eventos[3]==0:
                        if self.mao != 0:
                            eventos[3]=10
                        else:
                            eventos[3]=1
                    if eventos[3]==9: #mudar de ideia
                        eventos[3]=0
                        self.mao=0
                        self.andar=True
                        break

                if mapa[pos]==6:      #LIMPEZA
                    if eventos[4]==10:
                        eventos[4]=0
                        self.andar=True
                        break
                    if eventos[4]==7:
                        if self.mao == 8:
                            eventos[4]=9
                        else:
                            eventos[4]=8
                        break
                    if eventos[4]==8: #peguei oq preciso
                        eventos[4]=7
                        self.andar=True
                    if eventos[4]==4:
                        self.mao=8
                        self.andar=True
                        eventos[4]=7
                    if eventos[4]==2:
                        eventos[4]=3
                    if eventos[4]==1:
                        eventos[4]=2
                    if eventos[4]==0:
                        if self.mao != 0:
                            eventos[4]=10
                        else:
                            eventos[4]=1
                    if eventos[4]==9: #mudar de ideia
                        eventos[4]=0
                        self.mao=0
                        self.andar=True
                        break

                if mapa[pos]==8:      #FOGAO
                    if self.panela < 1:
                        if eventos[6]==24:
                            eventos[6]=0
                            self.fogao = 0
                            self.andar=True
                            break
                        if eventos[6]==23:
                            eventos[6]=24
                        if eventos[6]==22:
                            eventos[6]=23
                        if eventos[6]==21:
                            eventos[6]=22
                        if eventos[6]==20:
                            eventos[6]=21
                        if eventos[6]==8:
                            eventos[6]=0
                            self.andar=True
                            break
                        if eventos[6]==7:
                            self.hud.limp=1
                            self.errados[3]=0
                            eventos[6]=8
                        if eventos[6]==6:
                            eventos[6]=7
                        if eventos[6]==5:
                            eventos[6]=0
                            self.panela+=1
                            if self.mao == 11 or self.mao == 9 or self.mao == 10 or self.mao == 12:
                                self.acerto+=3
                            if self.mao == 6 or self.mao == 8 or self.mao == 3 or self.mao == 13:
                                self.acerto-=20
                            if self.mao == 7:
                                self.acerto-=5
                            self.mao = 0
                            self.andar=True
                            break
                        if eventos[6]==3:
                            eventos[6]=4
                        if eventos[6]==2:
                            eventos[6]=0
                            self.andar=True
                            break
                        if eventos[6]==1:
                            if self.mao == 0:
                                if self.fogao == 1:
                                    eventos[6]=20
                                else:
                                    eventos[6]=2
                            else:
                                if self.mao==8 and self.hud.limp == 0:
                                    eventos[6]=6
                                else:
                                    eventos[6]=3
                        if eventos[6]==0:
                            eventos[6]=1
                    else:
                        if eventos[6]==16:
                            eventos[6]=-1
                        if eventos[6]==15:
                            eventos[6]=16
                        if eventos[6]==14:
                            eventos[6]=15
                        if eventos[6]==13:
                            eventos[6]=-1
                            eventos[7]=1
                        if eventos[6]==12:
                            #self.game.muda()
                            self.gameover[0]=1
                            self.gameover[0]=1
                            self.gameover[3]="Em caso de cheiro estranho na cozinha,"
                            self.gameover[4]="verifique se há algum vazamento de gás."
                            self.gameover[5]=""
                        if eventos[6]==11:
                            eventos[6]=12
                        if eventos[6]==9:
                            eventos[6]=10
                        if eventos[6]==0:
                            eventos[6]=9

                if mapa[pos]==9:      #Pia
                    if eventos[9]==5:
                        eventos[9]=0
                        self.andar=True
                        break
                    if eventos[9]==3:
                        eventos[9]=0
                        if self.mao == 4 or self.mao == 10:
                            self.lavado[0] +=1
                        if self.mao == 5 or self.mao == 9:
                            self.lavado[1] +=1
                        if self.mao <= 3:
                            self.errados[0]=1
                        self.andar=True
                        break
                    if eventos[9]==1:
                        if self.mao == 0:
                            eventos[9]=5
                        else:
                            eventos[9]=2
                    if eventos[9]==0:
                        eventos[9]=1

            if (player.x > (pos[0] * tamanho) -16) and (player.x < (pos[0] * tamanho) +16) and (player.y > (pos[1] * tamanho) - 16) and (player.y < (pos[1] * tamanho) +16):
                if mapa[pos]==7 and self.mao != 0:
                    if eventos[5]==1:
                        #self.game.muda()
                        self.gameover[0]=1
                        self.gameover[3]="Em cozinha ou ambientes onde se usa ferramentas "
                        self.gameover[4]="afiadas, não se pode deixar o piso molhado"
                        self.gameover[5]="para não ocorrer acidentes."
                if mapa[pos]==7 and self.mao == 8:
                    if eventos[5]==3:
                        self.andar=True
                        eventos[5]=-1
                    if eventos[5]==2:
                        self.maplayer2[pos]=8
                        self.errados[2]=0
                        eventos[5]=3
                    if eventos[5]==0:
                        eventos[5]=2

        if eventos[7]>3 and eventos[7]<10:
            #self.game.muda()
            self.gameover[0]=1
            self.gameover[3]="É importante verificar sempre a validade dos alimentos."
            self.gameover[4]="Alimentos fora da validade podem causar intoxicação"
            self.gameover[5]="Dica: verifique a validade do frango, usando o calendário."
        if eventos[7]==3:
            self.pontos += 275
            self.pontos += self.contar(self.errados)
            self.pontos -= self.game.retry[1]*50
            self.score[0]=1
            self.andar = False
            eventos[7]=10
        if eventos[7]==2:
            self.panela = 0
            if self.acerto == 3:
                eventos[7]=3
            if self.acerto == 0:
                eventos[7]=4
            if self.acerto < -10:
                eventos[7]=5
            if self.acerto < -1 and self.acerto > -10:
                eventos[7]=6
        if eventos[7]==1:
            eventos[7]=2

        if eventos[8] < 7:
            if eventos[8]==5:
                self.andar = True
                eventos[8]=6
            if eventos[8]==4:
                eventos[8]=5
            if eventos[8]==3:
                eventos[8]=4
            if eventos[8]==2:
                eventos[8]=3
            if eventos[8]==1:
                eventos[8]=2
                        
            
        return mapa,eventos
    
    def auto_event(self, player, mapa, eventos):
        for pos in mapa:
            if (player.x > (pos[0] * tamanho) -10) and (player.x < (pos[0] * tamanho) +22) and (player.y > (pos[1] * tamanho) - 7) and (player.y < (pos[1] * tamanho) +32):
                if mapa[pos]==1:
                    self.game.player.setpos(2,1,tamanho,0,15)
                    self.game.mapa=1
            if (player.x > (pos[0] * tamanho) -16) and (player.x < (pos[0] * tamanho) +16) and (player.y > (pos[1] * tamanho) - 16) and (player.y < (pos[1] * tamanho) +7):
                if mapa[pos]==7 and self.mao != 0 and self.mao != 8:
                    if eventos[5]==0:
                        self.game.player.moving_right = False
                        self.game.player.moving_left = False
                        self.game.player.moving_up = False
                        self.game.player.moving_down = False
                        eventos[5]=1



        if eventos[8]==0:
            eventos[8]=1

        return mapa,eventos


    def acao(self, player):
        if self.eventos[2]==9:
            self.minigame.ativarmini1()
        self.mapEvent,self.eventos = self.change_event(player, self.mapEvent, self.eventos)

    def events(self,event):
        if self.gameover[0]==1:
            self.gameover[2] = self.gameover[1].menuE(event,0)
        if self.gameover[2]==1:
            self.game.reiniciar(11)
            self.game.retry[1]+=1
            self.game.player.setpos(1,2,tamanho,15,0)

        if self.gameover[2]==2:
            self.game.muda()

        if self.score[0]==1:
            self.score[2] = self.score[1].menuE(event,0)
        if self.score[2]==1:
            self.game.player.setpos(7,10,tamanho,0,-15)
            self.game.mapa=21
            self.game.hud.missao = 2
            self.game.pontuacao += self.pontos
        if self.score[2]==2:
            self.game.muda()

    def update(self, player):
        self.mapEvent, self.eventos = self.auto_event(player, self.mapEvent, self.eventos)
        if self.mao == 1 or self.mao == 2 or self.mao == 3: #1 bom  2 meh 3 ruim
            self.game.player.mao = 4
        if self.mao == 0:
            self.game.player.mao = 0
        if self.mao == 4:#batata
            self.game.player.mao = 5
        if self.mao == 5:#cenoura
            self.game.player.mao = 6
        if self.mao == 6:
            self.game.player.mao = 7

        if self.mao == 7:
            self.game.player.mao = 8
        if self.mao == 8:
            self.game.player.mao = 9

        if self.mao == 9:
            self.game.player.mao = 10
        if self.mao == 10:
            self.game.player.mao = 11
        if self.mao == self.mao == 11 or self.mao == 12 or self.mao == 13:
            self.game.player.mao = 12

    def contar(self, vec):
        y = 0
        for x in vec:
            y -= 25*x
        return y
            
            

    def drawa(self):
        #[dis.blit(terra,(pos[0] * tamanho, pos[1] * tamanho)) for pos in self.worldmap]
        #[pygame.draw.rect(dis, 'darkgray', (pos[0] * tamanho, pos[1] * tamanho, tamanho, tamanho), 1) for pos in self.worldmap]
        self.scrow[0] += (self.game.player.player_rect.x -self.scrow[0]-200)/20
        self.scrow[1] += (self.game.player.player_rect.y -self.scrow[1]-100)/20
        
        if self.gameover[0]==0 and self.score[0]==0:
            if self.eventos[2]!=9:
                for pos in self.worldmap:
                    if self.worldmap[pos] == 8:
                        self.dis.blit(chao,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                    elif self.worldmap[pos] == 1:
                        self.dis.blit(teto,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                    elif self.worldmap[pos] == 2:
                        self.dis.blit(parede,(pos[0] * tamanhoT-int(self.scrow[0]), pos[1] * tamanhoT-int(self.scrow[1])))
                    elif self.worldmap[pos] == 3:
                        self.dis.blit(molhado,(pos[0] * tamanhoT-int(self.scrow[0]), pos[1] * tamanhoT-int(self.scrow[1])))
                    elif self.worldmap[pos] == 4:
                        self.dis.blit(calendario,(pos[0] * tamanhoT-int(self.scrow[0]), pos[1] * tamanhoT-int(self.scrow[1])))

                for pos in self.maplayer2:
                    if self.maplayer2[pos] == 1:
                        self.dis.blit(geladeira,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * (tamanho*.85)-int(self.scrow[1])))
                    if self.maplayer2[pos] == 2:
                        self.dis.blit(armario,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * (tamanho*.85)-int(self.scrow[1])))
                    if self.maplayer2[pos] == 3:
                        self.dis.blit(pia,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                    if self.maplayer2[pos] == 4:
                        self.dis.blit(cont,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                    if self.maplayer2[pos] == 5:
                        self.dis.blit(fogao,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                    if self.maplayer2[pos] == 7:
                        self.dis.blit(lixo,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                    if self.maplayer2[pos] == 8:
                        self.dis.blit(chao,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                    if self.maplayer2[pos] == 44:
                        self.dis.blit(contCF,(pos[0] * tamanho-int(self.scrow[0]), pos[1] * tamanho-int(self.scrow[1])))
                    #pygame.draw.rect(dis, 'darkgray', (pos[0] * tamanho, pos[1] * tamanho, tamanho, tamanho), 1)

                if self.eventos[0]==1:
                    self.andar=False
                    self.hud.draw('Leo','Deixa eu ver o que tem na geladeira...','')
                if self.eventos[0]==2:
                    self.andar=False
                    self.hud.draw('Leo','Caramba, esqueci que tinha essa comida estragada','aqui na quentinha.')
                if self.eventos[0]==4:
                    self.andar=False
                    self.hud.draw('Leo','Consegui achar o que eu queria.','')
                if self.eventos[0]==5:
                    self.andar=False
                    self.hud.draw('Leo','Posso fechar a geladeira.','')
                if self.eventos[0]==6:
                    self.andar=False
                    self.hud.draw('Leo','Agora não tem aquela quentinha estragada aqui.','')
                if self.eventos[0]==10:
                    self.andar=False
                    self.hud.draw('Leo','Eu não consigo abrir a geladeira com','as mãos ocupadas.')

                if self.eventos[1]==1:
                    self.andar=False
                    self.hud.draw('','Devo jogar esse item no lixo?','')
                if self.eventos[1]==2:
                    self.andar=False
                    self.hud.draw('','Devo jogar esse item no lixo?','')
                    self.eventos[1] = self.hud.Escolha(2,3,0)
                if self.eventos[1]==3:
                    self.andar=False
                    if self.mao==0:
                        self.hud.draw('Leo','Tenho nada na mão para jogar no lixo.','')
                    else:
                        self.hud.draw('Leo','Pronto, já está no lixo.','')
                if self.eventos[1]==5:
                    self.andar=False
                    self.hud.draw('Leo','Não posso jogar este item no lixo.','')

                if self.eventos[2]==1:
                    self.andar=False
                    self.hud.draw('Leo','Essa é a tábua de cortar alimentos.','')
                if self.eventos[2]==2:
                    self.andar=False
                    self.hud.draw('Leo','Mas como é que eu corto algo sem a faca?','')
                if self.eventos[2]==4:
                    self.andar=False
                    self.hud.draw('Leo','Agora, é só botar a faca aqui e pegar','as coisas para cortar.')
                if self.eventos[2]==6:
                    self.andar=False
                    self.hud.draw('Leo','Não tenho nada para cortar.','')
                if self.eventos[2]==8:
                    self.andar=False
                    self.hud.draw('Leo','Bora cortar esse frango.','')
                if self.eventos[2]==10:
                    self.andar=False
                    self.hud.draw('Leo','Pronto, consegui cortar tudo!','')

                if self.eventos[3]==1:
                    self.andar=False
                    self.hud.draw('Leo','Essa daqui é a gavetas dos talheres.','')
                if self.eventos[3]==2:
                    self.andar=False
                    self.hud.draw('Leo','Devo pegar uma faca?','')
                if self.eventos[3]==3:
                    self.andar=False
                    self.hud.draw('Leo','Devo pegar uma faca?','')
                    self.eventos[3] = self.hud.Escolha(3,4,0)
                if self.eventos[3]==4:
                    self.andar=False
                    self.hud.draw('Leo','Agora é hora de cortar!','')
                if self.eventos[3]==6:
                    self.andar=False
                    self.hud.draw('Leo','Já peguei o que preciso.','')
                if self.eventos[3]==8:
                    self.andar=False
                    self.hud.draw('Leo','Já peguei o que preciso.','')
                if self.eventos[3]==9:
                    self.andar=False
                    self.hud.draw('Leo','Mudei de ideia, vou guardar essa faca.','')
                if self.eventos[3]==10:
                    self.andar=False
                    self.hud.draw('Leo','Eu não consigo abrir o armário com','as mãos ocupadas.')

                if self.eventos[4]==1:
                    self.andar=False
                    self.hud.draw('Leo','Aqui é o armário dos produtos de limpeza.','')
                if self.eventos[4]==2:
                    self.andar=False
                    self.hud.draw('Leo','Devo pegar algum?','')
                if self.eventos[4]==3:
                    self.andar=False
                    self.hud.draw('Leo','Devo pegar algum?','')
                    self.eventos[4] = self.hud.Escolha(3,4,0)
                if self.eventos[4]==4:
                    self.andar=False
                    self.hud.draw('Leo','Vamos limpar isso com um pano e','produto de limpeza.')
                if self.eventos[4]==8:
                    self.andar=False
                    self.hud.draw('Leo','Já peguei o que preciso.','')
                if self.eventos[4]==9:
                    self.andar=False
                    self.hud.draw('Leo','Onde é que eles estavam mesmo?','')
                if self.eventos[4]==10:
                    self.andar=False
                    self.hud.draw('Leo','Não consigo abrir o armário com','as mãos ocupadas.')

                if self.eventos[5]==2:
                    self.andar=False
                    self.hud.draw('Leo','Bora secar essa poça!','')
                if self.eventos[5]==3:
                    self.andar=False
                    self.hud.draw('Leo','Pronto, agora não corro risco de escorregar.','')
                
                if self.eventos[9]==1:
                    self.andar=False
                    self.hud.draw('Leo','Essa pia é bem grande!','')
                if self.eventos[9]==2:
                    self.andar=False
                    self.hud.draw('Leo','Devo lavar esse item?','')
                    self.eventos[9] = self.hud.Escolha(2,3,0)
                if self.eventos[9]==3:
                    self.andar=False
                    self.hud.draw('Leo','Pronto! Está lavado','')
                if self.eventos[9]==5:
                    self.andar=False
                    self.hud.draw('Leo','Não tenho nada na mão para lavar.','')

                    
                
                if self.eventos[8]==1:
                    self.andar=False
                    self.hud.draw('Leo','Hummmm!!! Bateu uma vontade de comer','frango cozido.')
                if self.eventos[8]==2:
                    self.andar=False
                    self.hud.draw('Leo','Toda essa correria para apagar o fogo me fez ','ficar com fome.')
                if self.eventos[8]==3:
                    self.andar=False
                    self.hud.draw('Leo','Fazer o frango cozido é bem simples. É só cortá-lo,','e colocá-lo na panela com água fervendo.')
                if self.eventos[8]==4:
                    self.andar=False
                    self.hud.draw('Leo','Coisa mais simples que isso não há!','')
                if self.eventos[8]==4:
                    self.andar=False
                    self.hud.draw('Leo','Posso devolver os itens que eu pegar ao local ','onde estavam.')
                if self.eventos[8]==5:
                    self.andar=False
                    self.hud.draw('Leo','Estou ouvindo um barulho e sentindo um cheiro','estranho vindo do fogão.')

                if self.eventos[10]==1:
                    self.andar=False
                    self.hud.draw('Leo','Me lembro de ter comprado este calendario em','uma feira...')
                if self.eventos[10]==2:
                    self.andar=False
                    self.hud.draw('Leo','Deixa eu ver que dia é hoje.','')
                if self.eventos[10]==3:
                    self.andar=False
                    self.hud.draw('Leo','Hoje é dia 17/10.','')




    def drawb(self):

        if self.gameover[0]==0 and self.score[0]==0:
            if self.eventos[2]==9:
                    self.andar=False
                    if self.mao <= 3:
                        self.eventos[2],self.errados[4] = self.minigame.mini1(9,10,'imagens/minigame/1/Frango.png')
                    if self.mao == 5:
                        self.eventos[2],self.errados[4] = self.minigame.mini1(9,10,'imagens/minigame/1/Cenoura.png')
                    if self.mao == 4:
                        self.eventos[2],self.errados[4] = self.minigame.mini1(9,10,'imagens/minigame/1/Batata.png')

            if self.eventos[2]!=9:
                for pos in self.maplayer2:
                    if self.eventos[0]==3:
                        self.eventos[0],self.geladeira,self.mao = self.hud.drawGe(3,self.geladeira,self.mao)

                    #self.minigame.mini1()


                    if self.eventos[5]==1:
                        self.andar=False
                        self.hud.escurecer(6)
                        self.hud.draw('Leo','UAAAAA-','')

                    if self.eventos[6]==1:
                        self.andar=False
                        self.hud.draw('Leo','Eu só tenho que colocar os ingredientes','na panela')
                        self.hud.drawFo()
                    if self.eventos[6]==2:
                        self.andar=False
                        self.hud.draw('Leo','Mas não tenho nada para colocar.','')
                        self.hud.drawFo()
                    if self.eventos[6]==3:
                        self.andar=False
                        self.hud.draw('Leo','Devo colocar esse item na panela?.','')
                        self.hud.drawFo()
                    if self.eventos[6]==4:
                        self.andar=False
                        self.hud.draw('Leo','Devo colocar esse item na panela?.','')
                        self.hud.drawFo()
                        self.eventos[6] = self.hud.Escolha(4,5,0)
                    if self.eventos[6]==5:
                        self.andar=False
                        self.hud.draw('Leo','Tomara que esse frango cozido fique bom.','')
                        self.hud.drawFo()
                    if self.eventos[6]==6:
                        self.andar=False
                        self.hud.draw('Leo','Esse fogão tá sujo, hein!','')
                        self.hud.drawFo()
                    if self.eventos[6]==7:
                        self.andar=False
                        self.hud.draw('Leo','Deixa eu limpá-lo.','')
                        self.hud.drawFo()
                    if self.eventos[6]==8:
                        self.andar=False
                        self.hud.draw('Leo','Pronto, agora sim melhorou','')
                        self.hud.drawFo()

                    if self.eventos[6]==9:
                        self.andar=False
                        self.hud.draw('','Você quer acender o fogo?','')
                        self.hud.drawFo()
                    if self.eventos[6]==10:
                        self.andar=False
                        self.hud.draw('','Você quer acender o fogo?','')
                        self.hud.drawFo()
                        if self.fogao == 1:
                            self.eventos[6] = self.hud.Escolha(10,11,0)
                        if self.fogao == 0:
                            self.eventos[6] = self.hud.Escolha(10,13,0)
                    if self.eventos[6]==11:
                        self.andar=False
                        self.hud.drawFo()
                        self.hud.escurecer(4)
                        self.hud.draw('Leo','Bora acender esse fogo','')
                    if self.eventos[6]==12:
                        self.andar=False
                        self.hud.drawFo()
                        self.hud.escurecer(4)
                        self.hud.draw('Leo','AAAAAAHHHHHH!!!','')
                    if self.eventos[6]==13:
                        self.andar=False
                        self.hud.drawFo()
                        self.hud.escurecer(4)
                        self.hud.draw('Leo','Terminei de cozinhar o frango.','')
                    if self.eventos[6]==20:
                        self.andar=False
                        self.hud.draw('Leo','Estou sentindo um cheiro estranho aqui','no fogão.')
                        self.hud.drawFo()
                    if self.eventos[6]==21:
                        self.andar=False
                        self.hud.draw('Leo','Sabia! Alguém esqueceu a boca de gás aberta.','Ufa!!! Ainda bem que não acendi o fogo.')
                        self.hud.drawFo()
                    if self.eventos[6]==22:
                        self.andar=False
                        self.hud.draw('Leo','Agora é só esperar o gás sair e volto a cozinhar','o frango depois.')
                        self.hud.drawFo()
                    if self.eventos[6]==23:
                        self.andar=False
                        self.hud.drawFo()
                        self.hud.escurecer(4)
                        self.hud.draw('','Algum tempo depois...','')
                    if self.eventos[6]==24:
                        self.andar=False
                        self.hud.drawFo()
                        self.hud.clarear(4)
                        self.hud.draw('','Vamos voltar a fazer a comida.','')
                        


                    if self.eventos[7]==2:
                        self.andar=False
                        self.hud.escurecer(5)
                        self.hud.draw('Leo','Agora o frango está feito,','bora comer!')
                    if self.eventos[7]==3:
                        self.andar=False
                        self.hud.escurecer(5)
                        self.hud.draw('Leo','Huummmm! Tá muito gostoso...','')
                    if self.eventos[7]==4:
                        self.andar=False
                        self.hud.escurecer(5)
                        self.hud.draw('Leo','Puts! Esqueci de cortar o frango,','assim não dá!')
                    if self.eventos[7]==5:
                        self.andar=False
                        self.hud.escurecer(5)
                        self.hud.draw('Leo','Ughhhhhhhhhhhhhhhhhhhhhh','')
                    if self.eventos[7]==6:
                        self.andar=False
                        self.hud.escurecer(5)
                        self.hud.draw('Leo','Caramba! Tem uma FACA aqui no frango','')

        if self.gameover[0]==1:
            self.gameover[1].menuD(self.gameover[3],self.gameover[4],self.gameover[5])  

        if self.score[0]==1:
            self.score[1].ganhar2(self.game.retry[1],self.errados,self.pontos)         