# define numbers array
numbers = []

# try if input is value
try:
    # loop while input is valid
    while True:
        # input number and append to numbers
        numbers.append(int(input("Enter number: ")))

# catch error if input is invalid
except:
    # print average of numbers
    print(sum(numbers) / len(numbers))