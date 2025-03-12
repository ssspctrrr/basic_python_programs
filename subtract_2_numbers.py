# define numbers array
numbers = []

# loop 2 iterations
for i in range(1, 3):
    # input and append number to numbers array
    numbers.append(int(input(f"Enter number {i}: ")))

# print result of subtract first_number by second_number
print(numbers[0] - numbers[1])