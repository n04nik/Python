# Вариант 2
# Введите одномерный целочисленный список. Найдите наибольший нечетный элемент.
from random import randrange
#
# n = 10
# a = [randrange(1, 10) for i in range(n)]
# print(a)
# maxi = a[0]
# for i in range(1, len(a)):
#     if a[i] > maxi:
#         maxi = a[i]
# if maxi % 2 == 0:
#     print(maxi)
# else:
#     print(f'Максимальное число равно {maxi} и оно нечетное.')

# Найдите минимальный по модулю элемент списка.

# n = 10
# a = [randrange(-5, 10) for i in range(n)]
# print(a)
# mini = abs(a[0])
# for i in range(1, len(a)):
#     if abs(a[i]) < mini:
#         mini = abs(a[i])
# print(mini)


# Вариант 3
# Найдите сумму отрицательных элементов списка.

# n = 10
# a = [randrange(-5, 10) for i in range(n)]
# summ = 0
# print(a)
# for i in range(n):
#     if a[i] < 0:
#         summ += a[i]
# print(summ)

# Найдите сумму элементов списка между двумя первыми нулями. Если двух нулей нет в списке, то выведите ноль.

# n = 10
# a = [randrange(-5, 10) for i in range(n)]
# a = [1, 3, 34, 32, 31, 11, 0, 3]
# result = 0
# print(a)
# try:
#     first = a.index(0)
#     b = a.pop(first)
#     second = a.index(0) + 1
#     for i in range(first,second):
#         result += a[i]
#     print(result)
# except:
#     print(0)

# Задание 2. Задачи на многомерные списки
# В матрице найти номер строки, сумма чисел в которой максимальна.

import numpy as np

matrix = np.array([[1, 2, 3], [4, 15, 6], [7, 8, 9]])
row_sums = matrix.sum(axis=1)
max_row_index = np.argmax(row_sums)
print(max_row_index)