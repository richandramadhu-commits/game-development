import pgzrun
import random
HEIGHT=500
WIDTH=600
bee=Actor("bee")
bee.pos=100,100
flower=Actor("flower")
flower.pos=200,200
score=0
gameover=False
def draw():
    screen.blit("background",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("score: "+str(score),color="black",midtop=(WIDTH/2,10))
    if gameover:
        screen.fill("white")
        screen.draw.text("game over score: "+str(score),color="black",midtop=(WIDTH/2,10))
def update():
    global score
    if keyboard.a:
        bee.x-=10
    if keyboard.d:
        bee.x+=10
    if keyboard.w:
        bee.y-=10
    if keyboard.s:
        bee.y+=10
    flowercollected=bee.colliderect(flower)
    if flowercollected:
        score+=10
        move()
def move():
    flower.x=random.randint(0,600)  
    flower.y=random.randint(0,500)  
def timer():
    global gameover 
    gameover=True
clock.schedule(timer, 60.0)
pgzrun.go()