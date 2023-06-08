from flask import render_template, url_for, redirect, flash
from flaskmap import app, db
from flaskmap.forms import AddForm, AddComment, UpdateForm
from flaskmap.models import Marker, Comment 

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
        marker = Marker(name=form.name.data, 
                        author=form.author.data,
                        latitude=float(form.latitude.data),
                        longtitude=float(form.longtitude.data),
                        content=form.content.data, 
                        color=form.color.data, icon=form.icon.data)
        db.session.add(marker)
        db.session.commit()
        return redirect(url_for('map'))
    return render_template('add.html', title='Add Marker', form=form)

@app.route("/add_comment/<int:marker_id>", methods=['GET', 'POST'])
def add_comment(marker_id):
    form = AddComment()
    if form.validate_on_submit():
        comment = Comment(author=form.author.data, 
                          content=form.content.data, 
                          marker_id=marker_id)
        db.session.add(comment)
        db.session.commit()
        flash('Комментарий добавлен!', 'success')
        return redirect(url_for('list_comments', marker_id=comment.marker_id))
    return render_template('add_comm.html', title='Add Comment', form=form)

@app.route("/comments/<int:marker_id>", methods=['GET', 'POST'])
def list_comments(marker_id):
    comments = Comment.query.filter_by(marker_id=marker_id).order_by(Comment.upvotes.desc()).all()
    marker = Marker.query.filter_by(id=marker_id).first()
    return render_template('comments.html', title='Comment', comments=comments, marker=marker)

@app.route("/comments/<int:marker_id>/update", methods=['GET', 'POST'])
def update(marker_id):
    marker = Marker.query.get_or_404(marker_id)
    form = UpdateForm()
    if form.validate_on_submit():
        marker.content = form.content.data
        marker.color = form.color.data
        marker.icon = form.icon.data
        db.session.commit()
        flash('Информация успешно обновлена!', 'success')
        return redirect(url_for('list_comments', marker_id=marker.id))
    return render_template('update.html', title='Update', form=form)

@app.route("/like/<int:id>", methods=['GET'])
def like(id):
    comment=Comment.query.get_or_404(id)
    comment.upvotes += 1
    db.session.commit()
    return redirect(url_for('list_comments', marker_id=comment.marker_id))

@app.route("/dislike/<int:id>", methods=['GET'])
def dislike(id):
    comment=Comment.query.get_or_404(id)
    comment.upvotes -= 1
    db.session.commit()
    return redirect(url_for('list_comments', marker_id=comment.marker_id))

@app.route("/delete/<int:id>", methods=['GET'])
def delete(id):
    comment=Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    flash('Комментарий удален!', 'danger')
    return redirect(url_for('list_comments', marker_id=comment.marker_id))

@app.route("/delete_mr/<int:id>/<string:mode>", methods=['GET'])
def delete_mr(id, mode):
    marker=Marker.query.get_or_404(id)
    comments = Comment.query.filter_by(marker_id=id).all()
    for comment in comments:
        db.session.delete(comment)
    db.session.delete(marker)
    db.session.commit()
    if mode == 'map': 
        return redirect(url_for('map'))
    else: 
        flash('Метка удалена!', 'danger')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)