from datetime import datetime


class Car:
    # Статическое поле для хранения общего количества автомобилей
    total_cars = 0

    def __init__(self, id, brand, model, year, color, price, reg_number):
        self.id = id
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self._price = price  # Инкапсуляция поля "цена"
        self.reg_number = reg_number
        Car.total_cars += 1  # Увеличиваем общее количество автомобилей

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

    # Сеттер для цены с проверкой корректности
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной.")
        self._price = value

    # Метод для вывода информации об автомобиле
    def display_info(self):
        return (f"ID: {self.id}, Марка: {self.brand}, Модель: {self.model}, "
                f"Год: {self.year}, Цвет: {self.color}, "
                f"Цена: {self.price}, Регистрационный номер: {self.reg_number}")
