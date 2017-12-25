from flask import render_template, flash, request, \
                  url_for, redirect
from main import app, db
from models import Vocabulary

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        word = request.form['word']
        synonym = request.form['synonym']
        record = Vocabulary(word=word, synonym=synonym)
        db.session.add(record)
        db.session.commit()
        flash('Added')
        return redirect(url_for('index')) #TODO 
    return render_template('addword.html')

@app.route('/list/')
def show_word_list():
    words = Vocabulary.query.all()
    return render_template('list.html', words=words)