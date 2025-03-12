# define count_odds variable
count_odds = 0

# loop 10 iterations
for i in range(1, 11):
    # input number
    number = int(input(f"Enter number {i}: "))

    # check if number is odd
    if number % 2 == 1:
        # add 1 to count_odds if true
        count_odds += 1

# print count_odds
print(count_odds)