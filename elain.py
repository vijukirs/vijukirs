import random
import pygame
import math
import time

pygame.init()
def etaisyys(a,b,x,y):
    luku=math.sqrt((a-x)*(a-x)+(b-y)*(b-y))
    return luku
class elainkunta():
    def __init__(self,pedot,saaliit):
        self.pedot=pedot
        self.saaliit=saaliit
        self.elavat=self.pedot+self.saaliit
        self.kuolleet=[]
        self.kohtaamiset=[]
    def paivitaKohtaamiset(self):
        for elukka in self.elavat:
            self.kohtaamiset=self.kohtaamiset+elukka.paivitaKohtaamiset(self.elavat)
        for pari in self.kohtaamiset:
            for toinenpari in self.kohtaamiset:
                if pari[0]==toinenpari[1]:
                    self.kohtaamiset.remove(toinenpari)
    def tarkistaVanhuus(self):
        for elukka in self.elavat:
            elukka.tarkistaVanhuus(self.pedot)
    def liiku(self):
        for elukka in self.elavat:
            elukka.liiku()
    def piirra(self,naytto):
        for elukka in self.elavat:
            elukka.piirra(naytto)
    def kimpoa(self):
        for pallo in self.elavat:
            pallo.kimpoa(self.kohtaamiset)
    def paivitaElavat(self):
        self.elavat=[]
        for elukka in self.pedot:
            if elukka.tila==True:
                self.elavat.append(elukka)
        for elukka in self.saaliit:
            if elukka.tila==True:
                self.elavat.append(elukka)
    def paivitaPedot(self):
        for elukka in self.pedot:
            if elukka.tila==False:
                self.pedot.remove(elukka)
    def paivitaSaaliit(self):
        for elukka in self.saaliit:
            if elukka.tila==False:
                self.saaliit.remove(elukka)
    def pedotSyo(self):
        for elukka in self.pedot:
            if elukka.tila==True:
                elukka.syo(self.kohtaamiset,self.saaliit)
    def pedotLisaanny(self):
        for elukka in self.pedot:
            if elukka.tila==True:
                elukka.lisaanny(self.pedot)
                
    def saaliitLisaanny(self):
        for elukka in self.saaliit:
            if elukka.tila==True:
                elukka.lisaanny(self.saaliit)
    def tapaKarkurit(self,kentanleveys,kentankorkeus):
        for elukka in self.elavat:
            if elukka.x<0 or elukka.x>kentanleveys:
                elukka.tila=False
            if elukka.y<0 or elukka.x>kentankorkeus:
                elukka.tila=False
                
    def TarkistaSukupuutonVaara(self,uhanalaisuusRaja):
        if len(self.pedot)<uhanalaisuusRaja:
            for elukka in self.pedot:
                if elukka.hata==False:
                    elukka.hata=True
                    elukka.lisaantumisIndeksi=1
                    #elukka.dx=random.randint(-12,12)
                    #elukka.dy=random.randint(-12,12)
                    #elukka.suurinika=2*elukka.suurinika
                    #elukka.r=3*elukka.r
        if len(self.saaliit)<uhanalaisuusRaja:
            for elukka in self.saaliit:
                if elukka.hata==False:
                    elukka.hata=True
                    elukka.suurinika=3*elukka.suurinika
                    elukka.listodnak=1.7*elukka.listodnak
            for elukka in self.saaliit:
                if elukka.tutut==0:
                    elukka.suurinika=2*elukka.suurinika
                    elukka.listodnak=3*elukka.listodnak
    def laskekaaTutut(self):
        for elukka in self.pedot:
            elukka.tutut=elukka.laskeTutut(self.pedot)
        for elukka in self.saaliit:
            elukka.tutut=elukka.laskeTutut(self.saaliit)
            
class elain():
    def __init__(self,x,y,dx,dy,r=9):
        self.hata=False
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.r=r
        self.ika=0
        self.tila=True
        self.vari=(255,255,255)
        #self.kohtasi=False
        self.synttarit=time.time()
        self.ika=time.time()-self.synttarit
        self.suurinika=500
        self.tutut=0
        self.piiri=30
        
    def laskeTutut(self,lista):
        laskuri=0
        for elukka in lista:
            if etaisyys(self.x,self.y,elukka.x,elukka.y)<self.piiri+self.r+elukka.r:
                laskuri=laskuri+1
        return laskuri
    def tarkistaVanhuus(self,pedot):
        self.ika=time.time()-self.synttarit
        if random.randint(0,self.suurinika) in range(0,round(self.ika)) and self.laskeTutut(pedot)>1:
            self.tila=False

        
    def paivitaKohtaamiset(self,pallot):
        minuunOsuvat=[]#jos pallo törmää toiseen tämä muuttaa niiden
        for pallo in pallot:               #kohtasi=True       
            #if pallo.kohtasi==False and self.kohtasi==False:
            if not(self==pallo):
                if etaisyys(self.x,self.y,pallo.x,pallo.y)<self.r+pallo.r:
                    self.kohtasi=True
                    pallo.kohtasi=True
                    minuunOsuvat.append([self,pallo])
        return minuunOsuvat
                        
                        
    def kimpoa(self,kohtaamiset):
        for pari in kohtaamiset:
            if pari[0]==self:
                a=pari[1].dx
                b=pari[1].dy
                pari[1].dx=self.dx
                pari[1].dy=self.dy
                self.dx=a
                self.dy=b   
                        
  
        
        
    def piirra(self,naytto):
        pygame.draw.circle(naytto, self.vari, (self.x, self.y), self.r, self.r)
        
        
    def liiku(self):
        if not (self.r<self.x<800-self.r):
            self.dx=0-self.dx
        if not (self.r<self.y<800-self.r):
            self.dy=0-self.dy
        self.x=self.x+self.dx
        self.y=self.y+self.dy
    
    
class peto(elain):
    def __init__(self,x,y,dx,dy,lihavuus=1):
        super().__init__(x,y,dx,dy)
        self.lihavuus=lihavuus
        self.lisaantymisIndeksi=1.9
        self.vari=(255,0,0)
        
    def syo(self,kohtaamiset,saaliit):
        if len(saaliit)>1:
            for pari in kohtaamiset:
                if self==pari[0] and isinstance(pari[1],saalis):
                    pari[1].tila=False
                    self.lihavuus=self.lihavuus+0.9
                if self==pari[1] and isinstance(pari[0],saalis):
                    pari[0].tila=False
                    self.lihavuus=self.lihavuus+0.9
    def lisaanny(self,pedot):
        if self.lihavuus>self.lisaantymisIndeksi:
            px=random.randint(0,10)
            py=random.randint(0,10)
            poikanen=peto(self.x-2*self.r+px,self.y-2*self.r+py,1*self.dx,1*self.dy)
            pedot.append(poikanen)
            self.lihavuus=self.lihavuus-1
class saalis(elain):
    def __init__(self,x,y,dx,dy):
        super().__init__(x,y,dx,dy)
        self.vari=(0,255,0)
        self.listodnak=0.10/(1+self.tutut)
    def lisaanny(self,saaliit):
        if random.randint(0,1000)<self.listodnak*100:
            px=random.randint(0,10)
            py=random.randint(0,10)
            poikanen=saalis(self.x-2*self.r+px,self.y-2*self.r+py,+1*self.dx,+1*self.dy)
            saaliit.append(poikanen)
            
            
