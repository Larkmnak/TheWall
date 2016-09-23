from flask import Flask, render_template
# imports the Bcrypt module
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)

class Car(object):
	def __init__(self, name, price, speed, mileage):
		self.name = name
		self.price = price
		self.speed = speed
		self.mileage = mileage
		self.tax = 12
		if self.price > 10000:
			self.tax = 15
		self.total_price = (self.price * self.tax) + self.tax
		self.displayAll()
	def displayAll(self):
		print "--------------------------"
		print self.name
		print self.price
		print self.speed
		print self.mileage
		print self.tax
		print "--------------------------"

@app.route('/', methods=['GET'])
def index():
	Toyota = Car('Toyota',8000, 100, 80000)
	Mercedes = Car('Mercedes', 60000, 160, 20000)
	Kia = Car('Kia', 6000, 80, 120000)
	Lambragini = Car('Lambragini', 240000, 240, 2)
	Jeep = Car('Jeep', 7000, 120, 110000)
	Bug = Car('Bug', 5000, 60, 300000)
	return render_template('index.html')

app.run(debug=True)