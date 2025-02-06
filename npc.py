import pygame

class Npc:
    def __init__(self, nome, tam, num, aca):
        self.data_base = {}
        self.p_frame = 0
        self.nome=nome
        self.frames={}
        self.acao = aca
        self.vec = []
        self.vec = self.carreV(tam, num, self.vec)
        self.data_base[aca]= self.loadAnim('animacoes/npc/'+self.nome+'/'+aca,self.vec)

    def loadAnim(self, dire,duracao):
        frame_data=[]
        nomes = dire.split('/')[-1]
        n = 0
        for frame in duracao:
            id = nomes + '-' + str(n)
            img_dir = dire + '/' + id + '.png'
            animation_image = pygame.image.load(img_dir)
            self.frames[id] = animation_image.copy()
            for i in range(frame):
                frame_data.append(id)
            n += 1
        return frame_data


    def carreV(self, tam,num,vec):
        for x in range(num):
            vec.append(tam)
        return vec

    def criarAnim(self, tam, num, aca):
        veca=[]
        veca = self.carreV(tam, num, veca)
        self.data_base[aca]= self.loadAnim('animacoes/npc/'+self.nome+'/'+aca, veca)

    def mudar(self,atual,novo):
        if atual != novo:
            atual = novo
            self.acao = novo

    def events(self):
        self.p_frame += 1
        if self.p_frame >= len(self.data_base[self.acao]):
            self.p_frame=0
        img_id = self.data_base[self.acao][self.p_frame]
        self.frisk = self.frames[img_id]

    def draw(self, display,scrow,tamanhox,tamanhoy,pos):
        display.blit(self.frisk,(pos[0] * tamanhox-int(scrow[0]), pos[1] * tamanhoy-int(scrow[1])))