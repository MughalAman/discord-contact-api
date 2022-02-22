from dotenv import load_dotenv
from flask import Flask, request
from flask_restx import Api, Resource
from flask_cors import CORS
import json
import requests
import os

load_dotenv()

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000", "https://amppa.dev"])
api = Api(app, version='1.0', title='Discord contact API',
    description='API for sending contact messages to Discord using webhooks',
) 

class sendMessage(Resource):
    def post(self):
        data = request.get_json()
        if data is None:
            return {'error': 'No data received'}, 400
        else:
            result = requests.post(os.environ['WEBHOOK_URL'], json=data)
            return result.status_code

api.add_resource(sendMessage, '/api/sendMessage')

if __name__ == '__main__':
    app.run(debug=True)