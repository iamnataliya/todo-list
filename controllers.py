import csv
import os


# Декоратор. Очистка окна терминала в зависимости от типа ОС
def clear_terminal(function):
    def inner(*args, **kwargs):
        os.system('cls' if os.name == 'nt' else 'clear')
        function(*args, **kwargs)
        print('Для возврата в меню нажмите ENTER...')
        input()
        os.system('cls' if os.name == 'nt' else 'clear')

    return inner


def read_file(filename: str) -> dict:
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
                    'is_done': int(row[2])
                }
    except FileNotFoundError:
        print('Файл не найден. Проверьте имя файла и/или путь к файлу.')
    return result


all_task = read_file('todo.csv')


@clear_terminal
def add_task(todo: dict):
    todo_new = input("Введите новую задачу: ")
    id_new = len(todo.items()) + 1
    result_new = {}
    result_new = {
        'task': todo_new,
        'is_done': 0
    }
    todo[id_new] = result_new
    print("\033[35m {} \033[0m".format(f"Ваша задача < {todo_new} > добавлена."))


@clear_terminal
def edit_task(todo: dict):
    print_todo(all_task, 1)
    n = int(input('Введите ID задачи которую хотите изменить: '))
    for k,v in todo.items():
        if k == n:
            v['is_done'] = int(input('Введите статус задачи (1 - выполнено, 0 - не выполнено): '))
            v['task'] = input('Введите новое название задачи: ')
    


@clear_terminal
def del_task(todo: dict):
    print_todo(todo, 1)
    del_str = int(input('Введите id задачи для удаления: '))
    del todo[del_str]
    print(f'Задача {del_str} удалена')


@clear_terminal
def save_data(todo: dict):
    with open('todo-list/todo.csv', 'w', encoding='utf-8') as file:
        todo_save = csv.writer(file, delimiter=',')
        for k, v in todo.items():
            new_line = f"{k}, {v['task']}, {v['is_done']}"
            todo_save.writerow(new_line)
            print(k, v['task'], v['is_done'])


@clear_terminal
def print_todo(to_do: dict, done: int) -> None:
    """
    Вывод в консоль списка дел на основе переданного значения 'done'.

    :param to_do: словарь с данными.
    :param done: параметр match для печати соответствующих данных.
    :return: None.
    """
    match done:
        case 1:
            print('Список дел:')
            for key, value in to_do.items():
                # Вывод ID и названия дела
                print("\033[7m {} \033[0m".format(f'ID {key} >>> {value["task"]}'))
        case 2:
            print('Уже сделано:')
            for value in to_do.values():
                for k, v in value.items():
                    if k == 'is_done' and v:
                        # Вывод названия выполненных дел
                        print("\033[36m {} \033[0m".format(value['task']))
        case 3:
            print('Надо сделать:')
            for value in to_do.values():
                for k, v in value.items():
                    if k == 'is_done' and not v:
                        # Вывод невыполненных дел
                        print("\033[31m {} \033[0m".format(value['task']))
