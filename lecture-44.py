import functools
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

#reduce function
letters = ['h', 'e', 'l', 'l', 'o']
word = functools.reduce(lambda a, b: a + b, letters)

print(word)

#this is 5 factorial
numbers = [1, 2, 3, 4, 5]
result = functools.reduce(lambda a, b: a * b, numbers)
print(result)