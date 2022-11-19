import psycopg2

def connect_db():
    uri = "host=postgres dbname=postgres user=postgres password=postgres"
    conn = psycopg2.connect(uri)
    return conn.cursor()

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
