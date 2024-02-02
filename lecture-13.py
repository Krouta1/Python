#loop control statements

#break = terminate loop
#continue skip to next iteration
#pass does nothing (placeholder)

phone_number = "123-456-789"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1,21):
    if i==13:
        pass
    else:
        print(i,end="")
