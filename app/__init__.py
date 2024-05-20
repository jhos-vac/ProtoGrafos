from flask import Flask
from flask_restx import Api
from app.main import app

app = Flask(__name__)
api = Api(app)

api.register_blueprint(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)