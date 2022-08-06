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

# Посчитаем задачи и количество выполнений.
for key in json2:
    # Проверим ключ на наличие. Если нет - добавим с нулевым подсчетом.
    if key["userId"] not in user:
        user[key["userId"]] = {"num": 0, "completed": 0}
    # Считаем количество задач.
    user[key["userId"]]["num"] += 1
    # Считаем количество выполнений.
    if key["completed"]:
        user[key["userId"]]["completed"] += 1
