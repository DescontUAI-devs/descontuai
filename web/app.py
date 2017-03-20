# Configuring App
from flask import Flask

app = Flask(__name__)

# Todo: Connect app with MongoDB Server using Flask-Pymongo

# Todo: Parse parameters passed in API using reqparse (RequestParser)

# Todo: create API for register a new user (customer). (Only POST method) using Flask-RESTFul

# Todo: Implement Payment Gateway (Pagseguro).


@app.route("/")
def index():
    # Todo: Render index template
    return 'Yay! Tá no ar!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
