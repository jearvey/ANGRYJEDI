import sqlite3
from flask import Flask


###Links database and creates function to make db
DATABASE = '/root/ANGRYJEDI/JEDIARCHIVES/ANJE_db.sqlite'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

#returns dics instead of tuples from db
def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))
get_db()
db.row_factory = make_dicts

#easy db query, auto open and close
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


###end DB section


###Flask Code
app = Flask(__name__)
@app.route('/')

def hello_world():
    return "Hello Worl... how original"

test = query_db('SELECT * from agents')
if test is None:
    print("No data in table agents")
else:
    print(test)

@app.teardown_appxontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

###end flask code
