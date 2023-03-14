# Инициализация класса Снежинки
class Snowflakes:
    def __init__(self, number_of_snowflakes):
        self.number_of_snowflakes = number_of_snowflakes

    # Создание перегрузки оператора Сложения
    def __add__(self, other):
        return self.number_of_snowflakes + other.number_of_snowflakes

    # Создание перегрузки оператора Вычитания
    def __sub__(self, other):
        return self.number_of_snowflakes - other.number_of_snowflakes

    # Создание перегрузки оператора Умножения
    def __mul__(self, other):
        return self.number_of_snowflakes * other.number_of_snowflakes

    # Создание перегрузки оператора Деления
    def __truediv__(self, other):
        return round(self.number_of_snowflakes / other.number_of_snowflakes)

    # Создание перегрузки оператора Целочисленного деления
    def __floordiv__(self, other):
        return self.number_of_snowflakes // other.number_of_snowflakes

    # Создание перегрузки оператора Взятия остатка
    def __mod__(self, other):
        return self.number_of_snowflakes % other.number_of_snowflakes


# Создание объекта А
A = Snowflakes(10)

# Тестирование перегрузки операторов
print("Сложение -", A + Snowflakes(5))
print("Вычитание -", A - Snowflakes(3))
print("Умножение -", A * Snowflakes(2))
print("Деление -", A / Snowflakes(5))
print("Целочисленное деление -", A // Snowflakes(3))
print("Взятие остатка -", A % Snowflakes(3))
