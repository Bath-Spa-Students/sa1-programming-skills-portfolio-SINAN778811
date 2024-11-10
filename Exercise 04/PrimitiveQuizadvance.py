# Exercise no 04, Primitive Quiz advance
# listing 10 countries and capitals
Country_Capital = "Albania,Tirana,Andorra,Andorra la Vella,Austria,Vienna,Belarus,Minsk,Belgium,Brussels,Bosnia,Herzegovina,Sarajevo,Bulgaria,Sofia,Croatia,Zagreb,Cyprus,Nicosia"
user = Country_Capital.split(',')
# using range and user  
for i in range(0, len(user), 2):
    Country = user [i]
# joining country and capital 
    Capital = user [i+1]
# ask the user to given the countries capital
    output = input (f"what is the capital of {Country}? ").lower()
# checking the countries capital given by the user either correct or incorrect
    if output==Capital.lower():
        print("the answer is correct")
    else:
        print("the answer is incorrect")

