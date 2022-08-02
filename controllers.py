import csv
import os


def clear_terminal():
    """
    Очистка окна терминала

    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


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


def add_task(todo: dict):
    clear_terminal()
    # Start coding here
    print('Для возврата в меню нажмите ENTER...')
    input()
    clear_terminal()


def edit_task(todo: dict):
    clear_terminal()
    # Start coding here
    print('Для возврата в меню нажмите ENTER...')
    input()
    clear_terminal()


def del_task(todo: dict):
    clear_terminal()
    # Start coding here
    print('Для возврата в меню нажмите ENTER...')
    input()
    clear_terminal()


def save_data(todo: dict):
    clear_terminal()
    # Start coding here
    print('Для возврата в меню нажмите ENTER...')
    input()
    clear_terminal()


def print_todo(to_do: dict, done: int) -> None:
    """
    Вывод в консоль списка дел на основе переданного значения done.

    :param to_do: словарь с данными.
    :param done: параметр match для печати соответствующих данных.
    :return: None.
    """
    match done:
        case 1:
            clear_terminal()
            print('Список дел:')
            for key, value in to_do.items():
                print("\033[7m {} \033[0m".format(f'ID {key} >>> {value["task"]}'))
            print('Для возврата в меню нажмите ENTER...')
            input()
            clear_terminal()
        case 2:
            clear_terminal()
            print('Уже сделано:')
            for value in to_do.values():
                for k, v in value.items():
                    if k == 'is_done' and v:
                        print("\033[36m {} \033[0m".format(value['task']))
            print('Для возврата в меню нажмите ENTER...')
            input()
            clear_terminal()
        case 3:
            clear_terminal()
            print('Надо сделать:')
            for value in to_do.values():
                for k, v in value.items():
                    if k == 'is_done' and not v:
                        print("\033[31m {} \033[0m".format(value['task']))
            print('Для возврата в меню нажмите ENTER...')
            input()
            clear_terminal()


if __name__ == "__main__":
    pass
