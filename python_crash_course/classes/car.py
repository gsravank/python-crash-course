class Car():
    """Simple attempt to represent a car"""
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


class ElectricCar(Car):
    """Represents aspects of a car specific to any electric car"""
    def __init__(self, year, make, model):
        super().__init__(year, make, model)


my_car = Car(2017, 'audi', 'a1')
print(my_car.get_descriptive_name())

my_tesla = ElectricCar(2017, 'tesla', 'model s')
print(my_tesla.get_descriptive_name())
