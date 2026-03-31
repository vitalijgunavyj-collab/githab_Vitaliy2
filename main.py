from pywebio.input import input, select, slider
from pywebio.output import put_text, put_markdown
import math

from discount import apply_discount


def school_trip():
    put_markdown("## 🏫 Організація шкільної поїздки")
    students = input("Кількість учнів:", type="number")
    teachers = input("Кількість вчителів:", type="number")


    if students == 0:
        put_text("❌ Помилка: кількість учнів не може бути 0")
        return

    transport = select("Оберіть транспорт:", ["🚌 Автобус", "🚆 Поїзд"])
    days = slider("Кількість днів:", min_value=0, max_value=10, value=1)

    # Загальна кількість людей
    total_people = students + teachers

    # 🚍 Транспорт
    if transport == "🚌 Автобус":
        buses = math.ceil(total_people / 40)
        transport_cost = buses * 5000
    else:
        buses = 0
        transport_cost = total_people * 300

    # 🏨 Проживання
    if days == 0:
        hotel_cost = 0
    else:
        nights = days - 1
        hotel_cost = total_people * 400 * nights

    # Загальна сума без знижки
    total_cost = transport_cost + hotel_cost

    # 🎉 Знижка (через окремий файл)
    total_cost, discount = apply_discount(total_people, total_cost)

    # Вивід
    put_markdown("## 📊 Результат")
    put_text(f"👥 Людей: {total_people}")

    if transport == "🚌 Автобус":
        put_text(f"🚌 Автобусів потрібно: {buses}")

    put_text(f"💰 Транспорт: {transport_cost} грн")
    put_text(f"🏨 Проживання: {hotel_cost} грн")

    if discount > 0:
        put_text(f"🎉 Знижка: {discount:.2f} грн")

    put_markdown(f"## 💵 Разом: {total_cost:.2f} грн")


if __name__ == "__main__":
    school_trip()