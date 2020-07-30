import sys

# get hte input from the command line
arr = list(map(int, sys.argv[1].split(",")))
print('unsorted array before: ', arr)

# insertion sort from algorithms book.
# not a fan of how they use one letter names for arrays...
# Also... not a fan of or how they start their counting variable with j.
def insertion_sort(A):

    for j in range(1, len(A)):
        key = A[j]
        print('key: ', key)
        i = j - 1

        while i >= 0 and key < A[i]:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

# arr = [12, 11, 13, 5, 6]
# call function and print out result
insertion_sort(arr)
for i in range(len(arr)):
    print(arr[i])

