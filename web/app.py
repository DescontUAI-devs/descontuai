# Configuring App
from flask import Flask
from flask import render_template

app = Flask(__name__)

# Todo: Connect app with MongoDB Server using Flask-Pymongo

# Todo: Parse parameters passed in API using reqparse (RequestParser)

# Todo: create API for register a new user (customer). (Only POST method) using Flask-RESTFul

# Todo: Implement Payment Gateway (Pagseguro).


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
