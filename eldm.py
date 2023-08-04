import math
class ABC:
	def __init__(self, a):
		self.a = a
	def __len__(self):
		return len(self.a)
	def __lt__(self, b):
		return self.a < b.a
	def __floor__(self):
		return math.floor(self.a)
	def __ceil__(self):
		return math.ceil(self.a)
	def __str__(self):
		return str(obj1)

obj1 = [1, 2, 3]
obj2 = [3, 4, 5]
print(len(obj1))
print(obj1 < obj2)
print(math.floor(4.5))
print(math.ceil(4.5))
print(str(obj1))
