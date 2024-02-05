#daemon thread = a thread that runs in the background, not important for program to run

import threading
import time

def  timer():
    print()
    count = 0
    while count <= 5:
        time.sleep(1)
        count += 1
        print("Logged in for: ", count, "seconds.")

x = threading.Thread(target=timer, daemon=True)
x.start()


answer = input("Do you wish to exist the program? (yes/no): ")