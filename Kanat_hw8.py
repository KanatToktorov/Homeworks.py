import sqlite3

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def insert_data(conn, sql, data):
    try:
        cursor = conn.cursor()
        cursor.executemany(sql, data)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def select_cities(conn):
    sql = '''SELECT cities.title FROM cities'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_students_by_city(conn, city_id):
    sql = '''
    SELECT students.first_name, students.last_name, countries.title as country, cities.title as city, cities.area
    FROM students
    JOIN cities ON students.city_id = cities.id
    JOIN countries ON cities.country_id = countries.id
    WHERE cities.id = ?
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (city_id,))
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)


sql_create_students_table = '''
CREATE TABLE IF NOT EXISTS students(    
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,    
    last_name TEXT NOT NULL,
    city_id INTEGER,    
    FOREIGN KEY (city_id) REFERENCES cities (id)
)
'''

sql_to_create_cities_table = '''
CREATE TABLE IF NOT EXISTS cities(    
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,    
    area REAL DEFAULT 0,
    country_id INTEGER,    
    FOREIGN KEY (country_id) REFERENCES countries (id)
)
'''

sql_to_create_countries_table = '''
CREATE TABLE IF NOT EXISTS countries(    
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL    
)
'''

sql_insert_students_data = '''
INSERT INTO students (first_name, last_name, city_id) VALUES (?,?,?)
'''

sql_insert_countries_data = '''
INSERT INTO countries (title) VALUES (?)
'''

sql_insert_cities_data = '''
INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)
'''


cities_data = [('Москва', 90000, 1), ('Бишкек', 12000, 2), ('Вашингтон', 70000, 3), ('Томск', 30000, 1), ('Ош', 8000, 2), ('Чикаго', 50000, 3), ('Сочи', 25000, 1)]
countries_data = [('РФ',), ('КР',), ('США',)]
students_data = [
    ('Никита', 'Камнев', 1),
    ('Алмаз', 'Ташов', 2),
    ('Давид', 'Стоун', 3),
    ('Егор', 'Камнев', 4),
    ('Бакыт', 'Ташов', 5),
    ('Джон', 'Стоун', 6),
    ('Иван', 'Камнев', 7),
    ('Максим', 'Камнев', 1),
    ('Адилет', 'Ташов', 2),
    ('Джек', 'Стоун', 3),
    ('Андрей', 'Камнев', 4),
    ('Бектур', 'Ташов', 5),
    ('Роберт', 'Стоун', 6),
    ('Михаил', 'Камнев', 7),
    ('Матвей', 'Камнев', 1)
]
connection = create_connection('hw8.db')
if connection is not None:
    print('Succesfully connected')
create_table(connection, sql_create_students_table)
insert_data(connection, sql_insert_students_data, students_data)
create_table(connection, sql_to_create_countries_table)
insert_data(connection, sql_insert_countries_data, countries_data)
create_table(connection, sql_to_create_cities_table)
insert_data(connection, sql_insert_cities_data, cities_data)
select_cities(connection)
select_students_by_city(connection, city_id=1)


while True:
    print('Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:')
    select_cities(connection)

    selected_city_id = int(input('Введите id города: '))
    if selected_city_id == 0:
        break

    select_students_by_city(connection, selected_city_id)


connection.close()

