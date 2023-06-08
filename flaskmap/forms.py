from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Length
from flaskmap.models import Marker


class AddForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    author = StringField('Автор', validators=[DataRequired()])
    latitude = StringField('Широта', validators=[DataRequired()])
    longtitude = StringField('Долгота', validators=[DataRequired()])
    content = TextAreaField('Описание', validators=[DataRequired()])
    color = SelectField('Цвет', choices=[('red', 'Красный'), ('blue', 'Синий'), ('green', 'Зеленый'),
                                         ('purple','Фиолетовый'), ('orange','Оранжевый'), ('black','Черный')])
    icon = SelectField('Иконка', choices=[('info-sign','Информация'), ('user', 'Человек'), ('warning-sign', 'Важно'),
                                          ('home','Здание'), ('tree-deciduous', 'Дерево'), ('file','Документы')])
    submit = SubmitField('Добавить')
        
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
        
class UpdateForm(FlaskForm):
    content = TextAreaField('Описание', validators=[DataRequired()])
    color = SelectField('Цвет', choices=[('red', 'Красный'), ('blue', 'Синий'), ('green', 'Зеленый'),
                                         ('purple','Фиолетовый'), ('orange','Оранжевый'), ('black','Черный')])
    icon = SelectField('Иконка', choices=[('info-sign','Информация'), ('user', 'Человек'), ('warning-sign', 'Важно'),
                                          ('home','Здание'), ('tree-deciduous', 'Дерево'), ('file','Документы')])
    submit = SubmitField('Изменить')
        
class AddComment(FlaskForm):
    author = StringField('Автор', validators=[DataRequired()])
    content = TextAreaField('Комментарий', validators=[DataRequired()])
    submit = SubmitField('Добавить')