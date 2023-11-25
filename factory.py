from flask import Flask
from flask_restful import Api
from config import Config

from alfabet.resources.view import init_view
from alfabet.database import db
from flask_cors import CORS

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    api = Api(app)
    init_view(api)
    db.init_app(app)
    CORS(app)

    with app.app_context():
        db.create_all()
    return app 