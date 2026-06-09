def calculate(a: int = 0, b: int = 0, operation: str = "sum") -> int:
    if operation == "sub":
        return a - b
    return a + b


def change_text(text: str = "", upper: bool = True) -> str:
    if upper:
        return text.upper()
    return text.lower()


def sum_numbers(numbers: str = "", separator: str = ",") -> int:
    return sum(int(num) for num in numbers.split(separator))