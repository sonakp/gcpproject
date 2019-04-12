from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def enternew():
    return render_template('student.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            #addr = request.form['add']
            city = request.form['city']
            #pin = request.form['pin']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name,city) VALUES(?,?)",(nm,city) )
                con.commit()
                msg1 = "Record successfully added"
        except:
            #with sql.connect("database.db") as con:
            con.rollback()
            msg1 = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg1)
            con.close()


@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall()
    return render_template("list.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True,port=8000)