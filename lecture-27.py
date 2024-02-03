#file detection
import os

path = '/Users/petrkroutil/Downloads/document.pdf'

if os.path.exists(path):
    print('That file exists')
    if os.path.isfile(path):
        print('That is a file')
    elif os.path.isdir(path):
        print('That is a directory')
else:
    print('That file does not exist')