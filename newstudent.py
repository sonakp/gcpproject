from flask import Flask,render_template

app=Flask(__name__)

@app.route('/enternew')
def new_Student():
    return render_template('student.html')


