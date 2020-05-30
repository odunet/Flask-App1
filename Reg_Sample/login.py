from flask import Flask, url_for, render_template,request,redirect, session, flash, g

import sqlite3

from markupsafe import escape

from sqlite3 import Error

app = Flask(__name__)

app.secret_key = 'yahoo'

def create_connection(data):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(data)
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM REGISTER")


    rows = cur.fetchall()

    return rows

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login', methods=["POST","GET"])
def login():
    if request.method == 'POST':
        session.pop('user',None)

        user = request.form['email1']
        pwd = int(request.form['pwd1'])
        conn = create_connection('finance.db')
        c = conn.cursor()
        #Create SQlite Connection
        try:
            c.execute('''CREATE TABLE IF NOT EXISTS REGISTER
                         (USER          CHAR(50),
                         PWD            INT,
                         FIRST           TEXT,
                         LAST           TEXT,
                         ADDRESS        CHAR(50));''')
            print ("Table created successfully")
        except Error as e:
            print(e)
        conn.commit()
        row = select_all_tasks(conn)
        if len(row) >= 1:
            a = len(row)
            for i in range(a):
                if (user == row[i][0]) and (pwd == row[i][1]):
                    session['user']=user
                    session['pwd']=pwd
            if 'user' in session:
                return redirect(url_for('loggedin'))
            else:
                return render_template('login.html', error="      WRONG USERNAME OR PW ENTERED")
        else:
            return render_template('login.html', error="     NO USERS REGISTERED YET")
    else:
        return render_template('login.html')


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == "POST":
        firstn = str(request.form.get('fir'))
        lastn = str(request.form.get('las'))
        usern = str(request.form.get('ema'))
        pwdn = int(request.form.get('pww'))
        addn = str(request.form.get('add'))
        conn = create_connection('finance.db')
        c = conn.cursor()
        try:
            c.execute('''CREATE TABLE IF NOT EXISTS REGISTER
                         (USER          CHAR(50),
                         PWD            INT,
                         FIRST           TEXT,
                         LAST           TEXT,
                         ADDRESS        CHAR(50);''')
            print ("Table created successfully");
        except Error as e:
            print(e)
        row = select_all_tasks(conn)
        if len(row) == 0:
            sqlite_insert_with_param = "INSERT INTO REGISTER (USER, PWD, FIRST, LAST, ADDRESS) VALUES (?, ?, ?, ?, ?);"
            data_tuple = (usern, pwdn, firstn, lastn, addn)
            c.execute(sqlite_insert_with_param, data_tuple)
            conn.commit()
            rows = select_all_tasks(conn)
            print(type(rows))
            print(rows)
            return redirect(url_for('index'))
        else:
            a = len(row)
            for i in range(a):
                if (usern == row[i][0]):
                    flash("Username exist!", "info")
                    print("badder")
                    return render_template('register.html')

        #This will run if username does not existbut data in db
            sqlite_insert_with_param = "INSERT INTO REGISTER (USER, PWD, FIRST, LAST, ADDRESS) VALUES (?, ?, ?, ?, ?);"
            data_tuple = (usern, pwdn, firstn, lastn, addn)
            c.execute(sqlite_insert_with_param, data_tuple)
            conn.commit()
            rows = select_all_tasks(conn)
            print(type(rows))
            print(rows)
            return redirect(url_for('index'))
    else:
        return render_template('register.html')

@app.route('/loggedin')
def loggedin():
    wel_message = g.user
    return render_template('loggedin.html', user = g.user)

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']
