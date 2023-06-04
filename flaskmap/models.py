from flaskmap import db

class Marker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longtitude = db.Column(db.Float, nullable=False)
    content = db.Column(db.String(200), nullable=False)
    color = db.Column(db.String(10), nullable=False, default='red')
    upvotes = db.Columd(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return f"Marker('{self.id}', '{self.latitude}', '{self.longtitude}')"
    
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    marker_id = db.Column(db.Integer, db.ForeignKey('marker.id'), nullable=False)
    upvotes = db.Columd(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return f"Comment('{self.id}'. {self.author}: '{self.content}; Upvotes: {self.upvotes}')"