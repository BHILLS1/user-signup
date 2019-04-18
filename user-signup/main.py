from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/log-in', methods=['POST'])
def validate_form():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if len(username) == '' or len(username) > 20 or len(username) < 3 or (" " in username):
        username_error = 'Invalid username, username should contain between 3 and 20 characters'
        username = ''
    if len(password) == '' or len(password) > 20 or len(password) < 3 or (" " in password):
        password_error = 'Invalid password, password should contain between 3 and 20 characters'
        password = ''

    if verify_password != password:
        verify_password_error = 'Passwords do not match'
        verify_password = ''

    if len(email) > 20 or len(email) < 3 or email.count('@') > 1 or email.count('.') > 1:
         email_error = 'Invalid email, email should contain between 3 and 20 characters, have (1) @ and (1) .'
         email = ''
        
        
    if not username_error and not password_error and not verify_password_error and not email_error:
        return render_template('welcome.html', username=cgi.escape(username))
    else:
        return render_template('index.html', username=username, username_error=username_error, 
        password=password, password_error=password_error, verify_password=verify_password, 
        verify_password_error=verify_password_error, email=email, email_error=email_error)



app.run()

  

