class Tribonacci:
    def __init__(self, n):
        self.n = n  # Количество чисел, которые нужно сгенерировать

    def __iter__(self):
        self.a, self.b, self.c = 0, 0, 1  # Начальные значения
        self.count = 0  # Счетчик для контролирования количества возвращаемых чисел
        return self

    def __next__(self):
        if self.count < self.n:
            if self.count == 0:
                result = self.a
            elif self.count == 1:
                result = self.b
            elif self.count == 2:
                result = self.c
            else:
                result = self.a + self.b + self.c
                self.a, self.b, self.c = self.b, self.c, result  # Сдвиг значений
            self.count += 1
            return result
        else:
            raise StopIteration  # Останавливаем итерацию

# Создаем экземпляр генератора Трибоначчи
tribonacciGenerator = Tribonacci(35)

for number in tribonacciGenerator:
    print(number)