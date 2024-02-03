#fromat method

animal = "dog"
item = "bone"
text = "The {0} chased the {1}"
number = 1000
#print("The " + animal + " chased the " + item)

print("The {0} chased the {1}".format(animal, item))
print("The {0:<10} chased the {1}".format(animal, item))
print("The {0:^10} chased the {1}".format(animal, item))
print("The {0:>10} chased the {1}".format(animal, item))

print("The number is {:,}".format(number))
print("The number is {:b}".format(number))
print("The number is {:o}".format(number))
print("The number is {:x}".format(number))
print("The number is {:e}".format(number))

print(text.format(animal, item))