weight = int(input("Enter your weight "))
lbs_kgs = input("L(bs) or K(g)")
if lbs_kgs.upper()=="L":
	print(weight*0.45, "kg")
elif lbs_kgs.upper()=="K":
	print(weight/0.45, "lbs")
else:
	print("Entered unit is not valid")
