# Используйте функцию reduce() и перепишите код

# product = 1
# list = [1, 2, 3, 4]
# for num in list:
#     product = product * num
# print(product)

from functools import reduce

list = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, list)
print(product)