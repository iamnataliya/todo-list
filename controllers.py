import csv
import os
import string


def clear_terminal():
    """
    Очистка окна терминала в зависимости от типа ОС

    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


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


all_task = read_file('todo-list/todo.csv')


def add_task(todo: dict):
    clear_terminal()
    todo_new = input("Введите новую задачу: ")
    id_new = max(all_task)+1
    all_task[id_new] = all_task.append(todo_new,0)
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
    print_todo(todo, 1)
    del_str = int(input('Введите id задачи для удаления: '))
    del todo[del_str]
    print(f'Задача {del_str} удалена')
    print('Для возврата в меню нажмите ENTER...')
    input()
    clear_terminal()


def save_data(todo: dict):
    # clear_terminal()
    with open('todo-list/todo.csv', 'w', encoding='utf-8') as file:
        todo_save = csv.writer(file, delimiter=',')
        for k, v in todo.items():
            new_line = f"{k}, {v['task']}, {v['is_done']}"
            todo_save.writerow(new_line)
            print(k, v['task'], v['is_done'])

    
    # print('Для возврата в меню нажмите ENTER...')
    # input()
    # clear_terminal()


def print_todo(to_do: dict, done: int) -> None:
    """
    Вывод в консоль списка дел на основе переданного значения 'done'.

    :param to_do: словарь с данными.
    :param done: параметр match для печати соответствующих данных.
    :return: None.
    """
    match done:
        case 1:
            clear_terminal()
            print('Список дел:')
            for key, value in to_do.items():
                # Вывод ID и названия дела
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
                        # Вывод названия выполненных дел
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
                        # Вывод невыполненных дел
                        print("\033[31m {} \033[0m".format(value['task']))
            print('Для возврата в меню нажмите ENTER...')
            input()
            clear_terminal()


if __name__ == "__main__":
    pass
