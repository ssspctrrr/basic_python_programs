# define numbers array
numbers = []

# try if input is invalid
try:
    # loop while input is invalid
    while True:
        # input number and append to numbers array
        numbers.append(int(input("Enter number: ")))

# catch error if input is invalid
except:
    # sort numbers array
    numbers.sort()
    # print sorted_numbers
    print(numbers)