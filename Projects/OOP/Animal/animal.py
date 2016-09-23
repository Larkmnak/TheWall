from flask import Flask, render_template
# imports the Bcrypt module
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)

class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100
	def walk():
		self.health -= 1
	def run():
		self.health -= 5
	def displayHealth():
		print "Name: "+self.name
		print "Health: "+str(self.health)

class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self):
		super(Dog, self).__init__()
		self.health = 150
	def pet():
		self.health += 5

class Dragon(Animal):
	def __init__(self):
		super(Dragon, self).__init__()
		self.health = 170
	def fly():
		self.health -= 10
	def displayHealth():
		print "this is a dragon!"
		print "Name: "+self.name
		print "Health: "+str(self.health)

app.run(debug=True)