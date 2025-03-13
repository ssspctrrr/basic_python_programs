# define numbers array
numbers = []
# define count_duplicate
count_duplicate = 0
# define number_most_duplicate variable
number_most_duplicate = 0

# try if input is valid
try:
    # loop while input is valid
    while True:
        # input number
        number = int(input("Enter number: "))
        # append input to numbers array
        numbers.append(number)

        # check if the inputted number has more duplicates than current count_duplicate
            # set the inputted number as number_most_duplicate if true
            # set the count of inputted number in numbers array as count_duplicate

# catch error if input is invalid
except:
    print(numbers)
    # print number_most_duplicate 