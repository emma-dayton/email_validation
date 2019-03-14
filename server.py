from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = '4a136bc896d8e3657d1799320bb2aa37'


@app.route('/')
def email_valid():
    session['title'] = 'Email Validation'
    return render_template('index.html')

@app.route('/success')
def success():
    session['title'] = 'Success'
    return render_template('success.html')


if __name__ == "__main__":
    app.run(debug=True)
