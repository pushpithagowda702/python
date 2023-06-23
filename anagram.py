str1 = input ("Enter string1: ")
str2 = input ("Enter string2: ")
if (len(str1) != len(str2)):
	print ("Strings are not anagram")
else:
	for i in range(len(str1)):
		if (str1[i] not in str2 or str2[i] not in str1):
			print ("String is not an anagram")
			exit()
	print ("String is an anagram")
