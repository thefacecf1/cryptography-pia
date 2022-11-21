def select_users(cursor):
    query = "SELECT * FROM accounts"
    cursor.execute(query)
    return cursor.fetchall()


def select_user(cursor, username: str):
    query = "SELECT * FROM accounts WHERE username='{}'".format(username)
    cursor.execute(query)
    return cursor.fetchone()


def insert_user(cursor, username: str, password: str):
    query = "INSERT INTO accounts (username,password) VALUES ('{}', '{}')".format(username, password)
    cursor.execute(query)


def select_messages(cursor):
    query = "SELECT * FROM messages"
    cursor.execute(query)
    return cursor.fetchall()


def insert_message(cursor, username: str, message: str):
    query = "INSERT INTO messages(username,message) VALUES ('{}', '{}')".format(username, message)
    cursor.execute(query)
