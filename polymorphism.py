class Parrot:
    def fly(self):
        print("Parrot can fly")
    def swim(self):
        print("Parrot cannot swim")

class Penguin:
    def fly(self):
        print("Penguin cannot fly")
    def swim(self):
        print("Penguin can swim")

# common interface (polymorphism)
def flying_test(bird):
    bird.fly()

# instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)
