from flask import Flask, request, render_template, session
from mysqlconnection import MySQLConnector
# imports the Bcrypt module
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'Login')
app.secret_key = 'super secret key'
# this will load a page that has 2 forms one for registration and login
@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/new_user', methods=['POST'])
def newUser():
	return render_template('create.html')

@app.route('/new_user/create', methods=['POST'])
def create_user():
	session['dialogue'] = ''
	email = request.form['email']
	VarEmail = email
	AtCheck = 0
	ErrorBool = 0
	NewStr = ['']
	ComList = ['.','c','o','m', '']
	AtChar = ['@']
	session['dialogue'] = ''
	while ErrorBool == 0:
	    print 'Checking size'
	    if len(VarEmail) < 8:
	        print len(VarEmail)
	        print 'Too small'
	        session['dialogue'] = 'Error 12-4: EMAIL NOT VALID: too short'
	        ErrorBool = 1
	        break
	    print 'Checking for .com'
	    NewStr = list(NewStr)
	    print type(NewStr)
	    for countCom in range(0,4): 
	        count = len(VarEmail)+countCom-4
	        print VarEmail[count]          
	        NewStr.insert(countCom, VarEmail[count])
	    print NewStr
	    if NewStr != ComList:
	        print VarEmail
	        print 'Missing .com'
	        session['dialogue'] = 'Error 30-8: EMAIL NOT VALID: missing .com'
	        ErrorBool = 1
	        break
	    print 'Checking for at symbol in '
	    print VarEmail
	    print AtChar[0]
	    for countAt in range(0, len(VarEmail)):
	        if VarEmail[countAt] == AtChar[0]:
	            print 'symbol found'
	            AtCheck = 1
	            ErrorBool = 2
	            break
	    if AtCheck != 1:
	        print VarEmail
	        print 'Missing symbol'
	        session['dialogue'] = 'Error 30-9: EMAIL NOT VALID: missing @'
	        ErrorBool = 1
	        break
	    else:
	    	ErrorBool = 2
	    	break
	if ErrorBool == 1:
		print 'error'
		return render_template('create.html', dialogue = session['dialogue'])
	password = request.form['password']
	if len(password) < 8:
		session['dialogue'] = 'Error 39-6 PASSWORD ERROR: password must be at least 8 characters long!'
		return render_template('create.html', dialogue = session['dialogue'])
	c_password = request.form['c_password']
	if password != c_password:
		session['dialogue'] = 'Error 39-2 PASSWORD ERROR: passwords did not match!'
		return render_template('create.html', dialogue = session['dialogue'])
	first_name = request.form['first_name']
	if len(first_name) < 3:
		session['dialogue'] = 'Error39-2 FIRST_NAME ERROR: first_name must be more than 2 characters!'
		return render_template('create.html', dialogue = session['dialogue'])
	last_name = request.form['last_name']
	if len(last_name) < 3:
		session['dialogue'] = 'Error39-2 LAST_NAME ERROR: last_name must be more than 2 characters!'
		return render_template('create.html', dialogue = session['dialogue'])
	password = bcrypt.generate_password_hash(password)
	# run validations and if they are successful we can create the password hash with bcrypt
	# pw_hash = bcrypt.generate_password_hash(password)
	# now we insert the new user into the database
	insert_query = "INSERT INTO users (email, password, first_name, last_name) VALUES (:email, :password, :first_name, :last_name)"
	query_data = { 'email': email, 'password': password, 'first_name':first_name, 'last_name':last_name }
	mysql.query_db(insert_query, query_data)
	# redirect to success page
	return render_template('index.html')
	# we are going to add functions to create new users and login users

@app.route('/login', methods=['POST'])
def login():
	message = ''
	print 'login'
	email = request.form['email']
	print email
	password = request.form['password']
	print password
	user_query = "SELECT email FROM users WHERE email = :email LIMIT 1"
	query_data = { 'email': email }
	user = mysql.query_db(user_query, query_data) # user will be returned in a list
	print user
	if not user:
		print 'email error'
		message = 'Error 86-5 EMAIL NOT FOUND: incorrect email'
		return render_template('index.html', dialogue = message)
	else:
		print "email equal"
		print user[0]['email']
	user_query = "SELECT password FROM users WHERE email = :email LIMIT 1"
	query_data = { 'email': email }
	print password
	user = mysql.query_db(user_query, query_data)
	print user
	if not user:
		print 'password error'
		message = 'Error 86-5 EMAIL NOT FOUND: incorrect password'
		return render_template('index.html', dialogue = message)
	if bcrypt.check_password_hash(user[0]['password'], password):
		print 'correct'
		print user[0]['password']
		user_query = "SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM users WHERE email = :email LIMIT 1"
		query_data = { 'email': email }
		name = mysql.query_db(user_query, query_data)
		return render_template('success.html', Welcome = name[0]['full_name'])
	else:
		print 'incorrect'
		message = 'Error 86-5 EMAIL NOT FOUND: incorrect password'
		return render_template('index.html', dialogue = message)
	return render_template('index.html', dialogue = message)

@app.route('/success', methods=['POST'])
def success():
	return render_template('success.html')

app.run(debug=True)