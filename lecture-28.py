#read a file and print the content

path = '/Users/petrkroutil/Downloads/login.sv'
try:
    with open(path) as file:
        print(file.read())
except FileNotFoundError:
    print(f"File {path} not found")