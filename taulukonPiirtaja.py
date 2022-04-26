import random
import pygame
import math
import time
pygame.init()
class taulukko:
    def __init__(self,naytto):
        self.naytto=naytto
        self.taulukko=[] #lista, jossa kerätyt funktion arvot ovat
        self.x=850#taulukon vasen alakulma
        self.y=800#taulukon vasen alakulma
        self.leveys=2 #yhden aikapalkin leveys pikseleinä
        self.kerroin0=8
        self.kerroin1=8
        self.time=time.time()
        self.gridinLeveys=35
    def piirraPallo(self):
        pygame.draw.circle(self.naytto, (0,225,0), (400, 400), 900, 900)
    def taulukonPiirtaja(self):
        
        s=0
        for kerta in self.taulukko:
            s=s+1
            pygame.draw.line(self.naytto, (255,0,0),
            (self.x+self.leveys*s,self.y),#alkupiste
           (self.x+self.leveys*s,self.y-self.kerroin0*kerta[0]),#loppulpiste
            self.leveys)
            #if self.y-self.kerroin0*kerta[0]>380:
             #   self.kerroin0=self.kerroin0/1.1
            #if self.y-self.kerroin0*kerta[0]<750:
             #   self.kerroin0=self.kerroin0*1.1
            
            pygame.draw.line(self.naytto, (0,255,0),
            (self.x+self.leveys*s,self.y-400),#alkupiste
           (self.x+self.leveys*s,self.y-self.kerroin1*kerta[1]-400),#loppulpiste
            self.leveys)
           # if self.y-self.kerroin1*kerta[1]-400>300:
            #    self.kerroin1=self.kerroin1*1.1
            #if self.y-self.kerroin1*kerta[1]-400<100:
             #   self.kerroin1=self.kerroin1/1.1
           

        for i in range (1,50):
            pygame.draw.line(self.naytto, (210,170,100),
            (self.x+i*self.gridinLeveys,self.y),#alkupiste
            (self.x+i*self.gridinLeveys,0),#loppulpiste
            self.leveys) 
    def tilastoi(self,lista):
        if time.time()>self.time+0.5:
            self.time=self.time+0.5
            self.taulukko.append([len(lista.pedot),len(lista.saaliit)])