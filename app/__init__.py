from app.configuration import Config
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config.from_object(Config)

ma = Marshmallow(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)


from app.views import *
from database.cli_commands import *
