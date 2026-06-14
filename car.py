class Car:
    def __init__(self, model, age, owner=None, fuel=0):
        self.model = model
        self.age = age
        self.owner = owner
        self.fuel = fuel
        self.car_id = id(self)

    def __str__(self):
        return (
            f"Автомобіль: {self.model}\n"
            f"Вік авто: {self.age} років\n"
            f"Власник: {self.owner}\n"
            f"Кількість бензину: {self.fuel} л\n"
            f"ID: {self.car_id}"
        )

    def refuel(self, amount):
        self.fuel += amount
        print(f"Авто {self.model} заправлено на {amount} л.")
        print(f"Тепер бензину: {self.fuel} л.")

    @property
    def condition(self):
        if self.age <= 3:
            return "нове авто"
        elif self.age <= 10:
            return "середній стан"
        else:
            return "старе авто"

    @property
    def fuel_status(self):
        if self.fuel >= 30:
            return "Можна їхати далеко"
        elif self.fuel >= 10:
            return "Достатньо бензину"
        else:
            return "Потрібно заправитись"