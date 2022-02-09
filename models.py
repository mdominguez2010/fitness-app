
# Data models
app_db = SQLAlchemy(app)

class Run(app_db.Model):
    id = app_db.Column(app_db.Integer(), primary_key=True)    
    date = app_db.Column(app_db.String(length=10), nullable=False)
    distance = app_db.Column(app_db.String(length=6), nullable=False)
    duration = app_db.Column(app_db.String(length=6), nullable=False)
    calories = app_db.Column(app_db.String(length=7), nullable=False)
    avg_pace = app_db.Column(app_db.String(length=10), nullable=False)
    
    def __repr__(self):
        return f"The run on {self.date} was {self.distance} mile(s)"