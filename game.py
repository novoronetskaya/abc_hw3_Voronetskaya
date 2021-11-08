from film import *


# ----------------------------------------------
class Game(Film):
    def __init__(self):
        self.publication_year = 0
        self.name = ""
        self.director = ""

    # Вывод сообщения об ошибке при некорректных данных в файле
    def error_message(self, i):
        print("Incorrect input! The data about the film will be generated randomly")
        self.in_random()
        i += 3
        return i

    # Инициализация полей данными из файла или случайными данными при некорректном вводе
    def read_string_array(self, string_array, i):
        # должно быть как минимум три непрочитанных значения в массиве
        if i >= len(string_array) - 2:
            return 0
        # Год должен состоять из цифр
        if not string_array[i].isdigit():
            return self.error_message(i)
        self.publication_year = int(string_array[i])
        # 1896 - год выпуска первого в истории фильма, 2021 - текущий год, следовательно других значений быть не может
        if self.publication_year < 1896 or self.publication_year > 2021:
            return self.error_message(i)
        self.name = string_array[i + 1]
        self.director = string_array[i + 2]
        i += 3
        return i

    # Инициализация полей случайными данными
    def in_random(self):
        self.publication_year = Randomizer.get_random_year()
        self.name = Randomizer.get_random_string()
        self.director = Randomizer.get_random_string()

    # Вывод информации об игровом фильме в консоль
    def print(self):
        print("Game: publication year = ", self.publication_year, " name = ", self.name, " director = ",
              self.director, ", Division result = ", self.divide_year_by_length())

    # Вывод информации об игровом фильме в файл
    def write(self, out_stream):
        out_stream.write("Game: publication year = {} name = {} director = {}, Division result = {}".
                         format(self.publication_year, self.name, self.director, self.divide_year_by_length()))

    # Вычисление частного от деления года выпуска на длину названия
    def divide_year_by_length(self):
        return self.publication_year / len(self.name)
