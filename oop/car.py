class Car:
    wheels = 4  # class variable

    # constructor
    def __init__(self, make, model, year, color):
        self.make = make    # instance variable
        self.model = model  # instance variable
        self.year = year    # instance variable
        self.color = color  # instance variable

    def drive(self):
        print("This {} is driving".format(self.make))

    def stop(self):
        print("This {} is stopped".format(self.make))
