"""
1. Сохранить JSON-набор, полученный через внешний API, в файл.
2. Посчитать количество уникальных пользователей в этом наборе.
3. Посчитать для каждого пользователя, сколько у него оригинальных задач, и сколько из них выполнено.
"""
import json
import requests

# Получим данные по API.
response = requests.get("https://jsonplaceholder.typicode.com/todos")

# Откроем файл для записи, и запишем туда данные.
with open('lesson2_json_exp.json', 'w', encoding='utf-8') as file:
    file.write(response.text)

# Десериализируем данные.
with open('lesson2_json_exp.json', 'r', encoding='utf-8') as json_file:
    json2 = json.load(json_file)

# Создадим словарь
user = {}
# Заполним словарь уникальными пользователями,
# и добавим шаблон для подсчета задач и количества выполнения.
for key in json2:
    user[key["userId"]] = {"num": 0, "completed": 0}

# Посчитаем задачи и количество выполнений.
for key in json2:
    user[key["userId"]]["num"] += 1
    if key["completed"]:
        user[key["userId"]]["completed"] += 1
