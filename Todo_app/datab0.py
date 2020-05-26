import sqlite3

conn = sqlite3.connect('test2.db')

print ("Opened database successfully");

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS COMPANY
         (ID            INT,
         NAME           TEXT,
         AGE            INT,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')

print ("Table created successfully");

c.execute("INSERT INTO COMPANY VALUES ({},'{}',{},'{}',{})".format(3,'Ayokunle', 29, 'stadium', 400))
c.execute("INSERT INTO COMPANY VALUES ({},'{}',{},'{}',{})".format(4, 'Tosin', 30, 'agege', 350))

conn.commit()

c.execute("SELECT * FROM COMPANY")

rows = c.fetchall()

print(rows)

conn.close()
