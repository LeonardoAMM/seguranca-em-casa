import pygame
import os

class Score:
    def __init__(self, dis, game):
        self.game = game
        self.display = dis
        self.texto = pygame.image.load('imagens/Hud/texto.png')
        self.my_font = pygame.font.SysFont('Comic Sans MS', 15)
        self.my_font2 = pygame.font.SysFont('Comic Sans MS', 14)
        self.voltar = pygame.image.load('imagens/Hud/voltar.png')
        self.tentar = pygame.image.load('imagens/Hud/ganhar/proxima.png')
        self.luzp = [0,pygame.image.load('imagens/Hud/ganhar/luzp.png')]
        self.menu = pygame.image.load('imagens/Hud/ganhar/menu.png')
        self.salvar = pygame.image.load('imagens/Hud/ganhar/salvar.png')
        self.luzm = [0,pygame.image.load('imagens/Hud/ganhar/luzm.png')]
        self.fundo = pygame.image.load('imagens/Hud/ganhar/fundo3.png')
        self.fundoFinal = pygame.image.load('imagens/Hud/ganhar/fundoFinal.png')
        self.back = pygame.image.load('imagens/Hud/fundo.png')
        self.tentarB = pygame.Rect(275,30,self.tentar.get_width(),self.tentar.get_height())
        self.menuB = pygame.Rect(290,160,self.menu.get_width(),self.menu.get_height())
        self.salvarB = pygame.Rect(150,150,self.menu.get_width(),self.menu.get_height())
        self.click = False

        self.active = False
        self.color = (0,0,0)
        self.user_ip = ''
        self.text_box = pygame.Rect(145,115,120,25)
        self.save = 0


    def ganhar1(self,retry,total):
        self.display.fill('black')
        self.display.blit(self.back, (0,0))
        self.display.blit(self.fundo, (0,0))
        sretry = str(retry*50*-1)
        stotal = str(total)

        self.display.blit(self.tentar, (275,30))
        self.display.blit(self.menu, (290,160))
        

        self.text_surface = self.my_font.render("Fase concluída = ", False, (0, 0, 0))
        self.t300 = self.my_font.render("+200", False, (0, 200, 0))
        self.text_surface2 = self.my_font.render("Tentativas = ", False, (0, 0, 0))
        self.tret = self.my_font.render(sretry, False, (200, 0, 0))
        self.text_surface8 = self.my_font.render("Total = ", False, (0, 0, 0))

        self.display.blit(self.text_surface, (64,50))
        self.display.blit(self.text_surface2, (64,75))
        self.display.blit(self.t300, (184,50))
        self.display.blit(self.tret, (164,75))

        self.ttotal = self.my_font.render(stotal, False, (0, 0, 0))

        if self.luzp[0] == 1:
            self.display.blit(self.luzp[1], (275,30))
        if self.luzm[0] == 1:
            self.display.blit(self.luzm[1], (290,160))

        self.display.blit(self.text_surface8, (64,165))
        self.display.blit(self.ttotal, (115,165))

    def ganhar2(self,retry,vec,total):
        self.display.fill('black')
        self.display.blit(self.back, (0,0))
        self.display.blit(self.fundo, (0,0))
        sretry = str(retry*50*-1)
        slavar = str(vec[0]*25*-1)
        smini = str(vec[4]*25*-1)
        stotal = str(total)

        self.display.blit(self.tentar, (275,30))
        self.display.blit(self.menu, (290,160))

        self.text_surface = self.my_font.render("Fase concluída = ", False, (0, 0, 0))
        self.t300 = self.my_font.render("+200", False, (0, 200, 0))
        self.text_surface2 = self.my_font.render("Tentativas = ", False, (0, 0, 0))
        self.tret = self.my_font.render(sretry, False, (200, 0, 0))

        self.tlav = self.my_font.render(slavar, False, (200, 0, 0))
        self.testra = self.my_font.render("+25", False, (0, 200, 0))
        self.tmolha = self.my_font.render("+25", False, (0, 200, 0))
        self.tfogao = self.my_font.render("+25", False, (0, 200, 0))
        self.tmini = self.my_font.render(smini, False, (200, 0, 0))
        self.ttotal = self.my_font.render(stotal, False, (0, 0, 0))

        self.text_surface3 = self.my_font.render("lavou Frango = ", False, (0, 0, 0))
        self.text_surface4 = self.my_font.render("jogou comida estragada fora = ", False, (0, 0, 0))
        self.text_surface5 = self.my_font.render("secou o chão = ", False, (0, 0, 0))
        self.text_surface6 = self.my_font.render("limpou o fogão = ", False, (0, 0, 0))
        self.text_surface7 = self.my_font.render("minigame = ", False, (0, 0, 0))
        self.text_surface8 = self.my_font.render("Total = ", False, (0, 0, 0))

        self.display.blit(self.text_surface, (4,50))
        self.display.blit(self.text_surface2, (4,75))
        self.display.blit(self.t300, (124,50))
        self.display.blit(self.tret, (104,75))


        if vec[0] == 1:
            self.display.blit(self.text_surface3, (4,95))
            self.display.blit(self.tlav, (104,95))

        if vec[1] == 0:
            self.display.blit(self.text_surface4, (4,115))
            self.display.blit(self.testra, (224,115))

        if vec[2] == 0:
            self.display.blit(self.text_surface5, (4,135))
            self.display.blit(self.tmolha, (104,135))

        if vec[3] == 0:
            self.display.blit(self.text_surface6, (134,75))
            self.display.blit(self.tfogao, (254,75))

        self.display.blit(self.text_surface7, (164,95))
        self.display.blit(self.tmini, (244,95))

        self.display.blit(self.text_surface8, (64,165))
        self.display.blit(self.ttotal, (115,165))

        if self.luzp[0] == 1:
            self.display.blit(self.luzp[1], (275,30))
        if self.luzm[0] == 1:
            self.display.blit(self.luzm[1], (290,160))


    def ganhar3(self,retry,vec,total):
        self.display.fill('black')
        self.display.blit(self.back, (0,0))
        self.display.blit(self.fundo, (0,0))
        sretry = str(retry*50*-1)
        sminiP = str(vec[1]*25*-1)
        sminiC = str(vec[3]*25*-1)
        stotal = str(total)

        self.display.blit(self.tentar, (275,30))
        self.display.blit(self.menu, (290,160))

        self.text_surface = self.my_font.render("Fase concluída = ", False, (0, 0, 0))
        self.t300 = self.my_font.render("+200", False, (0, 200, 0))
        self.text_surface2 = self.my_font.render("Tentativas = ", False, (0, 0, 0))
        self.tret = self.my_font.render(sretry, False, (200, 0, 0))

        self.tlimpP = self.my_font.render("+25", False, (0, 200, 0))
        self.tminiP = self.my_font.render(sminiP, False, (200, 0, 0))
        self.tclor = self.my_font.render("-25", False, (200, 0, 0))
        self.tminiC = self.my_font.render(sminiC, False, (200, 0, 0))
        self.tcobr = self.my_font.render("+25", False, (0, 200, 0))
        self.ttotal = self.my_font.render(stotal, False, (0, 0, 0))

        self.text_surface3 = self.my_font.render("Limpou a piscina = ", False, (0, 0, 0))
        self.text_surface4 = self.my_font.render("errou na limpeza da piscina = ", False, (0, 0, 0))
        self.text_surface5 = self.my_font.render("não botou cloro = ", False, (0, 0, 0))
        self.text_surface6 = self.my_font.render("errou em cortar grama = ", False, (0, 0, 0))
        self.text_surface7 = self.my_font.render("tirou a cobra do jardim = ", False, (0, 0, 0))
        self.text_surface8 = self.my_font.render("Total = ", False, (0, 0, 0))

        self.display.blit(self.text_surface, (4,30))
        self.display.blit(self.t300, (124,30))
        self.display.blit(self.text_surface2, (4,70))
        self.display.blit(self.tret, (104,70))


        if vec[0] == 0:
            self.display.blit(self.text_surface3, (4,90))
            self.display.blit(self.tlimpP, (127,90))

        if vec[0] == 0:
            self.display.blit(self.text_surface4, (4,110))
            self.display.blit(self.tminiP, (207,110))

        if vec[2] == 1:
            self.display.blit(self.text_surface5, (4,130))
            self.display.blit(self.tclor, (129,130))

        self.display.blit(self.text_surface6, (4,50))
        self.display.blit(self.tminiC, (184,50))

        if vec[4] == 0:
            self.display.blit(self.text_surface7, (4,150))
            self.display.blit(self.tcobr, (179,150))

        self.display.blit(self.text_surface8, (64,170))
        self.display.blit(self.ttotal, (125,170))

        if self.luzp[0] == 1:
            self.display.blit(self.luzp[1], (275,30))
        if self.luzm[0] == 1:
            self.display.blit(self.luzm[1], (290,160))


    def ganharFinal(self,total):
        self.display.fill('black')
        self.display.blit(self.back, (0,0))
        self.display.blit(self.fundoFinal, (0,0))
        stotal = str(total)

        self.display.blit(self.salvar, (150,150))
        

        self.text_surface = self.my_font.render("Pontuação Final =", False, (0, 0, 0))
        self.ttotal = self.my_font.render(stotal, False, (0, 0, 0))

        self.display.blit(self.text_surface, (104,85))
        self.display.blit(self.ttotal, (225,85))

        if self.active:
            color = (20,20,20)
            pygame.draw.rect(self.display,color, self.text_box)
            pygame.draw.rect(self.display,(255,255,0), self.text_box,1)
        else:
            color = (0,0,0)
            pygame.draw.rect(self.display,color, self.text_box)

        surf = self.my_font.render(self.user_ip,False,(255, 255, 255))
        self.display.blit(surf, (self.text_box.x +5 , self.text_box.y))
        self.text_box.w = max(100, surf.get_width()+10)


        if self.luzm[0] == 1:
            self.display.blit(self.luzm[1], (150,150))

        if self.save == 1:
            patha = 'score'
            if os.path.exists(patha) == False:
                os.mkdir("score")
            f = open("score/salvar.txt", "a")
            f.write(str(self.user_ip)+","+str(total)+",")
            f.write("\n")
            f.close()
            self.save = 2


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
            self.luzp[0]=1
            if self.click == True:
                return 1
        else:
            self.luzp[0]=0

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
    

    def menuFinal(self,event,num):
        self.m1, self.m2 = pygame.mouse.get_pos()
        self.hm1 = int(self.m1/3.2)
        self.hm2 = int(self.m2/3.6)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.text_box.collidepoint((self.hm1, self.hm2)):
                self.active = True
            else:
                self.active = False

            if event.button == 1:
                self.click = True

        if self.salvarB.collidepoint((self.hm1, self.hm2)):
            self.luzm[0]=1
            if self.click == True:
                self.save = 1
        else:
            self.luzm[0]=0


        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.user_ip = self.user_ip[:-1]
                else:
                    self.user_ip += event.unicode

        if self.save == 2:
            return 2

        self.click = False
        
        return num

