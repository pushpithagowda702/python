class Greet:
	def Hello(self, a=None, b=None):
		if (a==None and b==None):
			print("No name and age")
		elif (a==None):
			print("No name and age is ", b)
		elif (b==None):
			print("No age and name is ", a)
		else:
			print("Name ", a, "Age ", b)

obj = Greet()
while True:
	print("1. No Name and age \n2. Only name \n3. Only age \4. Name and age")
	ch = int(input("Enter your choice: "))
	if ch == 1:
		obj.Hello()
	elif ch == 2:
		name = input("Enter your name: ")
		obj.Hello(name)
	elif ch == 3:
		age = input("Enter your age: ")
		obj.Hello(b=age)
	elif ch == 4:
		name = input("Enter your name: ")
		age = input("Enter your age: ")
		obj.Hello(name, age)
	else:
		print("Invalid Input")
		exit()

