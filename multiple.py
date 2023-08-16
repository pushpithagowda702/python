class Student:
	def __init__(self):
		self.name=input("Enter your name: ")
		self.usn=int(input("Enter your usn: "))
		self.age=int(input("Enter your age: "))
	def display(self):
		print("Name: ", self.name, "\nUSN: ", self.usn, "\nAge: ", self.age)
class Ug(Student):
	def __init__(self):
		super().__init__()
		self.sem=int(input("Enter your semester: "))
		self.fees=int(input("Enter your fee: "))
		self.stipend=int(input("Enter stipend: "))
		self.display()
	def display(self):
		super().display()
		print("Semester: ", self.sem, "\nFees: ", self.fees, "\nStipend: ", self.stipend)
class Pg(Student):
	def __init__(self):
		super().__init__()
		self.sem=int(input("Enter your semester: "))
		self.fees=int(input("Enter your fee: "))
		self.stipend=int(input("Enter stipend: "))
		self.display()
	def display(self):
		super().display()
		print("Semester: ", self.sem, "\nFees: ", self.fees, "\nStipend: ", self.stipend)

print("1. UG Student\n2. PG Student\n3. Exit")
ch=int(input("Enter your choice: "))
if ch==1:
	u=Ug()
elif ch==2:
	p=Pg()
else:
	exit()
