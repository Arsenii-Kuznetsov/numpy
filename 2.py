import numpy as np

try:
    N = int(input('Введите натуральное число: '))
except ValueError:
    exit('Введено некорректное число')
if N <= 0:
    exit('Чмсло должно быть положительным')
A = np.random.randint(1, 101, size=(N, N))
print('Получена матрица')
print(A)
col_sums = np.sum(A, axis=0)
min_column_index = np.argmin(col_sums)
print(f"Номер столбца с минимальной суммой: {min_column_index + 1}")
