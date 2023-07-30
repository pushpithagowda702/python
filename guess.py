num = 9
cur_count = 0
guess_count = 3
while cur_count < guess_count:
	guess=int(input("Guess: "))
	if guess==num:
		print('You win')
		break
	else:
		print("Guess again")
	cur_count += 1
else:
	print('You failed')
