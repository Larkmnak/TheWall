from flask import Flask, render_template
# imports the Bcrypt module
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)

class MathDojo(object):
	"""docstring for MathDojo"""
	def __init__(self):
		self.total = 0
	def add(self, n, *num):
		if str(type(n)) == "<type 'int'>":
			self.total += n
		else:
			for number in n:
				print 'n: ' + str(n)
				print 'type: ' + str(type(n))
				print 'number in n = '+ str(number)
				print 'number type: ' + str(type(number))
				print 'total = ' + str(self.total)
				if str(type(number)) == "<type 'int'>":
						self.total += number
				else:
					for item in number:
						print 'number: ' + str(number)
						print 'type: ' + str(type(number))
						print 'item in number = '+ str(item)
						print 'item type: ' + str(type(item))
						print 'total = ' + str(self.total)
						print 'total = ' + str(self.total)
						self.total += item
				print 'total = ' + str(self.total)

		if str(type(num)) == "<type 'int'>":
			self.total += num
		else:
			for number in num:
				print 'num: ' + str(num)
				print 'type: ' + str(type(num))
				print 'number in num = '+ str(number)
				print 'number type: ' + str(type(number))
				print 'total = ' + str(self.total)
				if str(type(number)) == "<type 'int'>":
						self.total += number
				else:
					for item in number:
						print 'number: ' + str(number)
						print 'type: ' + str(type(number))
						print 'item in number = '+ str(item)
						print 'item type: ' + str(type(item))
						print 'total = ' + str(self.total)
						print 'total = ' + str(self.total)
						self.total += item
				print 'total = ' + str(self.total)
		return self

	def sub(self, n, *num):
		if str(type(n)) == "<type 'int'>":
			self.total -= n
		else:
			for number in n:
				print 'n: ' + str(n)
				print 'type: ' + str(type(n))
				print 'number in n = '+ str(number)
				print 'number type: ' + str(type(number))
				print 'total = ' + str(self.total)
				if str(type(number)) == "<type 'int'>":
						self.total -= number
				else:
					for item in number:
						print 'number: ' + str(number)
						print 'type: ' + str(type(number))
						print 'item in number = '+ str(item)
						print 'item type: ' + str(type(item))
						print 'total = ' + str(self.total)
						print 'total = ' + str(self.total)
						self.total -= item
		if str(type(num)) == "<type 'int'>":
			self.total -= num
		else:
			for number in num:
				print 'num: ' + str(num)
				print 'type: ' + str(type(num))
				print 'number in num = '+ str(number)
				print 'number type: ' + str(type(number))
				print 'total = ' + str(self.total)
				if str(type(number)) == "<type 'int'>":
						self.total -= number
				else:
					for item in number:
						print 'number: ' + str(number)
						print 'type: ' + str(type(number))
						print 'item in number = '+ str(item)
						print 'item type: ' + str(type(item))
						print 'total = ' + str(self.total)
						print 'total = ' + str(self.total)
						self.total -= item
				print 'total = ' + str(self.total)
		return self

	def result(self):
		print 'Result: ' + str(self.total)
		return(self)


@app.route('/', methods=['GET'])
def index():
	MD = MathDojo()
	MD.add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).sub(2, [2,3], [1.1, 2.3]).result()
	return render_template('index.html')

app.run(debug=True)