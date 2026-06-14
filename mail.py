from jinja2 import Environment, FileSystemLoader
import smtplib
from email.mime.text import MIMEText


def render_template(name, text, length):
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("string.html")

    return template.render(
        name=name,
        text=text,
        length=length
    )


def send_email(name, text, length, receiver):
    body = render_template(name, text, length)

    sender = "YOUR_EMAIL@gmail.com"
    password = "YOUR_APP_PASSWORD"

    msg = MIMEText(body, "html")
    msg["Subject"] = "Результат обчислення"
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)