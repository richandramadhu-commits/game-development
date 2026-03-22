import pgzrun
import random

WIDTH=690
HEIGHT=690
def draw():
    screen.fill("red")
    w=127.5
    h=172.5
    for i in range(20):
        r1=Rect((0,0),(w,h))
        r1.center=(WIDTH/2,HEIGHT/2)
        screen.draw.rect(r1,((random.randint(0,255), random.randint(0,255), random.randint(0,255))))
        w-=10
        h+=10
pgzrun.go()