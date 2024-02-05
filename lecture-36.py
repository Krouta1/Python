# objects as arguments

class Car:
    color = None
    
def change_color(car,color):
    car.color = color
    
car_one = Car()
change_color(car_one,"blue")

print(car_one.color)
