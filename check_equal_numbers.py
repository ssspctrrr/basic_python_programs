# define numbers array
numbers = []

# loop for 2 iterations
for i in range(1, 3):
    # input the numbers and append into the numbers array
    numbers.append(int(input(f"Enter number {i}: ")))

# if first_number is equal to second_number
if numbers[0] == numbers[1]:
    # print "Equal"
    print("Equal")