class CM:
	def __init__(self, fn, mo):
		print ("Context Managers")
		self.fn = fn
		self.mo = mo
		self.f = None

	def __enter__(self):
		print ("Enter method")
		self.f = open(self.fn, self.mo)
		return self.f

	def __exit__(self, exc_type, exc_value, exc_traceback):
		print ("Exit method")
		self.f.close()

with CM('cm.txt', 'w') as f:
	print("Execution")
	f.write("Hello")

print (f.closed)
