import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def insert_product(connection, product):
    sql = '''INSERT INTO products
    (product_title, price, quantity)
    VALUES
    (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def update_product_quantity(connection, product):
    sql = '''UPDATE products SET quantity = ? 
                    WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_product_price(connection, product):
    sql = '''UPDATE products SET price = ?
                    WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def delete_product(connection, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(connection):
    sql = '''SELECT * FROM products'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_by_limit(connection, limit_one, limit_two):
    sql = '''SELECT * FROM products WHERE price < ? AND quantity < ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (limit_one, limit_two))
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)
def select_products_by_word(connection, word):
    sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, ('%' + word + '%',))
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)


sql_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10,2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

my_connection = create_connection('hw.db')
if my_connection is not None:
    print('Successfully connected to DB!')
    # create_table(my_connection, sql_create_products_table)
    # insert_product(my_connection, ('мыло хозяйственное', 40.5, 200))
    # insert_product(my_connection, ('мыло туалетное', 55.0, 100))
    # insert_product(my_connection, ('мыло детское', 80.0, 155))
    # insert_product(my_connection, ('жидкое мыло с запахом ванили', 120.0, 38))
    # insert_product(my_connection, ('порошок автомат', 120.0, 84))
    # insert_product(my_connection, ('порошок ручная стирка', 96.54, 49))
    # insert_product(my_connection, ('шампунь детский Три кота', 180.55, 3))
    # insert_product(my_connection, ('мужской шампунь Clear', 280.0, 24))
    # insert_product(my_connection, ('женский шампунь PRO', 345.09, 55))
    # insert_product(my_connection, ('зубная паста', 130.6, 8))
    # insert_product(my_connection, ('средство для мытья посуды', 180.0, 15))
    # insert_product(my_connection, ('чистящее средство', 85.3, 4))
    # insert_product(my_connection, ('туалетная бумага', 14.7, 670))
    # insert_product(my_connection, ('бумажные салфетки', 20.8, 560))
    # insert_product(my_connection, ('влажные салфетки', 85.0, 3))
    # update_product_quantity(my_connection, (900, 13))
    # update_product_price(my_connection, (300.3, 8))
    # delete_product(my_connection, 11)
    # select_all_products(my_connection)
    # select_products_by_limit(my_connection, 100, 5)
    # select_products_by_word(my_connection, 'мыло')

    my_connection.close()