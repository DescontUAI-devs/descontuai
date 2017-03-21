# Configuring App
from datetime import datetime
from flask import Flask
from flask import render_template
from flask_mail import Mail, Message
from flask_restful import Resource, Api, reqparse
from decouple import config
app = Flask(__name__)
api = Api(app)

# EMAIL CONFIGURATION

app.config['MAIL_SERVER'] = config('MAIL_SERVER')
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = config('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = config('MAIL_PASSWORD')

mail = Mail(app)

class Customer(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, location='json')
        parser.add_argument('email', type=str, required=True, location='json')

        data = parser.parse_args(strict=True)
        data['enviado_em'] = datetime.now()
        content = {"mensagem": "Cliente cadastrado com sucesso!", "status_code": 200}

        return content, content['status_code']


class Contact(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, location='json')
        parser.add_argument('email', type=str, required=True, location='json')
        parser.add_argument('phone', type=str, location='json')
        parser.add_argument('description', type=str, required=True, location='json')

        data = parser.parse_args(strict=True)
        data['enviado_em'] = datetime.now()

        # Email Message

        msg = Message(
            '[Descontuai] Dúvida de {}'.format(data.name),
            sender='doscontuai@gmail.com',
            recipients=
            ['doscontuai@gmail.com'])

        msg.html = render_template('contact_mail_template.html', contact=data)

        mail.send(msg)

        content = {"mensagem": "Dúvida enviada com sucesso!", "status_code": 200}

        return content, content['status_code']

api.add_resource(Customer, '/api/v1/customer')
api.add_resource(Contact, '/api/v1/contact')

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
