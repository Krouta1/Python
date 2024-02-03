#kwargs parametr

def name (first_name, last_name):
    print("First Name: ", first_name + " Last Name: ", last_name)

name(first_name = "John", last_name = "Doe")

def name_kwargs (**kwargs):
   #print("First Name: ", kwargs['first_name'] + " Last Name: ", kwargs['last_name'])
    for key, value in kwargs.items():
        print(f"{key}: {value}")

name_kwargs(first_name = "John", last_name = "Doe", age = 30, city = "New York", country = "USA")