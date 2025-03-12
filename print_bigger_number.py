# define numbers array
numbers = []

# loop two iterations
for i in range(1, 3):
    # input number and append input to numbers array
    numbers.append(int(input(f"Enter number {i}: ")))

# check if first_number is greater than second_number
if numbers[0] > numbers[1]:
    # print first_number 
    print(numbers[0])
# else if second_number is greater than first_number
elif numbers[1] > numbers[0]:
    # print second_number 
    print(numbers[1])
# else
else:
    # print "Numbers are equal"
    print("Nubers are equal.")