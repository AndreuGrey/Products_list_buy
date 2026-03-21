import sqlite3 as sq


def delete_db():  # Удаляет таблицу
    with sq.connect("my_products.db") as con:
        cur = con.cursor()

        cur.execute("DROP TABLE IF EXISTS products")


def create_db():  # Создаёт таблицу
    with sq.connect("my_products.db") as con:
        cur = con.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS products(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL)
        """)


def check_product_db(name):  # Проверяет есть ли продукт в таблице
    with sq.connect("my_products.db") as con:
        cur = con.cursor()

        cur.execute("SELECT * FROM products")

        products = cur.fetchall()
        for product in products:
            if product[1] == name:
                return False
            else:
                continue


def add_product_db(name):  # Добавление продукта в таблицу
    with sq.connect("my_products.db") as con:
        cur = con.cursor()

        cur.execute("INSERT INTO products (name) VALUES (?)", (name,))
        print('\033[H\033[J', end='')
        print(f'Продукт {name} добавлен в список!')


def list_product_db():  # Выдаёт список продуктов в таблице
    with sq.connect("my_products.db") as con:
        cur = con.cursor()

        cur.execute("SELECT * FROM products")

        products = cur.fetchall()
        for product in products:
            print(f"{product[0]}: {product[1]}")  # Выводит так: (id: name)
# В SQLite (product[0] или [1]) перебирает значения в строках. Можно выбрать какое надо


def del_product_db(name):  # Удаление продукта из таблицы
    with sq.connect("my_products.db") as con:
        cur = con.cursor()

        if name == 'Все' or name == 'Всё':  # Удаляет все продукты
            cur.execute("DROP TABLE IF EXISTS products")
            print('Удалены все продукты из списка!')
            create_db()
        else:  # Удаляет выбранный продукт (удаляет все одинаковые названия)
            cur.execute("SELECT name FROM products")
            prod_list = cur.fetchone()
            if name == prod_list[0]:  # Проверяет на наличие такого названия
                cur.execute("""
                    DELETE FROM products 
                    WHERE name == (?)
                """, (name,))
                print(f'Продукт - <{name}> удалён!')
            else:
                print(f'Такого продукта нет в списке!')
# Нужно изменять порядок id 1, 2, 4, 5 на 1, 2, 3, 4 после удаления


def check_count():  # Считает кол-во записей в таблице(нужно для изменения удаления)
    with sq.connect("my_products.db") as con:
        cur = con.cursor()

        cur.execute("SELECT count() FROM products")

        count_products = cur.fetchone()
        print(count_products[0])
