while True:
	print ("1. IOError \n2. Value Error \n3. ZerDivisionError \n4. NameError \n5. FileNotFoundErro")
	ch=int(input("Enter your choice: "))
	if ch==1:
		try:
			f1=open("overr.py", 'r')
			f1.write("Hello")
			print("Successful")
		except IOError:
			print ("File opened in read mode")
	elif ch==2:
		try:
			f1=open("overr.py", 'z')
			print("successfu")
		except ValueError:
			print("Value Error")
	elif ch==3:
		try:
			c=10/0
			print(c)
		except ZeroDivisionError:
			print("Exception")
	elif ch==4:
		try:
			f1=opens("overr.py", 'r')
			print ("success")
		except NameError:
			print("Name Error")
	elif ch==5:
		try:
			f = open('f9.txt', 'r')
			print("Successful")
		except FileNotFoundError:
			print("File Not Found error")
	else:
		exit()
