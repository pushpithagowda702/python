msg = input("Type here: ")
msg_list = msg.split(" ")
emoji = {
":)": "Smile", ":(": "'Depressed'", ";)": "'Wink'"
}
y = " "
for x in msg_list:
	y += emoji.get(x, x) + " "
print (y)
