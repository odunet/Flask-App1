# commands to load app (1) env\scripts\activate (2) $env:FLASK_APP = "XXX"

from flask import Flask, url_for, render_template,request, redirect, session
from flask_session.__init__ import Session

from markupsafe import escape

app = Flask(__name__)
app.secret_key = 'abc'
# This is so because we dont want the session to be permanent
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'

#make active session for this app
Session(app)

or_usr = 'a'
or_pww = 'o'

@app.route('/')
def login():
#    usr = request.form.get('username')
#    pww = request.form.get('pwd')
#    if ((or_usr == usr) or (or_pww == pww)):
#        session['success'] = 'success'
    if 'todos' not in session:
        session['todos']=['crap']
        print("In link in ", session['todos'])
    print("In link out ", session['todos'])
    return render_template('login.html')

@app.route('/home', methods=['GET','POST'])
def home():
    if request.method == "POST":
        usr = request.form.get('username')
        pww = request.form.get('pwd')
        if ((or_usr == usr) or (or_pww == pww)):
            print("In home out ", session['todos'])
            return render_template('home.html', todos=session['todos'])
        else:
            print('redirect crazy')
            return redirect('/')
    else:
        print('fishy')
        print(session['todos'])
        return render_template('home.html', todos=session['todos'])

@app.route('/home2')
def home2():
        print('fishy_sharp')
        print(session['todos'])
        return render_template('home.html', todos=session['todos'])

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == "POST":
        todo = request.form.get('nam')
        name = todo
        session['todos'].append(todo)
        session.modified = True
        print("In add in ", session['todos'])
        return redirect('/home2')
        #render_template('home.html', todos=session['todos'])
    else:
        return render_template('add.html')
