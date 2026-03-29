import pgzrun
HEIGHT=500
WIDTH=600
bee=Actor("bee")
bee.pos=100,100
flower=Actor("flower")
flower.pos=200,200
def draw():
    screen.blit("background",(0,0))
    bee.draw()
    flower.draw()
pgzrun.go()