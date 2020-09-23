import sqlite3


def create_connection(db_file)
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def write_agents(agent_id, callback_id=needtomakethis, agent_name=test, os=nix, socket=todo, status=up):
    c = conn.cursor()
    c.execute("INSERT INTO agents(agent_id,callback_id,agent_name,os,socket,status) VALUES (?,?,?,?,?,?)", (agent_id,callback_id, agent_name, os, socket,status))
    conn.commit()
    c.close()
    #maybe needs conn.close()
    return


