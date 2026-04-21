import requests

# отримуємо дані з API
url = "https://dummyjson.com/recipes?limit=0"
data = requests.get(url).json()

recipes = data["recipes"]

# 1. список рецептів піцци
pizza_recipes = [r for r in recipes if "Pizza" in r["name"] or "Pizza" in r.get("tags", [])]

print("Рецепти піцци:")
for r in pizza_recipes:
    print("-", r["name"])

# 2. скільки страв італійської кухні
italian_count = sum(1 for r in recipes if r["cuisine"] == "Italian")
print("\nКількість італійських страв:", italian_count)

# 3. найбільш калорійна страва
max_cal_recipe = max(recipes, key=lambda r: r["caloriesPerServing"])
print("\nНайбільш калорійна страва:", max_cal_recipe["name"])
print("Калорії:", max_cal_recipe["caloriesPerServing"])

# 4. страви, що готуються при 190°C
recipes_190 = []

for r in recipes:
    if r["instructions"]:
        first_step = r["instructions"][0]
        if "190" in first_step:
            recipes_190.append(r["name"])

print("\nСтрави при 190°C:")
for name in recipes_190:
    print("-", name)

# 5. загальна кількість переглядів (reviewCount)
total_reviews = sum(r["reviewCount"] for r in recipes)
print("\nЗагальна кількість переглядів:", total_reviews)