#create dictionary
blue={}
while True:
    print("1. insert\n 2. display all countries\n 3. display all captials\n 4. get capital\n 5. delete\n 6. exit")
    ask=int(input("choose an option.")) 
    if 1==ask: 
        country=input("enter the country")
        capital=input("enter the capital")
        blue[country]=capital 
        print("country added")
    elif 2==ask:
        print(blue.keys())
    elif 3==ask:
        print(blue.values())