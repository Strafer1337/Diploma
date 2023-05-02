from flaskmap import db

class Marker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longtitude = db.Column(db.Float, nullable=False)
    content = db.Column(db.String(200), nullable=False)
    # color = db.Column(db.String(20), nullable=False, default='red')

    def __repr__(self):
        return f"Marker('{self.id}', '{self.latitude}', '{self.longtitude}')"