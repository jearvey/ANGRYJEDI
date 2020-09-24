import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_location = os.path.join(BASE_DIR, "ANJE_db.sqlite")

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn



#defaults need changing once all implemented
def write_agents(agent_id, callback_id=1, agent_name="johnathan", os="nix", socket="todo", status="up"):
    conn = create_connection(db_location)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO agents(agent_id,callback_id,agent_name,os,socket,status) VALUES (?,?,?,?,?,?)", (agent_id,callback_id, agent_name, os, socket,status))
    except sqlite3.IntegrityError as e:
        print('sqlite error: ', e.args[0])
    conn.commit()
    c.close()
    #maybe needs conn.close()
    return




