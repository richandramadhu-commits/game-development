#count the occurrence of vowels in the string
enter=input("enter the string  ")
vowels={"a":0, "e":0, "i":0, "o":0, "u":0}
for i in enter:
    if i in vowels:
        vowels[i]+=1
print(vowels)
enter=input("enter the string  ")
list=["a","e","i","o","u"]
vowels={}
for i in enter:
    if i in list:
        if i in vowels:
            vowels[i]+=1
        else:
            vowels[i]=1
print (vowels)
#count the occurrence of each alphabhet in the string
enter2=input("enter the string  ")
count={}
for i in enter2:
    if i. isalpha():
        if i in count:
            count[i]+=1
        else:
            count[i]=1
print(count)