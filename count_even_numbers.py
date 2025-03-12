# define count_even variable
count_even = 0

# loop 10 iterations
for i in range(1, 11):
    # input number
    number = int(input(f"Enter number {i}: "))

    # check if number is even
    if number % 2 == 0:
        # add 1 to count_even if true
        count_even += 1

# print count_even
print(count_even)