
class Car:
    """ A class for all types of vehicles"""

    def __init__(self, car_type):
        self.car_type = car_type

    def car_ignition(self):
        print("car is started")

    def car_off(self):
        print("car is off")


class Lambo(Car):
    """Class for one car type"""

    def __init__(self, lane, car_type, speed=0):
        super().__init__(car_type)
        self.lane = lane
        self.speed = speed

    def accelerate(self):
        print(self.speed + 10)

    def decrease_speed(self):
        return self.speed - 10


car_1 = Lambo(1, 'Lambo', 300)
print(car_1.car_type)
car_1.car_ignition()
car_1.accelerate()
car_1.decrease_speed()




