from app import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
db.init_app(app)

from database.db_schema import Performance, User, user_schema, users_schema, performances_schema, performance_schema
