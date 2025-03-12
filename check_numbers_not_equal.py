# define numbers array
numbers = []

# loop two iterations
for i in range(1, 3):
    # input and append numbers to numbers array
    numbers.append(int(input(f"Enter number {i}: ")))

# check if first_number is not equal to second_number
if numbers[0] != numbers[1]:
    # print "Not equal"
    print("Not equal")