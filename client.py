import requests

url = "https://script.google.com/macros/s/AKfycbw9aflblDTzx4tnKGqntXr5fh5NMf2muKApKT5K6gOvYgFp_IkIzblxWyI45E30no_M_g/exec"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    animals = data['animals']

    venomous_cost = 0
    african_count = 0

    for animal in animals:
        if animal['is_venomous'] == 'так':
            venomous_cost += animal['care_cost'] * animal['count']

        if animal['continent'] == 'Африка':
            african_count += animal['count']

    print("Стоимость ухода за ядовитыми:", venomous_cost)
    print("Количество африканских животных:", african_count)

else:
    print("Ошибка:", response.status_code)