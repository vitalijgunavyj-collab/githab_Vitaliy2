# 1. Сначала объявляем декоратор
def check_integer_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, int):
            return result + 10
        else:
            return result
    return wrapper

# 2. Потом объявляем функции с этим декоратором
@check_integer_result
def add(a, b):
    return a + b

@check_integer_result
def divide(a, b):
    return a / b

# 3. В самом конце вызываем их и выводим результат
print(add(5, 3))        # Выведет 18 (так как 5 + 3 = 8 (int), и декоратор добавит 10)
print(divide(5, 2))     # Выведет 2.5 (так как это float, декоратор вернет его без изменений)