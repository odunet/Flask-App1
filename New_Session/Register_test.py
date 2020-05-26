from flask import Flask, url_for, render_template,request, make_response, session

import sqlite3

from markupsafe import escape

from sqlite3 import Error

app = Flask(__name__)
app.secret_key = "abc"

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
    cur.execute("SELECT * FROM COMPANY")


    rows = cur.fetchall()

    return rows

@app.route('/')
def register():
    return render_template('register.html')

@app.route('/index', methods=['GET','POST'])
def home():
    if request.method == "POST":
        nam = str(request.form.get('name'))
        ag = int(request.form.get('age'))
        ad = str(request.form.get('address'))
        sa = int(request.form.get('salary'))
        conn = create_connection('test.db')
        c = conn.cursor()
        try:
            c.execute('''CREATE TABLE COMPANY
                         (ID            INT,
                         NAME           TEXT,
                         AGE            INT,
                         ADDRESS        CHAR(50),
                         SALARY         REAL);''')
            print ("Table created successfully");
        except Error as e:
            print(e)
        row = select_all_tasks(conn)
        k = (len(row) +1)
        c.execute("INSERT INTO COMPANY VALUES ({},'{}',{},'{}',{})".format(k,nam, ag, ad, sa))
        rows = select_all_tasks(conn)
        conn.commit()
        print(type(rows))
        print(rows)
        return render_template('index.html', rows = rows);
