from flask import render_template, url_for, redirect
from sqlalchemy import func
from flaskmap import app, db
from flaskmap.forms import AddForm, AddComment
from flaskmap.models import Marker, Comment 

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
    dict = {}
    markers = Marker.query.all()
    for marker in markers:
        most_liked = Comment.query.filter_by(marker_id=marker.id).order_by(Comment.upvotes.desc()).first()
        dict[marker.id] = most_liked
    return render_template('map.html', markers=markers, dict=dict)

@app.route("/add", methods=['GET', 'POST'])
def add_marker():
    form = AddForm()
    if form.validate_on_submit():
        marker = Marker(latitude=float(form.latitude.data), longtitude=float(form.longtitude.data), content=form.content.data, 
                        color=form.color.data)
        db.session.add(marker)
        db.session.commit()
        return redirect(url_for('map'))
    return render_template('add.html', title='Add Marker', form=form)

@app.route("/add_comment/<int:marker_id>", methods=['GET', 'POST'])
def add_comment(marker_id):
    form = AddComment()
    if form.validate_on_submit():
        comment = Comment(author=form.author.data, content=form.content.data, marker_id=marker_id) #####
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('list_comments', marker_id=comment.marker_id))
    return render_template('add_comm.html', title='Add Comment', form=form)

@app.route("/comments/<int:marker_id>", methods=['GET', 'POST'])
def list_comments(marker_id):
    comments = Comment.query.filter_by(marker_id=marker_id).all()
    marker = Marker.query.filter_by(id=marker_id).first()
    return render_template('comments.html', title='Comment', comments=comments, marker=marker)

@app.route("/like/<int:id>", methods=['GET'])
def like(id):
    comment=Comment.query.filter_by(id=id).first()
    comment.upvotes += 1
    db.session.commit()
    return redirect(url_for('list_comments', marker_id=comment.marker_id))

@app.route("/dislike/<int:id>", methods=['GET'])
def dislike(id):
    comment=Comment.query.filter_by(id=id).first()
    comment.upvotes -= 1
    db.session.commit()
    return redirect(url_for('list_comments', marker_id=comment.marker_id))

@app.route("/delete/<int:id>", methods=['GET'])
def delete(id):
    comment=Comment.query.filter_by(id=id).first()
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('list_comments', marker_id=comment.marker_id))

# убрать
@app.route("/delete_mr/<int:id>", methods=['GET'])
def delete_mr(id):
    marker=Marker.query.filter_by(id=id).first()
    db.session.delete(marker)
    db.session.commit()
    return redirect(url_for('map'))

if __name__ == '__main__':
    app.run(debug=True)