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
                if db.check_product_db(product) != False:
                    db.add_product_db(product)
                else:
                    print(f"<{product}> уже есть в списке!")
                    continue
    elif command == 'Удалить таблицу':
        db.delete_db()
    elif command == 'Перезапустить таблицу':
        db.delete_db()
        db.create_db()
    elif command == 'Проверка':
        db.check_count()
    elif command == 'Удалить':
        while True:
            product = input('Введите продукт: ')
            if product == '' or product == 'Стоп':
                print('\033[H\033[J', end='')  # очистка терминала
                print('Список продуктов: ')
                db.list_product_db()
                break
            else:
                print('\033[H\033[J', end='')
                db.del_product_db(product)
                break
    elif command == 'Список':
        print('\033[H\033[J', end='')
        print('Список продуктов: ')
        db.list_product_db()


# Работа самой программы
working_programm(starting_programm())
while True:
    working_programm(continue_programm())
