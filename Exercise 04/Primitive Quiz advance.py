# Exercise no 04, Primitive Quiz advance

Country_Capital = "Albania,Tirana,Andorra,Andorra la Vella,Austria,Vienna,Belarus,Minsk,Belgium,Brussels,Bosnia,Herzegovina,Sarajevo,Bulgaria,Sofia,Croatia,Zagreb,Cyprus,Nicosia"
user = Country_Capital.split(',')
 
for i in range(0, len(user), 2):
    Country = user [i]

    Capital = user [i+1]

    output = input (f"what is the capital of {Country}? ").lower()

    if output==Capital.lower():
        print("the answer is correct")

    else:
        print("the answer is incorrect")

