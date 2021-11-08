import sys
import string
import time

from extender import *

# ----------------------------------------------
if __name__ == '__main__':
    # start = time.time()
    print('==> Start')

    if len(sys.argv) != 4:
        print("Incorrect command line! You must write: command -f <input_file_name> <output_file_name> "
              "or command -n <container_size> <output_file_name> (for random generation)")
        exit()

    container = Container()

    # Ввод данных из файла
    if sys.argv[1] == "-f":
        input_file_name = sys.argv[2]
        output_file_name = sys.argv[3]
        # Если файла не существует или его невозможно открыть - конец работы программы
        try:
            in_file = open(input_file_name)
        except IOError:
            print("Problem while opening file!")
            exit()
        # Чтение исходного файла, содержащего данные, разделенные пробелами и переводами строки
        input_string = in_file.read()
        in_file.close()
        # Формирование массива строк, содержащего чистые данные в виде массива строк символов.
        string_array = input_string.replace("\n", " ").split(" ")
        film_number = read_string_array(container, string_array)
    # Генерация данных
    elif sys.argv[1] == "-n":
        string_length = sys.argv[2]
        # Проверка корректности введённого размера контейнера
        if string_length.isdigit():
            container_size = int(string_length)
            if container_size < 1 or container_size > 10000:
                print("Container size must not be less than one or more than 10 000!")
                container_size = randint(1, 10000)
        else:
            print("Container size must be a non-negative integer number!")
            container_size = randint(1, 10000)
        output_file_name = sys.argv[3]
        container.generate(container_size)
    else:
        print("Incorrect command line! You must write: command -f <inputFileName> <outputFileName>"
              "or command -n <inputFileName> <outputFileName>")
        exit()

    # Вывод информации об исходном контейнере в консоль
    container.print()

    # Вывод информации об исходном контейнере в файл
    out_file = open(output_file_name, 'w')
    container.write(out_file)

    # Фильтрация контейнера в соответствии с заданной функцией
    container.filter()

    # Вывод информации об изменённом контейнере
    container.write(out_file)
    out_file.close()

    print('==> Finish')
    # print("Time: ", round(time.time() - start, 5), " seconds")
