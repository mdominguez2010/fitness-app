from fitness_app import app_db

class User(app_db.Model):
    id = app_db.Column(app_db.Integer(), primary_key=True)
    username = app_db.Column(app_db.String(length=30), nullable=False, unique=True)
    email_address = app_db.Column(app_db.String(length=50), nullable=False, unique=True)
    password_hash = app_db.Column(app_db.String(length=60), nullable=False)
    budget = app_db.Column(app_db.Integer(), nullable=False, default=1000)
    runs = app_db.relationship('Run', backref='owned_user', lazy=True)

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