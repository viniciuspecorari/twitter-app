
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.cli import FlaskGroup
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
cli = FlaskGroup(app)
migrate = Migrate()
migrate.init_app(app, db)


from app.controllers import default 