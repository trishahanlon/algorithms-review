# a Factorial of a number is the product of all the integers from 1 to that number
# I.E.: 6! = 1*2*3*4*5*6 = 720

num = 7

factorial = 1

if num < 0:
    print("Factorials only work for positive numbers")
elif num == 0:
    print("Factorial for", num, "is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)
