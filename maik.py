from pywebio.input import input
from pywebio import start_server
from mail import send_email


def app():
    name = input("Введіть ім'я")
    text = input("Введіть рядок")
    email = input("Введіть email")

    text = text.strip()
    length = len(text)

    send_email(name, text, length, email)


start_server(app, port=8080, debug=True)