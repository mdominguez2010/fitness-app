from fitness_app import app_db, SQLAlchemy
from fitness_app.db import config

class User(app_db.Model):
    id = app_db.Column(app_db.Integer(), primary_key=True)
    username = app_db.Column(app_db.String(length=30), nullable=False, unique=True)
    email_address = app_db.Column(app_db.String(length=50), nullable=False, unique=True)
    password_hash = app_db.Column(app_db.String(length=60), nullable=False)
    runs = app_db.relationship('Run', backref='owned_user', lazy=True)
    weight = app_db.relationship('Weight', backref='owned_user', lazy=True)
    workout = app_db.relationship('Weight', backref='owned_user', lazy=True)

class Run(app_db.Model):
    id = app_db.Column(app_db.Integer(), primary_key=True)    
    date = app_db.Column(app_db.String(length=10), nullable=False)
    distance = app_db.Column(app_db.String(length=6), nullable=False)
    duration = app_db.Column(app_db.String(length=6), nullable=False)
    calories = app_db.Column(app_db.String(length=7), nullable=False)
    avg_pace = app_db.Column(app_db.String(length=10), nullable=False)
    owner = app_db.Column(app_db.Integer(), app_db.ForeignKey("user.id"))    
    
    def __repr__(self):
        return f"The run on {self.date} was {self.distance} mile(s) and lasted {self.duration}"

class Weight(app_db.Model):
    id = app_db.Column(app_db.Integer(), primary_key=True)    
    date = app_db.Column(app_db.String(length=10), nullable=False)
    weight = app_db.Column(app_db.String(length=6), nullable=False)
    fatmass = app_db.Column(app_db.String(length=6), nullable=False)
    bonemass = app_db.Column(app_db.String(length=6), nullable=False)
    musclemass = app_db.Column(app_db.String(length=6), nullable=False)
    hydration = app_db.Column(app_db.String(length=6), nullable=False)
    comments = app_db.Column(app_db.String(length=10), nullable=False)
    owner = app_db.Column(app_db.Integer(), app_db.ForeignKey("user.id"))

    def __repr__(self):
        return f"Date: {self.date}, Weight: {self.weight}"

class Workouts(app_db.Model):
    id = app_db.Column(app_db.Integer(), primary_key=True)    
    Date = app_db.Column(app_db.String(length=10), nullable=False)
    Exercise = app_db.Column(app_db.String(length=6), nullable=False)
    Reps = app_db.Column(app_db.String(length=6), nullable=False)
    Weight = app_db.Column(app_db.String(length=6), nullable=False)
    Duration = app_db.Column(app_db.String(length=6), nullable=False)
    Distance = app_db.Column(app_db.String(length=6), nullable=False)
    Incline = app_db.Column(app_db.String(length=6), nullable=False)
    Resistance = app_db.Column(app_db.String(length=6), nullable=False)
    Note = app_db.Column(app_db.String(length=60), nullable=False)
    Multiplier = app_db.Column(app_db.String(length=6), nullable=False)
    owner = app_db.Column(app_db.Integer(), app_db.ForeignKey("user.id"))

    def __repr__(self):
        return f"Date: {self.date}, Exercise: {self.exercise}, Reps: {self.reps}, Weight: {self.weight}"
    
# Connect to db
engine = SQLAlchemy.create_engine("sqlite:///" + config.DB_FILE_PATH)

#