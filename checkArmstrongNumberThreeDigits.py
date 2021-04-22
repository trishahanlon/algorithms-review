# check whether an n-digit integer is an Armstrong number or not
# in case of Armstrong number of 3 digits: the sum of the cubes of each digit is equal to the number itself
# 153 = 1*1*1 + 5*5*5 + 3*3*3

num = int(input("Enter a number: "))

sum = 0

temp = num
print("Temp before while:", temp)
while temp > 0:
    # NOTE: % = modulo
    digit = temp % 10
    print("digit: ", digit)
    # NOTE: ** = Exponentiation
    sum += digit ** 3
    print("sum", sum)
    # NOTE: // = floor division
    temp //= 10
    print('temp:', temp)

# actually test if it's an armstrong number
if num == sum:
    print(num,'is an Armstrong number')
else:
    print(num,' is not an Armstrong number')