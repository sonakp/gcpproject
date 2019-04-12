from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)


class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))


    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin


@app.route('/')
def show_all():
    return render_template('show_all.html', students=students.query.all())


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields', 'error')
        else:
            student = students(request.form['name'], request.form['city'],request.form['addr'],request.form['pin'])

            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')

@app.route('/del', methods=['GET', 'POST'])
def del1():
    if request.method == 'POST':
        username1 = request.form['name']
        print "username1",username1
        #username = students.query.get(username1)
        #db.session.delete(username)
        #db.session.query(Model).filter(Model.id == request.form['name']).delete()
        delete_this=students.query.filter(students.name==username1).first()
        #student = students(request.form['name'])
        db.session.delete(delete_this)
        #db.session.delete(student)
        db.session.commit()
        flash('Record was successfully deleted')
        return redirect(url_for('show_all'))
    return render_template('del.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True,port=9000)

