class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.upper()

    def read_odometer(self):
        print(f"This car has {self.odometer} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer!")


spaceship = Car('spacex', 'Super Heavy', 2023)
print(spaceship.get_descriptive_name())
spaceship.update_odometer(110)
spaceship.read_odometer()
spaceship.update_odometer(50)
spaceship.read_odometer()
