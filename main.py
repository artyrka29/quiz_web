from flask import Flask, url_for, render_template, redirect, session
import db_scipts


def start_session(quiz_id=0):
    session['quiz'] = quiz_id
    session['last_question'] = 0
    session['right_ans'] = 0
    session['wrong_ans'] = 0
    session['total'] = 0


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return '<h1>Hello world</h1>'

@app.route('/test')
def test():
    return '<h1>test</h1>'

@app.route('add_quiz')
def add_quiz():
    return '<h1>Add quiz</h1>'

@app.route('/result')
def route():
    return '<h1>Result</h1>'


app.config['SECRET_KEY'] = 'imkrytoy'
if __name__ == '__main__':
    app.run()

