import pgzrun
HEIGHT=700
WIDTH=750
mbox=Rect(0,0,750,150)
qbox=Rect(0,0,599,199.9999999999999)
tb=Rect(0,0,130,199.999999999999999999)
sb=Rect(0,0,130,280)
ab1=Rect(0,0,290,140)
ab2=Rect(0,0,290,140)
ab3=Rect(0,0,290,140)
ab4=Rect(0,0,290,140)
ab=[ab1,ab2,ab3,ab4]
mbox.move_ip(0,0)
qbox.move_ip(0,160)
tb.move_ip(610,160)
sb.move_ip(610,370)
ab1.move_ip(0,370)
ab2.move_ip(310,370)
ab3.move_ip(0,520)
ab4.move_ip(310,520)
score=0
timeleft=10
message=""
is_gameover=False
question_file="questions.txt"
questions=[]
count=0
index=0
def readquestion():
    global count,questions
    file=open(question_file,"r")
    for i in file:
        questions.append(i)
        count+=1
    file.close()
def draw():
    screen.clear()
    screen.fill("cyan")
    screen.draw.filled_rect(mbox,"black")
    screen.draw.filled_rect(qbox,"orange")
    screen.draw.filled_rect(tb,"dark blue")
    screen.draw.filled_rect(sb,"green")
    for i in ab:
        screen.draw.filled_rect(i,"dark blue")
pgzrun.go()