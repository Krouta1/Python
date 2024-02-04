# Description: This file is to demonstrate the use of classes and objects in Python
class Car:
    #class variables
    wheels = 4

    #constructor
    def __init__(self, make, model, year, color):
        self.make = make #instance variables
        self.model = model
        self.year = year
        self.color = color

    #methods    
    def drive(self):
        print(self.model + " Driving")
    def stop(self):
        print(self.model + " Stopping")

car_one = Car("Toyota", "Corolla", 2015, "Red")
print(car_one.make)

car_one.drive()