#Создайте класс и поля соответствующему вашему варианту (поля статические и динамические).
# Создайте три метода (класса, объекта и статический). Выберете поле или метод для реализации инкапсуляции.
# Пропишите запись и считывание (get, set) инкапсулированных полей. ДОБАВИТЬ МЕТОДЫ КЛАССА И СТАТИЧЕСКИЕ МЕТОДЫ.
# Вар.5 Kласс Car: id, Марка, Модель, Год выпуска, Цвет, Цена, Регистрационный номер
# Функции-члены реализуют запись и считывание полей (проверка корректности), вывода возраста машины.
# Создать список объектов. Вывести:
# a)	список автомобилей заданной марки;
# б) список автомобилей заданной модели, которые эксплуатируются больше n лет;
#Добавить: магические методы __setattr__, __str__, арифметические методы __add__ и __sub__,
# операторы сравнения __eq__ и __lt__, а также методы __new__ и __del__.

from datetime import datetime

class Car:
    # Статическое поле для хранения общего количества автомобилей
    total_cars = 0

    def __new__(cls, *args, **kwargs):
        instance = super(Car, cls).__new__(cls)
        return instance

    def __init__(self, id, brand, model, year, color, price, reg_number):
        self.id = id
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self._price = price  # Инкапсуляция поля "цена"
        self.reg_number = reg_number
        Car.total_cars += 1  # Увеличиваем общее количество автомобилей

    def __del__(self):
        Car.total_cars -= 1  # Уменьшаем общее количество автомобилей при удалении экземпляра

    def __setattr__(self, name, value):
        if name == 'price' and value < 0:
            raise ValueError("Цена не может быть отрицательной.")
        super().__setattr__(name, value)

    # Метод для получения возраста автомобиля
    def get_age(self):
        current_year = datetime.now().year
        car_age = current_year - self.year
        if car_age < 0:
            raise ValueError("Age cannot be negative")
        return car_age

    # Статический метод для получения общего количества автомобилей
    @staticmethod
    def get_total_cars():
        return Car.total_cars

    # Геттер для цены
    @property
    def price(self):
        return self._price

    # Сеттер для цены
    @price.setter
    def price(self, value):
        self.__setattr__('price', value)

    # Метод для вывода информации об автомобиле
    def display_info(self):
        return (f"ID: {self.id}, Марка: {self.brand}, Модель: {self.model}, "
                f"Год: {self.year}, Цвет: {self.color}, "
                f"Цена: {self.price}, Регистрационный номер: {self.reg_number}")

    # Переопределение метода __str__ для удобного вывода информации
    def __str__(self):
        return self.display_info()

    # Арифметические методы
    def __add__(self, other):
        if isinstance(other, Car):
            return self.price + other.price
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Car):
            return self.price - other.price
        return NotImplemented

    # Операторы сравнения
    def __eq__(self, other):
        if isinstance(other, Car):
            return self.price == other.price
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Car):
            return self.price < other.price
        return NotImplemented

    # Метод для изменения регистрационного номера
    def change_reg_number(self, new_reg_number):
        self.reg_number = new_reg_number

    # Метод для вывода возраста автомобиля в строковом формате
    def age_info(self):
        return f"Возраст автомобиля: {self.get_age()} лет."

if __name__ == "__main__":
    car1 = Car(1, "Toyota", "Camry", 2018, "Синий", 20000, "A123BC")
    car2 = Car(2, "Honda", "Civic", 2020, "Красный", 22000, "B456CD")

    print(car1)
    print(car2)
    print(car1.age_info())
    print(f"Всего автомобилей: {Car.get_total_cars()}")

    car1.change_reg_number("A789EF")
    print(car1)

    # Арифметические операции
    total_price = car1 + car2
    price_difference = car1 - car2
    print(f"Общая цена: {total_price}, Разница в цене: {price_difference}")

    # Сравнение автомобилей
    print(f"Автомобили равны по цене: {car1 == car2}")
    print(f"Автомобиль 1 дешевле автомобиля 2: {car1 < car2}")