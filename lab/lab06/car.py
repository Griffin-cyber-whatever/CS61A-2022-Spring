class Car:
    num_wheels = 4
    gas = 30
    headlights = 2
    size = 'Tiny'

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = 'No color yet. You need to paint me.'
        self.wheels = Car.num_wheels
        self.gas = Car.gas

    # modify the intance variable for color and return a str
    def paint(self, color):
        self.color = color
        return self.make + ' ' + self.model + ' is now ' + color

    # check for valid wheels num and gas num
    def drive(self):
        if self.wheels < Car.num_wheels or self.gas <= 0:
            return 'Cannot drive!'
        self.gas -= 10
        return self.make + ' ' + self.model + ' goes vroom!'

    # check for valid wheel num and minus one
    def pop_tire(self):
        if self.wheels > 0:
            self.wheels -= 1

    # modify gas with + 20
    def fill_gas(self):
        self.gas += 20
        return 'Gas level: ' + str(self.gas)


class MonsterTruck(Car):
    size = 'Monster'

    def rev(self):
        print('Vroom! This Monster Truck is huge!')

    def drive(self):
        self.rev()
        return super().drive()
