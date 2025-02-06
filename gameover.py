import pygame

class Gameover:
    def __init__(self, dis, game):
        self.game = game
        self.display = dis
        self.texto = pygame.image.load('imagens/Hud/texto.png')
        self.my_font = pygame.font.SysFont('Comic Sans MS', 15)
        self.my_font2 = pygame.font.SysFont('Comic Sans MS', 14)
        self.voltar = pygame.image.load('imagens/Hud/voltar.png')
        self.tentar = pygame.image.load('imagens/Hud/gameover/tentar.png')
        self.luzt = [0,pygame.image.load('imagens/Hud/gameover/luzt.png')]
        self.menu = pygame.image.load('imagens/Hud/gameover/menu.png')
        self.luzm = [0,pygame.image.load('imagens/Hud/gameover/luzm.png')]
        self.gameover = pygame.image.load('imagens/Hud/gameover/gameover.png')
        self.tentarB = pygame.Rect(50,60,self.tentar.get_width(),self.tentar.get_height())
        self.menuB = pygame.Rect(250,60,self.menu.get_width(),self.menu.get_height())
        self.click = False


    def menuD(self,texto,texto2,texto3):
        self.display.fill('black')
        self.display.blit(self.gameover, (0,0))
        self.display.blit(self.tentar, (50,60))
        self.display.blit(self.menu, (250,60))

        self.text_surface = self.my_font.render(texto, False, (0, 0, 0))
        self.text_surface2 = self.my_font.render(texto2, False, (0, 0, 0))
        self.text_surface3 = self.my_font.render(texto3, False, (0, 0, 0))
        self.display.blit(self.text_surface, (24,115))
        self.display.blit(self.text_surface2, (24,140))
        self.display.blit(self.text_surface3, (24,165))

        if self.luzt[0] == 1:
            self.display.blit(self.luzt[1], (50,60))
        if self.luzm[0] == 1:
            self.display.blit(self.luzm[1], (250,60))

    def draw(self,texto,texto2):
        self.display.blit(self.texto,(20,135))
        self.text_surface = self.my_font.render(texto, False, (0, 0, 0))
        self.text_surface2 = self.my_font.render(texto2, False, (0, 0, 0))
        self.display.blit(self.text_surface, (24,155))
        self.display.blit(self.text_surface2, (24,175))
        

    def menuE(self,event,num):
        self.m1, self.m2 = pygame.mouse.get_pos()
        self.hm1 = int(self.m1/3.2)
        self.hm2 = int(self.m2/3.6)
        if self.tentarB.collidepoint((self.hm1, self.hm2)):
            self.luzt[0]=1
            if self.click == True:
                return 1
        else:
            self.luzt[0]=0

        if self.menuB.collidepoint((self.hm1, self.hm2)):
            self.luzm[0]=1
            if self.click == True:
                return 2
        else:
            self.luzm[0]=0

        self.click = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.click = True
        return num

