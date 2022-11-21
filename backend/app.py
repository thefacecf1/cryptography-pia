from flask_cors import CORS
from db import querys, postgres
from crypto import eliptic_keys
from flask import Flask, request

app = Flask(__name__)
CORS(app)
cursor = postgres.cursor()


@app.post("/login")
def login():
    if not isinstance(request.json, dict):
        return {"error": True, "message": "invalid json format"}, 500

    username = request.json.get("username")
    password = request.json.get("password")

    if not isinstance(username, str) or not isinstance(password, str):
        return {"error": True, "message": "invalid values"}, 500

    user = querys.select_user(cursor, username)

    if user is None:
        return {"login": False, "register": False}, 404

    isLoginWithPassword = password == user.get("password")
    isLoginWithKeys = eliptic_keys.login(username, password)

    if not isLoginWithPassword or not isLoginWithKeys:
        return {"login": False, "register": True}, 401

    return {"login": True, "register": True}, 200


@app.get("/users")
def list_users():
    return {"users": querys.select_users(cursor)}


@app.post("/users")
def store_user():
    if not isinstance(request.json, dict):
        return {"error": True, "message": "invalid json format"}, 500

    username = request.json.get("username")
    password = request.json.get("password")

    if not isinstance(username, str) or not isinstance(password, str):
        return {"error": True, "message": "invalid values"}, 500

    user = querys.select_user(cursor, username)
    if user:
        return {"error": True, "message": "user already exists"}, 403

    eliptic_keys.register(username, password)
    querys.insert_user(cursor, username, password)

    return "Created", 201


@app.get("/messages")
def list_messages():
    return {"messages": querys.select_messages(cursor)}


@app.post("/messages")
def store_message():
    if not isinstance(request.json, dict):
        return {"error": True, "message": "invalid json format"}, 500

    username = request.json.get("username")
    message = request.json.get("message")

    if not isinstance(username, str) or not isinstance(message, str):
        return {"error": True, "message": "invalid values"}, 500

    user = querys.select_user(cursor, username)

    if user is None:
        return {"error": True, "message": "not found user"}, 404

    querys.insert_message(cursor, username, message)

    return "Created", 201
