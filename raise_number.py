# define numbers array 
numbers = []

# loop for two iterations
for i in range(1, 3):
    # input number and append to numbers array
    numbers.append(int(input(f"Enter number {i}: ")))

# print first_number raise to second number
print(numbers[0] ** numbers[1])