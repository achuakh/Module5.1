import sqlite3

conn = sqlite3.connect('user.db')
conn.execute('CREATE TABLE user (name TEXT, timestamp TEXT)')
conn.commit()
conn.close()
