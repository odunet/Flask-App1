from flask import Flask, url_for, render_template,request,redirect

from markupsafe import escape

app = Flask(__name__)

#tst = 'ayokunle'

@app.route('/')
def index():
    return render_template('home.html')
"""
@app.route('/<name>')
def home(name):
    return f'This is the best {tst}'
"""
@app.route('/redir')
def redir():
    masun = str(input("What is your P?= "))
    return redirect(url_for('catch',play=masun))

@app.route('/<play>')
def catch(play):
    return f'This is the best {play}'
