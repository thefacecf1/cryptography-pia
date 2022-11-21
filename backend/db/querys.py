def select_users(cursor):
    query = "SELECT * FROM accounts"
    cursor.execute(query)
    return cursor.fetchall()


def select_user(cursor, username: str):
    query = "SELECT * FROM accounts WHERE username='{}'".format(username)
    cursor.execute(query)
    return cursor.fetchall()


def insert_user(cursor, username: str, password: str):
    query = "INSERT INTO accounts (username,password) VALUES ('{}', '{}')".format(username, password)
    cursor.execute(query)
