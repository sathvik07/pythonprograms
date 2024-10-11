class Node:
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None


def push(head_ref, new_data):

    new_node = Node()
    new_node.data = new_data
    new_node.next = (head_ref)
    new_node.prev = None

    if ((head_ref)!= None):
        (head_ref).prev = new_node
    (head_ref) = new_node
    return head_ref

def findsize(node):
    count = 0
    while (node != None):
        count += 1
        node = node.next

    return count




head = None
head = push(head, 4)
head = push(head, 3)
head = push(head, 2)
head = push(head, 1)


print(findsize(head))