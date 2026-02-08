#create a matrix
tod=[[1,2,3],[4,5,6],[7,8,9]]
print (tod)
#find the number of rows
print (len(tod))
#find the number of columns
print (len(tod[1]))
#access the element in 2d list
print (tod[1][2])
print (tod [2][1])
#take an input for a matrix and print the elements
r=int (input ("enter the number of rows "))
c=int (input ("enter the number of columns ")) 
matrix=[]
for i in range (r):
    t=[]
    for j in range (c):
        e=int (input ("enter the element "))
        t.append(e)
    matrix.append(t)
for i in range (r):
    for j in range (c):
        print (matrix[i][j],end=" ")
    print ()
m1=[[1, 3, 69],[5,2,1]]
m2= [[10,1000,100],[9,99,999]]
a=[[0, 0, 0],[0,0,0]]
s=[[0,0,0],[0,0,0]]
for i in range (2):
    for j in range (3):
        a[i][j]=m1[i][j]+m2[i][j]
        s[i][j]=m1[i][j]-m2[i][j]
for i in range (2):
    for j in range (3):
        print (a[i][j],end=" ")
    print ()
for i in range (2):
    for j in range (3):
        print (s[i][j],end=" ")
    print ()