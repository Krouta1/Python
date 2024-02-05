# higher oder functions

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)

#second example
def divisor(x):
    def divident(y):
        return y / x
    return divident

divide = divisor(2)
print(divide(10))
