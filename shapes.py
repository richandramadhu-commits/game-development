import pgzrun
import random

WIDTH=690
HEIGHT=690
def draw():
    screen.fill("red")
    w=172.5
    h=172.5
    r=172.5
    for i in range(20):
        # r1=Rect((0,0),(w,h))
        # r1.center=(WIDTH/2,HEIGHT/2)
        # screen.draw.rect(r1,"black")
        # w-=10
        # h+=10
        # screen.draw.circle((WIDTH/2, HEIGHT/2),r,"green")
        screen.draw.filled_circle((WIDTH/2, HEIGHT/2),r,"green")
        r-=32
        screen.draw.text("message",(260,120),color="cyan",fontsize=69)
        screen.draw.line((69,69),(420,420),color="orange")
pgzrun.go()