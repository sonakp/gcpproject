from flask import Flask
import MySQLdb
import gc

app = Flask(__name__)
app.debug=True

#database connection method

def connection():
    conn = MySQLdb.connect(host="localhost",user="testuser",passwd="testpassword",db="testflask")

    c= conn.cursor()
    return c,conn
c,con = connection()

#routing
@app.route("/")
def hello():
    return
@app.route("/get/")
def get_data():
    c.execute("Select * from users")
    users = c.fetchall()

    data = 'Name of users:

    for user in users:
    data = data + user[1] + ':'\
    +user[2]+user[3]+'
    



