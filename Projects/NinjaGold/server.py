from flask import Flask, render_template, request, redirect, session, Markup
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	session['gold'] = 0
  	return render_template("index.html", gold = session['gold'])

@app.route('/process_money', methods=["POST"])
def processMoney():
	if request.form['building'] == 'farm':
		print 'farm'
		session['gold'] = session['gold'] + (round(random.random()*10))+10
		session['message'] += Markup("<p>You walk into the dank farm, reeking of hey and animal dung.</p><p>You found "+str(session['gold'])+" gold!...in a cow pie...ew...</p>")
	elif request.form['building'] == 'cave':
		print 'cave'
		session['gold'] = session['gold'] + random.randint(5,10)
		session['message'] += Markup("<p>You walk into the cold and damp cave as quietly as you can.</p><p>You found "+str(session['gold'])+" gold!...in the carcus of a fresh bear meal...ew...</p>")
	elif request.form['building'] == 'house':
		print 'house'
		session['gold'] = session['gold'] + random.randint(2,5)
		session['message'] += Markup("<p>You walk into a warm home, hopefully its yours!</p><p>You stole "+str(session['gold'])+" gold!...in your neighbor's purse...thats low man...</p>")
	elif request.form['building'] == 'casino':
		print 'casino'
		session['gold'] = session['gold'] + random.randint(0,100)-50
		if session['gold'] < 0:
			session['message'] += Markup("<p>You walk into a smelly casino called Bazooko's Circus, you plunk down next to a car salesmen and try your luck.</p><p>You lost "+str(session['gold'] * -1)+" gold!...\nBazooko's Circus is what the world would be doing every Saturday night if the Nazis had won the war. This was the Sixth Reich.</p>")
		elif session['gold'] > 0:
			session['message'] += Markup("<p>You walk into a smelly casino called Bazooko's Circus, you plunk down next to a car salesmen and try your luck.</p><p>You won "+str(session['gold'])+" gold!...\n...that vision of the big winner somehow emerging from the last minute pre-dawn chaos of a stale Vegas casino.</p>")
		elif session['gold'] == 0:
			session['message'] += Markup("<p>You walk into a smelly casino called Bazooko's Circus, you plunk down next to a car salesmen and try your luck.</p><p>You broke even!...</p><p>...Too weird to live, and too rare to die... </p>")
	return render_template("index.html", gold = session['gold'], info =session['message'])

app.run(debug=True)


