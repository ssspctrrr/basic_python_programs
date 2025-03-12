# define numbers array
numbers = []

# loop 2 iterations
for i in range(1, 3):
    # input and append it to numbers array
    numbers.append(int(input(f"Enter number {i}: ")))

# print remainder of first_number divided by second_number
print(numbers[0] % numbers[1])