import csv

import numpy as np

try:
    with open('udemy_courses.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        try:
            data_list = list(reader)
        except csv.Error:
            exit('Файл содержит некорректный CSV')
except FileNotFoundError:
    exit('Файл не найден')
if not data_list:
    exit('Файл пуст')
headers = ['course_title', 'price', 'num_subscribers', 'num_lectures', 'level', 'content_duration']
if [h.strip() for h in data_list[0]] != headers:
    exit('Некорректная структура файла')
courses_data = data_list[1:]
if not courses_data:
    exit('Файл содержит только заголовки')
prices = np.array([float(row[1]) for row in courses_data])
subscribers = np.array([int(row[2]) for row in courses_data])
lectures = np.array([int(row[3]) for row in courses_data])
levels = [row[4].strip() for row in courses_data]
durations = np.array([float(row[5]) for row in courses_data])
mean_price = np.mean(prices)
min_subscribers = np.min(subscribers)
max_duration = np.max(durations)
unique_levels = sorted(list(set(levels)))
level_dict = {level: idx for idx, level in enumerate(unique_levels)}
levels_encoded = np.array([level_dict[lvl] for lvl in levels])
counts = np.bincount(levels_encoded)
most_frequent_code = np.argmax(counts)
most_frequent_level = unique_levels[most_frequent_code]
print(f"Средняя цена на курс: {mean_price}")
print(f"Минимальное число подписчиков: {min_subscribers}")
print(f"Максимальная продолжительность лекций: {max_duration}")
print(f"Уровень с наибольшим количеством курсов: {most_frequent_level}")
