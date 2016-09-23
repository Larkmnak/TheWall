from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import string
app = Flask(__name__)
mysql = MySQLConnector(app,'email')
app.secret_key = 'super secret key'
@app.route('/')
def index():                         # run query with query_db()
    return render_template('index.html') # pass data to our template

@app.route('/submit', methods=['POST'])
def submit():
    VarEmail = request.form['email_address']
    print VarEmail
    print len(VarEmail)
    VarEmail = list(VarEmail)
    print VarEmail
    print VarEmail[len(VarEmail) - 3]
    AtCheck = 0
    ErrorBool = 0
    NewStr = ['']
    ComList = ['c','o','m', '']
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
        for countCom in range(0,3): 
            count = len(VarEmail)+countCom-3
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
                print 'not breaking'
        if AtCheck != 1:
            print VarEmail
            print 'Missing symbol'
            session['dialogue'] = 'Error 30-9: EMAIL NOT VALID: missing @'
            ErrorBool = 1
            break
    if ErrorBool == 2:
        print 'passed email to database'
        query = "INSERT INTO users (email, created_at, updated_at)  VALUES (:email, NOW(), NOW())"
        data = {
            'email': request.form['email_address']
        }
        mysql.query_db(query, data)
    return render_template('index.html', dialogue = session['dialogue'])

@app.route("/success", methods=['POST'])
def success():
    query = "SELECT * FROM users"                           # define your query
    emails = mysql.query_db(query)                           # run query with query_db()
    return render_template('success.html', all_emails=emails)



# @app.route('/friends/<friend_id>')
# def show(friend_id):
#     # Write query to select specific user by id. At every point where
#     # we want to insert data, we write ":" and variable name.
#     query = "SELECT * FROM friends WHERE id = :specific_id"
#     # Then define a dictionary with key that matches :variable_name in query.
#     data = {'specific_id': friend_id}
#     # Run query with inserted data.
#     friends = mysql.query_db(query, data)
#     # Friends should be a list with a single object,
#     # so we pass the value at [0] to our template under alias one_friend.
#     return render_template('index.html', one_friend=friends[0])

# @app.route('/friends', methods=['POST'])
# def create():
#     # Write query as a string. Notice how we have multiple values
#     # we want to insert into our query.
#     query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
#     # We'll then create a dictionary of data from the POST data received.
#     data = {
#              'first_name': request.form['first_name'], 
#              'last_name':  request.form['last_name'],
#              'occupation': request.form['occupation']
#            }
#     # Run query, with dictionary values injected into the query.
#     mysql.query_db(query, data)
#     return redirect('/')

# @app.route('/update_friend/<friend_id>', methods=['POST'])
# def update(friend_id):
#     query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
#     data = {
#              'first_name': request.form['first_name'], 
#              'last_name':  request.form['last_name'],
#              'occupation': request.form['occupation'],
#              'id': friend_id
#            }
#     mysql.query_db(query, data)
#     return redirect('/')

# @app.route('/remove_friend/<friend_id>', methods=['POST'])
# def delete(friend_id):
#     query = "DELETE FROM friends WHERE id = :id"
#     data = {'id': friend_id}
#     mysql.query_db(query, data)
#     return redirect('/')

app.run(debug=True)