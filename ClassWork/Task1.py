# Используя функцию map() переписать функцию
# items = [1, 2, 3, 4, 5]
# squared = []
# for i in items:
#     squared.append(i**2)
#
# print(squared)

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)