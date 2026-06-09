# 1. Среднее значение трех чисел

def average(a, b, c):
    return round((a + b + c) / 3, 2)

print(average(5, 7, 9))


# 2. Число четное и больше 10

def foo(something) -> bool:
    if something % 2 == 0 and something > 10:
        return True
    else:
        return False

print(foo(12))
print(foo(7))


# 3. Количество гласных букв

def foo2(text: str) -> int:
    vowels = "aeiouyAEIOUY"
    count = 0

    for letter in text:
        if letter in vowels:
            count += 1

    return count

print(foo2("Hello World"))