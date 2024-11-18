# Дано натуральное трехзначное число n. Верно ли, что среди его цифр есть 0 или 9?

a = (input("Введите трехзначное число: "))
li = []
for i in a:
    li.append(int(i))
print(li)

res = True

for i in range(3):
    if li[i] == 0 or li[i] == 9:
        res = True
    else:
        res = False

if res:
    print("Число содержит 0 или 9!")
else:
    print("Число не содержит 0 или 9!")
    