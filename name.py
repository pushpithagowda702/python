name = input("Enter your name ")
if len(name) < 3:
	print("Name should have minimum three letters")
elif len(name) > 10:
	print("Name can have maximum 10 letters")
else:
	print("Perfect")
