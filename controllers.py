import csv


def read_file(filename: str) -> dict[dict]:
    """
    Выгружает в память словарь с данными из CSV файла.

    :param filename: имя файла.
    :return: словарь.
    """
    result = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                result[int(row[0])] = {
                    'task': str(row[1]),
                    'is_done': bool(int(row[2]))
                }
    except FileNotFoundError:
        print('Файл не найден. Проверьте имя файла и/или путь к файлу.')
    return result


all_task = read_file('todo.csv')


def print_todo(to_do: dict, done: int) -> None:
    """
    Вывод в консоль списка дел на основе переданного значения done.

    :param to_do: словарь с данными.
    :param done: параметр match для печати соответствующих данных.
    :return: None.
    """
    match done:
        case 1:
            for value in to_do.values():
                print(value)
        case 2:
            for value in to_do.values():
                for k, v in value.items():
                    if k == 'is_done' and v:
                        print(value)
        case 3:
            for value in to_do.values():
                for k, v in value.items():
                    if k == 'is_done' and not v:
                        print(value)


def main():
    pass


if __name__ == "__main__":
    main()
