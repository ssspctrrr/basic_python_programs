# define numbers array
numbers = []

# loop 10 iterations
for i in range(1, 11):
    # input number
    number = int(input(f"Enter number {i}: "))

    # check if number is not yet in numbers
    if number not in numbers:
        # append to numbers if true
        numbers.append(number)

# print numbers array
print(numbers)