#list comprehension

squares = [] #empty list
for i in range(1, 11): #create a for loop
    squares.append(i * i) #define what ech element of the list should be
print(squares)

#using list comprehension
square = [i * i for i in range(1, 11)]
print(square)

#without comprehension list to filter students who passed
students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students)

#using list comprehension to filter
passed_students = [x for x in students if x >= 60]
print(passed_students)

passed_students = [x if x >= 60 else "Failed" for x in students ]
print(passed_students)
