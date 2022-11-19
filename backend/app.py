from db import querys
from flask_cors import CORS
from crypto import eliptic_keys
from flask import Flask, request

app = Flask(__name__)
CORS(app)
cursor = querys.connect_db()


@app.get("/users")
def get_user():
    return {"users": querys.select_users(cursor)}


@app.post("/register")
def register_user():
    if not isinstance(request.json, dict):
        return {"error": True, "message": "invalid json format"}, 500

    username = request.json.get("username")
    password = request.json.get("password")

    if not isinstance(username, str) or not isinstance(password, str):
        return {"error": True, "message": "invalid values"}, 500

    eliptic_keys.register(username, password)
    querys.insert_users(cursor, username, password)

    return "Created", 201


@app.post("/login")
def create_user():
    if not isinstance(request.json, dict):
        return {"error": True, "message": "invalid json format"}, 500

    username = request.json.get("username")
    password = request.json.get("password")

    if not isinstance(username, str) or not isinstance(password, str):
        return {"error": True, "message": "invalid values"}, 500

    user = querys.select_user(cursor, username)
    if not user:
        return {"login": False, "register": False}

    isLoginWidthPassword = password != user[0][2]
    isLoginWidthKeys = eliptic_keys.login(username, password)

    if isLoginWidthPassword and isLoginWidthKeys:
        return {"login": False, "register": True}

    return {"login": True, "register": True}
