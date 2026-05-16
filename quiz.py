import pgzrun
HEIGHT=700
WIDTH=750
mbox=Rect(0,0,750,100)
qbox=Rect(0,0,599,99.9999999999999)
tb=Rect(0,0,99,99.999999999999999999)
sb=Rect(0,0,99,149.999999)
ab1=Rect(0,0,300,50)
ab2=Rect(0,0,300,50)
ab3=Rect(0,0,300,50)
ab4=Rect(0,0,300,50)
ab=[ab1,ab2,ab3,ab4]
mbox.move_ip(0,0)
qbox.move_ip(0,110)
tb.move_ip(610,110)
sb.move_ip(610,220)
def draw():
    screen.clear()
    screen.fill("cyan")
    screen.draw.filled_rect(mbox,"black")
    screen.draw.filled_rect(qbox,"orange")
pgzrun.go()