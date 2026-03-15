import pgzrun
WIDTH=999 
HEIGHT=999
gar=Actor("garfield")
def draw():
    screen.fill("yellow")
    gar.draw()
def update():
    if keyboard.a:
        gar.x-=10
    if keyboard.d:
        gar.x+=10
    if keyboard.w:
        gar.y-=10
    if keyboard.s:
        gar.y+=10
pgzrun.go()