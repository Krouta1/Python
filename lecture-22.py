#keyword arguments

def hello(first,middle,last):
    print("Hello " +first+ " " +middle+ " " +last +".")
    
hello(middle="Bro",last="Petr",first="Kroutil")

#nested function calls
print(round(abs(float(input ("Enter a whole positive number: ")))))

#variable scope
name_global = "Petr"

def display_name():
    name = "CodeExpert420" #local scope
    print(name)

display_name()
