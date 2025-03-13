# define highest_number variable
highest_number = None

# try if input is valid
try:
    # loop while input is valid
    while True:
        # input number
        number = int(input("Enter number: "))

        # check if highest_number is not None or if input greater than current highest_number
        if highest_number is None or number > highest_number:
            # assign highest_number as number if true
            highest_number = number

# catch error if input is invalid
except:
    # print highest_number
    print(highest_number)