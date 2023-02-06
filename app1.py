import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE users (Username text, Password text,firstname text, lastname text, email text, count integer)''')
conn.commit()
conn.close()
