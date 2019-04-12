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


@app.route('/del', methods=['GET', 'POST'])
def del1():
    if request.method == 'POST':
        student = students(request.form['name'])
        db.session.delete(student)
        db.session.commit()
        flash('Record was successfully deleted')
        return redirect(url_for('show_all'))
    return render_template('del.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True,port=9090)