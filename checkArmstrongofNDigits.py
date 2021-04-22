# Python program to check if any number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# calculate the length of the number:
order = len(str(num))
print(order)

sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** int(order)
    temp //= 10

# display if armstrong or not
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")