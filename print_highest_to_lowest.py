# define numbers array
numbers = []

# try if input is valid
try:
    # loop while input is valid
    while True:
        # input number and append to numbers
        numbers.append(int(input("Enter number: ")))

# catch error if input is invalid
except:
    # sort numbers highest to lowest
    numbers.sort(reverse=True)
    # print sorted numbers
    print(numbers)