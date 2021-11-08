from game import *
from cartoon import *
from documentary import *


def read_string_array(container, string_array):
    array_len = len(string_array)
    i = 0  # Индекс, задающий текущую строку в массиве
    film_number = 0
    while i < array_len:
        film_type = string_array[i]
        if not film_type.isdigit():
            key = randint(1, 3)
        else:
            key = int(film_type)
            if key < 1 or key > 3:
                key = randint(1, 3)
        if key == 1:  # Признак игрового фильма
            i += 1
            film = Game()
            i = film.read_string_array(string_array, i)  # Чтение игрового фильма с возвратом позиции за ним
        elif key == 2:  # Признак мультфильма
            i += 1
            film = Cartoon()
            i = film.read_string_array(string_array, i)  # Чтение мультфильма с возвратом позиции за ним
        elif key == 3:  # Признак документального фильма
            i += 1
            film = Documentary()
            i = film.read_string_array(string_array, i)  # Чтение документального фильма с возвратом позиции за ним
        else:
            # Что-то пошло не так. Должен быть известный признак
            # Возврат количества прочитанных фильмов
            return film_number
        if i == 0:
            return film_number
        # Количество прочитанных фильмов увеличивается на 1
        film_number += 1
        container.store.append(film)
    return film_number
