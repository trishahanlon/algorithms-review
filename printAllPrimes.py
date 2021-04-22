# program to display all the prime numbers between two numbers

lower = 1
upper = 5

print("The Prime numbers between", lower, "and", upper, "are:")

# loop through all the numbers between our bounds
for num in range(lower, upper + 1):
    # prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)