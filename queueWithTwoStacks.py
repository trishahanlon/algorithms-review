# implement a queue with 2 stacks
# your queue should have an enqueue and dequeue method
# and it should be "first in first out"

class QueueTwoStacks(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if len(self.out_stack) == 0:
            # Move items from in_stack to out_stack, reversing order
            while len(self.in_stack) > 0:
                newest_in_stack_item = self.in_stack.pop()
                self.out_stack.append(newest_in_stack_item)

            # if out_stack is still empty, raise an error
            if len(self.out_stack) == 0:
                raise IndexError("Can't dequeue from an empty queue")

        return self.out_stack.pop()


myStack = QueueTwoStacks()
myStack.enqueue("a")
print("dequeue", myStack.dequeue())
myStack.enqueue("b")
print("dequeue", myStack.dequeue())
myStack.enqueue("c")
print("dequeue", myStack.dequeue())
myStack.enqueue("d")
print("dequeue", myStack.dequeue())
myStack.enqueue("e")
print("dequeue", myStack.dequeue())
myStack.enqueue("f")
print("dequeue", myStack.dequeue())
