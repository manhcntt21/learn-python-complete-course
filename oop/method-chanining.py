# method chaining: calling multiple methods sequentially
# each call performs an action on the same object and returns self

class Car:
    def turn_on(self):
        print("You start the engine!")
        return self

    def drive(self):
        print("you drive the car!")
        return self

    def brake(self):
        print("you stop the car!")
        return self

    def turn_off(self):
        print("you turn off the car!")
        return self


if __name__ == '__main__':
    car = Car()

    # car.turn_on()
    # car.drive()

    car.turn_on().drive()  # method chaining (return self in method definition), logic: methods are sequential
    car.brake().turn_off()

    car.turn_on().drive().brake().turn_off()

    # split multiple line when we call multiple method
    car.turn_on()\
        .drive()\
        .brake()\
        .turn_off()
