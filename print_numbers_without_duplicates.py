# define numbers array
numbers = []

# loop 10 iterations
for i in range(1, 11):
    # input number and append to numbers array
    numbers.append(int(input(f"Enter numbers {i}: ")))

# iterate over the values of numbers
for number in numbers:
    # check if current value is unique in numbers
    if numbers.count(number) == 1:
        # print if true
        print(number)