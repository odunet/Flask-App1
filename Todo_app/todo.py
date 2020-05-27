# commands to load app (1) env\scripts\activate (2) $env:FLASK_APP = "XXX"

from flask import Flask, url_for, render_template,request, redirect, session
from flask_session.__init__ import Session

from markupsafe import escape

app = Flask(__name__)
app.secret_key = 'abcde'
# This is so because we dont want the session to be permanent
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'

#make active session for this app
#Session(app)

or_usr = 'a'
or_pww = 'o'

@app.route('/')
def home():
#    usr = request.form.get('username')
#    pww = request.form.get('pwd')
#    if ((or_usr == usr) or (or_pww == pww)):
#        session['success'] = 'success'
    if 'todos3' not in session:
#        session['todos'] = []
        print('new')
        return render_template('home.html')
    else:
#        print("In link out ", session['todos'])
        print (session['todos3'])
        return render_template('home.html',todos = session['todos3'])

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        usr = request.form.get('username')
        pww = request.form.get('pwd')
        if ((or_usr == usr) and (or_pww == pww)):
            print("In heading to add ")
            return redirect(url_for('add'))
        else:
            print('Password or user name is wrong')
            return redirect('/login')
    else:
        print('fishy')
        return render_template('login.html')
"""
@app.route('/home2')
def home2():
        print('fishy_sharp')
        print(session['todos'])
        return render_template('home.html', todos=session['todos'])
"""
@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == "POST":
#        todo = request.form['nam']
        if 'todos3' not in session:
            session['todos3']=[]
            session['todos3'].append(request.form.get('nam'))
            #        session['todos'].append(todo)
            #session.modified = True
            print("In add in ", session['todos3'])
            return redirect(url_for('home'))
            #render_template('home.html', todos=session['todos'])
        else:
    #        session['todos3'].append(request.form.get('nam'))
            y = session['todos3']
            y.append(request.form.get('nam'))
            print ("the value of z is ",y)
            session['todos3'] = y
            print("the value of sessions is ",session['todos3'])
    #        session['todos'].append(todo)
            #session.modified = True
            return redirect(url_for('home'))
            #render_template('home.html', todos=session['todos'])
    else:
        print("Now is add using GET")
        return render_template('add.html')
