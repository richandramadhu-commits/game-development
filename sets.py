#sets are same as list, but it will not contain duplicate elements and the brackets are {}
s=[6,9,11,7,12,6,4,9,3]
print(s)
S=set(s)
print(S)
#cheak if the element exists in the set
if 69 in S:
    print("message")
else:
    print("noooooo")
#add element to the set
Ss=set([])
Ss.add("([])")
Ss.add("(2)""([69])""([{(intercontinentinal ballistic missile)}])")
Ss.add("9")
Ss.add("9")
print(Ss)
#remove element from the set
Ss.remove("(2)""([69])""([{(intercontinentinal ballistic missile)}])")
print(Ss)
#set operations
#union means adding 2 sets
sS={"([{([intercontinentinal ballistic missile])}])","(col)","3.10291209918234834857484759","1.333333333333333","8","6"}
SsS={"1","3","6","8","69"}
print(sS.union(SsS))
print(sS|SsS)
#intersection means common elements
print(sS.intersection(SsS))
print(sS&SsS)
#difference means unique elements of firstset
print(sS.difference(SsS))
print(sS-SsS)
#symmetric difference means union-intersection
print(sS.symmetric_difference(SsS))
print(sS^SsS)