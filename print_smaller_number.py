# define numbers array
numbers = []

# create loop for 2 iterations
for i in range(1, 3):

    # input number and append the number to the numbers array
    numbers.append(int(input(f"Enter number {i}: ")))

# if first_number less than second_number
if numbers[0] < numbers[1]:
    # print first_number
    print(numbers[0])
# else if second_number less than first_number
elif numbers[1] < numbers[0]:
    # print second_number
    print(numbers[1])
# else 
else:
    #print "Numbers are equal"
    print("Numbers are equal.")