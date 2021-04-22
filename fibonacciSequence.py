# a fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8
# the first to terms are 0 and 1.
# all the other terms are obtained by adding the preceeding two terms
# nth term = (n-1) + (n-2)

number_of_terms = 7
counter = 0
first = 0
second = 1
temp = 0

while counter < number_of_terms:
    print(first)
    temp = first + second
    first = second
    second = temp
    counter = counter + 1

