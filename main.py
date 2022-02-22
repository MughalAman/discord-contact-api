from dotenv import load_dotenv
from flask import Flask, request
from flask_restx import Api, Resource
import json
import requests
import os

load_dotenv()

app = Flask(__name__)
api = Api(app, version='1.0', title='Discord contact API',
    description='API for sending contact messages to Discord using webhooks',
) 

class sendMessage(Resource):
    def post(self):
        data = request.get_json()
        if data is None:
            return {'error': 'No data received'}, 400
        else:
            result = requests.post(os.environ['WEBHOOK_URL'], data=data)
            return result.status_code

api.add_resource(sendMessage, '/sendMessage')

if __name__ == '__main__':
    app.run(debug=True)