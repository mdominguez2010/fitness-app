from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from fitness_app.db import config

# import db.config
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + config.DB_FILE_PATH
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app_db = SQLAlchemy(app)

from fitness_app import routes