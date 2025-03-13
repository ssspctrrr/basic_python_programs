# define numbers array
numbers = []

# loop while input is valid
while True:
    # try if input is valid
    try:
        # input number
        number = int(input("Enter number: "))

        # check if number is in numbers array
        if number not in numbers:
            # print "Unique" if true
            print("Unique")
            # append to numbers if true
            numbers.append(number)

        # else if number is not in numbers array
        else:
            # print "Duplicate"
            print("Duplicate")

    # catch error if input is invalid
    except:
        break
        # break loop