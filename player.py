import pygame

friska = pygame.image.load('imagens/tileset/frisk.png')
tamanhol = friska.get_width()
tamanhoc = friska.get_height()

WINDOW_SIZE = (600,400)

global frames
frames = {}


def loadAnim(dire,duracao):
    global frames
    frame_data=[]
    nomes = dire.split('/')[-1]
    n = 0
    for frame in duracao:
        id = nomes + '-' + str(n)
        img_dir = dire + '/' + id + '.png'
        animation_image = pygame.image.load(img_dir)
        frames[id] = animation_image.copy()
        for i in range(frame):
            frame_data.append(id)
        n += 1
    return frame_data

class Player:
    def __init__(self,game,posx,posy):
        self.game = game
        self.x, self.y = 1.5,1.5
        self.angle = 0
        self.tam = 28
        self.player_rect = pygame.Rect(posx,posy,tamanhol,tamanhoc)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.corr = 1
        self.acao = 'parado'
        self.p_frame = 0
        self.flip = False
        self.data_base = {}
        self.data_base['parado']= loadAnim('animacoes/player/parado',[23,23,23])
        self.data_base['andando']= loadAnim('animacoes/player/andando',[16,13,16,13])
        self.data_base['andandoF']= loadAnim('animacoes/player/andandoF',[16,16])
        self.data_base['andandoT']= loadAnim('animacoes/player/andandoT',[16,16])
        self.lados = {'cima':False,'lado':False,'baixo':False}
        self.hud=False
        self.hud2=0
        self.event = [0,0,0]
        self.mao = 0



    
    def mudar(self,atual,pframe,novo):
        if atual != novo:
            atual = novo
            pframe = 0
        return atual,pframe

    def events(self):
        velo = (0.09*self.corr) * self.game.delta_time
        self.x=0
        self.y=0

        if self.moving_right == True:
            self.x += velo
        if self.moving_left == True:
            self.x -= velo
        if self.moving_up == True:
            self.y -= velo
        if self.moving_down == True:
            self.y += velo

        if self.x == 0 and self.y == 0:
            self.acao, self.p_frame = self.mudar(self.acao,self.p_frame,'parado')
        if self.x > 0 and self.y == 0:
            self.acao, self.p_frame = self.mudar(self.acao,self.p_frame,'andando')
            self.lados['lado'] = False
        if self.x < 0 and self.y == 0:
            self.lados['lado'] = True
            self.acao, self.p_frame = self.mudar(self.acao,self.p_frame,'andando')
        if self.y > 0:
            self.lados['cima'] = True
            self.lados['baixo'] = False
            self.acao, self.p_frame = self.mudar(self.acao,self.p_frame,'andandoF')
        if self.y < 0:
            self.lados['baixo'] = True
            self.lados['cima'] = False
            self.acao, self.p_frame = self.mudar(self.acao,self.p_frame,'andandoT')

        self.p_frame += 1
        if self.p_frame >= len(self.data_base[self.acao]):
            self.p_frame=0
        img_id = self.data_base[self.acao][self.p_frame]
        self.frisk = frames[img_id]

    def eventos(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                self.game.map.acao(self.player_rect)
                self.moving_right = False
                self.moving_left = False
                self.moving_up = False
                self.moving_down = False
        self.game.map.events(event)


    def setpos(self,x,y,tamanho, offx,offy):
        self.player_rect.x = (x*tamanho)+offx
        self.player_rect.y =  (y*tamanho)+offy


    def andar(self,event):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.hud == True:
                        self.game.map.andar = True
                        self.hud = False
                        return

            if self.game.map.andar == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.moving_right = True
                    if event.key == pygame.K_LEFT:
                        self.moving_left = True
                    if event.key == pygame.K_UP:
                        self.moving_up = True
                    if event.key == pygame.K_DOWN:
                        self.moving_down = True
                    if event.key == pygame.K_LSHIFT:
                        self.corr=1.5
                    if event.key == pygame.K_ESCAPE:
                        self.hud = True
                        self.game.map.andar = False
                        self.moving_right = False
                        self.moving_left = False
                        self.moving_up = False
                        self.moving_down = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.moving_right = False
                    if event.key == pygame.K_LEFT:
                        self.moving_left = False
                    if event.key == pygame.K_UP:
                        self.moving_up = False
                    if event.key == pygame.K_DOWN:
                        self.moving_down = False
                    if event.key == pygame.K_LSHIFT:
                        self.corr=1

            if self.hud == True:
                self.hud2 = self.game.hud.menuE(event)

            if self.hud2 == 1:
                self.game.muda()
 

    def draw(self, display):
        #if self.collisions['top'] == True:
            #pygame.draw.rect(display, 'red', (self.player_rect.x -self.game.map.scrow[0], self.player_rect.y -self.game.map.scrow[1],self.tam, self.tam), 0)
        #else:
            #pygame.draw.rect(display, 'green', (self.player_rect.x -self.game.map.scrow[0], self.player_rect.y -self.game.map.scrow[1],self.tam, self.tam), 0)
        if self.invisivel == False:
            display.blit(pygame.transform.flip(self.frisk,self.lados['lado'],False),(self.player_rect.x -int(self.game.map.scrow[0]), self.player_rect.y -int(self.game.map.scrow[1])))
        self.game.hud.drawM(self.mao)

    def drawb(self,display):
        if self.hud == True:
                self.game.hud.menuD()
    
    #def check_wall(self, x, y):
        #return (x, y) not in self.game.map.worldmap
    
    #def check_wall_collision(self, dx, dy):
        #if self.check_wall(int(self.x + dx * 6), int(self.y)):
    #        self.x += dx
    #    if self.check_wall(int(self.x), int(self.y + dy * 6)):
    #        self.y += dy

    def move(self,rect,x,y,tiles):
        collision_types = {'top':False,'bottom':False,'right':False,'left':False}
        rect.x += x
        hit_list = self.game.map.colisos(rect,tiles)
        for tile in hit_list:
            if x > 0:
                rect.right = tile.left
                collision_types['right'] = True
            elif x < 0:
                rect.left = tile.right
                collision_types['left'] = True
        rect.y += y
        hit_list = self.game.map.colisos(rect,tiles)
        for tile in hit_list:
            if y > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            elif y < 0:
                rect.top = tile.bottom
                collision_types['top'] = True
        return rect, collision_types

    def update(self):
        self.events()
        self.player_rect,self.collisions = self.move(self.player_rect, self.x, self.y,self.game.map.vetor)
        self.game.map.update(self.player_rect)

    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def pos_mapa(self):
        return int(self.x), int(self.y) 