from film import *
from enum import Enum


# Перечисление, характеризующие доступные виды мультфильмов
class CartoonType(Enum):
    DRAWN = 1
    PUPPET = 2
    PLASTICINE = 3


# ----------------------------------------------
class Cartoon(Film):
    def __init__(self):
        self.publication_year = 0
        self.type = CartoonType.DRAWN
        self.name = ""

    # Вывод сообщения об ошибке при некорректных данных в файле
    def error_message(self, i):
        print("Incorrect input! The data about the film will be generated randomly")
        self.in_random()
        i += 3
        return i

    # Инициализация полей данными из файла или случайными данными при некорректном вводе
    def read_string_array(self, string_array, i):
        # Должно быть как минимум три непрочитанных значения в массиве
        if i >= len(string_array) - 2:
            return 0
        # Год должен состоять из цифр
        if not string_array[i].isdigit():
            return self.error_message(i)
        self.publication_year = int(string_array[i])
        # 1896 - год выпуска первого в истории фильма, 2021 - текущий год, следовательно других значений быть не может
        if self.publication_year < 1896 or self.publication_year > 2021:
            return self.error_message(i)
        # Тип - число от 1 до 3 включительно
        if not string_array[i + 1].isdigit():
            return self.error_message(i)
        k = int(string_array[i + 1])
        if k < 1 or k > 3:
            return self.error_message(i)
        self.type = CartoonType(k)
        self.name = string_array[i + 2]
        i += 3
        return i

    # Инициализация полей случайными данными
    def in_random(self):
        self.publication_year = Randomizer.get_random_year()
        self.type = CartoonType(randint(1, 3))
        self.name = Randomizer.get_random_string()

    # Вывод информации о мультфильме в консоль
    def print(self):
        print("Cartoon: publication year = ", self.publication_year, " type = ", self.type.name,
              "name = ", self.name, ", Division result = ", self.divide_year_by_length())

    # Вывод информации о мультфильме в файл
    def write(self, out_stream):
        out_stream.write("Cartoon: publication year = {} type = {} name = {}, Division result = {}".
                         format(self.publication_year, self.type.name, self.name, self.divide_year_by_length()))

    # Вычисление частного от деления года выпуска на длину названия
    def divide_year_by_length(self):
        return self.publication_year / len(self.name)
