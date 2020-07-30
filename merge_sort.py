import sys

# get the input from the command line
arr = list(map(int, sys.argv[1].split(",")))
print('unsorted array before: ', arr)


def merge_sort(array):
    if len(array) > 1:
        # divide the array into left and right
        middle = (len(array)//2)
        left = array[:middle]
        right = array[middle:]

        # call merge_sort on our left and right arrays recursively
        left = merge_sort(left)
        right = merge_sort(right)

        # start building our final, sorted array
        array = []

        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                array.append(left[0])
                left.pop(0)
            else:
                array.append(right[0])
                right.pop(0)

        for i in left:
            array.append(i)
        for i in right:
            array.append(i)

    return array

# call merge sort on our array from the command line
# merge_sort(arr)
print('Sorted array from merge sort: ', merge_sort(arr))