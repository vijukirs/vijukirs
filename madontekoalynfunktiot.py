import numpy
maailmanKoko=20
def kissa():
    print("kissa")
def listaaLuvutValilta(x,y): 
    luvut=[]
    for i in range(0,int(abs(x-y))+1):
        luvut.append(int(x+i*numpy.sign(y-x)))
    return luvut
#print(listaaLuvutValilta(-4,-8))
def Vaakareitti(x,y,z,w):       #luettelee aluksi vaakaa menevät
    coordX=listaaLuvutValilta(x,z) #reitti (x,y)-->(z,w)
    coordY=listaaLuvutValilta(y,w)
    reitti=[]
    for osa in coordX:
        reitti.append([osa,coordY[0]])
    for i in range(1,len(coordY)):
        reitti.append([coordX[len(coordX)-1],coordY[i]])
    return reitti

def Pystyreitti(x,y,z,w):
    reitti=[]
    for osa in Vaakareitti(y,x,w,z):
        reitti.append([osa[1],osa[0]])
    return reitti

def onkoReittiVapaa(reitti,esteet):
    if esteet[0] in reitti:
        reitti.remove(esteet[0])
    for osa in reitti:
        for este in esteet:
            if osa==este:
                return False
    return True
def voikoMenna(x,y,z,w,esteet):
    if onkoReittiVapaa(Vaakareitti(x,y,z,w),esteet)==True:
        return True
    if onkoReittiVapaa(Pystyreitti(x,y,z,w),esteet)==True:
        return True
    else:
        return False
def ruudutJoihinVoiMenna(x,y,este):
    mahdollisetRuudut=[]
    for i in range(0,maailmanKoko):
        for j in range(0,maailmanKoko):
            if voikoMenna(x,y,i,j,este)==True:
                mahdollisetRuudut.append([i,j])
    return mahdollisetRuudut


def moneenkoRuutuunVoiMenna(x,y,este):
    maara=0
    for i in range(0,maailmanKoko):
        for j in range(0,maailmanKoko):
            if voikoMenna(x,y,i,j,este)==True:
                maara=maara+1
    return maara

def hyvaPaikka(mahdollisetRuudut,este):
    luku=0
    for ruutu in mahdollisetRuudut:
        print(ruutu)
        if moneenkoRuutuunVoiMenna(ruutu[0],ruutu[1],este)>luku:
            hyvaruutu=ruutu
            luku=moneenkoRuutuunVoiMenna(ruutu[0],ruutu[1],este)
    return hyvaruutu
def suuntaTurvaan(lahtoX,lahtoY,hyvaruutu,esteet):
    if onkoReittiVapaa(Vaakareitti(lahtoX,lahtoY,hyvaruutu[0],hyvaruutu[1]),esteet)==True:
        return reittiSuunniksi(Vaakareitti(lahtoX,lahtoY,hyvaruutu[0],hyvaruutu[1]))
    else:
        return reittiSuunniksi(Pystyreitti(lahtoX,lahtoY,hyvaruutu[0],hyvaruutu[1]))

def reittiSuunniksi(reitti):
    suunnat=[]
    for i in range(0,len(reitti)-1):
        suunta=[reitti[i+1][0]-reitti[i][0],reitti[i+1][1]-reitti[i][1]]
        suunnat.append(suunta)
    return suunnat
print(reittiSuunniksi(Vaakareitti(5,5,10,10)))

def hamilton():
    print("tätä kannattaa miettiä!")

