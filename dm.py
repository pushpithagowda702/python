class Dunder:
	def __init__(self):
		self.l1 = []

	def data(self):
		n = int(input("Enter number of elements the list will contain: "))
		for x in range(n):
			self.l1.append(int(input("Enter the list element: ")))

	def __and__(self, other):
		self.newlist = []
		for i in range(len(self.l1)):
			self.newlist.append(self.l1[i] & other.l1[i])
		print(self.newlist)

	def __or__(self, other):
		self.newlist = []
		for i in range(len(self.l1)):
			self.newlist.append(self.l1[i] | other.l1[i])
		print(self.newlist)

	def __gt__(self, other):
		self.newlist = []
		for i in range(len(self.l1)):
			self.newlist.append(self.l1[i] > other.l1[i])
		print(self.newlist)

	def __lt__(self, other):
		self.newlist=[]
		for i in range(len(self.l1)):
			self.newlist.append(self.l1[i] < other.l1[i])
		print (self.newlist)

	def __xor__(self, other):
		self.newlist=[]
		for i in range(len(self.l1)):
			self.newlist.append(self.l1[i] ^ other.l1[i])
		print(self.newlist)

