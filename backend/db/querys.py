import psycopg2

def connect():
    uri = "host=postgres dbname=postgres user=postgres password=postgres"
    return psycopg2.connect(uri)


def connect_db():
    connection = None

    for i in range(10):
        try:
            connection = connect()
            break
        except:
            print(i)
            pass

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
    query = "INSERT INTO accounts (username,password) VALUES ('{}', '{}')".format(username, password)
    cursor.execute(query)
