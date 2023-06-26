import time

def timed (func):
	def timer ():
		st = time.time()
		print (st)
		result = func ()
		et = time.time()
		print (et)
		return result
	return timer

def func():
	a,b=0,1
	while True:
		yield a
		a,b=b,a+b


n=int(input("ENter the number: "))

@timed
def my():
	fib = func()
	for i in range(n):
		print(next(fib))

my()
