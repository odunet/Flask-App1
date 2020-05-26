import sqlite3, random

conn = sqlite3.connect('test2.db')

print ("Opened database successfully");

c = conn.cursor()
"""
c.execute("UPDATE COMPANY SET NAME = 'Etohan' WHERE AGE = 29")

for i in range(4):
    c.execute("INSERT INTO COMPANY VALUES ({},'{}',{},'{}',{})".format(5+i,'Ayokunle', random.randint(1,10), 'stadium', 400))


for i in range(6):
    c.execute("UPDATE COMPANY SET ID = {} WHERE ID = {}".format(i,(2+i)))

c.execute("UPDATE COMPANY SET NAME = 'DAMILOLA' WHERE AGE = 2")
"""
c.execute("DELETE FROM COMPANY WHERE AGE = 8 AND ID = 8")

conn.commit()

c.execute("SELECT * FROM COMPANY")

rows = c.fetchall()

print(rows)

conn.close()
