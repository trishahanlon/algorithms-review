class Parrot:
    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance methods
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))

# access our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())

# me fucking around
#print("{} is {} years old and is a {}".format(blu.name, blu.age, blu.species))