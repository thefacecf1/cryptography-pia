import time
import psycopg2


def connect():
    uri = "host=postgres dbname=postgres user=postgres password=postgres"
    try:
        return psycopg2.connect(uri)
    except:
        return None


def connect_db():
    connection = None

    for i in range(10):
        res = connect()
        if res is not None:
            connection = res
            break
        time.sleep(2)

    return connection


def select_users(cursor):
    query = "SELECT * FROM accounts"
    cursor.execute(query)
    return cursor.fetchall()


def select_user(cursor, username: str):
    query = "SELECT * FROM accounts WHERE username='{}'".format(username)
    cursor.execute(query)
    return cursor.fetchall()


def insert_users(cursor, username: str, password: str):
    query = "INSERT INTO accounts (username,password) VALUES ('{}', '{}')".format(
        username, password
    )
    cursor.execute(query)
