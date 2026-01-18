#create dictionary 
blue={"red":"keys1", "orange":"keys2", "lster":"keys3"}
print(blue)
#access value with the help of key
print(blue["lster"])
#get all the keys
print(blue.keys())
#get all the values
print(blue.values())
#cheak if key exist in the dictionary
if "range" in blue:
    print("yes, it is present")
else:
    print("no!!!!!!!")
#add a new keyvalue pair in the dictionary
blue["C.I.A."]="keys4"
print(blue)
#delete key value from the dictionary
del(blue["C.I.A."])
print(blue)
#update a value in the dictionary
blue["lster"]="keys4"
print(blue)