def all_even():
    n = 0
    while True:
        yield n
        n += 2

for even_number in all_even():
    print(even_number)