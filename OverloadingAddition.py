class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # for printing the points pretty like
    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    # overloading the + operator
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

# Let's test it out
p1 = Point(1,2)
p2 = Point(2,3)

print(p1+p2)