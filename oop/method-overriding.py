# parent class
class Animal:
    def eat(self):
        print("This animal is eating!")


# child class
class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot!")


if __name__ == '__main__':
    rabbit = Rabbit()
    rabbit.eat()