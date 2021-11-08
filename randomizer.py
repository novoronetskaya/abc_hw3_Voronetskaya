from random import randint


class Randomizer:

    # Генерация строки
    @staticmethod
    def get_random_string():
        length = randint(1, 19)
        alphabet = "qwertyuiopasdfghjklzxcvbnm"
        result = ""
        for i in range(length):
            result += alphabet[randint(0, len(alphabet) - 1)]
        return result

    # Случайный год
    @staticmethod
    def get_random_year():
        return randint(1896, 2021)

    # Случайная продолжительность фильма
    @staticmethod
    def get_random_length():
        return randint(1, 14400)
