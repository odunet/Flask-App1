from flask import Flask, url_for, render_template,request,redirect, session

from markupsafe import escape

app = Flask(__name__)

app.secret_key = 'yahoo'

#tst = 'ayokunle'

@app.route('/')
def index():
    return render_template('home.html')
"""
@app.route('/<name>')
def home(name):
    return f'This is the best {tst}'
"""
@app.route('/redir', methods=['GET','POST'])
def redir():
    if request.method == 'POST':
        masun = request.form['name']
        session['user'] = masun
        print(session['user'] ,' This is the value of session in Redir')
        return redirect(url_for('catch'))
    else:
        print("badder")
        return render_template('redir.html')


@app.route('/catch')
def catch():
    if 'user' in session:
        user = session['user']
        print(user,  "I am the boss")
        return render_template('catch.html', name = user)
    else:
        print("bad")
        return redirect(url_for('redir'))


"""
@app.route('/<play>')
def catch(play):
#    return f'This is the best {play}'
    return render_template('catch.html', name = play)
"""
