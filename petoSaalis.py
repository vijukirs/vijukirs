import random
import pygame
import math
import time
from elain import*
from taulukonPiirtaja import*

# ... do something ...
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

    

def main():
    tilasto=[]
    kaisa=peto(1,2,3,4)  
    kentanleveys=800
    kentankorkeus=800
    pygame.init()
    screen=pygame.display.set_mode((2000,800))
    speed=20
    petoja=7
    saaliita=7
    running=True
    pedot=[]
    saaliit=[]
    kuvaajat=taulukko(screen)
    for i in range(0,petoja):
        jussi=peto(random.randint(20,kentanleveys-20),random.randint(20,kentankorkeus-20),random.randint(-10,10),random.randint(-10,10))
        pedot.append(jussi)
    for i in range(0,saaliita):
        kaisa=saalis(random.randint(20,kentanleveys-20),random.randint(20,kentankorkeus-20),random.randint(-10,10),random.randint(-10,10))
        saaliit.append(kaisa)
    elaimet=elainkunta(pedot,saaliit)
    print(len(elaimet.elavat))
    while running:
        pygame.time.wait(speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        elaimet.kohtaamiset=[]
        elaimet.laskekaaTutut()
        elaimet.paivitaPedot()
        elaimet.paivitaSaaliit()
        elaimet.TarkistaSukupuutonVaara(3) #argumetti keroo mikä on uhanalaisuuden raja
        elaimet.paivitaKohtaamiset()
        elaimet.pedotSyo()
        elaimet.pedotLisaanny()
        elaimet.paivitaElavat()
        elaimet.saaliitLisaanny()
        elaimet.paivitaElavat()
        elaimet.kohtaamiset=[]
        elaimet.paivitaKohtaamiset()
        elaimet.kimpoa()
        elaimet.tarkistaVanhuus()
        elaimet.paivitaElavat()
        elaimet.paivitaPedot()
        elaimet.paivitaSaaliit()
        elaimet.liiku()
        elaimet.tapaKarkurit(kentanleveys,kentankorkeus)
        kuvaajat.tilastoi(elaimet)
        
        
        screen.fill((0,0,0))
        elaimet.piirra(screen)
        kuvaajat.taulukonPiirtaja()
        pygame.draw.line(screen, (145,163,70),(805,0),(805,800),5)
        pygame.display.update()           
        if (len(elaimet.pedot)<2 and len(elaimet.saaliit)==0) or len(elaimet.pedot)==0:
            wait()

    pygame.quit()   
                

main()
