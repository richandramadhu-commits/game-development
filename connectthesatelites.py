import pgzrun
import random
import time
HEIGHT=600
WIDTH=600
satelites=[]
lines=[]
nextsatelite=0
starttime=0
endtime=0
totaltime=0
totalsatelites=10
def create():
    global starttime 
    for i in range (10):
        satelite=Actor("satellite")
        satelite.pos=random.randint(40,560),random.randint(40,560)
        satelites.append(satelite)
    starttime=time.time()
def draw():
    global totaltime
    screen.blit("background2",(0,0))
    n=1
    for i in satelites:
        screen.draw.text(str(n),(i.pos[0],i.pos[1]+20))
        i.draw()
        n+=1

    for i in lines:
        screen.draw.line(i[0],i[1],"red")
    if nextsatelite<totalsatelites:
        totaltime=time.time()-starttime
        screen.draw.text(str(round(totaltime,1)),(10,10),fontsize=30)
    else:
        screen.draw.text(str(round(totaltime,1)),(10,10),fontsize=30)
def update():
    pass
def on_mouse_down(pos):
    global nextsatelite,lines 
    if nextsatelite<totalsatelites:
        if satelites[nextsatelite].collidepoint(pos):
            if nextsatelite:
                lines.append((satelites[nextsatelite-1].pos,satelites[nextsatelite].pos))
            nextsatelite+=1
        else:
            lines=[]
            nextsatelite=0
create()
pgzrun.go()