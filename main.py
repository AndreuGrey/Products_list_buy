# здесь будет меню программы
from list import list_product


def starting_programm():
    print('Добро пожаловать в Список продуктов')
    command = input('Введите свой запрос: ')
    return command.capitalize()


def continue_programm():
    command = input('Введите свой запрос: ')
    return command.capitalize()


def working_programm(command):
    if command == 'Добавить':
        while True:
            product = input('Введите продукт: ')
            if product == '' or product == 'Стоп':
                break
            else:
                list_product.append(product)
    elif command == 'Удалить':
        pass
    elif command == 'Список':
        print('Список продуктов: ')
        for i in range(len(list_product)):
            print(f'{i + 1}:{list_product[i]}', sep='\n')


# Работа самой программы
working_programm(starting_programm())
while True:
    working_programm(continue_programm())
