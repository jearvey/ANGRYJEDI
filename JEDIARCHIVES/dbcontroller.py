import sqlite3

conn = sqlite3.connect('ANJE_db.sqlite')
cur = conn.cursor()
cur.execute('CREATE TABLE agents (agent_id VARCHAR(36), callback_time VARCHAR(3), last_callback DATETIME)')
conn.commit()


conn.close()
