# use stack class to implement a new class MaxStack with a method get_max()
# that returns the largest element in the stack. Does not remove the item.

class Stack(object):
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]


# our new class that inherits from Stack class
class MaxStack(object):
    def __init__(self):
        super().__init__()
        # stack holds all of our integers
        self.stack = Stack()
        # maxes_stack holds our "maxima" - update as we push and pop
        self.maxes_stack = Stack()

    def push(self, item):
        """add a new item on to the top of our stack"""
        self.stack.push(item)

        # If our item is greater than or equal to the last item in maxes_stack,
        # it's the new max! we'll had it to our maxes_stack
        if self.maxes_stack.peek() is None or item >= self.maxes_stack.peek():
            self.maxes_stack.push(item)

    def pop(self):
        """Remove and return the top item from our stack"""
        item = self.stack.pop()

        # if it equals the top item in maxes_stack, they must have been pushed
        # in together. So we'll pop it out of maxes_stack too.
        if item == self.maxes_stack.peek():
            self.maxes_stack.pop()

        return item

    def get_max(self):
        """The last item in maxes_stack is the max item in our stack"""
        return self.maxes_stack.peek()


max_int = MaxStack()
max_int.push(1)
max_int.push(5)
max_int.push(9)
max_int.push(1)

# have to pop to print out the first item
print(max_int.pop())

# call get_max() method
print(max_int.get_max())
