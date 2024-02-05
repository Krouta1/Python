# warlus operator :=

happy = True
print(happy)

#kinda cool 
print(happy:=True)

#more practical one
foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)
#same one with warlus operator, much nicer
foods = list()
while food:=input("What food do you like: ") != "quit":
    foods.append(food)
    
    
