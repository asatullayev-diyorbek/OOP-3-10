class Car:
    total_cars = 0

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.add_obj()

    @classmethod
    def add_obj(cls):
        cls.total_cars += 1

    @staticmethod
    def is_valid_year(year):
        return 1886 <= year <= 2024

    def __str__(self):
        return f"{self.year} {self.model}"


car1 = Car("Model S", 2020)
car2 = Car("Mustang", 2019)

print(car1)
print(car2)

print(Car.is_valid_year(2020))
print(Car.is_valid_year(1800))
