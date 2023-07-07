d={}
class Employee:
	def add1(self):
		self.empid = input("Enter empid: ")
		self.name = input("Enter name: ")
		self.add = input("Enter address: ")
		self.pan = input("Enter pan: ")
		self.basic = int(input("Enter basic pay: "))
		self.deduct = int(input("Enter deduct: "))
		self.hra = 0.25 * self.basic
		self.da = 0.15 * self.basic
		self.gross = self.basic + self.hra + self.da - self.deduct
		self.update()

	def update(self):
		d.update({self.empid: {"Empid": self.empid, "Name": self.name, "Address": self.add, "PAN": self.pan, "Basic": self.basic, "HRA": self.hra, "DA": self.da, "Gross": self.gross}})

	def display(self):
		for x in d:
			print("EMPid", x, " - Details")
			for i in d[x]:
				print(i, " - ", d[x][i])
	def search(self, key):
		print(d.get(key))

obj1 = Employee()
while True:
	print("1. Add \n2. Display \n3. Search \n4. Backup \n5. Clear Data \n6. Delete specific employee details \n7. Remove last entry")
	ch = int(input("Enter choice: "))
	if ch == 1:
		obj1.add1()
	elif ch == 2:
		obj1.display()
	elif ch == 3:
		key = input("Enter empid: ")
		obj1.search(key)
	elif ch == 4:
		d1=d.copy()
		print(d1)
	elif ch == 5:
		d.clear()
		print(d)
	elif ch == 6:
		key = input("Enter the empid you want to delete: ")
		d.pop(key)
		print(d)
	elif ch == 7:
		d.popitem()
		print(d)
	else:
		exit()

