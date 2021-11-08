from game import *
from cartoon import *
from documentary import *


# ----------------------------------------------
class Container:
    def __init__(self):
        self.store = []

    # Генерация контейнера указанного размера
    def generate(self, film_number):
        for i in range(film_number):
            film_type = randint(1, 3)
            if film_type == 1:
                film = Game()
            elif film_type == 2:
                film = Cartoon()
            else:
                film = Documentary()
            film.in_random()
            self.store.append(film)

    # Вывод информации о контейнере и его содержимом в консоль
    def print(self):
        print("Container stores ", len(self.store), "films:")
        for film in self.store:
            film.print()
        print("\nDivision result average = ", self.divide_year_by_length_average())

    # Вывод информации о контейнере и его содержимом в файл
    def write(self, out_stream):
        out_stream.write("Container stores {} films:\n".format(len(self.store)))
        for film in self.store:
            film.write(out_stream)
            out_stream.write("\n")
        out_stream.write("\nDivision result average = {}\n\n".format(self.divide_year_by_length_average()))

    # Среднее значение частного для содержимого контейнера
    def divide_year_by_length_average(self):
        total = 0.0
        for film in self.store:
            total += film.divide_year_by_length()
        return total / len(self.store)

    # Удаление элементов, значение частного от деления года выпуска на длину названия меньше, чем среднее по контейнеру
    def filter(self):
        division_average = self.divide_year_by_length_average()
        i = 0
        while i != len(self.store):
            if self.store[i].divide_year_by_length() < division_average:
                self.store.pop(i)
            else:
                i += 1
