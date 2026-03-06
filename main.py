# здесь будет меню программы
from list import list_product


def starting_programm():
    print('Добро пожаловать в Список продуктов')
    command = input('Введите свой запрос: ')
    return command


def continue_programm():
    command = input('Введите свой запрос: ')
    return command


def working_programm(command):
    if command == 'Добавить':
        list_product.append(input('Введите продукт: '))
    elif command == 'Удалить':
        pass
    elif command == 'Список':
        print('Список продуктов: ')
        for i in range(len(list_product)):
            print(list_product[i], sep='\n')


# Работа самой программы
working_programm(starting_programm())
while True:
    working_programm(continue_programm())
