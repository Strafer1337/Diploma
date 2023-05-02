from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Marker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longtitude = db.Column(db.Float, nullable=False)
    content = db.Column(db.String(200), nullable=False)
    color = db.Column(db.String(20), nullable=False, default='red')

    def __repr__(self):
        return f"Marker('{self.id}', '{self.latitude}', '{self.longtitude}')"

# posts = [
#     {
#         'author': 'Corey Schafer',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'April 20, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'April 21, 2018'
#     }
# ]

markers = [
    {
        'id': 1,
        'latitude': 55.70045,
        'longtitude': 37.87769,
        'content': 'Москва, ул. Камова, д. 28',
        'color': 'red'
    },
    {
        'id': 2,
        'latitude': 55.88104,
        'longtitude': 37.68363,
        'content': 'Москва, ул. Тайнинская, д. 9',
        'color': 'green'
    },
    {
        'id': 3,
        'latitude': 55.751999,
        'longtitude': 37.617734,
        'content': 'Московский кремль',
        'color': 'orange'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', markers=markers, title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/map")
def map():
    return render_template('map.html', markers=markers)

if __name__ == '__main__':
    app.run(debug=True)