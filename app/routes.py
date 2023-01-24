from app import app
from flask import render_template, flash, request, url_for
from app.forms import Sendform


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    form = Sendform()
    if form.validate_on_submit():
        mensagem = flash('Mensagem enviada com sucesso')
    return render_template('contato.html', form=form)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/jobs')
def jobs():
    return render_template('jobs.html')