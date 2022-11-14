from flask import Flask
from flask_cors import CORS
from crypto.keys import (
    key_gen_ed25519,
    decrypt_with_private_key,
    encrypt_with_public_key,
)


app = Flask(__name__)
CORS(app)


@app.get("/")
def hello_world():
    return "Hello world from Backend"


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
