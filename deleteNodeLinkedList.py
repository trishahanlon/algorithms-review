# Delete a node from a singly-linked list, ↴ given only a variable pointing to that node.

class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None


def delete_node(node_to_delete):
    # Get the input node's next node, the one we want to skip tp
    next_node = node_to_delete.next

    if next_node:
        # Replace the input node's value and pointer with the next
        # node's value and pointer. The previous node now effectively
        # skips over the input node.
        node_to_delete.value = next_node.value
        node_to_delete.next = next_node.next
    else:
        # Oops, we're trying to delete the last node!
        raise Exception("Can't delete the last node with this code.")


a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

print('a.next before we delete: ', a.next, a.value)
print('b.next before we delete: ', b.next, b.value)
print('c.next before we delete: ', c.next, c.value)

delete_node(b)

print('a.next after we delete: ', a.next, a.value)
print('b.next after we delete: ', b.next, b.value)
print('c.next after we delete: ', c.next, c.value)


