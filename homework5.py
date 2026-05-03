import pgzrun
import random
import time
HEIGHT=600
WIDTH=600
garfields=[]
lines=[]
nextgarfield=0
starttime=0
endtime=0
totaltime=0
totalgarfields=10
def create():
    global starttime 
    for i in range (10):
        garfield=Actor("garfield")
        garfield.pos=random.randint(40,560),random.randint(40,560)
        garfields.append(garfield)
    starttime=time.time()
def draw():
    global totaltime
    screen.blit("background2",(0,0))
    n=1
    for i in garfields:
        screen.draw.text(str(n),(i.pos[0],i.pos[1]+40))
        i.draw()
        n+=1

    for i in lines:
        screen.draw.line(i[0],i[1],"red")
    if nextgarfield<totalgarfields:
        totaltime=time.time()-starttime
        screen.draw.text(str(round(totaltime,1)),(10,10),fontsize=30)
    else:
        screen.draw.text(str(round(totaltime,1)),(10,10),fontsize=30)
def update():
    pass
def on_mouse_down(pos):
    global nextgarfield,lines 
    if nextgarfield<totalgarfields:
        if garfields [nextgarfield].collidepoint(pos):
            if nextgarfield:
                lines.append((garfields[nextgarfield-1].pos,garfields[nextgarfield].pos))
            nextgarfield+=1
        else:
            lines=[]
            nextgarfield=0
create()
pgzrun.go()