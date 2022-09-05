# prevents a user from creating an object of that class
# compels a user to override abstract methods in a child class

# abstract class: a class which contains ONE or MORE abstract methods
# abstract method: a method what has a declaration but does not have an implementation

# abc abstract based class
from abc import ABC, abstractmethod


# abstract class
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# child class
class Car(Vehicle):
    def go(self):
        print("You drive the car!")

    def stop(self):
        print("This car is stopped")


# child class
class Motorcycle(Vehicle):
    def go(self):
        print("you ride the motorcycle!")

    def stop(self):
        print("this motorcycle is stopped")


if __name__ == '__main__':
    # vehicle = Vehicle()
    car = Car()
    motorcycle = Motorcycle()
    motorcycle.stop()
    car.stop()
