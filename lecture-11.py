# for loops
import time
for index in range(10):
    print(index + 1 )

for i in range(50,100+1):
    print(i)

for i in range(50,100+1,2):
    print(i)

for i in "Petr Krotuil":
    print(i)
    
    
#Simulate count down
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)#sleep for one sec in each loop
print("Happy new year!")
