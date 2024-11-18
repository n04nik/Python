# С помощью функции filter() переместите из списка numbers = [1, 2, 4, 5, 7, 8, 10, 11]
# нечетные элементы в новый список.

numbers = [1, 2, 3, 4, 5, 7, 8, 10, 11]

oddNumbers = list(filter(lambda x: x % 2 != 0, numbers))
print(oddNumbers)