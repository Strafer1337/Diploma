from flask import render_template, url_for, redirect
from flaskmap import app, db
from flaskmap.forms import AddForm
from flaskmap.models import Marker 

# markers = [
#     {
#         'id': 1,
#         'latitude': 55.70045,
#         'longtitude': 37.87769,
#         'content': 'Москва, ул. Камова, д. 28',
#         'color': 'red'
#     },
#     {
#         'id': 2,
#         'latitude': 55.88104,
#         'longtitude': 37.68363,
#         'content': 'Москва, ул. Тайнинская, д. 9',
#         'color': 'green'
#     },
#     {
#         'id': 3,
#         'latitude': 55.751999,
#         'longtitude': 37.617734,
#         'content': 'Московский кремль',
#         'color': 'orange'
#     }
# ]

@app.route("/")
@app.route("/home")
def home():
    markers = Marker.query.all()
    return render_template('home.html', markers=markers, title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/map")
def map():
    markers = Marker.query.all()
    return render_template('map.html', markers=markers)

@app.route("/add", methods=['GET', 'POST'])
def login():
    form = AddForm()
    if form.validate_on_submit():
        marker = Marker(latitude=float(form.latitude.data), longtitude=float(form.longtitude.data), content=form.content.data)
        db.session.add(marker)
        db.session.commit()
        return redirect(url_for('map'))
    return render_template('add.html', title='Add Marker', form=form)

if __name__ == '__main__':
    app.run(debug=True)