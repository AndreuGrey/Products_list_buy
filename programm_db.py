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


def check_product_db(product):  # Проверяет есть ли продукт в таблице
    with sq.connect("my_products.db") as con:
        cur = con.cursor()

        cur.execute("SELECT name FROM products")

        rows = cur.fetchall()
        for row in rows:
            print(row)
            if row == product:
                print("Этот продукт уже есть в списке!")
                return False
            else:
                return True


def add_product_db(product):  # Добавление продукта в таблицу
    with sq.connect("my_products.db") as con:
        cur = con.cursor()

        cur.execute("INSERT INTO products (name) VALUES (?)", (product,))


def list_product_db():  # Выдаёт список продуктов в таблице
    with sq.connect("my_products.db") as con:
        cur = con.cursor()

        cur.execute("SELECT * FROM products")

        rows = cur.fetchall()
        for row in rows:
            print(row)


def del_product_db(product):  # Удаление продукта из таблицы
    with sq.connect("my_products.db") as con:
        cur = con.cursor()

        if product == 'Все' or product == 'Всё':
            cur.execute("DROP TABLE IF EXISTS products")
            print('Удалены все продукты из списка!')
            create_db()
        else:
            cur.execute("DELETE FROM products WHERE name == (?)", (product,))
            print(f'Продукт - {product} удалён!')
