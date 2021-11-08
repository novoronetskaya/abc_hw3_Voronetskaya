from film import *


# ----------------------------------------------
class Documentary(Film):
    def __init__(self):
        self.publication_year = 0
        self.length = 0
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
        # Продолжительность должна состоять из цифр
        if not string_array[i + 1].isdigit():
            return self.error_message(i)
        self.length = int(string_array[i + 1])
        # 14 400 - продолжительность самого длинного фильма в истории
        if self.length < 1 or self.publication_year > 14400:
            return self.error_message(i)
        self.name = string_array[i + 2]
        i += 3
        return i

    # Инициализация полей случайными данными
    def in_random(self):
        self.publication_year = Randomizer.get_random_year()
        self.length = Randomizer.get_random_length()
        self.name = Randomizer.get_random_string()

    # Вывод информации о документальном фильме в консоль
    def print(self):
        print("Documentary: publication year = ", self.publication_year, " length = ", self.length,
              " name = ", self.name, ", Division result = ", self.divide_year_by_length())

    # Вывод информации о документальном фильме в файл
    def write(self, out_stream):
        out_stream.write("Documentary: publication year = {} length = {} name = {}, Division result = {}".
                         format(self.publication_year, self.length, self.name, self.divide_year_by_length()))

    # Вычисление частного от деления года выпуска на длину названия
    def divide_year_by_length(self):
        return self.publication_year / len(self.name)
