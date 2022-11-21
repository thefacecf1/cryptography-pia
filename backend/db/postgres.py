import time
import psycopg2

def connect():
    try:
        return psycopg2.connect("host=postgres dbname=postgres user=postgres password=postgres")
    except:
        return None


def cursor():
    connection = None
    for i in range(5):
        connection = connect()
        if connection is not None:
            return connection.cursor()
        print("Retry to connect after 2 sec")
        print("Try number {} of 5".format(i))
        time.sleep(2)
    raise Exception("Failed to connect to database")

