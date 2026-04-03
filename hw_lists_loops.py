text = "1 5 2 8 3 7"
numbers = text.split()

largest = 0
smallest = int(numbers[0])
total = 0

for num in numbers:
    print(num)
    current_number = int(num)
    print(current_number)

    if current_number > largest:
        largest = current_number

    if current_number < smallest:
        smallest = current_number

    total += current_number

print("Найбільше число:", largest)
print("Найменше число:", smallest)
print("Сума:", total)

# Список оцінок учня
grades = [10, 8, 12, 7, 9]

average = sum(grades) / len(grades)

print("Середній бал:", average)

print("Оцінки вище середнього:")

for grade in grades:
    if grade > average:
        print(grade)