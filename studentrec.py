from flask import Flask,render_template,request
import requests
import sqlite3 as sql

app=Flask(__name__)

@app.route('/addrec',Method=['GET','POST'])
def addrec():
    if request.method =='POST':
        try:
            nm=request.form['nm']
            city=request.form['city']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students(name,city) VALUES(?,?)",(nm,city))
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"
        finally:

            return render_template("result.html",msg=msg)

