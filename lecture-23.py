#args parametr

def add (num1, num2):
    return num1 + num2

print(10, 20)

def add_with_args (*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(add_with_args(10, 20, 30, 40, 50, 60, 70, 80, 90, 100))