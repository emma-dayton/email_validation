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

@app.route('/success', methods=["POST", "GET"])
def success():
    if 'email' in request.form:
        email = {'email':request.form['email']}
        if not email_regex.match(email['email']):
            flash('Invalid email address!')
            return redirect('/')
        session['title'] = 'Success'
        db = connectToMySQL('dojo_emails')
        query = 'SELECT * FROM emails WHERE email=%(email)s'
        check_in_db = db.query_db(query, email)
        # print(check_in_db, '&&&&&&&&&&&&&&&&&&&&&&&')
        # print(email, '&&&&&&&&&&&&&&&&&&&&&&&')
        if len(check_in_db) > 0:
            email = email['email']
            flash(f'{email} already in database')
            return redirect('/')
        else:
            db = connectToMySQL('dojo_emails')
            query = 'INSERT INTO emails (email, created_at) VALUES(%(email)s, now())'
            db.query_db(query, email)
    elif 'id' in request.form:
        db = connectToMySQL('dojo_emails')
        query = 'DELETE FROM emails WHERE id=%(id)s'
        db.query_db(query, request.form)
    db = connectToMySQL('dojo_emails')
    query = 'SELECT * FROM emails'
    emails = db.query_db(query)
    return render_template('success.html', emails=emails)


if __name__ == "__main__":
    app.run(debug=True)
