#filter function
friends = [
    ("Rolf", 25),
    ("Anne", 37),
    ("Charlie", 31),
    ("Bob", 22)
]

age = lambda data: data[1] >= 30
friends_over_30 = list(filter(age, friends))

for i in friends_over_30:
    print(i)