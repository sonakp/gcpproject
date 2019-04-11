from flask import Flask,render_template
import sqlite3 as sql

app=Flask(__name__)
@app.route('/list')
def list():

    con =sql.connect("database.db")
    con.row_factory =sql.Row
    cur= con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall();
    return render_template("list.html",rows=rows)





