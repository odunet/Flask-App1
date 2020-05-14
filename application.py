from flask import Flask, url_for, render_template,request

from markupsafe import escape

app = Flask(__name__)
"""
@app.route("/")
def index(name):
    return "Hello World"

@app.route("/goodbye")
def index(name):
    return "Bye Ayo"
"""

@app.route("/hello")
def hello():
    name = request.args.get('name')
    return render_template('todo.html', name=name)

"""
@app.route('/')
@app.route('/<hii>')
def hello(hii=None):
"""

@app.route('/')
def index():
    return render_template('home.html')
"""
url_for('static', filename='style.css')
url_for('static', filename='jscript.css')


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
"""
