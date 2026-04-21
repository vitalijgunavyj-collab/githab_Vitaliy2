# 1. Створення словника
car = {
    "model": "Toyota RAV4 Hybrid",
    "price": 1800000,  # грн
    "engine_volume": 2.5,  # л
    "full_weight": 2100,  # кг
    "max_speed": 180,  # км/год
    "fuel_consumption": 4.6,  # л/100 км

    "interior_features": [
        "Шкіряний салон",
        "Підігрів сидінь",
        "Клімат-контроль",
        "Мультимедійна система"
    ],

    "trunk": {
        "volume": 580,  # л
        "volume_with_seats_folded": 1690  # л
    }
}

# 2. Додаємо нове поле
car["trailer_weight_with_brakes"] = 1500  # кг

# 3. Отримання даних
print("Назва авто:", car["model"])
print("Ціна:", car["price"])
print("Перша опція інтер'єру:", car["interior_features"][0])
print("Об'єм багажника зі складеними сидіннями:", car["trunk"]["volume_with_seats_folded"])

# 4. Страховий платіж (0.5%)
insurance = car["price"] * 0.005
car["insurance_payment"] = insurance

print("Страховий платіж:", insurance)

# 5. Вартість поїздки на 200 км
distance = 200  # км
fuel_price = 93  # грн/літр

fuel_needed = (car["fuel_consumption"] / 100) * distance
trip_cost = fuel_needed * fuel_price

print("Вартість поїздки на 200 км:", trip_cost, "грн")