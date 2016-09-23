from flask import Flask, render_template
# import animal
# imports the Bcrypt module
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)

class Animal(object):
	def __init__(self):
		self.name = ''
		self.health = 100
	def walk(self, times = 1):
		self.health -= 1 * times
		return self
	def run(self, times = 1):
		self.health -= 5 * times
		return self
	def displayHealth(self):
		print "Name: "+self.name
		print "Health: "+str(self.health)
		return self

class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self):
		super(Dog, self).__init__()
		self.health = 150
	def pet(self, times = 1):
		self.health += 5 * times
		return self

class Dragon(Animal):
	def __init__(self):
		super(Dragon, self).__init__()
		self.health = 170
	def fly(self, times = 1):
		self.health -= 10 * times
		return self
	def displayHealth(self):
		print "this is a dragon!"
		print "Name: "+self.name
		print "Health: "+str(self.health)
		return self

@app.route('/', methods=['GET'])
def index():
	animal = Animal()
	animal.name = 'animal'
	animal.walk(3).run(2).displayHealth()
	Cliffard = Dog()
	Cliffard.name = 'Cliffard'
	Cliffard.walk(3).run(2).pet().displayHealth()
	Thorn = Dragon()
	Thorn.name = 'Thorn'
	Thorn.walk(3).run(2).fly(2).displayHealth()
	return render_template('index.html')

app.run(debug=True)