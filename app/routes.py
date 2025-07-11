from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Andrew'}
    posts = [
        {
            'author': {'username': 'George'},
            'body': 'Beautiful day in Grand Rapids!'
        },
        {
            'author': {'username': 'Marshall'},
            'body': 'The F1 movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
