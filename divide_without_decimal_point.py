# define numbers array
numbers = []

# loop 2 iterations
for i in range(1, 3):
    # input and append number to numbers array
    numbers.append(int(input(f"Enter number {i}: ")))

# print first_number divided by second_number without decimal point
print(numbers[0] // numbers[1])