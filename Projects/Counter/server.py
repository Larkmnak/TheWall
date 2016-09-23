from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

def init():
	session['count'] = 0

@app.route('/', methods=["GET"])
def index():
	session['count'] = session['count'] +1
  	return render_template("index.html")

@app.route('/ninja', methods=["POST"])
def ninjaPress():
	print "for ninjas! pressed"
	session['count'] = session['count'] + 1
	return redirect('/')

@app.route('/hacker')
def hackerPress():
	print "for hackers! pressed"
	session['count'] = 0
	return redirect('/')

app.run(debug=True)