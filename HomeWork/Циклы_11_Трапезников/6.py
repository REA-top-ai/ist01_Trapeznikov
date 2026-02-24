single_digits = list(range(10))
squares = []
cubes = []

for num in single_digits:
    print(num)
    squares.append(num ** 2)

print(squares)

for num in single_digits:
    cubes.append(num ** 3)

print(cubes)

