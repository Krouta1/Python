# sort method

students = ["Sandy","Petr","Tom","Lucy","Anna"]

students.sort(reverse=True)
sorted_students = sorted(students,reverse=True)

students_two = [("Sandy","F",60),
                ("Adam","D",100),
                ("Lucy","E",24),
                ("Tom","A",11),
                ("Zara","B",30)]
#students_two.sort() # sort by first element
students_two.sort(key = lambda x: x[1],reverse=True) # sort by third element
for i in students_two:
    print(i)
