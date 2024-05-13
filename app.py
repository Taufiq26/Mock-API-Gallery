from flask import Flask, request

app = Flask(__name__)

mock_user_id = "0ef8a3f7-2779-4208-95e4-5a5488e5e3c4"
mock_username = "demo_user"
mock_password = "d3m0password123"
mock_access_token = "hs0IcxqvC24SZDad5FGRbVHe2mH5x1dlkiBCDuxspsAipgaCvZFsyHJI5YBSvJAu"

@app.get("/")
def hello_world():
    res = {
        'message': 'Hello, World!'
    }

    return res

@app.post("/login")
def do_login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == mock_username and password == mock_password:
        status = 200
        res = {
            'id': mock_user_id,
            'name': 'Demo User',
            'address': 'Bandung, Jawa Barat, Indonesia',
            'access_token': mock_access_token
        }
    else:
        status = 401
        res = {
            'message': 'Wrong username and password combination!'
        }

    return res, status