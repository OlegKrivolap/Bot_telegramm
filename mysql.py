import pymysql.cursors
import parcer

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    database='sys',
    user='root',
    password='qwerty',
    cursorclass=pymysql.cursors.DictCursor
)

conn.autocommit(True)


def create_table(conn_1):
    with conn_1.cursor() as cursor:
        cursor.execute(
            'CREATE TABLE page_1 (id serial PRIMARY KEY, '
            'name TEXT, price TEXT, picture TEXT, url TEXT);'
        )
        print('[INFO]CREATE TABLE successfully')


def insert_data(conn_1, data):
    count = 1
    with conn_1.cursor() as cursor:
        while count < len(data):
            cursor.execute(
                'INSERT INTO page_1 (name, price, picture, url) '
                f'VALUES (\'{data[count]["name"]}\', \'{data[count]["price"]}\', '
                f'\'{data[count]["picture"]}\', \'{data[count]["url"]}\');'
            )
            count += 1
        print('[INFO]Data inserted successfully')


def select_data(conn_1, id_1):
    with conn_1.cursor() as cursor:
        cursor.execute(
            'SELECT name, price, picture, url FROM page_1 '
            f'WHERE id ={id_1};'
        )
        for_return = cursor.fetchone()
    return for_return


def select_jeans(conn_1):
    with conn_1.cursor() as cursor:
        cursor.execute(
            'SELECT name, price, picture, url FROM sys.page_1 WHERE name LIKE \'%Jeans\';'
        )
        for_return = cursor.fetchall()
    return for_return


def select_dress(conn_1):
    with conn_1.cursor() as cursor:
        cursor.execute(
            'SELECT name, price, picture, url FROM page_1 WHERE name LIKE \'%Dress\';'
        )
        for_return = cursor.fetchall()
    return for_return


def select_slacks(conn_1):
    with conn_1.cursor() as cursor:
        cursor.execute(
            'SELECT name, price, picture, url FROM page_1 WHERE name LIKE \'%Slacks\';'
        )
        for_return = cursor.fetchall()
    return for_return


def select_top(conn_1):
    with conn_1.cursor() as cursor:
        cursor.execute(
            'SELECT name, price, picture, url FROM page_1 WHERE name LIKE \'%Top%\';'
        )
        for_return = cursor.fetchall()
    return for_return


def select_jumpsuit(conn_1):
    with conn_1.cursor() as cursor:
        cursor.execute(
            'SELECT name, price, picture, url FROM page_1 WHERE name LIKE \'%Jumpsuit%\';'
        )
        for_return = cursor.fetchall()
    return for_return


def select_jacket(conn_1):
    with conn_1.cursor() as cursor:
        cursor.execute(
            'SELECT name, price, picture, url FROM page_1 WHERE name LIKE \'%Jacket%\';'
        )
        for_return = cursor.fetchall()
    return for_return


def select_sweatshirt(conn_1):
    with conn_1.cursor() as cursor:
        cursor.execute(
            'SELECT name, price, picture, url FROM page_1 WHERE name LIKE \'%Sweatshirt%\';'
        )
        for_return = cursor.fetchall()
    return for_return


def select_blouse(conn_1):
    with conn_1.cursor() as cursor:
        cursor.execute(
            'SELECT name, price, picture, url FROM page_1 WHERE name LIKE \'%Blouse%\';'
        )
        for_return = cursor.fetchall()
    return for_return


if __name__ == '__main__':
    create_table(conn)
    for i in parcer.our_dict[1:]:
        insert_data(conn, i)
    conn.close()
