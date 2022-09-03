# multi-level inheritance: when a child class inherits another child class
class Organism:
    alive =True


class Animal(Organism):
    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Rabbit(Animal):
    def run(self):
        print("This rabbit is running!")


class Fish(Animal):
    def swim(self):
        print("This fish is swimming")


class Hawk(Animal):
    def fly(self):
        print('This hawk is flying')


if __name__ == '__main__':
    rabbit = Rabbit()
    fish = Fish()
    hawk = Hawk()
    print(rabbit.alive, fish.alive, hawk.alive)
    fish.eat()
    hawk.sleep()

    rabbit.run()
    fish.swim()
    hawk.fly()