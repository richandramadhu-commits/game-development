import pgzrun
import random
HEIGHT=500
WIDTH=600
ball=Actor("ball")
ball.pos=100,100
hoop=Actor("hoop")
hoop.pos=200,200
score=0
gameover=False
def draw():
    screen.blit("background",(0,0))
    ball.draw()
    hoop.draw()
    screen.draw.text("score: "+str(score),color="black",midtop=(WIDTH/2,10))
    if gameover:
        screen.fill("white")
        screen.draw.text("game over score: "+str(score),color="black",midtop=(WIDTH/2,10))
def update():
    global score
    if keyboard.a:
        ball.x-=10
    if keyboard.d:
        ball.x+=10
    if keyboard.w:
        ball.y-=10
    if keyboard.s:
        ball.y+=10
    hoopcollected=ball.colliderect(hoop)
    if hoopcollected:
        score+=10
        move()
def move():
    hoop.x=random.randint(0,600)  
    hoop.y=random.randint(0,500)  
def timer():
    global gameover 
    gameover=True
clock.schedule(timer, 60.0)
pgzrun.go()