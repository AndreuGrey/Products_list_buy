import programm_db as db


def starting_programm():
    print('Добро пожаловать в Список продуктов')
    db.create_db()
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
                print('\033[H\033[J', end='')  # очистка терминала
                print('Список продуктов: ')
                db.list_product_db()
                break
            else:
                db.add_product_db(product)
    elif command == 'Удалить таблицу':
        db.delete_db()
    elif command == 'Удалить':
        while True:
            product = input('Введите продукт: ')
            if product == '' or product == 'Стоп':
                print('\033[H\033[J', end='')  # очистка терминала
                print('Список продуктов: ')
                db.list_product_db()
                break
            else:
                db.del_product_db(product)
    elif command == 'Список':
        print('\033[H\033[J', end='')
        print('Список продуктов: ')
        db.list_product_db()


# Работа самой программы
working_programm(starting_programm())
while True:
    working_programm(continue_programm())
