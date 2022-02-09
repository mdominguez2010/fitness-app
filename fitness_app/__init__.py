from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from fitness_app.db import config

# import db.config
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + config.DB_FILE_PATH
# app.config["SERVER_NAME"] = "127.0.0.1:5000"
app_db = SQLAlchemy(app)

from fitness_app import routes
from fitness_app import models