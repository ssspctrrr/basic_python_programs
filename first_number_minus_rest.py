# define numbers array
numbers = []

# loop 10 iterations
for i in range(1, 11):
    # input number and append to numbers array
    numbers.append(int(input(f"Enter number {i}: ")))

# print the first_number minus the sum of the second_number to tenth_number altogether
print(numbers[0] - sum(numbers[1:]))