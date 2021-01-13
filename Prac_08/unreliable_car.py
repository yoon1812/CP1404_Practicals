import random
from Prac_08.car import Car
class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability
        self.odometer=0


    def __str__(self):
        return"{}, fuel={}, reliability={}%, {}".format(self.name, self.fuel,
                                                 self.trust_quality(),self.drive)

    def trust_quality(self):
        return self.reliability/100



my_car = UnreliableCar("limbo",120,30)
print(my_car)