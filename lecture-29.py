import shutil
import os
#writing files

with open('test.txt', 'w') as f:
    f.write('Hello, world!\n')
    f.write('How are you?\n')
    f.write('I am fine.\n')

#copying files
shutil.copy('test.txt', 'test_copy.txt')

#moving files
source = 'test.txt'
destination = '/Users/petrkroutil/Downloads/test.txt'

try:
    if os.path.exists(destination):
        print(f"File {destination} already exists")
    elif os.path.exists(source):
        shutil.move(source, destination)
except FileNotFoundError:
    print(f"File {source} not found")

#deleting files
os.remove('test_copy.txt')