from flask import render_template, flash, request, \
                  url_for, redirect
from main import app, db
from models import Vocabulary

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('add.html')
        
    word = request.form['word']
    synonym = request.form['synonym']

    if not word or not synonym:
        flash('Пусто')
    elif word_exists(word):
        flash('Уже есть')
    else:
        word_add(word, synonym)
        flash('Добавил')
    return redirect(url_for('index')) #TODO 

@app.route('/list/')
def show_word_list():
    words = word_list()
    return render_template('list.html', words=words)

def word_exists(word):
    query = Vocabulary.query.filter_by(word=word)
    result = db.session.query(query.exists())
    return result.scalar()

def word_add(word, synonym):
    record = Vocabulary(word=word, synonym=synonym)
    db.session.add(record)
    db.session.commit()
    return True

def word_list():
    return Vocabulary.query.all()