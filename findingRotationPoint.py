'''
I opened up a dictionary to a page in the middle and started flipping through, looking for words I didn't know.
I put each word I didn't know at increasing indices in a huge list I created in memory.
When I reached the end of the dictionary, I started from the beginning and did the same thing until
I reached the page I started at.

Now I have a list of words that are mostly alphabetical, except they start somewhere in the middle of the alphabet,
 reach the end, and then start from the beginning of the alphabet.
'''

def find_rotation_point(words):
    first_word = words[0]
    floor_index = 0
    ceiling_index = len(words) - 1

    # we're going to modify binary search to use words
    while floor_index < ceiling_index:
        # guess a point halfway between floor and ceiling
        guess_index = int(floor_index + ((ceiling_index - floor_index) / 2))

        # if guess comes after first word or is the first word
        if words[guess_index] >= first_word:
            # go right
            floor_index = guess_index
        else:
            # go left
            ceiling_index = guess_index

        # if floor and ceiling have converged
        if floor_index + 1 == ceiling_index:
            # between floor and ceiling is where we flipped to the beginning
            # so ceiling is alphabetically first
            return ceiling_index

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

# call our function
print(find_rotation_point(words))
