import psycopg2
from flask import Flask
from flask_cors import CORS
from crypto.keys import (
    key_gen_ed25519,
    decrypt_with_private_key,
    encrypt_with_public_key,
)


app = Flask(__name__)
CORS(app)


def connect():
    uri = "host=postgres dbname=postgres user=postgres password=postgres"
    conn = psycopg2.connect(uri)
    cursor = conn.cursor()
    cursor.execute("SELECT NOW()")
    res = cursor.fetchone()
    return str(res[0]) if res else "No response"


@app.get("/")
def hello_world():
    return connect()


@app.get("/keygen")
def key_gen():
    keys = key_gen_ed25519()
    private_key = keys.get("private_key")
    public_key = keys.get("public_key")
    return {"private_key": private_key.decode(), "public_key": public_key.decode()}


@app.get("/main")
def main():
    keys = key_gen_ed25519()
    message = b"You can do it"
    encrypted = encrypt_with_public_key(keys.get("public_key"), message)
    decrypted = decrypt_with_private_key(keys.get("private_key"), encrypted)

    print("message: ", message)
    print("encrypted_message: ", encrypted)
    print("decrypted_message: ", decrypted)

    return "Success"
