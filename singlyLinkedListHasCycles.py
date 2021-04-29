# You have a singly-linked list and want to check if it contains a cycle.
# A cycle occurs when a node’s next points back to a previous node in the list.

class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None


# Write a function contains_cycle() that takes the first node in a singly-linked list
#  and returns a boolean indicating whether the list contains a cycle.
def contains_cycle(first_node):
    # start both runners at the beginning
    slow_runner = first_node
    fast_runner = first_node

    # until we hit the end of the list
    while fast_runner is not None and fast_runner.next is not None:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

        # case: fast_runner is about the "lap" slow_runner
        if fast_runner is slow_runner:
            return True

    # case: fast_runner hit the end of the list
    return False


a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c
c.next = a

print(contains_cycle(a))
