# Выполнить задание без хранения последовательностей. Дано натуральное k. Определить k-ю цифру
# последовательности: 1248163264 ..., в которой выписаны подряд степени 2.

k = int(input("Введите натуральное число k: "))

current_start = 0
count = 0

while True:
    current = str(2 ** current_start)
    if count + len(current) >= k:

        result = current[k - count - 1]
        break
    count += len(current)
    current_start += 1

print(f"{k}-я цифра последовательности: {result}")
