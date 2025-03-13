# define unique_numbers array
unique_numbers = []
# define duplicate_numbers array
duplicate_numbers = []

# loop for 10 iterations
for i in range(1, 11): 
    # input number
    number = int(input(f"Enter number {i}: "))

    # check if number is unique
    if number not in unique_numbers:
        # append number to unique_numbers if true
        unique_numbers.append(number)
    # else check if number is not yet in duplicate_numbers
        # append number to duplicate_numbers if true

print(unique_numbers)

# print duplicate_numbers