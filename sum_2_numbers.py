# define numbers array
numbers = []

# loop for 2 iterations
for i in range(1, 3):
    # input number and append to numbers array
    numbers.append(int(input(f"Enter number {i}: ")))

# add the two numbers and print the sum
print(numbers[0] + numbers[1])