command = ""
started = True
while command != "quit":
	command=input("> ").lower()
	if command == "start":
		if started:
			print("Car has started already")
		else:
			started == True
			print("Let's go")
	elif command == "stop":
		if started:
			print("Car stopped")
		else:
			started == False
			print("Car has stopped already")
	elif command == "help":
		print("1\n2\n3")
	else:
		print("Enter correct value")
