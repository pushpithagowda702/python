X = [[1,73, 9],
    [4 ,3,6],
    [6 ,8,9]]

Y = [[6,8,2],
    [4,7,3],
    [4,5,7]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)
