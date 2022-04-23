import random
import pygame
pygame.init()
t=[[[1,1,1,0],
        [0,1,0,0],
        [0,0,0,0],
        [0,0,0,0]],
       [[1,0,0,0],
        [1,1,0,0],
        [1,0,0,0],
        [0,0,0,0]],
       [[0,0,0,0],
        [0,1,0,0],
        [1,1,1,0],
        [0,0,0,0]],
       [[0,1,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,0,0,0]],
       [[0,0,0,0],
        [0,1,0,0],
        [1,1,1,0],
        [0,0,0,0]]]
n=[[[1,1,0,0],
    [1,1,0,0],
    [0,0,0,0],
    [0,0,0,0]],[[1,1,0,0],
    [1,1,0,0],
    [0,0,0,0],
    [0,0,0,0]],[[1,1,0,0],
    [1,1,0,0],
    [0,0,0,0],
    [0,0,0,0]],[[1,1,0,0],
    [1,1,0,0],
    [0,0,0,0],
    [0,0,0,0]]]
I=[[[1,0,0,0],
    [1,0,0,0],
    [1,0,0,0],
    [1,0,0,0]],[[1,1,1,1],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]],[[1,0,0,0],
    [1,0,0,0],
    [1,0,0,0],
    [1,0,0,0]],[[1,1,1,1],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]]
L=[[[1,0,0,0],
        [1,0,0,0],
        [1,1,0,0],
        [0,0,0,0]],
       [[1,1,1,0],
        [1,0,0,0],
        [0,0,0,0],
        [0,0,0,0]],
       [[1,1,0,0],
        [0,1,0,0],
        [0,1,0,0],
        [0,0,0,0]],
       [[0,0,1,0],
        [1,1,1,0],
        [0,0,0,0],
        [0,0,0,0]],
       ]
J=[[[0,1,0,0],
        [0,1,0,0],
        [1,1,0,0],
        [0,0,0,0]],
       [[1,0,0,0],
        [1,1,1,0],
        [0,0,0,0],
        [0,0,0,0]],
       [[1,1,0,0],
        [1,0,0,0],
        [1,0,0,0],
        [0,0,0,0]],
       [[1,1,1,0],
        [0,0,1,0],
        [0,0,0,0],
        [0,0,0,0]],
       ]

S=[[[1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,0,0,0]],
       [[0,1,1,0],
        [1,1,0,0],
        [0,0,0,0],
        [0,0,0,0]],
       [[1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,0,0,0]],
       [[0,1,1,0],
        [1,1,0,0],
        [0,0,0,0],
        [0,0,0,0]],
       ]
Z=[[[0,1,1,0],
        [1,1,0,0],
        [0,0,0,0],
        [0,0,0,0]],
       [[0,1,0,0],
        [1,1,0,0],
        [1,0,0,0],
        [0,0,0,0]],
       [[0,1,1,0],
        [1,1,0,0],
        [0,0,0,0],
        [0,0,0,0]],
       [[0,1,0,0],
        [1,1,0,0],
        [1,0,0,0],
        [0,0,0,0]],
       ]


class palikka():
    def __init__(self,matriisi,x,y,asento,vari):
        self.matriisi=matriisi
        self.x=x
        self.y=y
        self.asento=asento
        self.vari=vari
        self.tila=True
        
    def tilaFalse(self):
        self.tila=False
        
    def piirra(self,lista,naytto):
        if self.tila==True:
            for j in range(0,4):
                for i in range(0,4):
                    if self.matriisi[self.asento][j][i]==1:
                        pygame.draw.rect(naytto,self.vari,((self.x+i)*40,(self.y+j)*40,40,40))
        if self.tila==False:
            for j in range(0,4):
                for i in range(0,4):
                    if self.matriisi[self.asento][j][i]==1 and [self.x+i,self.y+j] in lista:
                        pygame.draw.rect(naytto,self.vari,((self.x+i)*40,(self.y+j)*40,40,40))
    def tarkistaVapausAlas(self,lista):
        for j in range(0,4):
            for i in range(0,4):
                if self.matriisi[self.asento][j][i]==1:
                    if [self.x+i,self.y+j+1] in lista:
                        return False
                    if self.y+j>=19:
                        return False
        else:
            return True
    def tarkistaVapausOikealle(self,lista):
        for j in range(0,4):
            for i in range(0,4):
                if self.matriisi[self.asento][j][i]==1:
                    if [self.x+i+1,self.y+j] in lista:
                        return False
                    elif self.x+i+1>9:
                        return False
        else:
            return True
    def tarkistaVapausVasemmalle(self,lista):
        for j in range(0,4):
            for i in range(0,4):
                if self.matriisi[self.asento][j][i]==1:
                    if [self.x+i-1,self.y+j] in lista:
                        return False
                    elif self.x+i-1<0:
                        return False
        else:
            return True
    
    def varaa(self,lista):
        for j in range(0,4):
            for i in range(0,4):
                if self.matriisi[self.asento][j][i]==1:
                    lista.append([self.x+i,self.y+j])
        
    def pudota(self):
        self.y=self.y+1
    def nosta(self):
        self.y=self.y-1
    def kaanna(self):
        self.asento=(self.asento-1)%4
    def oikealle(self):
        self.x=self.x+1
    def vasemmalle(self):
        self.x=self.x-1
        
def gameOver(lista):
    for i in range(0,10):
        if [i,2] in lista:
            return True
    else:
        return False
        

def tarkistaTaydet(lista,luku):
    poistetutRivit=0
    pudotus=False
    for j in range(0,20):
        k=0
        for i in range(0,10):
            if [i,j] in lista:
                k=k+1
        if k==10:
            poistetutRivit=poistetutRivit+1
            pudotus=True
            for p in range(0,10):
                lista.remove([p,j])
            for s in range(1,20):
                for p in range(0,10):
                    if [p,19-s] in lista and [p,19-s+1] not in lista:
                        lista.append([p,19-s+1])
                        lista.remove([p,19-s])
    print(poistetutRivit)
    luku=luku+poistetutRivit
    return luku
def tausta(naytto):
    for j in range(0,20):
        for i in range(0,10):
            pygame.draw.rect(naytto,(0,255,0),((i)*40,(j)*40,40,40),3)
def arpoja():
    k=random.randint(0,6)
    if k==0:
        kappale=palikka(n,1,1,0,(255,0,0))
        return kappale
    if k==1:
        kappale=palikka(t,1,1,0,(0,255,0))
        return kappale
    if k==2:
        kappale=palikka(I,1,1,0,(0,0,255))
        return kappale
    if k==3:
        kappale=palikka(L,1,1,0,(255,255,0))
        return kappale
    if k==4:
        kappale=palikka(J,1,1,0,(255,0,255))
        return kappale
    if k==5:
        kappale=palikka(S,1,1,0,(0,255,255))
        return kappale
    if k==6:
        kappale=palikka(Z,1,1,0,(200,80,150))
        return kappale
def nautaViesti(naytto,viesti,paikka,koko,vari):
    font=pygame.font.Font('freesansbold.ttf',32)
    teksti=font.render(viesti ,True,vari)
    naytto.blit(teksti,paikka)    


def main():
    pisteet=0
    normal=400
    fast=10
    speed=normal
    varatut=[]
    kappale=arpoja()
    palikat=[]
    palikat.append(kappale)
    screen=pygame.display.set_mode((700,800))
    running=True
    while running:
        pygame.time.wait(speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_SPACE:
                    kappale.kaanna()
                if event.key == pygame.K_RIGHT and kappale.tarkistaVapausOikealle(varatut):
                    kappale.oikealle()
                if event.key == pygame.K_LEFT and kappale.tarkistaVapausVasemmalle(varatut):
                    kappale.vasemmalle()
                if event.key == pygame.K_DOWN:
                    speed=fast
                    
        if kappale.tarkistaVapausAlas(varatut)==True:      
            kappale.pudota()     
        else:
            kappale.varaa(varatut)
            kappale.tilaFalse()
            speed=normal
            if gameOver(varatut)==False:
                kappale=arpoja()
                palikat.append(kappale)
                pisteet=tarkistaTaydet(varatut,pisteet)
            
                
                    #näyttö
               
        screen.fill((0,0,0))
        tausta(screen)
        kappale.piirra(varatut,screen)
        for kappale in palikat:
            kappale.piirra(varatut,screen)
        if gameOver(varatut):
            nautaViesti(screen,"GAME OVER", (100,70), 100, (255,255,255))
        nautaViesti(screen,"Pisteet: "+ str(pisteet), (475,70), 100, (255,255,255))
        pygame.display.update()
            
    pygame.quit()
    
main()