from flask import Flask, render_template, request, redirect, session, Markup
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	session['number'] = random.randrange(0, 101)
  	return render_template("index.html", number = session['number'])

@app.route('/guessed', methods=["POST"])
def guessPress():
	textc = int(request.form['text'])
	randomNumber = int(session['number'])
	print textc
	print type(textc)
	if randomNumber < textc:
		session['message'] = Markup("<h1>WRONG! Too high try agian</h1>")	
	elif randomNumber > textc:
		session['message'] = Markup("<h1>WRONG! Too low try agian</h1>")
	elif randomNumber == textc:
		session['message'] = Markup("<h1>CORRECT!</h1><form action = '/new' method='post'><button type='submit'>Restart?</button></form>")
	else:
		session['message'] = Markup("WTF just happened")
	return render_template("index.html", message = session['message'], number = session['number'])

@app.route('/new', methods=["POST"])
def newGame():
	session['number'] = random.randrange(0, 101)
  	return render_template("index.html", number = session['number'])
	
app.run(debug=True)


