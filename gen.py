def square_generator(n):
    for i in range(1, n+1):
        yield i ** 2

n = int(input("Enter the value of n: "))
# Using the generator to print the first n squares
for square in square_generator(n):
    print(square)


