import random
import pygame
import math
import time

class henkilo:
    def __init__(self,x,y,dx,dy,r,tila):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.r=5
        self.tila=tila
        self.osuma=False
        self.aika=time.time()
        self.osumia=0
    def varitys(self):
        if self.tila=="terve":
            return (225,225,225)
        if self.tila=="sairas":
            return (225,0,0)
        if self.tila=="parantunut":
            return (0,225,0)
        if self.tila=="kuollut":
            return (0,0,255)
        
    def piirra(self,naytto):
        #if not(self.tila=="kuollut"):
        pygame.draw.circle(naytto, self.varitys(), (self.x, self.y), self.r, self.r)
    def liiku(self):
        if not (self.r<self.x<800-self.r):
            self.dx=0-self.dx
        if not (self.r<self.y<800-self.r):
            self.dy=0-self.dy
        self.x=self.x+self.dx
        self.y=self.y+self.dy
    def tarkistaosuma(self,pallot,tarttumistodnakTerve,tarttumistodnakParantunut):
        for pallo in pallot:
            if pallo.osuma==False and self.osuma==False:
                if not(pallo.x==self.x and pallo.y==self.y):
                    if etaisyys(self.x,self.y,pallo.x,pallo.y)<2*self.r+pallo.r:
                        self.osuma=True
                        pallo.osuma=True
                        a=self.dx
                        b=self.dy
                        self.dx=pallo.dx
                        self.dy=pallo.dy
                        pallo.dx=a
                        pallo.dy=b
                        self.osumia=self.osumia+1
                        if self.tila=="sairas":
                            self.tartuta(pallo,tarttumistodnakTerve,tarttumistodnakParantunut)
                        if pallo.tila=="sairas":
                            pallo.tartuta(self,tarttumistodnakTerve,tarttumistodnakParantunut)
        return self.osumia
    def tartuta(self,pallo,tarttumistodnakTerve,tarttumistodnakParantunut):
        if pallo.tila=="terve":
            if random.randint(0,100)<tarttumistodnakTerve:
                pallo.tila="sairas"
                pallo.aika=time.time()
        elif pallo.tila=="parantunut":
            if random.randint(0,100)<tarttumistodnakParantunut:
                pallo.tila="sairas"
                pallo.aika=time.time()
    def paranetaikuole(self,sairasaika,kuolemantodnak):
        if self.tila=="sairas" and time.time()-self.aika>sairasaika:
            if random.randint(0,100)<kuolemantodnak:
                self.tila="kuollut"
                self.aika=time.time()
            else:
                self.tila="parantunut"
                self.time=time.time()
def wait():
    tauko=True
    while tauko:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tauko=False

def nautaViesti(naytto,viesti,paikka,koko,vari):
    font=pygame.font.Font('freesansbold.ttf',32)
    teksti=font.render(viesti ,True,vari)
    naytto.blit(teksti,paikka) 
def etaisyys(a,b,x,y):
    luku=math.sqrt((a-x)*(a-x)+(b-y)*(b-y))
    return luku
def main():
    kohtaamisia=0
    tarttumistodnakTerve=20
    tarttumistodnakParantunut=10
    sairasaika=5
    kuolemantodnak=5
    aika=time.time()
    tilasto=[]
    maara=75
    sairaat=5
    terveet=maara
    kuolleet=0
    t0=time.time()
    k=0
    karanteeni=False #onko toiminto käytössä
    karanteeniteho=40 #paljonko hidastuu
    karanteeniherkkyys=15 #prosenttia sairaita ennenku hidastuu
    speed=5 #liikkeen määrä
    kohtaamisia=0 #laskurin nollaus elä muuta.
    tarttumistodnakTerve=20
    tarttumistodnakParantunut=10
    sairasaika=5
    kuolemantodnak=5
    sairaatmax=sairaat #laskuri elä muuta
    pygame.init()
    
    pallot=[]
    screen=pygame.display.set_mode((1400,800))
    running=True
    for i in range(0,sairaat):
        pallo= henkilo(random.randint(20,780),random.randint(20,780),random.randint(-10,10),random.randint(-10,10),7,"sairas")
        pallot.append(pallo)
    for i in range(0,maara-1):
        pallo= henkilo(random.randint(20,780),random.randint(20,780),random.randint(-10,10),random.randint(-10,10),7,"terve")
        pallot.append(pallo)
    while running:
        pygame.time.wait(speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        
        for pallo in pallot:
            pallo.paranetaikuole(sairasaika,kuolemantodnak)
            pallo.tarkistaosuma(pallot,tarttumistodnakTerve,tarttumistodnakParantunut)
            pallo.liiku()
            osumat=0
        for pallo in pallot:
            osumat=osumat+pallo.osumia
        kohtaamiset=osumat
        for pallo in pallot:
            pallo.osuma=False
            
            
           
        parantuneet=0
        sairaat=0
        terveet=0
        kuolleet=0    
        for pallo in pallot:
            if pallo.tila=="terve":
                terveet=terveet+1
            if pallo.tila=="parantunut":
                parantuneet=parantuneet+1
            if pallo.tila=="sairas":
                sairaat=sairaat+1
            if pallo.tila=="kuollut":
                kuolleet=kuolleet+1
        
        
        
        sairaatmax=max(sairaat,sairaatmax)
        smp=parantuneet/maara
        sms=sairaat/maara
        smt=terveet/maara
        smk=kuolleet/maara
        if karanteeni ==True and sms>0.1:
            speed=karanteeniteho
        if time.time()>aika+0.2:
            aika=aika+0.2
            smp=parantuneet/maara
            sms=sairaat/maara
            smt=terveet/maara
            smk=kuolleet/maara
            tilasto.append([smt,sms,smp,smk])
        
            
        kerroin=400
        screen.fill((0,0,0))
        pygame.draw.line(screen, (255,0,255), (800,0), (800,800), 6)
        nautaViesti(screen,"Tyyppejä: "+ str(maara), (900,5), 100, (255,255,255))
        nautaViesti(screen,"Kohtaamisia: "+ str(kohtaamiset), (900,40), 100, (255,255,255))        
        nautaViesti(screen,"Terveet: "+ str(terveet), (900,70), 100, (255,255,255))
        nautaViesti(screen,"Sairaat: "+ str(sairaat), (900,100), 100, (255,0,0))
        nautaViesti(screen,"Parantuneet: "+ str(parantuneet), (900,130), 100, (0,255,0))
        nautaViesti(screen,"Kuolleet: "+ str(kuolleet), (900,160), 100, (0,0,255))
        nautaViesti(screen,"Sairaita enimmillään: "+ str(sairaatmax), (900,187), 100, (255,0,0))        
        nautaViesti(screen,"kuolemantodnäk. "+str(kuolemantodnak)+"%", (900,650), 100, (0,0,255))
        nautaViesti(screen,"tarttumistodnäk. "+str(tarttumistodnakTerve)+"%", (900,700), 100, (0,0,255))
        nautaViesti(screen,"uusimistodnäk. "+str(tarttumistodnakParantunut)+"%", (900,750), 100, (0,0,255))
        palkinylaosa=250
        leveys=1
        vasenreuna=800
    
        
        s=0
        for kerta in tilasto:
            s=s+1
            pygame.draw.line(screen, (255,255,255), (vasenreuna+leveys*s,palkinylaosa), (vasenreuna+leveys*s,palkinylaosa+kerroin*kerta[0]), leveys)
            pygame.draw.line(screen, (255,0,0), (vasenreuna+leveys*s,palkinylaosa+kerroin*kerta[0]), (vasenreuna+leveys*s,palkinylaosa+kerroin*(kerta[0]+kerta[1])), leveys)        
            pygame.draw.line(screen, (0,255,0), (vasenreuna+leveys*s,palkinylaosa+kerroin*(kerta[0]+kerta[1])), (vasenreuna+leveys*s,palkinylaosa+kerroin*(kerta[0]+kerta[1]+kerta[2])), leveys)
            pygame.draw.line(screen, (0,0,255), (vasenreuna+leveys*s,palkinylaosa+kerroin*(kerta[0]+kerta[1]+kerta[2])), (vasenreuna+leveys*s,palkinylaosa+kerroin*(kerta[0]+kerta[1]+kerta[2]+kerta[3])), leveys)
        for pallo in pallot:
            
            pallo.piirra(screen)
        pygame.display.update()
        if sairaat==0:
            wait()
             
    pygame.quit()
    

main()