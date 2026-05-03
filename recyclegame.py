import random
import pgzrun
WIDTH=800
HEIGHT=600
center=(WIDTH/2,HEIGHT/2)
levels=6
startspeed=10
Items=["bag","battery","bottle","chips"]
gameover=False
gamecomplete=False
currentlevel=1
items=[]
animations=[]
def draw():
    global items,currentlevel,gameover,gamecomplete
    screen.clear()
    screen.blit("bground",(0,0))
    if gameover:
        screen.draw.text("game over",fontsize=30,center=center,color="red")
    elif gamecomplete:
        screen.draw.text("good job",fontsize=30,center=center,color="red")
    else:
        for i in items:
            i.draw()
def update():
    global items
    if len(items)==0:
        items=makeitems(currentlevel)
def makeitems(extraitems):
    itemstocreate=optiontocreate(extraitems)
    newitems=createitems(itemstocreate)
    layoutitems(newitems)
    animateitems(newitems)
    return newitems
def optiontocreate(extraitems):
    itemstocreate=["paper"]
    for i in range(extraitems):
        option=random.choice(Items)
        itemstocreate.append(option)
    return itemstocreate
def createitems(itemstocreate):
    newitems=[]
    for i in itemstocreate:
        item=Actor(i+"img")
        newitems.append(item)
    return newitems
def layoutitems(itemstolayout):
    gaps=len(itemstolayout)+1
    gapsize=WIDTH/gaps
    random.shuffle(itemstolayout)
    for i,j in enumerate(itemstolayout):
        newx=(i+1)*gapsize
        j.x=newx