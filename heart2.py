n = int(input("Enter the value of n: "))
count = n
for i in range(1, n):
  for j in range(i, n):
    print (" ", end="")
  for k in range(i):
    print ("* ", end="")
  for m in range(1, count):
    print ("  ", end="")
  count-=1
  for l in range(i):
    print ("* ", end="")
  print ()
n*=2
for i in range(0, n):
 for k in range(i):
  print (" ", end="")
 for j in range(n):
  print ("* ", end="")
 n-=1
 print ()

