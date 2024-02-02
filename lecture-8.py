# if statements

age = int(input("Tell me your age: "))

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are adult")
elif age <= 0:
    print("You haven't been born yet!")
else:
    print ("You are a child.")
    
