class Car:
    color = None


class Motorcycle:
    color = None


# pass objects as arguments
def change_color(car, color):
    car.color = color


if __name__ == '__main__':
    car_1 = Car()
    car_2 = Car()
    car_3 = Car()

    bike_1 = Motorcycle()
    bike_2 = Motorcycle()
    bike_3 = Motorcycle()

    print(car_1.color)
    print(car_2.color)
    print(car_3.color)

    print(bike_1.color)
    print(bike_2.color)
    print(bike_3.color)

    change_color(car_1, 'red')
    change_color(car_2, 'blue')
    change_color(car_3, 'green')

    change_color(bike_1, 'yellow')
    change_color(bike_2, 'pink')
    change_color(bike_3, 'purple')

    print(car_1.color)
    print(car_2.color)
    print(car_3.color)

    print(bike_1.color)
    print(bike_2.color)
    print(bike_3.color)