import numpy as np

try:
    N = int(input('Введите натуральное число: '))
except ValueError:
    exit('Введено некорректное число')
if N <= 0:
    exit('Чмсло должно быть положительным')
print('Введены матрицы')
A = np.random.randint(1, 101, size=(N, N))
print(A)
B = np.random.randint(1, 101, size=(N, N))
print(B)
C = np.array([A > B, A < B, A == B])
print('Получена матрица')
print(C)
