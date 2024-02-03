#exception handeling
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter a valid number!")
except Exception as e:
    print("Error: ", e)
else:
    print(result)
finally:
    print("This will always execute.")