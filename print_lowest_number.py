# define lowest_number variable as None
lowest_number = None

# try if input is valid
try:
    # loop while input is valid
    while True:
    # input number
        number = int(input("Enter number: "))

        # check if lowest_number is still None or number is less than lowest_number
        if lowest_number is None or number < lowest_number:
            # assign lowest_number as the value of number
            lowest_number = number

#catch error if input is invalid
except:
    # print lowest_number
    print(lowest_number)