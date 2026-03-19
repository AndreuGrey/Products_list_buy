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


def check_product_db(name):  # Проверяет есть ли продукт в таблице(не работает)
    with sq.connect("my_products.db") as con:
        cur = con.cursor()

        cur.execute("SELECT name FROM products")

        products = cur.fetchall()  # Не работает выборка продукта
        for product in products:
            if product[1] == name:
                print("Этот продукт уже есть в списке!")
                return False
            else:
                return True


def add_product_db(name):  # Добавление продукта в таблицу
    with sq.connect("my_products.db") as con:
        cur = con.cursor()

        cur.execute("INSERT INTO products (name) VALUES (?)", (name,))


def list_product_db():  # Выдаёт список продуктов в таблице
    with sq.connect("my_products.db") as con:
        cur = con.cursor()

        cur.execute("SELECT * FROM products")

        products = cur.fetchall()  # Не могу сделать вывод (1. Сыр) и тд.
        for product in products:
            print(f"{product[0]}: {product[1]}")  # Выводит так: (id: name)


def del_product_db(name):  # Удаление продукта из таблицы
    with sq.connect("my_products.db") as con:
        cur = con.cursor()

        if name == 'Все' or name == 'Всё':  # Удаляет все продукты
            cur.execute("DROP TABLE IF EXISTS products")
            print('Удалены все продукты из списка!')
            create_db()
        else:  # Удаляет выбранный продукт
            cur.execute(
                "DELETE FROM products WHERE name == (?)", (name,))
            print(f'Продукт - "{name}" удалён!')
