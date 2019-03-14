from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = '935d94dafc5f03c6567ae138c60cf105'
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def email_valid():
    session['title'] = 'Email Validation'
    return render_template('index.html')

@app.route('/success', methods=["POST"])
def success():
    email = request.form['email']
    print(email, '&&&&&&&&&&&&&&&&&&&&&&&&&&&')
    session['title'] = 'Success'
    db = connectToMySQL('dojo_emails')
    query = 'SELECT * FROM emails'
    emails = db.query_db(query)
    return render_template('success.html', emails=emails)


if __name__ == "__main__":
    app.run(debug=True)
