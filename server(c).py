from flask import Flask, request, render_template
from mysqlconnection import MySQLConnector
# imports the Bcrypt module
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'my_database_here')
# this will load a page that has 2 forms one for registration and login
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    # run validations and if they are successful we can create the password hash with bcrypt
    pw_hash = bcrypt.generate_password_hash(password)
    # now we insert the new user into the database
    insert_query = "INSERT INTO users (email, username, pw_hash, created_at) VALUES (:email, :username, :pw_hash, NOW())"
    query_data = { 'email': email, 'username': username, 'password': pw_hash }
    mysql.query_db(insert_query, query_data)
    # redirect to success page

# we are going to add functions to create new users and login users
app.run(debug=True)