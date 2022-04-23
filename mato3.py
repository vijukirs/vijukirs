import random
import pygame
import math
import numpy
from madontekoalynfunktiot import *
class ruoka():
    def __init__(self,x,y,syoty):
        self.x=x
        self.y=y
        self.syoty=syoty
    def piirra(self):
        pygame.draw.rect(screen,(255,0,0),(self.x*elementinSivunPituus,self.y*elementinSivunPituus,elementinSivunPituus,elementinSivunPituus)) 

    def teeUusi(self,mato):
        omenaValmis=False
        while (not omenaValmis):
            omppu=ruoka(random.randint(0,maailmanKoko-1),random.randint(0,maailmanKoko-1),False)
            omenaValmis=True
            omppu=ruoka(random.randint(0,maailmanKoko-1),random.randint(0,maailmanKoko-1),False)
            for osa in mato.osat:
                if osa==[omppu.x,omppu.y]:
                    omenaValmis=False
        return omppu
class elukka():
    def __init__(self,osat,suunta):
        self.vari=(0,225,0)
        self.osat=osat
        self.suunta=suunta
        self.pituus=len(self.osat)
        self.tila=True
        self.hata=False
        self.pakoreitti=[]
    def liiku(self,omena):
        uudetosat=[]
        uudetosat.append([self.osat[0][0]+self.suunta[0],self.osat[0][1]+self.suunta[1]])
        for osa in self.osat:
            uudetosat.append(osa)
        
            
        self.osat=uudetosat
        if self.osat[0][0]==omena.x and self.osat[0][1]==omena.y:
            omena.syoty=True
            self.pituus=self.pituus+1#jos omena on madon päänkohdalla syöty = True 
        else:
            uudetosat.pop(len(uudetosat)-1) #Jos omena ei ole madon päänkohdalla se ei kasva
        
    def OsuikoSeinaan(self):
        if self.osat[0][0]>maailmanKoko or self.osat[0][0]<0:
            self.tila=False
        if self.osat[0][1]>maailmanKoko or self.osat[0][1]<0:
            self.tila=False
    def OsuikoItseen(self):
        for i in range(1,len(self.osat)-1):
            if self.osat[0]==self.osat[i]:
                self.tila=False
    
    def piirraElukka(self):
        for osa in self.osat:
            pygame.draw.rect(screen,(225,225,225),((osa[0])*elementinSivunPituus,(osa[1])*elementinSivunPituus,elementinSivunPituus,elementinSivunPituus))
            pygame.draw.rect(screen,self.vari,((5+osa[0]*elementinSivunPituus),(osa[1]*elementinSivunPituus+5),elementinSivunPituus-10,elementinSivunPituus-10))
        pygame.draw.rect(screen,(225,123,153),((self.osat[0][0]*elementinSivunPituus),(self.osat[0][1]*elementinSivunPituus),elementinSivunPituus,elementinSivunPituus))
   
        
    def kokoaSallitutSuunnat(self,omena):
        koemato=elukka(self.osat,self.suunta)
        koeomena=ruoka(omena.x,omena.y,False)
        suunnat=[[1,0],[-1,0],[0,1],[0,-1]]
        sallitut=[]
        for suunta in suunnat:
            koemato.suunta=suunta
            koemato.liiku(koeomena)
            koemato.OsuikoItseen()
            koemato.OsuikoSeinaan()
            if koemato.tila==True and moneenkoRuutuunVoiMenna(koemato.osat[0][0],koemato.osat[0][1],koemato.osat)>1.5*self.pituus:
                sallitut.append(suunta) 
            koemato=elukka(self.osat,self.suunta)
            koeomena=ruoka(omena.x,omena.y,False)
        return sallitut
        
    def aly(self,omena):
        koeomena=ruoka(omena.x,omena.y,False)
        turva=koeomena
        if self.hata==True and len(self.pakoreitti)>0:
            return self.pakoreitti.pop(0)
        if self.hata==True and len(self.pakoreitti)==0:
            self.vari=(0,225,0)
            self.hata=False
        
        if moneenkoRuutuunVoiMenna(self.osat[0][0],self.osat[0][1],self.osat)<2*self.pituus:
            self.hata=True
            self.vari=(200,100,50)
            mahdollisetRuudut=ruudutJoihinVoiMenna(self.osat[0][0],self.osat[0][1],self.osat)
            hyvaruutu=hyvaPaikka(mahdollisetRuudut,self.osat)
            self.pakoreitti=suuntaTurvaan(self.osat[0][0],self.osat[0][1],hyvaruutu,self.osat)
            if len(self.pakoreitti)==0:#tämä tarkoittaa, että pää on jo parhassa ruudussa
                print("nyt kävi näin")
                return self.suunta
            else:
                return self.pakoreitti.pop(0)
        
                
        if self.hata==False:
            koemato=elukka(self.osat,self.suunta)
            kohde=koeomena
            sallitut=self.kokoaSallitutSuunnat(kohde)  
            if koemato.osat[0][0]<kohde.x and [1,0] in sallitut:
                return [1,0]
            elif koemato.osat[0][1]<kohde.y and [0,1] in sallitut:
                return [0,1]
            elif koemato.osat[0][0]>kohde.x and [-1,0] in sallitut:
                return [-1,0]
            elif koemato.osat[0][1]>kohde.y and [0,-1] in sallitut:
                return [0,-1]
            else:
                if sallitut==[]:
                    print("no way to go")
                    return [0,-1]
                else:
                    return sallitut[random.randint(0,len(sallitut)-1)]
            
        
        


pygame.init()
naytonsivupix=800
maailmanKoko=20
elementinSivunPituus=int(naytonsivupix/maailmanKoko)
screen=pygame.display.set_mode((naytonsivupix,naytonsivupix))
speed=0


def piirraGridi():
    for j in range(0,maailmanKoko):
        for i in range(0,maailmanKoko):
            pygame.draw.rect(screen,(0,255,0),((i)*elementinSivunPituus,(j)*elementinSivunPituus,elementinSivunPituus,elementinSivunPituus),2)




def main():
    omena=ruoka(19,19,False)
    mato=elukka([[10,6],[10,5],[10,4],[10,3]],[0,1])
    running=True
    while running:
        pygame.time.wait(speed)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_RIGHT:
                    mato.suunta=[1,0]
                if event.key == pygame.K_LEFT:
                    mato.suunta=[-1,0]
                if event.key == pygame.K_UP:
                    mato.suunta=[0,-1]
                if event.key == pygame.K_DOWN:
                    mato.suunta=[0,1]
        mato.suunta=mato.aly(omena)    
        mato.liiku(omena)
        
        
        if omena.syoty==True:
            omena=omena.teeUusi(mato)
                    
        mato.OsuikoSeinaan()
        mato.OsuikoItseen()
        if mato.tila==False:
            running=False
            print("Game Over")
            pygame.time.wait(1000)   
        #print(moneenkoRuutuunVoiMenna(mato.osat[0][0],mato.osat[0][1],mato.osat))
        #print(hyvaPaikka(ruudutJoihinVoiMenna(mato.osat[0][0],mato.osat[0][1],mato.osat),mato.osat))
                    #näyttö
            
        screen.fill((0,0,0))
        piirraGridi()
        mato.piirraElukka()
        omena.piirra()
        pygame.display.update()
        #screen.fill((0,0,0))
        #pygame.display.update()
            
    pygame.quit()
        
main()  



