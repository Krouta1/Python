# duck typing = concept where the calss of an object is less important than methods/attributes

class Duck:
    def walk(self):
        print("This duck is walking.")
    def talk(self):
        print("This duck is qwuacking.")

class Chicken:
    def walk(self):
        print("This chicken is walking.")
    def talk(self):
        print("This chicken is clucking.")

class Person:
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("You cought the critter!")
        
duck = Duck()
chicken = Chicken()
person = Person()

#this works with chicken and duck even the method is written only for duck
person.catch(chicken)
