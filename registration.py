import message

name = input(message.MSG_INPUT_NAME).strip()

if name.isalpha():
    name = name.title()
    print(message.MSG_NAME_OK.format(name=name))
else:
    print(message.MSG_NAME_ERROR)

age = input(message.MSG_INPUT_AGE).strip()
age = age.lstrip('0')

if age == "":
    age = "0"

if age.isdigit():
    print(message.MSG_AGE_OK.format(age=age))
else:
    print(message.MSG_AGE_ERROR)

phone = input(message.MSG_INPUT_PHONE).strip()

if phone.isdigit():
    print(message.MSG_PHONE_OK.format(phone=phone))
else:
    print(message.MSG_PHONE_ERROR)

print(message.MSG_FINISH)