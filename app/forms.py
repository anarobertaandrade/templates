from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
class Sendform(FlaskForm):
    nome = StringField('nome' , validators=[DataRequired()])
    email = EmailField('email' , validators=[DataRequired('Obrigatório um email válido')])
    assunto = StringField('assunto' , validators=[DataRequired()])
    mensagem = TextAreaField('mensagem' , validators=[DataRequired()])
    submit = SubmitField('enviar' , validators=[DataRequired()])