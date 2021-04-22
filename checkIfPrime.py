# program to see if a number is prime or not
# a prime number is an integer greater than 1 that was no factors
# except 1 and the number itself.

number = 88

# prime numbers are greater than 1
if number > 1:
    # loop through from 2 to our number to check if it has factors
    for i in range(2, number):
        # if the number has a factor, it's not prime
        if (number % i) == 0:
            print(str(number) + " not prime")
            break
    # else for statement - if we don't break then this'll run
    # if we didn't find any factors: aka we didn't break from the if statement, we have a prime number
    else:
        print(str(number) + " is prime")

