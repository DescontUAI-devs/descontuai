# Configuring App
from datetime import datetime
from flask import Flask
from flask import render_template
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class Customer(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, location='json')
        parser.add_argument('email', type=str, required=True, location='json')

        data = parser.parse_args(strict=True)
        data['enviado_em'] = datetime.now()
        content = {"mensagem": "Cliente cadastrado com sucesso!", "status_code": 200}

        return content, content['status_code']


api.add_resource(Customer, '/api/v1/customer')

# Todo: Connect app with MongoDB Server using Flask-Pymongo

# Todo: Parse parameters passed in API using reqparse (RequestParser)

# Todo: create API for register a new user (customer). (Only POST method) using Flask-RESTFul

# Todo: Implement Payment Gateway (Pagseguro).


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
