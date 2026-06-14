from car import Car

car1 = Car("BMW X5", 2, "Віталій", 15)
car2 = Car("Audi A6", 12, "Олександр", 5)

print("===== ID автомобілів =====")
print(car1.car_id)
print(car2.car_id)

print("\n===== __dict__ =====")
print(car1.__dict__)
print(car2.__dict__)

print("\n===== Інформація про авто =====")
print(car1)
print()
print(car2)

print("\n===== Зміна кількості бензину =====")
car1.fuel = 25
print(f"У {car1.model} тепер {car1.fuel} л бензину")

print("\n===== Заправка =====")
car2.refuel(20)

print("\n===== Стан автомобілів =====")
print(f"{car1.model}: {car1.condition}")
print(f"{car2.model}: {car2.condition}")

print("\n===== Статус пального =====")
print(f"{car1.model}: {car1.fuel_status}")
print(f"{car2.model}: {car2.fuel_status}")

print("\n===== Порівняння кількості бензину =====")
if car1.fuel > car2.fuel:
    print(f"Більше бензину має {car1.model}")
elif car2.fuel > car1.fuel:
    print(f"Більше бензину має {car2.model}")
else:
    print("Кількість бензину однакова")




