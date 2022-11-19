def create_users_table(cursor):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS accounts(
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        password VARCHAR(255) NOT NULL)
        """
    )


def insert_users(cursor, username, password):
    cursor.execute(
        "INSERT INTO accounts (username,password) VALUES ('{}', '{}')".format(
            username, password
        )
    )


def select_users(cursor):
    cursor.execute(
        """
        SELECT * FROM accounts
        """
    )
    return cursor.fetchall()


def select_user(cursor, username, password):
    cursor.execute(
        """
        SELECT * FROM accounts WHERE username='{}' AND password='{}'
        """.format(
            username, password
        )
    )
    return cursor.fetchall()
