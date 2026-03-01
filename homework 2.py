mt=[]
for i in range(5):
    gn=input("enter the group name ")
    size=int(input("enter the size of the group "))
    date=input("enter the date ")
    area=input("enter the area ")
    medal=input("enter type of medal")
    g=(gn, size, date, area, medal)
    mt.append(g)
print (mt)