import query
import psycopg2
from crypto import eliptic
from crypto import keys
from flask_cors import CORS
from flask import Flask, request


app = Flask(__name__)
CORS(app)

uri = "host=postgres dbname=postgres user=postgres password=postgres"
conn = psycopg2.connect(uri)
cursor = conn.cursor()


@app.get("/users")
def get_user():
    users = query.select_users(cursor)
    return {"users": users}


@app.post("/register")
def register_user():
    username = request.json.get("username")
    password = request.json.get("password")
    eliptic.register(username, password)
    query.insert_users(cursor, username, password)
    return "Success"


@app.post("/login")
def create_user():
    username = request.json.get("username")
    password = request.json.get("password")

    register = query.select_user(cursor, username, password)
    if not bool(register):
        return {"login": False}

    dbPassword = register[0][2]
    isSamePassword = dbPassword == password
    isLogin = eliptic.login(username, password)

    if isLogin and isSamePassword:
        return {"login": True, "userPassword": password, "dbPassword": dbPassword}

    return {"login": False}


@app.get("/keygen")
def key_gen():
    keys_pair = keys.key_gen_RSA()
    private_key = keys_pair.get("private_key")
    public_key = keys_pair.get("public_key")
    return {"private_key": private_key.decode(), "public_key": public_key.decode()}
