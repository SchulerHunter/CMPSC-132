class Vehicle:
    MAX_FUEL = 80
    def __init__(self, driver, color, fuel):
        self.driver = driver
        self.color = color
        if fuel <= Vehicle.MAX_FUEL:
            self.fuel = fuel
        else:
            self.fuel = Vehicle.MAX_FUEL

    def refuel(self, amount):
        if (self.fuel + amount)<Vehicle.MAX_FUEL:
            self.fuel += amount
            return self.fuel
        else:
            return 'Limit Exceeded'

class Truck(Vehicle):
    FUEL_PENALTY = 5
    def __init__(self, driver, color, fuel, transmission='Manual'):
        super().__init__(driver, color, fuel)
        self.transmission = transmission
    def refuel(self.amount):
        Vehicle.refuel(self, amount-Truck.FUEL_PENALTY)
