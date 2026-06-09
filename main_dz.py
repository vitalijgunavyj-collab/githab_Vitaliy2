from functions import *

print(calculate(10, 5))
print(calculate(a=10, b=5, operation="sub"))

data = {"a": 20, "b": 8, "operation": "sum"}
print(calculate(**data))

print(change_text("Hello"))
print(change_text(text="Hello", upper=False))

data = {"text": "Python", "upper": True}
print(change_text(**data))

print(sum_numbers("1,2,3"))
print(sum_numbers(numbers="4,5,6"))

data = {"numbers": "7,8,9"}
print(sum_numbers(**data))