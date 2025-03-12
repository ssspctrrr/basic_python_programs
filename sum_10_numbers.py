# define numbers array
numbers = []

# loop for 10 iterations
for i in range(1, 11):
    # input and append number to numbers array
    numbers.append(int(input(f"Enter number {i}: ")))

# print the sum of first_number to tenth_number
print(sum(numbers))