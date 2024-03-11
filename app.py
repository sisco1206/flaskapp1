from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "<b> My first Flask application is in action! </b>"

    # return {"Message": "Hello world"}  json file
