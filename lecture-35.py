#abstract classes
from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass


class Car(Vehicle):
    def go(self):
        print("You drive a car.")
        
        
class Motocycle(Vehicle):
    def go(self):
        print("You drive a motocycle.")

#vehicle = Vehicle() #this failes
car = Car()
motocycle = Motocycle()


car.go()
motocycle.go()
