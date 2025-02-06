import pygame

def loadIm(dire,num):
    global frames
    vetor=[]
    for x in range(num):
        id = str(x)
        img_dir = dire + '/' + id + '.png'
        animation_image = pygame.image.load(img_dir)
        vetor.append(animation_image)
    return vetor

class Hud:
    def __init__(self, dis, game):
        self.game = game
        self.display = dis
        self.texto = pygame.image.load('imagens/Hud/texto.png')
        self.sim = pygame.image.load('imagens/Hud/sim.png')
        self.nao = pygame.image.load('imagens/Hud/nao.png')
        self.luz = loadIm('imagens/Hud/luz',6)
        self.my_font = pygame.font.SysFont('Comic Sans MS', 15)
        self.my_font2 = pygame.font.SysFont('Comic Sans MS', 14)
        self.black = pygame.image.load('imagens/Hud/black.png')
        self.salvar = pygame.image.load('imagens/Hud/menub.png')
        self.mao = loadIm('imagens/Hud/maos',16)
        self.geladeira = loadIm('imagens/Hud/geladeira',7)
        self.frango = loadIm('imagens/Hud/frango',3)
        self.voltar = pygame.image.load('imagens/Hud/voltar.png')
        self.aceitar = pygame.image.load('imagens/Hud/aceitar.png')
        self.fogaoS = pygame.image.load('imagens/fase1/fogaoS.png')
        self.fogaoL = pygame.image.load('imagens/fase1/fogaoL.png')
        self.escuro = pygame.image.load('imagens/Hud/cabana/escuro.png')
        self.missao = 0
        self.sarvbut = pygame.Rect(134,45,self.salvar.get_width(),self.salvar.get_height())
        self.click = False
        self.timer=0
        self.limp=0

        self.frang=False
        self.qualfrango=0


    def drawFo(self):
        if self.limp == 0:
            self.display.blit(self.fogaoS, (0,0))
        else:
            self.display.blit(self.fogaoL, (0,0))


    def drawGe(self,eventAtual,geladeira,mao):
        m1, m2 = pygame.mouse.get_pos()
        hm1 = int(m1/3.2)
        hm2 = int(m2/3.6)

        if mao !=0:
            geladeira[mao-1]=0
            mao=0

        if self.frang == False:
            self.display.blit(self.geladeira[0], (0,0))
            if geladeira[0]==0:
                self.display.blit(self.geladeira[1], (150,85))
            if geladeira[1]==0:
                self.display.blit(self.geladeira[2], (180,85))
            if geladeira[2]==0:
                self.display.blit(self.geladeira[3], (210,85))
            if geladeira[3]==0:
                self.display.blit(self.geladeira[4], (150,125))
            if geladeira[4]==0:
                self.display.blit(self.geladeira[5], (170,125))
            if geladeira[5]==0:
                self.display.blit(self.geladeira[6], (195,135))


        if self.frang == True:
            if self.qualfrango == 1:
                self.display.blit(self.frango[0], (0,0))
            if self.qualfrango == 2:
                self.display.blit(self.frango[1], (0,0))
            if self.qualfrango == 3:
                self.display.blit(self.frango[2], (0,0))
            self.display.blit(self.aceitar, (360,170))
        self.display.blit(self.voltar, (365,10))


        fran1 = pygame.Rect(150,85,self.geladeira[1].get_width(),self.geladeira[1].get_height())
        fran2 = pygame.Rect(180,85,self.geladeira[2].get_width(),self.geladeira[2].get_height())
        fran3 = pygame.Rect(210,85,self.geladeira[3].get_width(),self.geladeira[3].get_height())
        batata = pygame.Rect(150,125,self.geladeira[4].get_width(),self.geladeira[4].get_height())
        cenoura = pygame.Rect(170,125,self.geladeira[5].get_width(),self.geladeira[5].get_height())
        panela = pygame.Rect(195,135,self.geladeira[6].get_width(),self.geladeira[6].get_height())
        voltar = pygame.Rect(365,10,self.voltar.get_width(),self.voltar.get_height())
        aceitar = pygame.Rect(365,170,self.aceitar.get_width(),self.aceitar.get_height())
        

        if self.frang == False:
            if geladeira[0]==0:
                if fran1.collidepoint((hm1, hm2)):
                    self.display.blit(self.luz[1],(150,85))
                    if self.click == True:
                        self.frang = True
                        self.qualfrango=1
                        self.click=False

            if geladeira[1]==0:
                if fran2.collidepoint((hm1, hm2)):
                    self.display.blit(self.luz[1],(180,85))
                    if self.click == True:
                        self.frang = True
                        self.qualfrango=2
                        self.click=False

            if geladeira[2]==0:
                if fran3.collidepoint((hm1, hm2)):
                    self.display.blit(self.luz[2],(210,85))
                    if self.click == True:
                        self.frang = True
                        self.qualfrango=3
                        self.click=False

            if geladeira[3]==0:
                if batata.collidepoint((hm1, hm2)):
                    self.display.blit(self.luz[3],(150,125))
                    if self.click == True:
                        self.click=False
                        geladeira[3]=1
                        return 4,geladeira,4

            if geladeira[4]==0:
                if cenoura.collidepoint((hm1, hm2)):
                    self.display.blit(self.luz[4],(170,125))
                    if self.click == True:
                        self.click=False
                        geladeira[4]=1
                        return 4,geladeira,5

            if geladeira[5]==0:
                if panela.collidepoint((hm1, hm2)):
                    self.display.blit(self.luz[5],(195,135))
                    if self.click == True:
                        self.click=False
                        geladeira[5]=1
                        return 4,geladeira,6

            if voltar.collidepoint((hm1, hm2)):
                if self.click == True:
                    self.click=False
                    return 5,geladeira,mao

        if self.frang == True:
            if voltar.collidepoint((hm1, hm2)):
                if self.click == True:
                    self.frang = False
                    self.qualfrango=0
                    self.click=False
            if aceitar.collidepoint((hm1, hm2)):
                if self.click == True:
                    if self.qualfrango == 1:
                        geladeira[0]=1
                        self.click=False
                        self.frang = False
                        return 4,geladeira,1
                    if self.qualfrango == 2:
                        geladeira[1]=1
                        self.click=False
                        self.frang = False
                        return 4,geladeira,2
                    if self.qualfrango == 3:
                        geladeira[2]=1
                        self.click=False
                        self.frang = False
                        return 4,geladeira,3

        self.click = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

        return eventAtual,geladeira,mao


    def drawM(self,num):
        self.display.blit(self.mao[num],(0,0))

    def draw(self,nome,texto,texto2):
        self.display.blit(self.texto,(20,135))
        self.text_surface = self.my_font.render(texto, False, (0, 0, 0))
        self.text_surface2 = self.my_font.render(texto2, False, (0, 0, 0))
        self.text_surface3 = self.my_font2.render(nome, False, (0, 0, 0))
        self.display.blit(self.text_surface, (24,155))
        self.display.blit(self.text_surface2, (24,175))
        self.display.blit(self.text_surface3, (40,133))

    def escurecer(self,velocidade):
        self.black.set_alpha(self.timer)
        self.timer+=1*velocidade
        if self.timer > 255:
            self.timer=255
        self.display.blit(self.black, (0,0))

    def pisca(self,velocidade):
        self.escuro.set_alpha(self.timer)
        self.timer+=1*velocidade
        if self.timer > 455:
            self.timer=0
        self.display.blit(self.escuro, (0,0))

    def clarear(self,velocidade):
        self.black.set_alpha(self.timer)
        self.timer-=1*velocidade
        if self.timer < 0:
            self.timer=0
        self.display.blit(self.black, (0,0))

    def Escolha(self,eventAtual,event1,event2):
        m1, m2 = pygame.mouse.get_pos()
        isso = pygame.Rect(20,45,self.sim.get_width(),self.sim.get_height())
        naah = pygame.Rect(230,45,self.nao.get_width(),self.nao.get_height())
        hm1 = int(m1/3.2)
        hm2 = int(m2/3.6)
        self.display.blit(self.sim,(20,45))
        self.display.blit(self.nao,(230,45))
        if isso.collidepoint((hm1, hm2)):
            self.display.blit(self.luz[0],(20,45))
            if self.click:
                self.click = False
                return event1
        if naah.collidepoint((hm1, hm2)):
            self.display.blit(self.luz[0],(230,45))
            if self.click:
                self.click = False
                self.game.map.andar = True
                return event2


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

        return eventAtual


    def menuD(self):
        self.missaoD = pygame.image.load('imagens/Hud/missao/'+str(self.missao)+'.png')
        self.black.set_alpha(100)
        self.display.blit(self.black, (0,0))
        self.display.blit(self.salvar,(134, 45))
        self.display.blit(self.missaoD,(0, 0))
        

    def menuE(self,event):
        self.m1, self.m2 = pygame.mouse.get_pos()
        self.hm1 = int(self.m1/3.2)
        self.hm2 = int(self.m2/3.6)
        if self.sarvbut.collidepoint((self.hm1, self.hm2)):
            if self.click:
                #f = open("salvar.txt", "w")
                #f.write(str(self.game.mapa)+"\n")
                #f.write(str(self.game.player.player_rect.x)+"\n")
                #f.write(str(self.game.player.player_rect.y))
                #f.close()
                self.click = False
                return 1
            
        self.click = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.click = True

        return 0

