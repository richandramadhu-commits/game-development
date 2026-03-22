import pgzrun
import random 
message=""
WIDTH=999 
HEIGHT=999
gar=Actor("garfield")
def draw():
    screen.fill("yellow")
    gar.draw()
    screen.draw.text(message, (490,10),color="black")
def update():
    if keyboard.a:
        gar.x-=10
    if keyboard.d:
        gar.x+=10
    if keyboard.w:
        gar.y-=10
    if keyboard.s:
        gar.y+=10
def G():
    gar.x=random.randint(0,999)
    gar.y=random.randint(0,999)
def on_mouse_down(pos):
    global message 
    if gar.collidepoint(pos):
        G()
        message="nice shoot"
    else:
        message="you missed"
pgzrun.go()