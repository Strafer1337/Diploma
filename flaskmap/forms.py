from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Length
from flaskmap.models import Marker


class AddForm(FlaskForm):
    latitude = StringField('Широта', validators=[DataRequired()])
    longtitude = StringField('Долгота', validators=[DataRequired()])
    content = StringField('Описание', validators=[DataRequired()])
    color = StringField('Цвет (указывать на английском, по умолчанию - красный)')
    submit = SubmitField('Добавить')

    # def validate_on_submit(self, latitude, longtitude):
    #     marker = Marker.query.filter_by(latitude=latitude.data, longtitude=longtitude.data).first()
    #     if marker:
    #         raise ValidationError('Маркер с такими кооординатами уже создан!')
        
    def validate_latitude(self, latitude):
        try:
            float(latitude.data)
        except ValueError:
            raise ValidationError('Неверное введена широта!')
        marker = Marker.query.filter_by(latitude=self.latitude.data, longtitude=self.longtitude.data).first()
        if marker:
            raise ValidationError('Маркер с такими кооординатами уже создан!')
    
    def validate_longtitude(self, longtitude):
        try:
            float(longtitude.data)
        except ValueError:
            raise ValidationError('Неверное введена долгота!')
        marker = Marker.query.filter_by(latitude=self.latitude.data, longtitude=self.longtitude.data).first()
        if marker:
            raise ValidationError('Маркер с такими кооординатами уже создан!') 
        
class AddComment(FlaskForm):
    author = StringField('Автор', validators=[DataRequired()])
    content = StringField('Комментарий', validators=[DataRequired()])
    submit = SubmitField('Добавить')