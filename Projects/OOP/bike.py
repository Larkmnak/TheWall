from flask import Flask, render_template
# imports the Bcrypt module
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)

class Bike(object):
	"""docstring for Bike"""
	def __init__(self, price = 40, max_speed = 10):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print "Cost: "+str(self.price)
		print "Top Speed: "+str(self.max_speed)
		print "Miles: "+str(self.miles)
		return self
	def ride(self, times = 1):
		self.ride = "Ridding...\n"*times
		print self.ride
		self.miles += 10 * times
		return self
	def reverse(self, times = 1):
		self.beep = "beep...beep...beep...\n"
		print "Reversing..."+self.beep*times
		self.miles -= 5 * times
		return self

@app.route('/', methods=['GET'])
def index():

	Mongoose = Bike().ride(3).reverse().displayInfo()

	SantaCruz = Bike(80, 15).ride(2).reverse(2).displayInfo()

	GT = Bike(120, 20).reverse(3).displayInfo()

	return render_template('index.html')


# I would fix the negative milage by siply ipmlamenting an if statement to check if the miles fall to zero and keep them there

app.run(debug=True)