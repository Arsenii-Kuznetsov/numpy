import numpy as np

try:
    with open('system.txt') as file:
        lines = file.readlines()
except FileNotFoundError:
    exit('Файл не найден')
lines = [line.strip() for line in lines if line.strip()]
if not lines:
    exit("Файл пуст")
try:
    n = int(lines[0])
except ValueError:
    exit('Размер матрицы A должен быть целым числом')
if n <= 0:
    exit('Размер матрицы A должен быть положительным числом')
if len(lines) <1 + n * 2:
    exit("В файле недостаточно строк для матрицы A и вектора b")
A = []
for i in range(1, n + 1):
    row = list(map(float, lines[i].split()))
    if len(row) != n:
        exit(f'Строка {i} матрицы A содержит {len(row)} элементов вместо {n}')
    A += [row]
b = []
for i in range(n + 1, n + 1 + n):
    element = lines[i].split()
    if len(element) != 1:
        exit(f'Строка {i} вектора b содержит {len(element)} элементов вместо 1')
    b += [float(element[0])]
A = np.array(A)
print("Матрица A:")
print(A)
b = np.array(b)
print("Вектор b:")
print(b)
try:
    x = np.linalg.solve(A, b)
except np.linalg.LinAlgError:
    exit('Матрица системы вырождена (определитель равен 0). Система не имеет решений или имеет их бесконечно много.')
print('Решение')
print(x)