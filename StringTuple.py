while True:
	print("1. String Operations \n2. Tuples Operations")
	ch = int(input("Enter your choice: "))
	if ch==1:
		while True:
			print("*"*10, "String Operations", "*"*10)
			print("1. Capitalize \n2. Index \n3. Join \n4. Swapcase \n5. Replace")
			strch = int(input("Enter your choice: "))
			str1 = input("Enter your string: ")
			if strch==1:
				print(str1.capitalize())
			elif strch==2:
				ind=input("Enter the character: ")
				print(str1.index(ind))
			elif strch==3:
				str2 = input("Enter another string: ")
				print(str2.join(str1))
			elif strch==4:
				print(str1.swapcase())
			elif strch==5:
				old = input("Enter the string to be replaced: ")
				new = input("Enter the new string: ")
				print(str1.replace(old, new))
			else:
				print("Invalid input")
				break

	elif ch==2:
		while True:
			print("*"*10, "Tuple Operations", "*"*10)
			print("1. Tuple \n2. All \n3. Any \n4. Enumerate \n5. Sum")
			tupch = int(input("Enter your choice: "))
			if tupch==1:
				list1 = list(input("Enter list items: "))
				print ("List: ", list1)
				print ("Tuple: ", tuple(list1))
			elif tupch <= 4:
				tup = tuple(input("Enter tuple items: "))
				if tupch==2:
					print(all(tup))
				elif tupch==3:
					print(any(tup))
				elif tupch==4:
					print(list(enumerate(tup)))
			elif tupch==5:
				tupl = []
				for x in range(4):
					i = int(input("Enter tuple elements: "))
					tupl.append(i)
				tup = tuple(tupl)
				print(sum(tup))
			else:
				print("Invalid input")
				break
	else:
		print("Invalid input")
		exit()
