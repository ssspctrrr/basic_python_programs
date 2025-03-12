# define numbers array
numbers = []

# loop for 2 iterations
for i in range(1, 3):
    # input numbers and append to numbers array
    numbers.append(int(input(f"Enter number {i}: ")))

# print the product of the numbers
print(numbers[0] * numbers[1])