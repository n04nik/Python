from Car import Car



# Пример использования класса
if __name__ == "__main__":
    # Создание списка автомобилей
    cars = [
        Car(1, "Toyota", "Camry", 2035, "Синий", 1500000, "A123BC"),
        Car(2, "Honda", "Civic", 2018, "Красный", 1200000, "B456CD"),
        Car(3, "Toyota", "Corolla", 2010, "Чёрный", 800000, "C789EF"),
        Car(4, "Ford", "Focus", 2012, "Белый", 900000, "D012GH"),
        Car(5, "Honda", "Civic", 2015, "Серебристый", 1100000, "E345IJ"),
    ]

    # Вывод списка автомобилей заданной марки
    def filter_by_brand(cars, brand):
        return [car.display_info() for car in cars if car.brand == brand]

    # Вывод списка автомобилей заданной модели, которые эксплуатируются больше n лет
    def filter_by_model_and_age(cars, model, n):
        return [car.display_info() for car in cars if car.model == model and car.get_age() > n]

    # Примеры вывода
    print("Автомобили марки Toyota:")
    for info in filter_by_brand(cars, "Toyota"):
        print(info)

    print("\nАвтомобили модели Civic, которые эксплуатируются больше 5 лет:")
    for info in filter_by_model_and_age(cars, "Civic", 5):
        print(info)

    # Вывод общего количества автомобилей
    print(f"\nОбщее количество автомобилей: {Car.get_total_cars()}")
