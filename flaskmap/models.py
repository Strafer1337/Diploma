from datetime import datetime
from flaskmap import db

class Marker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    author = db.Column(db.String(30), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longtitude = db.Column(db.Float, nullable=False)
    content = db.Column(db.String(200), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    color = db.Column(db.String(10), nullable=False, default='red')
    icon = db.Column(db.String(15), nullable=False, default='info-sign')

    def __repr__(self):
        return f"Marker('{self.id}', '{self.latitude}', '{self.longtitude}')"
    
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    marker_id = db.Column(db.Integer, db.ForeignKey('marker.id'), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    upvotes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return f"Comment('{self.id}'. {self.author}: '{self.content}; Upvotes: {self.upvotes}')"