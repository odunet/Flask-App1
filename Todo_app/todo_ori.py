from flask import Flask, url_for, render_template,request, redirect

from markupsafe import escape

app = Flask(__name__)

name = ''
or_usr = 'odunet2000'
or_pww = 'starforce'
todos = []

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        usr = request.form.get('username')
        pww = request.form.get('pwd')
        if ((or_usr == usr) or (or_pww == pww)) or len(todos)>=2:
            return render_template('add.html', name=usr)
    else:
        return render_template('login.html')

@app.route('/')
def home():
    print(todos)
    return render_template('home.html', todos=todos)
"""
@app.route('/')
def login():
    return render_template('login.html')
"""
@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == "POST":
        todo = request.form.get('nam')
        todos.append(todo)
        print(todos)
        return redirect('/')
    else:
        return render_template('add.html', name='User')
