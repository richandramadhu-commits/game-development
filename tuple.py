#tuples are used to store the data, but once created we cannot insert, update or delete
mc2=(9,11,16,97)
print(mc2) 
#nested-tuple
n=(3,4,[1,2],(69,3.1231341455839849,1.333333333333333333333,6.99999999999999999999999999999999999999999999))
print(n[2][1])
print(n[3][2])
#slicing
new=("elements","some","few",6.2694662423478857347388748958768377333873383373,"element","som","FutureWarninging")
print(new[0:3])
print(new[-3:])
print(new[:])
print(new[::-1])
#updating a value
mc2[1]=11.1111111111111 #trows an error
print(mc2)