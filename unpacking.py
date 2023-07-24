num = {
"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
y=""
phone = input("Phone: ")
for x in phone:
	y += num.get(x, "!")+" "
print(y)
